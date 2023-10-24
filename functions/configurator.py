from functions.spectrum import success, error, italic
import os
zpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source .zprofile"\n
"""
bpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source .bash_profile"\n
"""
baseLoc = os.getcwd()
if 'apm' in baseLoc:
    baseLoc = baseLoc.replace('apm', '')
else:
    baseLoc = baseLoc + '/'

baseLoc = baseLoc.replace('//', '/')

apmshloc = baseLoc + 'apm/apm.sh'
apmdevshloc = baseLoc + 'apm/apmdev.sh'

print(baseLoc)
def config_zprofile():
    zprofile = None
    try:
        zprofile = open(baseLoc+'.zprofile','r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: ZPROFILE CONFIG FAIL: Likely profile does not exist.'))
        return
    try:
        print('PROCESS: ZPROFILE CONFIG')
        open(baseLoc+'.zprofile','w').write(zprofile+zpc)
        print(success('PROCESS: ZPROFILE CONFIG SUCCESS'))
    except:
        print(error('PROCESS: ZPROFILE CONFIG ERROR'))
        open(baseLoc+'.zprofile','w').write(zprofile)

def config_bash_profile():
    bash_profile = None
    try:
        bash_profile = open(baseLoc+'.bash_profile','r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: BASH_PROFILE CONFIG FAIL: Likely profile does not exist.'))
        return
    try:
        print('PROCESS: BASH_PROFILE CONFIG')
        open(baseLoc+'.bash_profile','w').write(bash_profile+bpc)
        print(success('PROCESS: BASH_PROFILE CONFIG SUCCESS'))
    except:
        print(error('PROCESS: BASH_PROFILE CONFIG ERROR'))
        open(baseLoc+'.bash_profile','w').write(bash_profile)

def config_apmshell(np):
    print('PROCESS: APM.SH CONFIG')
    replacing = '.zprofile'
    if np == '.zprofile':
        replacing = '.bash_profile'
    try:
        apmsh = open(apmshloc, 'r').read()
        open(apmshloc, 'w').write(apmsh.replace(replacing,np))
        print(success('PROCESS: APM.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APM.SH CONFIG FAIL'))


    try:
        print('PROCESS: APMDEV.SH CONFIG')
        apmdevsh = open(apmdevshloc, 'r').read()
        open(apmdevshloc, 'w').write(apmdevsh.replace(replacing,np))
        print(success('PROCESS: APMDEV.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APMDEV.SH CONFIG FAIL'))
