# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:03:43 2020

@author: Marcel
"""

import numpy as np
from dwave.system import DWaveSampler, FixedEmbeddingComposite, VirtualGraphComposite

import neal
import numpy as np
from dimod.reference.samplers import ExactSolver
import dwave.inspector
import pickle


import scipy.io





def getarbitraryCouplings( currentPermAsTable, newPerm, W,N):
   
    """
    The function creates the matrix \Tilde{W}. 
    It requires the full matrix W,
    the current Permutation (currentPermAsTable),
    the list of cycles (newPerm) and the dimension N
    """
   
    
    dim= len(newPerm)
    
    Wneu= np.zeros((dim, dim))
    cneu= np.zeros(( dim))
    constantPlaces= np.zeros((N**2))
    constantPlaces= TableToVector(currentPermAsTable)

    
    for count, cycle in enumerate(newPerm):
        for count2, cycle2 in enumerate( newPerm):
        
            placeList1=[]        
            placeList2= []
            for k in range(len(cycle)):
                placeList1.append(currentPermAsTable.index(cycle[k]))
                
            for k in range(len(cycle2)):
                placeList2.append(currentPermAsTable.index(cycle2[k]))
                

            variablePlaces= np.zeros((N**2))
            variablePlaces2= np.zeros((N**2))


            for iteration,elem in enumerate(placeList1):
                variablePlaces[N* elem +  cycle[iteration]]=-1
                variablePlaces[N* elem +  cycle[(iteration+1)% len(cycle)]]=1
            
            for iteration,elem in enumerate(placeList2):
                variablePlaces2[N* elem +  cycle2[iteration]]=-1
                variablePlaces2[N* elem +  cycle2[(iteration+1)% len(cycle2)]]=1
            
            
            
            
            Wneu[count, count2 ]= variablePlaces.T @ W @ variablePlaces2
    
            if count==0:
                cneu[ count2 ]+= constantPlaces.T @ W @ variablePlaces2
        cneu[count ]+= variablePlaces.T @ W @ constantPlaces
    
    return [Wneu, cneu]



def updatePermutationTable(permutationTable,newPerm, updateDecision ):
       
        """
        Apply the cycles that were chosen by solving the subproblem QUBO
        permutationTable: current,(initial) Permutation
        newPerm: List of cycles
        updateDecision: Should you apply the cycle or not
        """
    
    
        result= permutationTable.copy()
        for count, cycle in enumerate(newPerm):
            
            if updateDecision[count]==1:
                
                
                placeList=[]        
                for k in range(len(cycle)):
                    placeList.append(permutationTable.index(cycle[k]))
                
                for iteration,elem in enumerate(placeList):
                    result[elem]= cycle[(iteration+1)% len(cycle) ]
          
        return result
    








def RunAnneal(W,b):
    #Given the quadratic (W) and linear (b) weights use the quantum annealer to solve the optimization problem

    from dwave.system import DWaveSampler, EmbeddingComposite, VirtualGraphComposite

    import neal
    Q= W/4 
    size = W.shape[0]
    qu= (b/2).reshape(size,1) + (np.sum( W, axis=0, keepdims= True ).T + np.sum(W,axis= 1, keepdims=True) )/4
    #PLUS OR MINUS
    
    
    for i in range(0,size):
        Q[i,i]=0
    
    
        
    
    bias=qu.reshape(size).tolist()
    
    J={}
    
    for i in range(size):
    
        for j in range(size):
            
            J.update( {(i,j): Q[i,j]})
    

    chain = np.max( [np.max (1.0001*np.abs(bias)), 1.0001* np.max(np.abs(Q)) ])

    sampler = EmbeddingComposite(DWaveSampler())#, annealing_time=20),num_spin_reversal_transforms=10
    response = sampler.sample_ising(bias,J, auto_scale=True ,chain_strength=chain ,num_reads=500 ,return_embedding=True)#anneal_schedule=((0.0,0.0),(40.0,0.5),(140.0,0.5),(180.0,1.0)))
   
  
    
#    dwave.inspector.show(response)
    Result=[]
    for datum in response.data(['sample', 'energy', 'num_occurrences','chain_break_fraction']):   
    #        print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)
            Result.append([datum.sample,  datum.energy,  datum.num_occurrences, datum.chain_break_fraction])


    return [Result, response.info]



def RunAnnealSim(sweeps,W,b):
    #Given the quadratic (W) and linear (b) weights use an simulated annealing solver from neal to solve the optimization problem

    import neal
    Q= W/4 
    size = W.shape[0]
    qu= (b/2).reshape(size,1) + (np.sum( W, axis=0, keepdims= True ).T + np.sum(W,axis= 1, keepdims=True) )/4
    #PLUS OR MINUS
    
    
    for i in range(0,size):
        Q[i,i]=0
    
    
        
    
    bias=qu.reshape(size).tolist()
    
    J={}
    
    for i in range(size):
    
        for j in range(size):
            
            J.update( {(i,j): Q[i,j]})
    

    solver = neal.SimulatedAnnealingSampler()
    num_reads=100
    response = solver.sample_ising(bias, J ,num_reads=num_reads, num_sweeps=sweeps )
    Result=[]
    for datum in response.data(['sample', 'energy', 'num_occurrences']):   
          #  print(datum.sample, "Energy: ", datum.energy, "Occurrences: ", datum.num_occurrences)
            Result.append([datum.sample,  datum.energy,  datum.num_occurrences])
    

    return [Result, response.info]



def TableToVector(table):
    #vectorize the permutation

    N= len(table)
    vector= np.zeros(N**2)
    for count, value in enumerate(table):
        vector[N*count +value]=1
    return vector 


def IntToVector(n, digits):
    #binary representation of the number n, saved as list.

    num=n
    binary = []
    for k in range(digits): 
        if num!=0:
            bit = num % 2
            binary.insert(0, bit)
            num = num // 2
        else:
            binary.insert(0,0)
    
    return binary





def getNextPairs(firstPairs):
        #Fast way to make sure that every 2-cycle occurs.

            nextPairs= []
            
            nextPairs.append((firstPairs[0][0],firstPairs[1][1] ))
            
            if len(firstPairs)>2:
                nextPairs.append((firstPairs[0][1], firstPairs[2][1]))
                
                for k in range(2,len(firstPairs)-1):
                    nextPairs.append(( firstPairs[k-1][0], firstPairs[k+1][1] ))    
            
                nextPairs.append( ( firstPairs[len(firstPairs)-2][0], firstPairs[len(firstPairs)-1][0] ))
            else:
                nextPairs.append((firstPairs[0][1],firstPairs[1][0] ))
        
            
            return nextPairs

def optimize(sweeps,W, initial, CycleSuggestions,iterationNumber,problem ):
    
    """
      Apply the cyclic alpha-expansion:
        W: weight matrix of original problem
        initial: initial permutation
        CycleSuggestions: possible suggestions for the cycles that are being used
        iterationNumber, probl: only used for saving results
    """
    
    N = int( np.sqrt(W.shape[0]))
    if initial==None:
        initialPermutation= np.arange(N).tolist()
    else:
        initialPermutation= (np.array(initial)).tolist()
 
    
    if CycleSuggestions is None:
        CycleLists= []  #with many cycles
    else:
        CycleLists= CycleSuggestions
    
        
        
     
     
    elementToAdd=[]
    
    for i in range(N//2):
                 elementToAdd.append([i , N-i -1 ])

    elementToAdd=  np.random.permutation( np.array( elementToAdd).reshape(-1)).reshape((-1,2)).tolist()
    CycleLists.append(elementToAdd)
    
    currentPairs=getNextPairs(elementToAdd)
    
    for k in range(N-2 ):
        CycleLists.append(currentPairs)
    
        currentPairs=getNextPairs(currentPairs)
    

    
    
    
    
    Save=[]
    
    N= int( np.sqrt( W.shape[0]) )
    
    currentPermutationTable= initialPermutation
    
    Save.append(CycleLists)
    
    for i in range(len(CycleLists)):


            
            
            
             [We, ce]=getarbitraryCouplings( currentPermutationTable, CycleLists[i], W,N)
            
             [Result,info]= RunAnneal(We,ce) #RunAnnealSim(sweeps ,We,ce)
             change= Result
             Save.append(We)
             Save.append(ce)
             
             Save.append(Result)
             Save.append(info)
            
             currentPermutationTable= updatePermutationTable(currentPermutationTable, CycleLists[i], change[0][0])
   
             vector= TableToVector(currentPermutationTable)
             print( vector.T @ W @ vector )
    
    
    
    
    pickle.dump( Save , open("sweeps"+str(sweeps)+ "Problem"+ str(problem)+ "save"+str(iterationNumber)+".p", "wb" ) )
                
    return currentPermutationTable