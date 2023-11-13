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


def checkv(base,sendmsg=True):
    metadata = _getapmv(base)

    latestMetadata = KeyLang(readcloud('.apmv'),'\n')

    # print(latestMetadata.get('?VERSION'), metadata.get('?VERSION').strip())
    if latestMetadata.get('?VERSION') != metadata.get('?VERSION').strip():
        if sendmsg:
            print(spectrum.subtitle('Your current APM Version [{cv}] can be updated to the latest version [{lv}]. Run apm upgrade to do so.').format(cv=metadata.get('?VERSION'),lv=latestMetadata.get('?VERSION') or '?unknown'))
        else: return True

import time

def attempt(func, message, verbose):
    arg = None
    print(spectrum.bold('{msg}   ◦ '.format(msg=message)), end='\r')
    try:
        arg = func()
        print(spectrum.success('{msg}   • '.format(msg=message)))
    except:
        print(spectrum.error('{msg}   ! '.format(msg=message)))
    
    if verbose:
        print('[VERBOSE]: '+str(arg))
    return arg

def FileNote(setnotation, iprefix=''):
    # sample: functions(*)+setup.py+apm.sh+apmdev.sh+README.md
    # nodes = setnotation.strip().split('+')

    # for node in nodes:
    #     if '(' and ')' in node:
    #         # folder
    #         items = node.split('(')[1].replace(')','')
    #         if '+' in items:
    #             items = FileNote(items)

    def parseNodeSet(nodeSetData, prefix=''):
        print(nodeSetData+'\n')
        # nodeSetData e.g. Wow.py+Great.py
        nodes = nodeSetData.strip().split('+')

        outputBuffer = []
        for node in nodes:
            outputBuffer.append(prefix.strip()+node.strip())
        return outputBuffer

    blocks = setnotation.strip().split(',')

    output = []

    for block in blocks:
        if '(' and ')' in block:
            # folder
            newPrefix = iprefix + '/' + block.split('(')[0]
            blockContents = block.split('(')[1].replace(')','')
            folderout = FileNote(blockContents, newPrefix)
            output += folderout
        else:
            parseNodeSet(block, iprefix)
    return output
    
def UPDATE_APM(base, verbose=False):
    if checkv(base, False):
        print(spectrum.title('\n\nUPGRADING APM'))
        print('-------------\n')

        def getupdset():
            latestMetadata = KeyLang(readcloud('.apmv'),'\n')
            updset = latestMetadata.get('?UPDATE_SET')
            return updset
        updset = attempt(getupdset, 'FETCHING UPDATE SET', verbose)

        def getfiles():
            return FileNote(updset)
            
        files = attempt(getfiles, 'INTERPRETING UPDATE SET', verbose)
        

        print('\n\n')

