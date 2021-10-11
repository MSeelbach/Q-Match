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

## License
Permission is hereby granted, free of charge, to any person or company obtaining a copy of this software and associated documentation files (the "Software") from the copyright holders to use the Software for any non-commercial purpose. Publication, redistribution and (re)selling of the software, of modifications, extensions, and derivates of it, and of other software containing portions of the licensed Software, are not permitted. The Copyright holder is permitted to publically disclose and advertise the use of the software by any licensee.

Packaging or distributing parts or whole of the provided software (including code, models and data) as is or as part of other software is prohibited. Commercial use of parts or whole of the provided software (including code, models and data) is strictly prohibited. Using the provided software for promotion of a commercial entity or product, or in any other manner which directly or indirectly results in commercial gains is strictly prohibited.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
