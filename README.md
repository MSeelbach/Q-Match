# Q-Match
This is the code for the experiments in the ICCV publication 'Q-Match: Iterative Shape Matching using Quantum annealing' in http://gvv.mpi-inf.mpg.de/projects/QMATCH. 
## D-Wave leap
You can run the code with D-Wave leap: https://www.dwavesys.com/take-leap.
  One can either run code with the leap IDE or locally by installing ocean (https://docs.ocean.dwavesys.com/en/stable/getting_started.html). 
  To get to the Leap IDE one has to click on workspaces after logging in to Leap.
## Faust Dataset
  In the Folder Q-match/FaustDS there are subsampled instances of the Faust dataset from http://faust.is.tue.mpg.de/. 
  The instances are subsampled in a way that the one to one correspondence is still valid. The files also contain precomputed geodesic distances and point descriptors. They are from Isometric Multi-Shape Matching, Gao et al, CVPR 2021 and any further work that uses this folder should cite their publication.
  
 ## Qaplib
  In the folder Qaplib/Qaplib there are the problem instances from https://www.opt.math.tugraz.at/qaplib/. Only some linebreaks have been added for the readout.

## How to run?
Execute the corresponding Main.py file.


## License
Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
