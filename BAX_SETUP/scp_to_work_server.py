import os
from glob import glob
import mdtraj as md
import numpy as np

pdbs = sorted(glob('output/*/equilibrated.pdb'))

for run in range(len(pdbs)):
    pdb = pdbs[run].split('/')[1]

    os.system(f'bzip2 output/{pdb}/system.xml')
    os.system(f'bzip2 output/{pdb}/state.xml')
    os.system(f'bzip2 output/{pdb}/integrator.xml')

    os.system(f'scp output/{pdb}/system.xml.bz2 rafal@fah.redesignscience.com:~/projects/17804/RUNS/RUN{run}/')
    os.system(f'scp output/{pdb}/state.xml.bz2 rafal@fah.redesignscience.com:~/projects/17804/RUNS/RUN{run}/')
    os.system(f'scp output/{pdb}/integrator.xml.bz2 rafal@fah.redesignscience.com:~/projects/17804/RUNS/RUN{run}/')
    os.system(f'scp output/{pdb}/equilibrated.pdb rafal@fah.redesignscience.com:~/projects/17804/RUNS/RUN{run}/')
