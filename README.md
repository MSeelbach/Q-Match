# Q-Match
This is the code for the experiments in the ICCV publication 'Q-Match: Iterative Shape Matching using Quantum annealing' in http://gvv.mpi-inf.mpg.de/projects/QMATCH. 
You can run the code with D-Wave leap: https://www.dwavesys.com/take-leap.
  One can either run code with the leap IDE or locally by installing ocean (https://docs.ocean.dwavesys.com/en/stable/getting_started.html). 
  To get to the Leap IDE one has to click on workspaces after logging in to Leap.
  In the Folder Q-match/FaustDS there are subsampled instances of the Faust dataset from http://faust.is.tue.mpg.de/. 
  The instances are subsampled in a way that the one to one correspondence is still valid. The files also contain precomputed geodesic distances and point descriptors. These are taken from Maolin Gao, Zorah Lahner, Johan Thunberg, Daniel Cremers, Florian Bernard; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021 and any further work that uses this folder should cite this publication.
  
  
  In the Folder Qaplib/Qaplib there are the problem instances from https://www.opt.math.tugraz.at/qaplib/. Only some linebreaks have been added for the readout.
