import numpy as np
import ShapeMatching
import pickle

thth=0

sweeps= 1000

'''
Check if the read out works. For some instances you have to add a new line
'''

#for problem in ['esc16a','esc16b','esc16c','esc16d','esc16e','esc16f','esc16g'
#                ,'esc16h','esc16i','esc16j']:

#for dim in [12	,14	,17	,18	,20,	21]:

#for dim in [12	,14	,16,	18,	20]:    

    
#for dim in [12	,14	,16,18,20]:   

#initial= np.array([9 , 4 , 6 , 11 , 5 , 1 , 15 , 10 , 14 , 3 , 17 , 12 , 19  ,18  ,23 , 8 , 21,  2
 # , 22 , 7 , 16,  20 , 24 , 25 , 13]    )

#initial= np.array( [14  ,12  , 5 , 18 , 10 , 30 , 11  ,22  , 1  ,19   ,9  ,20  ,32  ,17 ,  2  ,33  , 3  , 8
#   ,13  ,27  ,16   ,4  ,34   ,7 , 23 , 24  , 6,  35 , 31 , 28 , 15,  21 , 29 , 26 , 25])


#newArrangement= (initial-1).tolist()

for dim in [35]:    
 for initial in ['a']:
#for problem in ['nug16a','nug16b']:    
#for problem in ['scr20']:  
    #problem= 'nug'+ str(dim)
    problem= 'Tai'+ str(dim)+initial
    #problem= 'rou'+ str(dim)

    print(problem)
    f = open('Qaplib/'+problem+'.dat','r')
    liste= []
    liste2= []
    #thth=thth+1
    #dim= 10+ 2*thth
    counter=0
    for l in f:
           if counter==0:
                dimension= int(l) 
                
           if counter>1 and counter <2+dim:
        
               #g = np.array([int(v) for v in l.strip().split(" ")])
               g = np.array( [ v for v in l.strip().split(" ")])
               g= np.delete(g,np.where(g==''))
    
                    
               g= [int(elem) for elem in g]
               
               liste.append(g)
           if counter>2+dim and counter<3+2*dim:
               g = np.array( [ v for v in l.strip().split(" ")])
               g= np.delete(g,np.where(g==''))
    
                    
               g= [int(elem) for elem in g]
                
               liste2.append(g)
           counter = counter +1
    A= np.array(liste)
    B= np.array(liste2)
    
    
    numberOfit=20
    
    
    
    W= np.kron(A,B)
    
    Permutations=[]
    

    Permutations=[]
    for i in range(numberOfit):
    
        
        if i==0:
            newArrangement=  ShapeMatching.optimize(sweeps,W,None,None,i, problem )
        else:
            newArrangement=  ShapeMatching.optimize(sweeps,W,newArrangement,None,i, problem )
            
        Permutations.append(newArrangement)
    
    pickle.dump( Permutations , open( "sweeps"+str(sweeps)+"savePermutations"+problem+".p", "wb" ) )
    
   
    
