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

def printDict(d,n):
    for i in d:
        try:
            print("%s%s"%('\t'*n,i))
            printDict(d[i],n+1)
        except:
            pass
def makeTree(path):
    a=os.walk(path)
    d={}
    for root,dirs,files in a:
            dictNest(root.split('\\'),d,files)
    printDict(d,0)


if __name__=="__main__":
    path=""#mention target path here
    makeTree(path)
