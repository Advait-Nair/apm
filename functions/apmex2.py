# @tag|v1|v2|v3;
from apmfunc import formatBase
from spectrum import error, subtitle, success
from debug import dbg

import os
# Base Methods


def prettify(base):
    data = getData(base)
    formatted = data.replace(';',';\n').replace('|', ' | ')
    getFile(base, 'w').write(formatted)

def getData(base):
    lines = getFile(base, 'r').read().strip().replace('RestorationFailure01', '')
    return lines

def getDataLines(base):
    return getFile(base, 'r').readlines()

def uglify(base):
    # data = getData(base)
    # formatted = data.strip().replace(' | ', '|')
    # getFile(base, 'w').write(formatted)
    data = getDataLines(base)
    
    formatted = ''
    for line in data:
        formatted += line.strip().replace(' | ', '|')
    getFile(base, 'w').write(formatted)


def getFile(base, m):
    return open(formatBase(base, '/masterdata.apm'), m)

def x(tag,v1,v2,v3):
    return '@{0}|{1}|{2}|{3};'.format(tag.replace('@',''), v1.lower(),v2,v3)


def getV(node):
    return node.split('|')


# Manipulative & Observative Methods


def checkExistence(data, tag, v1,v2,v3):
    if x(tag,v1,v2,v3) in data:
        return True
    else: return False


def filterData(data, pipeSeparatedMatchers):
    matchers = pipeSeparatedMatchers.strip().split('|')
    dataNodes = data.strip().split(';')

    resultNodes = []

    # print(673, data,'\n\n', pipeSeparatedMatchers,'\n\n', matchers)

    # print(2, dataNodes)

    for node in dataNodes:
        # If data contains all matching criteria, we will add it to a results list and return it

        # v is ['@c', 'component.ts', '24', '48'] from @c|component.ts|24|48;
        v = getV(node)
        # print(v)

        # For each item in v, e.g. '@c' is vi
        passedArguments = 0
        for vi in v:
            # For each matcher passed in, if they match that is recorded.
            # print(vi)
            for matcher in matchers:
                # print(matcher, matcher.strip() == vi.strip())
                if matcher.strip() == vi.strip():
                    # print(matcher, vi, passedArguments, 8567)
                    passedArguments += 1
        # print(passedArguments)
        # print(len(matchers))
        # if pipeSeparatedMatchers == '@a|c.ts|/Volumes/Sandisk/Client Data and Products/External Contracts/Altris_Trading_CL01':
            # dbg('match', [node,passedArguments,pipeSeparatedMatchers, len(matchers)],'node,passrate,psm,rpr')
        if passedArguments == len(matchers):
            resultNodes.append(node)
    
    # dbg('filterOut',[pipeSeparatedMatchers,resultNodes, len(matchers)],'psm,resnodes,matcherlen')

    return resultNodes

def deleteRow(base, tag, v1,v2,v3):
    uglify(base)
    data = getData(base)

    # dbg('deleteRow', [tag,v1,v2,v3],'tag,v1,v2,v3')


    if '*a' != v2:
        data = data.replace(x(tag, v1,v2,v3), '')
        getFile(base, 'w').write(data)
    else:
        matches = filterData(data, tag+'|'+v1+'|'+v3)

        if len(matches) >= 1:
            nv2 = getV(matches[0])[2]
            # print(12123, base, tag, v1, nv2, v3)
            # deleteRow(base, tag, v1, nv2, v3)
            data = data.strip().replace(x(tag.strip(),v1.strip(),nv2.strip(),v3.strip()), '')
            # print(data, 999)
            getFile(base, 'w').write(data)


def addRow(base, tag, v1,v2,v3):
    uglify(base)
    data = getData(base)
    f=getFile(base, 'w')

    if 'a' in tag and not checkExistence(data, tag, v1,v2,v3):
        filtered = filterData(data, '@a|'+v3+'|'+v1)
        # print(filtered, 234, '@a|'+v3+'|'+v1)

        for node in filtered:
            v = getV(node)
            deleteRow(base, v[0], v[1], v[2], v[3])
        
        f.write(data+x(tag, v1,v2,v3))
    elif not checkExistence(data, tag, v1,v2,v3):
        f.write(data+x(tag, v1,v2,v3))
    else:
        print(error('apmex2: Exact entry already exists within master file!'))
        f.write(data)
    
def editRow(base, tag,v1,v2,v3, rnv1=-669,rnv2=-669,rnv3=-669):
    uglify(base)
    data = getData(base)
    f=getFile(base, 'w')
    nv1=v1
    nv2=v2
    nv3=v3

    if rnv1 != -669: nv1=rnv1
    if rnv2 != -669: nv2=rnv2
    if rnv3 != -669: nv3=rnv3


    # print('raw', rnv1, rnv2, rnv3)
    # print('selected', nv1, nv2, nv3)
    # print('from', v1, v2, v3)

    if checkExistence(data,tag,v1,v2,v3):
        data = data.replace(
            x(tag,v1,v2,v3),
            x(tag,nv1,nv2,nv3),
        )
        f.write(data)




def getLatest(base, componentIdentifier):
    componentFile = filterData(getData(base), '@c|{f}'.format(f=componentIdentifier))

    # print(12, componentFile)
    # print(12, getV(componentFile[0]))
    # print(12, 21)
    if len(componentFile) >= 1:
        return getV(componentFile[0])[2]



# Recovery Methods

def restore(apmfile):
    open(apmfile, 'w').write(open(apmfile+'c','r').read())

def preservecopy(fileLoc):
    f = open(fileLoc, 'r')
    rf = open(fileLoc.replace('.apm', '.apmc'), 'w')
    rf.write(f.read())


def detectAbsenseOfContent(fileLoc):
    try:
        f = open(fileLoc, 'r')

        if f.read().strip() == '':
            return True
        else: return False
    except:
        return True


def manageRecovery(base):
    apmfile = formatBase(base, '/masterdata.apm')

    if detectAbsenseOfContent(apmfile):
            print(subtitle('An apmc is not present in Root APM. A new one is being created...'))
            preservecopy(apmfile)

    if not detectAbsenseOfContent(apmfile):
        preservecopy(apmfile)
    else:
        print(subtitle('Your APM File is empty. Auto-restoring...'))
        restore(apmfile)
        if detectAbsenseOfContent(apmfile):
            print(error('Unable to retrieve previous contents! Your data has been lost.'))
            open(apmfile, 'w').write('RestorationFailure01')

def customBackup(base, id='default'):
    try:
        apmfile = formatBase(base, '/masterdata.apm')
        open(apmfile+'c.'+id, 'w').write(open(apmfile, 'r').read())
        print(success('rsv: set'))
    except:
        print(error('rsv: execution failed'.format(id)))

def backupToCustom(base, id):
    try:
        apmfile = formatBase(base, '/masterdata.apm')
        open(apmfile, 'w').write(open(apmfile+'c.'+id, 'r').read())
        print(success('rsv: fetched & loaded'))
    except:
        print(error('rsv: No such save identity "{0}" exists'.format(id)))

def removeCustomBackup(base, id):
    try:
        apmfile = formatBase(base, '/masterdata.apm')
        os.remove(apmfile+'c.'+id)
        print(success('rsv: deleted'))
    except:
        print(error('rsv: No such save identity "{0}" exists'.format(id)))


def getBackups(base):
    dirlist = os.listdir(formatBase(base, '/'))

    backups = []
    
    for entity in dirlist:
        if 'masterdata.apmc.' in entity:
            backups.append(entity)
    
    return backups

    
# while True:
#     filterData(input('d> '), input('f> '))