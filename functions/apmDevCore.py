import sys
from spectrum import col, title, subtitle, italic, bold, error, success

from apmfunc import arglen, loadFileOntoCurrentDirectory, unloadFileFromDirectory, verifyModuleInformationIntegrity, formatBase, createComponent, deprecation, deleteComponent

from apmex2 import restore, addRow, deleteRow, prettify, uglify
from help import apmhelp

apmdevhelp = apmhelp+"""
{2}APMDEV FUNCTIONS:{4}

{4}{3}apmdev create{1} - load a file on the cwd to Root APM

{4}{3}apmdev update{1} - update an existing file to Root APM

{4}{3}apmdev depr{1} - Deprecate a module

{4}{3}apmdev undepr{1} - Undeprecate a module

{4}{3}apmdev delete{1} - Delete a module

{4}{3}apmdev metagen{1} - Generate Metadata

{4}{3}apm view{1} - view all installed components.
        -> -s: Filter components by name or type
            -> name:NAME type:FILETYPE
""".format(
    col('info-h'), # 0 is title
    col('italic'), # 1 is italic
    col('info'), # 2 is heading
    col('bold'), # 3 is bold
    col('straight') # 4 is normal
)


verifyModuleInformationIntegrity()
 


sysprompt = "help"
if sys.argv and len(sys.argv) > 2:
    sysprompt = sys.argv[2]



def main(prompt):
    uglify(sys.argv[0])

    if prompt == 'create':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component identifier you wish to load onto Root APM! It must be on this working directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            createComponent(sys.argv[0], sys.argv[3])

    elif prompt == 'update':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component identifier you wish to update at the Root APM! It must be on this working directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            createComponent(sys.argv[0], componentId, True, True)

    elif prompt == 'depr':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component identifier you wish to deprecate at the Root APM! It must be on this working directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            deprecation(sys.argv[0], componentId, True)
    
    elif prompt == 'undepr':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component identifier you wish to undeprecate at the Root APM! It must be on this working directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            deprecation(sys.argv[0], componentId, False)

    elif prompt == 'delete':
        if not arglen(sys.argv, 3):
            print(error('Please specify the component identifier you wish to delete at the Root APM! It must be on this working directory!'))
        else:
            # pwd apm load COMPONENT i = 3
            componentId = sys.argv[3]
            confirm = input(error('\nAre you sure you want to delete "{0}"? It will no longer be connected to Root APM and APM cannot work with the component anymore unless it is reinserted.\n\n[type CONFIRM press ENTER]\n[type anything else to cancel] > '.format(componentId)))

            if 'confirm' in confirm.lower():
                print(subtitle('\nDeleting component...')+'\n')
                deleteComponent(sys.argv[0], componentId, True)

    # elif prompt == 'view':
    #     print(title('View All Components'))

    
    elif prompt == 'help':
        print(apmdevhelp)

    elif prompt == 'metagen':
        print(title('\nMetadata Generator\n'))
        print(italic('Follow the prompts, use COMPL to exit and finish.'))
        print(error('NOTE: Name, Iteration and Descriptions are mandatory!\n'))

        name = input('Name > ').strip()
        iteration = input('Iteration > ').strip()
        desc = input('Description > ').strip()

        e = False
        try:
            inti = int(iteration)
            if inti < 0:
                e = True
        except:
            e = True

        
        if e:
            print(error('Iteration must be a positive integer!'))
            return

        if(name and iteration and desc):
            print(success('\nMandatory Fields Complete! You may add additional fields.\nA commit field is highly recommended for version change info and clarity.\n'))
        else:
            print(error('\nNice try, fill them all please.'))
            return
        

        metaDict = {
            'name': name,
            'iteration': iteration,
            'description': desc
        }
        
        compl = False
        
        print('Additional Tags: (COMPL to finish)\n')
        while not compl:
            tag = input('\nTag? Name > ').strip().lower()


            if tag == 'compl':
                compl = True
                break
            value = input('{tag} Value? > '.format(tag=tag)).strip().lower()

            if tag == 'name' or tag == 'description' or tag == 'iteration':
                print(error('Do not use these parameters again!'))
            else:
                metaDict[tag] = value

        mapped = ''

        for tag in dict.keys(metaDict):
            mapped += '{tag}:: {value}\n'.format(tag=tag, value=metaDict[tag])
        
        out = '\n%%%apm%%%\n\n{content}\n%%%apm%%%\n'.format(content=mapped)
        print(success('\n\nOUTPUT'))
        print(out + '\n')
        exportapmeta = input('Do you wish to export this to a .apmeta file? [Y/N] > ').strip().lower()

        if exportapmeta in 'yes ye ya yeh yeah yea yess yeahs yee yeahh':
            # Export
            f = open('{name}-metagen.apmeta'.format(name=name), 'w')
            f.write(out)
        else:
            print(success('\nProcess Complete.\n'))




main(sysprompt)