# apm (Adva Package Manager)

Adva Package Manager, abbreviated to apm, is a complete, localised file duplication, tracking and managing system that allows users to streamline, speed up and centralise their workflow. It utilises a CLI (Command Line Interface) from which the apm software can be easily accessed.
<br>

## SETUP

### Information: Prerequistes
You need a machine running Unix, or an emulator capable of executing bash/zsh shell commands.

Python must be installed for apm to function. Git is recommended to clone this repo to your machine.

- Unix machine/emulator/VM
- Python 3
- Git (Recommended)


---

### Part I: Installation

1. Navigate to home directory:
```shell
cd ~
```
2. Clone repo to home directory: 
```shell
git clone https://github.com/Advait-Nair/apm.git
```

### Part II: Auto-setup

3. Navigate to your apm directory
```shell
cd ~/apm
```
4. Run setup.py
```shell
python3 setup.py
```
Tip: When running setup.py, to speed up the process, you can insert your shell, zsh or bash, as an argument.
```shell
python3 setup.py zsh/bash
```

## Part III: Enjoy!

Enjoy using APM. Do not forget to flag any bug reports for fixing as this is still an early version!

<br><br>
# Documentation

## HOW IT WORKS

APM allows you to create 'components', also known as 'modules', which are files you upload to APM. Think of this file as the source file. You can upload as many as you want.

These modules can then be 'loaded' onto a working directory. This means that you take one of your components, duplicate it and insert it into your directory.

What APM does for you is that it allows you to perform this operation with ease. Once you have loaded a file, it will have to be managed and monitored.

Take this example: A component file had a mistake or error inside it, thus you need to update it. This file was used in quite a few projects, thus what APM allows you to do is update the version of each file, as well as the version of other files and what needs to be changed.

This is just a taste of what APM lets you do.



## CREDITS & INFORMATION

Developed by Advait Nair,
Advait Nair © 2023
APM, Adva Package Manager


Do not modify this software. Any modification could result in intellectual property loss or file destruction.

I take no liability for any damage to any individual, item or entity that has been inflicted by the software. You use this software at your own risk. There will always be bugs and kinks. Be careful, you have been warned.
<br><br><br>
# Commands
Use apm help for commands!

apm about - About apm
<br>

## FUNCTIONS

apm vwd or apm - View the component alias statuses in the current working directory.

apm gwd - View the component alias statuses globally.

apm help - prints this help message.

apm load - load a component onto your current directory.

apm unload - unload a component off your current directory.

apm update - Unload & Reload a component, updating it.

apm restoremaster - Restore the last cached version of masterdata.apm.

apm uglify - Compact masterdata.apm, saving space and allowing operations to be performed onto and with it.

apm prettify - Expand masterdata.apm and make it readable.

apm globalunloadall - Unload every component in existence. WARNING! PROJECTS MAY STOP WORKING!

## RESTORE SAVED (RSV)
apm getrsv - Use a stored manual backup.
apm rsv - Create a custom manual backup.
apm delrsv - Delete a custom manual backup.
apm listrsv - Get all manual backups currently in existence.

apm view - view all installed components.

  - *In File Name Match Filter*: __-ifn__:
    Show In File Name matches with the provided substring, separate each requirement by a whitespace, use multiple -ifn to create "or" ifn conditionals.
  e.g. apm view -ifn .ts -ifn app -rd, list all components with a .ts or app in the filename. Exclude deprecated items. 
  - *Remove Deprecated Filter*: __-rd__:
    Remove Deprecated from list


## APMDEV FUNCTIONS:

apmdev create - load a file on the cwd to Root APM

apmdev update - update an existing file to Root APM

apmdev depr - Deprecate a module

apmdev undepr - Undeprecate a module

apmdev delete - Delete a module

apm view - view all installed components.
        -> -s: Filter components by name or type
            -> name:NAME type:FILETYPE
