def b(c):
    return "\33[{c}m".format(c=c)

def s(c):
    return "\33[{c}m".format(c=c)

def c(c):
    return "\33[{c}m".format(c=c)

def rawcol(st,bg,col):
    return b(bg)+c(col)+s(st)

def col(rStyle):
    style=0
    bg=49
    col=37

    if ('error') in rStyle:
        style=1
        col=31
    if ('success') in rStyle:
        style=1
        col=92
    if ('info') in rStyle:
        col=44
        style=1
    if ('info-h') in rStyle:
        col=36
        style=1
    if ('underline') in rStyle:
        style=4
    if ('highlight') in rStyle:
        style=7
    if ('bold') in rStyle:
        style=1
    if ('italic') in rStyle:
        style=3
    if ('straight') in rStyle:
        style=0



     
    return rawcol(style,bg,col)



def title(string):
    return col('') + col('info-h')+string+col('')
def subtitle(string):
    return col('') + col('info')+string+col('')
def italic(string):
    return col('') + col('italic')+string+col('')
def bold(string):
    return col('') + col('bold')+string+col('')
def error(string):
    return col('') + col('error')+string+col('')
def success(string):
    return col('') + col('success')+string+col('')



#ANSITEST
# _z=True
# while _z:
#     x1=input("apm >>> insert info: ")
#     print(col(x1)+"TEST ANSI test ansi 1234567890 ABCDEF abcdef")
#     if '-e' in x1: _z = False