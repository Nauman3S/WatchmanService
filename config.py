def loadConfig():
    g=open('/boot/WatchmanService.conf','r')
    m=g.read()
    g.close()
    kk=m.split('=')
    if(kk[1]=="1"):
        return 1
    else:
        return 0

