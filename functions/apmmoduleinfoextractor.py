from spectrum import error
import os
import textwrap

jumpLength = os.get_terminal_size().columns -19
# def regulateLength(text):
#     chars = text.split(' ')



#     newText = ''
    
#     i=0
#     for char in chars:
#         # hyphen = ''
        
#         # try:
#         #     if char[i+1] != ' ':
#         #         hyphen = '-'
#         # except:
#         #     hyphen = ''
            
#         if i % jumpLength == 0:
#             newText += textwrap.indent(char, 4*' ')
#         newText+=char
#         i+=1

#     return newText


def extract(fileName, filePath):
    text = open(filePath).readlines()

    metadata = {}

    try:

        infoLines = []

        openedAPMTag = False

        for line in text:
            if openedAPMTag and not '%%%apm%%%' in line and '' != line.strip():
                infoLines.append(line)
            
            if '%%%apm%%%' in line:
                openedAPMTag = not openedAPMTag
            
            


        for tagPair in infoLines:
            # in each tagPair:
            # TAG NAME :: TAG CONTENT

            splitList = tagPair.split('::')
            tagName = splitList[0].strip()
            tagContent = splitList[1].strip()

            metadata[tagName] = tagContent.strip()
        
    except:
        metadata['\n\nAPM Exception Informer'] = error("This is not a meta tag. This is an error informing you that an internal APM Process, apmModuleInfoExtractor:extract() failed to extract information from \"{0}\". This is possibly due to improper formatting of the file.".format(fileName))
    
    metadata['size'] = '{0} lines totalling {1}kB'.format(len(text), os.path.getsize(filePath)/1024)

    return metadata

def formatMetadata(metadata, maxLengthEnabled):
    # if metadata.get('APM Exception Informer'):
    #     return metadata
    
    formatted = '\n'

    for key in list(dict.keys(metadata)):

        if maxLengthEnabled and key.strip() != 'APM Exception Informer':
            formatted += '{0}: {1}\n'.format(key, textwrap.shorten(metadata[key], width=jumpLength, placeholder="..."))
        else:
            formatted += '{0}: {1}\n'.format(key, metadata[key])


    return formatted