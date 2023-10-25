def KeyLang(text, sep=' '):
    apmv = open('.apmv', 'r').read()

    # Tab Separated Key Value Pairs
    tskvp = apmv.split(sep)

    data = {}

    try:

        for i in range(0, len(tskvp)):
            # If it is even it is a pair
            isKey = i % 2 == 0
            
            if isKey:
                data[tskvp[i]] = tskvp[i+1]
    except:
        print('keylang process error at internal update check process: mutated .apmv')
        return {}
    
    return data


import os

baseLoc = os.getcwd()
if 'apm' in baseLoc:
    baseLoc = baseLoc.replace('apm', '')
else:
    baseLoc = baseLoc + '/'

baseLoc = baseLoc.replace('//', '/')

def _getapmv():
    apmv = open(baseLoc+'apm/.apmv', 'r').read()
    data = KeyLang(apmv)
    return data

metadata = _getapmv()

import urllib

urllib.urlopen()