import pdb

from iniconfig import IniConfig

ini = IniConfig('pytest.ini')
pdb.set_trace()
if 'uitest' in ini:
    print(ini)
data = dict(ini['uitest'].items())
