import sys
import os
from spectrum import col, title, subtitle, italic, bold, error, success
# from slideprint import print
from apmfunc import arglen, loadFileOntoCurrentDirectory, unloadFileFromDirectory, verifyModuleInformationIntegrity, formatBase, getAllModules, formatModuleList, vwd, gwd, checkExistenceOfFile, isdepr

from apmex2 import restore, addRow, deleteRow, prettify, uglify, getData, filterData, getV, customBackup, backupToCustom, removeCustomBackup, getBackups, getFile, x

from apmmoduleinfoextractor import extract, formatMetadata

from help import apmhelp

verifyModuleInformationIntegrity()




sysprompt = "vwd"
if sys.argv and len(sys.argv) > 2:
    sysprompt = sys.argv[2]

from update import checkv, UPDATE_APM


# ! Zero-arg flag definers
def zeroFlags(flag, mlist):
    mlist2=[]
    if flag == '-rd':
        for file in mlist:
            # print(file)
            if not isdepr(sys.argv[0], file, True):
                mlist2.append(file)
    else:
        mlist2 = mlist
    return mlist2

def cleanList(xlist):
    return list(dict.fromkeys(xlist))

def main(prompt):
    uglify(sys.argv[0])
    flag = ''
    if arglen(sys.argv, 4):
        flag = sys.argv[4]

    if prompt == 'load':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component you wish to load onto your current directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            loadFileOntoCurrentDirectory(sys.argv[0], componentId, flag)

    elif prompt == 'upgrade':
        v = False
        if arglen(sys.argv, 3):
            if sys.argv[3] == '-v' or sys.argv[3] == '-verbose':
                v = True
        UPDATE_APM(formatBase(sys.argv[0],'/'), v)

    elif prompt == 'vwd':
        vwd(sys.argv[0])
    elif prompt == 'gwd':
        # TODO visualise whole working directory and identify what has to be updated
        gwd(sys.argv[0])

    elif prompt == 'view':
        # print(title('View All Components'))
        allModules = getAllModules(sys.argv[0])
        mlist = []

        if not arglen(sys.argv, 3):
            mlist = allModules
        elif len(sys.argv) == 4:
            mlist = zeroFlags(sys.argv[3], allModules)

            # ! Plus one argument error thrower
            if sys.argv[3] == '-ifn':
                print(error('What are you trying to in file name ifn sort? Nothing?'))
        
        elif arglen(sys.argv, 4):
            i = 0
            for arg in sys.argv:

                if i >= 3 and i <= len(sys.argv) - 2:
                    # print(i, len(sys.argv), sys.argv[i+3])
                    flag=sys.argv[i].strip().lower() # odd is a flag
                    filterc=sys.argv[i+1].strip().lower() # even is a filter

                    # ! Flag definers
                    if flag == '-ifn':
                        for file in allModules:
                            for filteri in filterc.strip().split(' '):
                                if filteri in file: mlist.append(file)
                
                i+=1
            
            for arg in sys.argv:
                # print(12)
                mlist = zeroFlags(arg, mlist)


        mlist = cleanList(mlist)
        p = formatModuleList(sys.argv[0], mlist)
        # ! NOT DEBUG!
        print(p)


    elif prompt == 'restoremaster':
        print(title('Restoring Master'))
        restore(formatBase(sys.argv[0], '/masterdata.apm'))
        print(success('Restored'))

    elif prompt == 'rsv':
        if not arglen(sys.argv, 3):
            print(error('No save id has been specified.'))
        else:
            id = sys.argv[3]
            customBackup(sys.argv[0], id)
    
    elif prompt == 'getrsv':
        if not arglen(sys.argv, 3):
            print(error('No save id has been specified.'))
        else:
            id = sys.argv[3]
            backupToCustom(sys.argv[0], id)
    
    elif prompt == 'delrsv':
        if not arglen(sys.argv, 3):
            print(error('No save id has been specified.'))
        else:
            id = sys.argv[3]
            removeCustomBackup(sys.argv[0], id)
    
    elif prompt == 'listrsv':
        saves = getBackups(sys.argv[0])

        print(bold('rsv: saves'))
        for save in saves:
            text = '-> {id} [{save}]'.format(id=save.replace('masterdata.apmc.', ''), save=save)
            print(italic(text))


    elif prompt == 'unload':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component you wish to unload off your current directory!'))
        else:
            print(title('Unload A Component'))
            unloadFileFromDirectory(sys.argv[0], sys.argv[3])

    elif prompt == 'update':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component you wish to update in your current directory!'))
        else:
            print(title('Update A Component'))
            print(subtitle('Removing component...'))
            unloadFileFromDirectory(sys.argv[0], sys.argv[3])
            print(subtitle('Reinstalling component...'))
            loadFileOntoCurrentDirectory(sys.argv[0], sys.argv[3], '-f')
    

    elif prompt == 'about':
        print(title('\nAbout APM (Adva Package Manager)')+'\n')
        print(
            """
Adva Package Manager, abbreviated to apm, is a complete, localised file duplication, tracking and managing system that allows users to streamline, speed up and centralise their workflow. It utilises a CLI (Command Line Interface) from which the apm software can be easily accessed.


{bst}HOW IT WORKS{r}

APM allows you to create 'components', also known as 'modules', which are files you upload to APM. Think of this file as the source file. You can upload as many as you want.

These modules can then be 'loaded' onto a working directory. This means that you take one of your components, duplicate it and insert it into your directory.

What APM does for you is that it allows you to perform this operation with ease. Once you have loaded a file, it will have to be managed and monitored.

Take this example: A component file had a mistake or error inside it, thus you need to update it. This file was used in quite a few projects, thus what APM allows you to do is update the version of each file, as well as the version of other files and what needs to be changed.

This is just a taste of what APM lets you do.



{bst}CREDITS & INFORMATION{r}

Developed by Advait Nair,
Advait Nair © 2023
APM, Adva Package Manager

{br}
Do not modify this software. Any modification could result in intellectual property loss or file destruction.

I take no liability for any damage to any individual, item or entity that has been inflicted onto by the software. You use this software at your own risk. There will always be bugs and kinks. Be careful, you have been warned. {r}

Use apm help for commands!

            """.format(br=col('error'),bst=col('info'),r=col(''))
        )
    
    elif prompt == 'globalunloadall':
        confirm = input(error('\nTHIS WILL DELETE EVERY COMPONENT INSTALLED IN YOUR WHOLE SYSTEM. PROJECTS MAY STOP WORKING. YOU HAVE BEEN WARNED.\n\n[type CONFIRM press ENTER]\n[type anything else to cancel] > '))

        if 'confirm' in confirm.lower():
            print(subtitle('\nDeleting all installed components...')+'\n')

            data = getData(sys.argv[0])
            aliases = filterData(data, '@a')
            
            for node in aliases:
                v = getV(node)
                name = v[1]
                loc = v[3]
                path = loc + '/' + name
                if checkExistenceOfFile(path):
                    print(error('REMOVE:  '+name))
                    os.remove(path)
                else:
                    print(italic('Registry Incorrect:  '+name))
            
            c = filterData(data, '@c')
            formatted = ''
            for cpoint in c:
                cpoint2 = getV(cpoint)
                componentPoint = x('@c', cpoint2[1], cpoint2[2], 0)

                formatted += componentPoint
            getFile(sys.argv[0], 'w').write(formatted)
            print(success('Wiped all alias components.'))


    # elif prompt == 'testitem':
    #     addRow(sys.argv[0], 't', 'component.ts', '24', '/Users/sample')
    # elif prompt == 'testitem2':
    #     addRow(sys.argv[0], 's', 'component.ts', '967', '/Users/sample2')
    # elif prompt == 'testitem3':
    #     deleteRow(sys.argv[0], 's', 'component.ts', '967', '/Users/sample2')
    elif prompt == 'desc':
        info = extract(sys.argv[3].strip(),
            formatBase(sys.argv[0], '/modules/'+sys.argv[3].strip()))
        print(subtitle('Information on ' + info.get('name')))
        print(
            formatMetadata(info, False)
        )

    elif prompt == 'prettify':
        prettify(sys.argv[0])
    elif prompt == 'uglify':
        uglify(sys.argv[0])
    

    # Misc prompts

    elif prompt == 'help':
        print(apmhelp)

    # Shell Escape & Doesn't Exist
    elif prompt == 'exit' and sysprompt == "shell":
        return -5
    
    else:
        print(error('That is not a command. Change something up and try again!'))



# Shell Toggle

# if sysprompt == "shell":
#     stay = True
#     while stay:
#         inputPrompt = str(input('apm >>> '))
#         returnedStatus = main(inputPrompt)
#         if(returnedStatus == -5):
#             stay = False
# else:
main(sysprompt)
if sysprompt != 'upgrade':
    checkv(formatBase(sys.argv[0],'/'))