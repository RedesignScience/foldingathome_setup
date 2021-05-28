from glob import glob

pdbs = glob('MSM/*/*.pdb')

for pdb in pdbs:
	with open(pdb) as pdb_f:
		lines = pdb_f.readlines()
	with open(pdb, 'w') as pdb_f:
		for line in lines:
			if 'TER' not in line:
				pdb_f.write(line)
