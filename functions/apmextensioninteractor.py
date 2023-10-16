# Private Methods
from spectrum import subtitle, error


def getAllLines(f):
    return open(f, 'r').readlines()

def removeComments(rl):

    linedata=''
    for l in rl:
        if not '#' in l:
            linedata+=l
    return linedata

def stripempty(x):
    r = []
    for it in x:
        if it.strip() != '':
            r.append(it)
    return r

def getLines(t):
    x = t.strip().split(';')
    return stripempty(x)

def join(list):
    res=''
    for x in list:
        res+=x
    return x

def deleteDuplicate(listA):
    return list(dict.fromkeys(listA))

def checkForExisting(list, item):

    passed = []
    duplicatesExist = False
    pi=0
    deleteP=[]
    for item in list:
        go = True
        for passedItem in passed:
            if item == passedItem:
                go = False
            elif item.get('iteration') != passedItem.get('iteration') and item.get('location') == passedItem.get('location') and item.get('name') == passedItem.get('name'):
            #     print(1)
            #     deleteP.append(pi)
                go = False
                # print(1111,item, passedItem,1111)

        if go:
            passed.append(item)
            pi+=1
        else:
            duplicatesExist = True
    
    # print(deleteP, len(passed))

    # deleteP = deleteDuplicate(deleteP)

    # finalList = []

    # fi = 0
    # for item in passed:
    #     for deleteIndex in deleteP:
    #         if fi != deleteIndex:
    #             finalList.append(item)

    #     fi+=1

    return [duplicatesExist, passed]

def spiltBySection(rl):
    sections=[]
    # for x in rl:
        # print(rl)

    sc=rl.split('>>>')



    for s in sc:
        if '%%%' in s:
            snac=s.split('%%%')
            sn=snac[0]
            sc=snac[1]
            sections.append({
                'name':sn,
                'content':sc
            })
    return sections

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

def getAttributes(rawl):
    l=rawl.strip()

    tc=l.split('|')

    ptc=[tc[0],tc[1],tc[2]]
    # for x in tc:
    #     if len(x) > 3:
    #         ptc.append(x)
    return ptc

def restore(apmfile):
    open(apmfile, 'w').write(open(apmfile+'c','r').read())


# Public Class
class APMInteractor:
    def __init__(self,apmfile):
        
        if detectAbsenseOfContent(apmfile+'c'):
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
        self.apmfile=apmfile
        self.latestAlias=None
        self.latestModules=None

    def reprint(self, aliasinfo, bmoduleinfo):

        info = '>>> apm/INSTALLEDALIASES %%%\n'
        info+='\n\n# MODULE NAME  |  ITERATION  |  LOCATION\n\n'
        for alias in aliasinfo:
            info += '{comp} | {iter} | {loc} ;\n'.format(
                comp=alias.get('name').lower(),
                iter=alias.get('iteration'),
                loc=alias.get('location'),
            )
        info+='\n>>> apm/DEVMODULEINFO %%%\n'
        info+='\n\n# MODULE NAME  |  ITERATION  |  SAME-ITERATED COPIES\n\n'
        for module in bmoduleinfo:
            info += '{comp} | {iter} | {sic} ;\n'.format(
                comp=module.get('name').lower(),
                iter=module.get('iteration'),
                sic=module.get('sameIteratedCopies'),
            )
        info+='\n\n'
        return info

    
    def getPure(self):
        lines = getAllLines(self.apmfile)
        pureLines = removeComments(lines)
        return pureLines
    
    def getAliasInfo(self):
        sections = spiltBySection(self.getPure())


        aliasInfo = None
        for section in sections:
            if "apm/INSTALLEDALIASES" in section["name"]:
                aliasInfo = section["content"]
        


        aliasArray = []
        nameI=0
        iterationI=1
        locationI=2

        if aliasInfo != None:
            for row in getLines(aliasInfo):
                attributes = getAttributes(row)
                if len(attributes) >= 3:
                    aliasArray.append(
                        {
                            "name": attributes[nameI].strip(),
                            "iteration": int(attributes[iterationI].strip()),
                            "location": attributes[locationI].strip(),
                        }
                    )
        # print(aliasArray)
        return aliasArray
    def getBaseModulesInfo(self):
        sections = spiltBySection(self.getPure())

        moduleInfo = None
        for section in sections:
            if "apm/DEVMODULEINFO" in section["name"]:
                moduleInfo = section["content"]

        moduleArray = []
        nameI=0
        iterationI=1
        sameIteratedCopies=2
        if moduleInfo != None:
            for row in getLines(moduleInfo):
                attributes = getAttributes(row)
                if len(attributes) >= 3:
                    # print(attributes)
                    moduleArray.append(
                        {
                            "name": attributes[nameI].strip(),
                            "iteration": int(attributes[iterationI].strip()),
                            "sameIteratedCopies": int(attributes[sameIteratedCopies].strip()),
                        }
                    )
        return moduleArray
    def getCustom(self, sectionTitle):
        sections = spiltBySection(self.getPure())

        miscInfo = None
        for section in sections:
            if sectionTitle in section["name"]:
                miscInfo = section["content"]

        miscInfo = []
        if miscInfo != None:
            for row in getLines(miscInfo):
                attributes = getAttributes(row)
                if len(attributes) >= 3:
                    # print(attributes)
                    miscInfo.append(
                        {
                            "1": attributes[0].strip(),
                            "2": int(attributes[1].strip()),
                            "3": attributes[2].strip(),
                        }
                    )
        return miscInfo
    
    def updateAPM(self):
        if self.latestAlias==None:
            self.latestAlias=self.getAliasInfo()
        if self.latestModules==None:
            self.latestModules=self.getBaseModulesInfo()
        
        p=self.reprint(self.latestAlias, self.latestModules)

        f = open(self.apmfile, 'w').write(p)

    def addAliasRow(self, dataList):
        aliascontents= self.getAliasInfo()

        # print(aliascontents)

        # 0 for if exists, 1 for filtered output

        # if clones[0]:
        #     aliascontents = clones[1]

        aliascontents.append(
            {
                "name": dataList[0],
                "iteration": dataList[1],
                "location": dataList[2],
            }
        )

        # print(aliascontents)
        clones = checkForExisting(aliascontents, dataList)
        if clones[0]:
            aliascontents = clones[1]
        
        # print(aliascontents)

        self.latestAlias = aliascontents

        self.updateAPM()

    def removeAliasRow(self, dataMatchList):
        aliascontents= self.getAliasInfo()

        i=0
        ipop = 0
        # print(aliascontents)
        for alias in aliascontents:
            if alias.get('name') == dataMatchList[0] and alias.get('iteration') == dataMatchList[1] and alias.get('location') == dataMatchList[2]:
                ipop=i
            
            i+=1

        try:
            aliascontents.pop(ipop)
        except:
            print(error('APMExtensionInteractor reports no record by {0} is present.'.format(dataMatchList)))

        self.latestAlias = aliascontents

        self.updateAPM()

    def getLatest(self, component):
        modulesInfo = self.getBaseModulesInfo()


        iteration = 0
        for module in modulesInfo:
            if module.get('name') == component:
                iteration = module.get('iteration')
        return iteration