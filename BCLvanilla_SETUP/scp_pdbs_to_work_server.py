import os
from glob import glob
import mdtraj as md
import numpy as np

pdbs = sorted(glob('output/*/solvated.pdb'))

lens = []
for i,pdb in enumerate(pdbs):
    traj = md.load(pdb)
    len_ = len(list(traj.top.atoms))
    lens.append(len_)
    print(i)

run = 0
for i in np.argsort(lens):
    pdb = pdbs[i].split('/')[1]

    os.system(f'scp output/{pdb}/equilibrated_solute.pdb server@pllwskifah2:/home/server/server2/projects/17800/RUNS/RUN{run}/')

    run += 1
