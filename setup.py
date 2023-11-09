from functions.spectrum import success, error, title, subtitle, italic, bold

from functions.configurator import config_apmshell, config_zrc, config_bash_rc

print(title('\nWELCOME TO APM!'))
print(italic('This setup guide will run you through some choices to configure APM for your machine.\n'))
input(italic('PRESS ANY KEY TO CONTINUE > '))
print('\n')

back = True
mode = 'zsh'
while back:
    shell = input(bold('Are you running a BASH or ZSH shell?: [BASH/ZSH] > '))
    confirmation = ''

    if shell.strip() in 'bash BASH':
        confirmation = input(bold('\nYou are running a bash shell: [ENTER for confirm, ANY OTHER KEY for cancel] > '))
        mode = 'bash'

    if shell.strip() in 'zsh ZSH':
        confirmation = input(bold('\nYou are running a zsh shell: [ENTER for confirm, ANY OTHER KEY for cancel] > '))
        mode = 'zsh'


    if confirmation.strip() == '':
        back = False
    else:
        print(italic('\nReturning...\n'))

if mode == 'zsh':
    print(subtitle('\nZSH CONFIG'))
    print(italic('apm has been zsh-configurated out of the box.\n'))

    config_zrc()
    config_apmshell('.zrc')
elif mode == 'bash':
    print(subtitle('\nBASH CONFIG'))
    print(italic('apm needs to be configured for bash.\n'))

    config_bash_rc()
    config_apmshell('.bashrc')


try:
    print('PROCESS: Creating masterdata.apm')
    md = open('masterdata.apm', 'x')
    print(success('PROCESS: masterdata.apm CREATION SUCCESS'))
except:
    print(error('ERROR: masterdata.apm CREATION FAIL: Likely already exists'))