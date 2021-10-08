import numpy as np
import scipy.io

from Wsampling import *
from MatchingFramework import match
import matplotlib.pyplot as plt
import pickle

figureNumber=1

CListe=[]


initialPermutation = pickle.load( open( "Initpermutations.p", "rb" ) )

[Permutation1, Permutation2]= initialPermutation
Permutation1=Permutation1.tolist()
Permutation2=Permutation2.tolist()


for problemInstance in [33,34]:

   for nrWorst in [ 15] :
   #for nrWorst in [ 35,38] :

       
        S = scipy.io.loadmat('C:/Users/Marcel/Documents/Promotion/ICCV/IterativeShapeMatching/IterativeShapeMatching/FaustDS/tr_reg_0'+str(problemInstance)+'.mat')

        geodesicsX = S['geodesics']
        geodesicsX[:,:]= geodesicsX[Permutation1,:]
        geodesicsX[:,:]= geodesicsX[:,Permutation1]
        
        descriptorsX = S['hks']
        descriptorsX[:,:]=  descriptorsX[Permutation1,:]
        
        T =scipy.io.loadmat('C:/Users/Marcel/Documents/Promotion/ICCV/IterativeShapeMatching/IterativeShapeMatching/FaustDS/tr_reg_0'+str(problemInstance+1)+'.mat')

        geodesicsY = T['geodesics']
        geodesicsY[:,:]= geodesicsY[Permutation2,:]
        geodesicsY[:,:]= geodesicsY[:,Permutation2]
        
        
        descriptorsY = T['hks']
        descriptorsY[:,:]=  descriptorsY[Permutation2,:]

        
     
        
        # test matching
        [C,elist] = match(geodesicsX, geodesicsY, descriptorsX, descriptorsY, nrWorst,problemInstance)
        plt.figure(figureNumber)
        CListe.append(C)
        figureNumber=figureNumber+1
        
        plt.plot(elist)
        plt.title("Consider "+str(nrWorst)+' worst Vertices')
        plt.xlabel("Iteration")
        plt.ylabel("Energy")
        plt.savefig('Instance'+str(problemInstance)+'NRWorst'+str(nrWorst))
        
        pickle.dump( CListe , open( "saveCorres.p", "wb" ) )