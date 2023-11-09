from functions.spectrum import success, error, italic
import os


def exists(filePath):
    try:
        open(filePath,'r')
        return True
    except:
        return False


_zsh='.zshrc'
_bash='.bashrc'

if not exists('~/'+_zsh):
    open('~/'+_zsh, 'n')
if not exists('~/'+_bash):
    open('~/'+_bash, 'n')


zpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source {_zsh}"\n
""".format(_zsh=_zsh)
bpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source {_bash}"\n
""".format(_bash=_bash)
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
        zprofile = open(baseLoc+_zsh,'r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: ZSH CONFIG FAIL: Likely profile does not exist.'))
        return
    try:
        print('PROCESS: ZSH CONFIG')
        open(baseLoc+_zsh,'w').write(zprofile+zpc)
        print(success('PROCESS: ZSH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: ZSH CONFIG ERROR'))
        open(baseLoc+_zsh,'w').write(zprofile)

def config_bash_profile():
    bash_profile = None
    try:
        bash_profile = open(baseLoc+_bash,'r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: BASH CONFIG FAIL: Likely profile does not exist.'))
        return
    try:
        print('PROCESS: BASH CONFIG')
        open(baseLoc+_bash,'w').write(bash_profile+bpc)
        print(success('PROCESS: BASH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: BASH CONFIG ERROR'))
        open(baseLoc+_bash,'w').write(bash_profile)

def config_apmshell(np):
    print('PROCESS: APM.SH CONFIG')
    replacing = _zsh
    replacebin = 'bash'
    newbin = 'zsh'
    if np == _zsh:
        replacing = _bash
    elif np == _bash:
        replacebin = 'zsh'
        newbin = 'bash'

    try:
        apmsh = open(apmshloc, 'r').read()
        open(apmshloc, 'w').write(apmsh.replace(replacing,np).replace('bin/'+replacebin,'bin/'+newbin))
        print(success('PROCESS: APM.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APM.SH CONFIG FAIL'))


    try:
        print('PROCESS: APMDEV.SH CONFIG')
        apmdevsh = open(apmdevshloc, 'r').read()
        open(apmdevshloc, 'w').write(apmdevsh.replace(replacing,np).replace('bin/'+replacebin,'bin/'+newbin))
        print(success('PROCESS: APMDEV.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APMDEV.SH CONFIG FAIL'))
    
