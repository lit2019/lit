import os
path = 'Mangas/'
for i in os.listdir(path):
    path0=path+i+"/"
    for k in os.listdir(path0):
        path2=path0+k+'/'
        for j in os.listdir(path2):
            print(path2+j)
            filepath=path2+j
            newpath=filepath[:-4]+".png"
            os.rename(src=filepath,dst=newpath)
