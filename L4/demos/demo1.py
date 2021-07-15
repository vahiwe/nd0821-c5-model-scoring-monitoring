# pip list (return a list of all installed Python modules)
# pip list --outdated (show only the outdated modules)
# pip freeze (provides an output in “requirements format”)
# pip show pandas(provide specific information an installed module)
# pip install pandas (installs modules)
# python -m pip list (run pip through Python)

import subprocess

broken=subprocess.check_output(['pip', 'check'])
with open('broken.txt', 'wb') as f:
     f.write(broken)

outdated = subprocess.check_output(['pip', 'list','--outdated'])
with open('outdated.txt', 'wb') as f:
       f.write(outdated)

numpyinfo=subprocess.check_output(['python','-m','pip', 'show', 'numpy'])
with open('numpy.txt', 'wb') as f:
       f.write(numpyinfo)