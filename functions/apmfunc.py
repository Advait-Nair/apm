from spectrum import success, error, italic, title, subtitle, col
# from apmextensioninteractor import APMInteractor
from apmmoduleinfoextractor import extract, formatMetadata
import os


def formatBase(base, path):

    if 'apmDevCore' in base:
        return base.replace('/functions/apmDevCore.py', path)
    else:
        return base.replace('/functions/apmCore.py', path)

from apmex2 import getLatest, editRow, addRow, deleteRow, manageRecovery, filterData, getData, getV

def checkExistenceOfFile(filePath):
    existence = None

    try:
        open(filePath)
        existence = True
    except:
        existence = False

    return existence


def loadFileOntoCurrentDirectory(base, fileNameRaw, flag):
    cwd = os.getcwd()

    fileName = fileNameRaw.lower()
    # fileName = fileNameRaw

    # Check if file exists
    moduleFilePath = formatBase(base, '/modules/{0}'.format(fileName))

    exists = checkExistenceOfFile(moduleFilePath)

    isDeprecated = isdepr(base, fileName)

    if not exists:
        print(
            error('This component does not exist! {0}'.format(italic('Run apm view to view all components.')))
        )
        return False
    
    if isDeprecated and not flag.strip() == '-f':
        print(error('This is a deprecated component.\nRun this command with a -f command to install anyway.'))
        return False
    

    print(title('\nLoading A Component'))
    # pwd apm load COMPONENT i = 3
    
    if isDeprecated:
        print(error(fileName + ' - DEPRECATED'))
    else:
        print(italic(fileName))


    data = extract(fileName, moduleFilePath)

    print(formatMetadata(data, True))

    base=formatBase(base, '/masterdata.apm')
    manageRecovery(base)

    moduleData = open(moduleFilePath, 'r').read()
    newFilePath = cwd+'/'+fileName
    if checkExistenceOfFile(newFilePath):
        print(subtitle('Component already exists in this working directory!'))
        return False
    alias = open(newFilePath, 'w').write(moduleData)

    latest = getLatest(base, fileName)

    if checkExistenceOfFile(newFilePath):
        # Delete older version info
        fileInfo = filterData(getData(base), '@a|'+fileName+'|'+cwd)
        # print(fileInfo, '@a|'+fileName+'|'+cwd)

        if len(fileInfo) >= 1:
            # print(fileInfo)
            for file in fileInfo:
                v = getV(file)
                deleteRow(base, '@a', fileName, v[2], cwd)

        addRow(base, '@a', fileName, latest, cwd)


        sic = filterData(getData(base), '@c|'+fileName)
        if len(sic) >= 1:
            sic = int(getV(sic[0])[3])
            nsic = sic + 1
            editRow(base, '@c', fileName, latest, sic, rnv3=nsic)
        

        print(success('Component Successfully Loaded!\n'))
    else:
        print(error('Something went wrong. Try again.\n'))


def downSIC(base, fileName, latest):
    sic = filterData(getData(base), '@c|'+fileName)
    if len(sic) >= 1:
        sic = int(getV(sic[0])[3])
        nsic = sic - 1
        editRow(base, '@c', fileName, latest, sic, rnv3=nsic)

def unloadFileFromDirectory(base, fileNameRaw):

    fileName = fileNameRaw.lower()
    # fileName = fileNameRaw

    cwd = os.getcwd()

    # print(fileName)
    wildcard = 'all' in fileName.strip()

    if wildcard:
        print(subtitle('Unloading All Components'))
        modules = getAllModules(base)

        deleted = 'Deleted:\n'
        for module in modules:
            fp = cwd + '/' + module
            # print(fp)
            if checkExistenceOfFile(fp):
                deleteRow(base, '@a', module, '*a', cwd)
                os.remove(fp)
                downSIC(base, fileName, getLatest(base, fileName))
                deleted += module + '\n'
        print(italic(deleted))
        return False

    elif not wildcard and not checkExistenceOfFile(
        formatBase(base, '/modules/{0}'.format(fileName))
    ):
        print(error('There is no such Component as "{0}"'.format(fileName)))
        return False


    filePath = cwd + '/' + fileName

    exists = checkExistenceOfFile(filePath)

    if exists:
        # interactor.removeAliasRow([fileName, interactor.getLatest(fileName), cwd])
        manageRecovery(base)
        deleteRow(base, '@a', fileName, '*a', cwd)
        os.remove(filePath)
        downSIC(base, fileName, getLatest(base, fileName))
        print(success('Component successfully unloaded!'))
    else:
        deleteRow(base, '@a', fileName, '*a', cwd)
        print(error('Component "{0}" does not exist in this directory.'.format(fileName)))



def arglen(argv, length):
    if len(argv) >= length+1:
        return True
    else:
        return False
    
# View

def getAllModules(base):
    dirlist = os.listdir(formatBase(base, '/modules'))
    return dirlist


def intoBulletPoint(base, isdepr, no, info, fileName):
    r = ''
    if isdepr:
        r = str(no)+'. {5}' + info.get('name') + ' - DEPRECATED -{3}{1} ['+fileName+']{4}\n'
    else:
        r = str(no)+'. {2}' + info.get('name') + '{3}{1} ['+fileName+']{4}\n'
    
    # print(base, isdepr, no, info, fileName)

    skipPrint = 'iteration, sameIteratedCopies, size'
    for tag in dict.keys(info):
        jump = False

        for skip in skipPrint.split(','):
            if skip.strip() == tag:
                jump = True
        
        if not jump:
            content = info.get(tag)
            r+= '   -> {3}'+tag+': {4}{1}'+content+'{4}\n'
    registeredCopies = filterData(getData(base), '@c|'+fileName.lower())
    # print(registeredCopies)
    if len(registeredCopies) != 0:
        registeredCopies = getV(registeredCopies[0])[3]
    else:
        registeredCopies = 'x'

    r+='\n    {3}--> Latest Version: {4}{1}'+info.get('iteration')+'{4}\n'
    r+='    {3}--> Number of Registered Copies: {4}{1}'+registeredCopies+'{4}\n'
    r+='    {3}--> Size: {4}{1}'+info.get('size')+'{4}\n'
    # r+='\n    {3}--> Latest Version: {1}{d}{4}\n'.format(d=info.get('iteration'))
    # r+='    {3}--> Number of Registered Copies: {1}{d}{4}\n'.format(d=registeredCopies)
    # r+='    {3}--> Size: {1}{d}{4}\n'.format(d=info.get('size'))

    return r

def formatModuleList(base, list):

    p = """\n{0}APM MODULES LIST{4}\n"""

    listNo = 1
    for file in list:
        isdeprecated = isdepr(base, file, True)
        # print(file, isdeprecated)

        fileInfo = extract(file, formatBase(base, '/modules/'+file))
        # print(file, fileInfo)
        text = intoBulletPoint(base, isdeprecated, listNo, fileInfo, file)
        if text:
            p += ('\n\n'+text+'\n\n')

        listNo += 1
    return p.format(
    col('info-h'), # 0 is title
    col('italic'), # 1 is italic
    col('info'), # 2 is heading
    col('bold'), # 3 is bold
    col('straight'), # 4 is normal
    col('error') # 5 is error
)

def verifyModuleInformationIntegrity():
    print(italic('Integrity Check...'))



# apmdev

def createComponent(base, fileName, overwrite=False, throwErrorOnOverwriteAndNotExists=False):
    cwd = os.getcwd()

    loc = formatBase(base, '/modules/')+fileName
    tbuLoc = cwd+'/'+fileName

    if not fileName:
        return False
    
    if checkExistenceOfFile(loc) and not overwrite:
        print(error('The specified file name is already a registered component!'))
        return False
    
    if not checkExistenceOfFile(loc) and overwrite and throwErrorOnOverwriteAndNotExists and checkExistenceOfFile(tbuLoc):
        print(error('This file does not exist at the Root APM!'))
        return False


    # try:

    # Flash file onto RAPM
    contents = open(tbuLoc, 'r').read()
    f = open(loc, 'w')
    f.write(contents)

    # Upload data onto RAPM

    iteration = extract(fileName, tbuLoc).get('iteration')
    filtered = filterData(getData(base), '@c|'+fileName)

    v = None
    lastIteration = None

    if len(filtered) >= 1:
        v = getV(filtered[0])
        lastIteration = v[2]


    if not iteration:
        print(error('An iteration declaration in the file metadata is needed in order to be uploaded to Root APM.'))
        return False
    
    if lastIteration and iteration == lastIteration:
        print(error('Your version is the same. Change it.'))
        return False

    if not overwrite:
        addRow(base, 'c', fileName, iteration, 0)
    elif overwrite and v:
        editRow(base, 'c',  v[1], v[2], v[3],  fileName, iteration, 0)

    # Success!
    print(success('Successfully completed creation/update process!'))
    # except:
    #     print(error('File "{f}" does not exist in this directory.').format(f=fileName))

def deleteComponent(base, componentName, throwErrorOnNotExists):
    componentLoc = formatBase(base, '/modules/{0}'.format(componentName))

    try:
        os.remove(componentLoc)

        data = filterData(getData(base), '@c|'+componentName)

        if len(data) >= 1:
            v = getV(data[0])
            deleteRow(base, '@c', v[1], v[2], v[3])
        else: print(italic('Component is not registered at Root APM'))
    except:
        if throwErrorOnNotExists:
            print(error('"{0}" is not a component at Root APM! Operation incomplete.'.format(componentName)))







def deprecation(base, componentName, deprecate):

    # Upload data onto RAPM
    filtered = filterData(getData(base), '@c|'+componentName)
    mfp=formatBase(base, '/modules/{0}'.format(componentName))
    storedVersion = extract(componentName, mfp).get('iteration')

    v = None

    if len(filtered) >= 1:
        v = getV(filtered[0])

    if deprecate:
        if v:
            editRow(base, 'c', v[1], v[2], v[3], rnv2=-5)
            print(success('File deprecated successfully. No longer can it be loaded or updated.'))
        else:
            print(error('This component has not been registered on Root APM.'))
    else:
        if v:
            editRow(base, 'c', v[1], v[2], v[3], rnv2=storedVersion)
            print(success('File undeprecated successfully.'.format(componentName)))
        else:
            print(error('This component has not been registered on Root APM.'))

def isdepr(base, componentName, silenceError=False):
    filtered = filterData(getData(base), '@c|'+componentName)

    v = None

    if len(filtered) >= 1:
        v = getV(filtered[0])
    elif not silenceError:
        print(error('Internal Error: Failed to retrieve deprecation status!'))
        return False
    
    if v:
        return v[2] == '-5'

def gwd(base, vwdEnabled=False):
    cwd = os.getcwd()

    # Begin by looping through all components & storing latest version & name
    components = filterData(getData(base), '@c')

    compIterInfo = {}

    for component in components:
        v = getV(component)
        name = v[1]
        iteration = v[2]
        compIterInfo[name] = iteration

    # Then we look at all aliases and see their versions

    aliases = filterData(getData(base), '@a')
    # print(aliases)

    unsynced = []

    for alias in aliases:
        v = getV(alias)
        name = v[1]
        iteration = v[2]

        if compIterInfo.get(name) != iteration:
            unsynced.append(alias)


    if not vwdEnabled:
        print(title('\nGlobal Directory Component Visualiser\n'))
        
        for alias in aliases:
            v = getV(alias)
            # print(v, alias)
            if len(v) >= 4:
                status = error('UNSYNCED')

                tv = compIterInfo.get(v[1])
                if tv == '-5':
                    tv = error('DEPRECATED')

                if tv == v[2]:
                    status = success('SYNCED')

                content = '{afn} is {us} at {loc}  -  [  {cv} --> {tv}  ]\n'.format(afn=subtitle(v[1]),us=status,cv=v[2],tv=tv,loc=italic(v[3]))
                print(content)
    else:
        print(title('\nLocal Directory Component Visualiser\n'))
        
        for alias in aliases:
            v = getV(alias)

            incwd = v[3].strip() == cwd

            if incwd:
                if len(v) >= 4:
                    status = error('UNSYNCED')

                    tv = compIterInfo.get(v[1])
                    if tv == '-5':
                        tv = error('DEPRECATED')

                    if tv == v[2]:
                        status = success('SYNCED')

                    content = '{afn} is {us}  -  [  {cv} --> {tv}  ]\n'.format(afn=subtitle(v[1]),us=status,cv=v[2],tv=tv)
                    print(content)
    
    print(italic('Utilise commands such as apm update or apm unload to handle these component aliases.\n'))


def vwd(base):
    gwd(base, True)