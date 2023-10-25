import spectrum

def KeyLang(rtext, separator=' '):

    # Tab Separated Key Value Pairs
    text = rtext
    try:
        text = rtext.decode('utf-8')
    except: pass
    tskvp = text.split(separator)

    data = {}

    try:

        for i in range(0, len(tskvp)):
            # If it is even it is a pair
            isKey = i % 2 == 0
            
            if isKey:
                data[tskvp[i].strip()] = tskvp[i+1].strip()
    except:
        print(spectrum.error('keylang process error at internal update check process: mutated .apmv'))
        return {}
    
    return data


import os



def _getapmv(base):
    apmv = open(base+'.apmv', 'r').read()
    data = KeyLang(apmv)
    return data


def checkv(base):
    metadata = _getapmv(base)

    import urllib.request as internet

    latest = 'https://raw.githubusercontent.com/Advait-Nair/apm/main/.apmv'
    content = internet.urlopen(latest).read()
    latestMetadata = KeyLang(content)


    if latestMetadata.get('?VERSION') != metadata.get('?VERSION').strip():
        print(spectrum.subtitle('Your current APM Version [{cv}] can be updated to the latest version [{lv}]. Run apm update to do so.').format(cv=metadata.get('?VERSION'),lv=latestMetadata.get('?VERSION') or '?unknown'))