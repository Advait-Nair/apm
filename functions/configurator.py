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


_zshpath=baseLoc+'/'+_zsh
_bashpath=baseLoc+'/'+_bash



print(baseLoc)
def config_zrc():
    if not exists(_zshpath):
        open(_zshpath, 'w')
    zrc = None
    try:
        zrc = open(baseLoc+_zsh,'r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: ZSH CONFIG FAIL: Likely rc does not exist.'))
        return
    try:
        print('PROCESS: ZSH CONFIG')
        open(baseLoc+_zsh,'w').write(zrc+zpc)
        print(success('PROCESS: ZSH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: ZSH CONFIG ERROR'))
        open(baseLoc+_zsh,'w').write(zrc)

def config_bash_rc():
    if not exists(_bashpath):
        open(_bashpath, 'w')
    bash_rc = None
    try:
        bash_rc = open(baseLoc+_bash,'r').read().replace(zpc, '').replace(bpc, '')
    except:
        print(error('PROCESS: BASH CONFIG FAIL: Likely rc does not exist.'))
        return
    try:
        print('PROCESS: BASH CONFIG')
        open(baseLoc+_bash,'w').write(bash_rc+bpc)
        print(success('PROCESS: BASH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: BASH CONFIG ERROR'))
        open(baseLoc+_bash,'w').write(bash_rc)

def config_apmshell(np):
    print('PROCESS: APM.SH CONFIG')
    
    replacebin = 'bash'
    newbin = 'zsh'

    replacing = _zsh
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
    
