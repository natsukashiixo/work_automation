import os
from pathlib import Path

rootfolder = Path('.')
filelist = [f for f in rootfolder.glob('*') if not f.name.startswith('sida') and not f.name.endswith('.py')]

latest_index = [f for f in rootfolder.glob('*') if f.name.startswith('sida')]

godhelpme = []

for file in latest_index:
    get_tail = file.name.replace('sida_', '')
    getint = get_tail.replace('.pdf', '')
    godhelpme.append(int(getint))

godhelpme.sort()

if len(latest_index) == 0:
    x = 0
else:
    x = godhelpme[-1]

filelist.sort(key=os.path.getmtime)

def rename(incrementor: int):
    for file in filelist:
        incrementor += 1
        file_ext = Path(file).suffix
        os.rename(file, './' + f'sida_{incrementor}' + file_ext)
        print(f'{file} renamed to sida_{incrementor}{file_ext}')

rename(x)