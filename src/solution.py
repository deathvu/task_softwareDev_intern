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
                return 0

        else:
            if os.listdir(path+'/ft_reference') != os.listdir(path+'/ft_run'):
               # if len(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))) != 0:
               ref_diff_list = list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))
               run_diff_list = list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path+'/ft_reference'))) 
               separator = ", "
               
               if ref_diff_list != []:
                   print("In ft_run there are missing files present in ft_reference:", separator.join(['\''+ x+os.path.join('/'+str(''.join(os.listdir(path+'/ft_reference/'+x))))+'\'' for x in ref_diff_list]))

               if run_diff_list != []:
                   print("In ft_run there are extra files not present in ft_reference:", separator.join(['\''+ x+os.path.join('/'+str(''.join(os.listdir(path+'/ft_run/'+x))))+'\'' for x in run_diff_list]))

               print('ref: ', ref_diff_list)
               print('run:', run_diff_list)
               print('\n\n\n\n\n\nFOUND\n\n\n\n')


#                   print(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))
#                   print(' '.join(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path + '/ft_run')))) + '/\n\n\n\n\n\nFOUND\n\n\n')

#               if list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path+'/ft_reference'))) != []:
#                   print(' '.join(list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path + '/ft_reference')))) + '/\n\n\n\n\n\nFOUND\n\n\n')        

    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            print("spuskaemsya", path+'/'+i)
            traversal(path+'/'+i, level+1)
#            print("vozvrat v", path)

traversal('../logs/')
