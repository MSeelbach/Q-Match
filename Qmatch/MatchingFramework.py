import numpy as np
from scipy.optimize import linear_sum_assignment

from Wsampling import *

import ShapeMatching

import pickle 

import time 


def match(Xgeodesics, Ygeodesics, Xdescriptors, Ydescriptors,nrWorst, problem):
    # initial matching by descriptor comparison
    softC = Xdescriptors.dot(Ydescriptors.transpose())
    rows, cols = linear_sum_assignment(-softC)
    C = np.array([rows, cols]).transpose()
    scoreList=[]
    # iterate optimizing subproblems
    countStagnation=0
    addUp=0
    Steps=30
    
    
   
    addUp=0
    for i in range(Steps):

        

        worst_matches, scores = evaluateCorrespondences(C, Xgeodesics, Ygeodesics,  nrWorst)#20)
        worst_vertices = C[worst_matches, :]        
        
        addUp=scores.sum()
        print('Energy: '+str(addUp))
        
        if len(scoreList)>0:
            if addUp>=scoreList[-1]:
                countStagnation+=1 
                break
                
                
            else:
                countStagnation=0
        
        scoreList.append(addUp)
        
        # generate subW
        begining= time.time()
        W = flattenW(subproblemW(C, worst_vertices[:, 0], worst_vertices[:, 1], Xgeodesics, Ygeodesics))
        ending= time.time()
        pickle.dump( [C,addUp,ending-begining] , open( "saveMatching"+str(i)+"problem"+str(problem)+".p", "wb" ) )

        # optimize
        newArrangement=  ShapeMatching.optimize(W,None,None,i, problem )
        
        # update C accordingly
        C[worst_matches,1]= C[ [worst_matches[k] for k in newArrangement ], 1]
        
        
        if addUp==0:
            break
        if countStagnation>1:
            break
        

    # final solution
    return [C,scoreList]


def evaluateCorrespondences(C, Xgeodesics, Ygeodesics, n):
    score = np.zeros(C.shape[0])

    # calc score for each correspondence
    for i in range(C.shape[0]):
        for j in range(i+1, C.shape[0]):
            score[i] += np.abs(Xgeodesics[C[i, 0], C[j, 0]] - Ygeodesics[C[i, 1], C[j, 1]])
            score[j] += np.abs(Xgeodesics[C[i, 0], C[j, 0]] - Ygeodesics[C[i, 1], C[j, 1]])

    # get n worst matches
    inds = np.argsort(score)
    inds = inds[-n:]

    return inds, score

