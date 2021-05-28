from glob import glob
import subprocess

pdbs = glob('MSM/*/*.pdb')

prefix = "bcl-equil"
hosts = "lu-gpu lv-gpu ld-gpu lt-gpu boson lx-gpu ly-gpu lw-gpu ls-gpu"
walltime = "2:00"
ngpus = 1
rusage = "rusage[mem=3] span[ptile=1]"

for pdb in pdbs:
	pdbname = pdb.split('/')[-1][:-4]
	jobname = (f'{prefix}-{pdbname}')
	fahcommand = f'python equil_prep_for_fah.py {pdb}'
	command = f'bsub -J {jobname} -m "{hosts}" -q gpuqueue -W {walltime} -n {ngpus} -gpu "num={ngpus}:j_exclusive=yes:mode=shared" -R "{rusage}" -eo "/home/rafal.wiewiora/job_outputs/{jobname}.stdout" "{fahcommand}"'
	subprocess.run(command, shell=True, check=True)
