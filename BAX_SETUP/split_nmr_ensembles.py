import mdtraj as md

pdbs = ['1f16', '2k7w', '2lr1']

for pdb in pdbs:
    traj = md.load(f'input/{pdb}.pdb')
    for j,frame in enumerate(traj):
        frame.save(f'input/{pdb}/{pdb}_{j}.pdb')

# for 2k7w and 2lr1 also remove the peptides (1f16 is already apo)
for pdb in pdbs[1:]:
    traj = md.load(f'input/{pdb}.pdb')
    traj = traj.atom_slice(traj.top.select('chainid 0'))
    for j,frame in enumerate(traj):
        frame.save(f'input/{pdb}_apo/{pdb}_{j}_apo.pdb')
