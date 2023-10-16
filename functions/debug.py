from spectrum import italic, success, subtitle
def dbg(header, args, csvnames):
    print(subtitle('\n'+header))
    for index in range(0,len(args)): print(italic(csvnames.split(',')[index]+': '+ str(args[index])))
    print(success('__\n'))
    return True