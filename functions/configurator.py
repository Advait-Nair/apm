from functions.spectrum import success, error, italic

zpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source .zprofile"\n
"""
bpc="""\n\nalias apm=~/apm/apm.sh
alias apmdev=~/apm/apmdev.sh
alias zpr="cd ~ && source .bash_profile"\n
"""

def config_zprofile():
    zprofile = open('~/.zprofile','r')
    try:
        print('PROCESS: ZPROFILE CONFIG')
        open('~/.zprofile','w').write(zprofile+zpc)
        print(success('PROCESS: ZPROFILE CONFIG SUCCESS'))
    except:
        print(error('PROCESS: ZPROFILE CONFIG ERROR'))
        open('~/.zprofile','w').write(zprofile)

def config_bash_profile():
    bash_profile = open('~/.bash_profile','r')
    try:
        print('PROCESS: BASH_PROFILE CONFIG')
        open('~/.bash_profile','w').write(bash_profile+bpc)
        print(success('PROCESS: BASH_PROFILE CONFIG SUCCESS'))
    except:
        print(error('PROCESS: BASH_PROFILE CONFIG ERROR'))
        open('~/.bash_profile','w').write(bash_profile)

def config_apmshell(np):
    print('PROCESS: APM.SH CONFIG')
    try:
        apmsh = open('../apm.sh', 'r').read()
        open('../apm.sh', 'w').write(apmsh.replace('.zprofile',np))
        print(success('PROCESS: APM.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APM.SH CONFIG ERROR'))


    try:
        print('PROCESS: APMDEV.SH CONFIG')
        apmdevsh = open('../apmdev.sh', 'r').read()
        open('../apmdev.sh', 'w').write(apmdevsh.replace('.zprofile',np))
        print(success('PROCESS: APMDEV.SH CONFIG SUCCESS'))
    except:
        print(error('PROCESS: APMDEV.SH CONFIG ERROR'))
