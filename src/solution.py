import os
from os.path import join, getsize

'''
for root, dirs, files in os.walk('../logs'):
    print("root: ", root)
    print("dirs: ", dirs)
    print("files: ", files)
    print('\n')
    '''

def traversal(path, level=1):
    print("level = ", level, "files: ", os.listdir(path))
    if level == 3:  
        if [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))] != ['ft_reference', 'ft_run']: # check if are the ft_reference and ft_run in test directories 
            with open(path+"/"+"report.txt", "a") as rep:
                rep.write('directory missing: '+' '.join([x for x in ['ft_reference','ft_run'] if x not in os.listdir(path)])+'\n')
                return 
        else:
            

    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            print("spuskaemsya", path+'/'+i)
            traversal(path+'/'+i, level+1)
            print("vozvrat v", path)

traversal('../logs/')
