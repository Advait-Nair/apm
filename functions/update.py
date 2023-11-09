import spectrum
from keylang import KeyLang
import os



def _getapmv(base):
    apmv = open(base+'.apmv', 'r').read()
    data = KeyLang(apmv, '\n')
    return data

import urllib.request as internet
def readcloud(file):
    latest = 'https://raw.githubusercontent.com/Advait-Nair/apm/main/'+file
    content = internet.urlopen(latest).read()
    return content


def checkv(base):
    metadata = _getapmv(base)

    latestMetadata = KeyLang(readcloud('.apmv'),'\n')


    if latestMetadata.get('?VERSION') != metadata.get('?VERSION').strip():
        print(spectrum.subtitle('Your current APM Version [{cv}] can be updated to the latest version [{lv}]. Run apm update to do so.').format(cv=metadata.get('?VERSION'),lv=latestMetadata.get('?VERSION') or '?unknown'))


def UPDATE_APM():
    pass