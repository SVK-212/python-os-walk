import os
def dictNest(path,d,files):
    if len(path)>1:
        if path[0] not in d:
            d[path[0]]={}
        dictNest(path[1:],d[path[0]],files)
    else:
        if path[0] not in d:
            d[path[0]]={}
        d[path[0]][':FILES:'+str(len(files))]=files

def printDict(d,n,line_sep,line_start):
    for i in d:
        try:
            print("%s%s%s"%((line_start if n else ""),line_sep*n,i))
            printDict(d[i],n+1,line_sep,line_start)
        except:
            pass
def makeTree(path,dir_sep='\\',line_sep='-',line_start='|'):
    a=os.walk(path)
    d={}
    for root,dirs,files in a:
            dictNest(root.split(dir_sep),d,files)
    printDict(d,0,line_sep,line_start)


if __name__=="__main__":
    path=""#mention target path here
    makeTree(path)
