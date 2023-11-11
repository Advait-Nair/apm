spectrum = None
try:
    import functions.spectrum as spectrum
except:
    import spectrum as spectrum

def KeyLang(rtext, separator=' '):

    # Tab Separated Key Value Pairs
    text = rtext
    try:
        text = rtext.decode('utf-8')
    except: pass
    tskvp = text.split(separator)

    data = {}

    try:

        for i in range(0, len(tskvp)):
            # If it is even it is a pair
            isKey = i % 2 == 0
            
            if isKey:
                data[tskvp[i].strip()] = tskvp[i+1].strip()
    except:
        print(spectrum.error('keylang process error at internal update check process: mutated KeyLangData'))
        return {}
    
    return data

def WriteKeyLang(data, key, value, separator=' '):
    # Tab Separated Key Value Pairs
    text = data
    try:
        text = data.decode('utf-8')
    except: pass
    tskvp = text.split(separator)

    newdata = {}

    # try:


    for i in range(0, len(tskvp)):
        # If it is even it is a pair
        isKey = i % 2 == 0
        
        if isKey and tskvp[i].strip() != False:
            if tskvp[i].strip() == key:
                newdata[tskvp[i].strip()] = value.strip()
            else:
                newdata[tskvp[i].strip()] = tskvp[i+1].strip()
    # except:
        # print(spectrum.error('keylang process error at internal update check process: mutated KeyLangData'))
        # return

    return newdata

def KLMap(data, separator=' '):
    out = ''

    i = 0
    keys = dict.keys(data)
    for key in keys:
        if i+1 == len(keys):
            out += key + separator + data[key]
        else:
            out += key + separator + data[key] + separator

        i+=1


    return out