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
order = []
for i in np.argsort(lens)[:35]:
    pdb = pdbs[i].split('/')[1]
    order.append(pdb)

    os.system(f'bzip2 output/{pdb}/system.xml')
    os.system(f'bzip2 output/{pdb}/state.xml')
    os.system(f'bzip2 output/{pdb}/integrator.xml')

    os.system(f'scp output/{pdb}/system.xml.bz2 server@pllwskifah2:/home/server/server2/projects/17801/RUNS/RUN{run}/')
    os.system(f'scp output/{pdb}/state.xml.bz2 server@pllwskifah2:/home/server/server2/projects/17801/RUNS/RUN{run}/')
    os.system(f'scp output/{pdb}/integrator.xml.bz2 server@pllwskifah2:/home/server/server2/projects/17801/RUNS/RUN{run}/')

    run += 1

np.save('17801_run_order', order)
