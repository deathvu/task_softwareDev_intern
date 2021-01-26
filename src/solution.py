import re
import os
from os.path import join, getsize

def traversal(path, level=1):
    print("level = ", level, "files: ", os.listdir(path))
    if level == 3:
        with open(path+"/"+"report.txt", "a") as rep:
            # check if are the ft_reference and ft_run in test directories 
            if [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))] != ['ft_reference', 'ft_run']:
                rep.write('directory missing: '+' '.join([x for x in ['ft_reference','ft_run'] if x not in os.listdir(path)])+'\n')
                return 0
            # missing and extra files checking in ft_run and ft_reference
            else:
                if os.listdir(path+'/ft_reference') != os.listdir(path+'/ft_run'):
                    
                # save difference between files in catalogues in two lists (ft_reference - ft_run) and
                # (ft_run - ft_reference)
                    
                    ref_diff_list = list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))
                    run_diff_list = list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path+'/ft_reference'))) 
                    separator = ", "
               
                    if ref_diff_list != []:
                        with open(path+"/report.txt", "a") as rep:
                            rep.write("In ft_run there are missing files present in ft_reference:" + separator.join(['\''+ x+os.path.join('/'+str(''.join(os.listdir(path+'/ft_reference/'+x))))+'\'' for x in ref_diff_list])+'\n')

                    if run_diff_list != []:
                        with open(path+"/report.txt", "a") as rep:
                            rep.write("In ft_run there are extra files not present in ft_reference:" + separator.join(['\''+ x+os.path.join('/'+str(''.join(os.listdir(path+'/ft_run/'+x))))+'\'' for x in run_diff_list])+'\n')
                
                
                    return 0
        
                else:
                    # if ft_reference and ft_run are equal by number of tests start 
                    # searching files with errors or without "Solver finished at"
                    for root, dirs, files in os.walk(path+'/ft_run/'):
                        if files != []:
                            for x in files: # in case if in ft_run/*/ will be more than 1 file
                                with open(root+'/'+ x, "r") as rfile:
                                    flines = rfile.readlines()
                                    for num, z in enumerate(flines, 1):
                                        if re.search("error", z, flags=re.IGNORECASE):
                                            with open(path+'/'+"report.txt", "a") as rep:
                                                rep.write(root.split('/').pop()+'/'+x+'('+str(num)+'): '+z)

                                    if re.search(r'Solver finished at', ' '.join(flines)) == None:
                                        with open(path+'/'+"report.txt", "a") as rep:
                                           rep.write(root.split('/').pop()+'/'+x+": missing 'Solver finished at'")

#                                    ft_run_mem_peak = 

                                           
#                    ft_run_files = os.listdir(path + '/ft_run/' 
#                    ft_references_files = os.listdir(path + '/ft_reference') 
#                    print(ft_run_files,'\n', ft_references_files, '\n\n\n\n\n')
#                    
                            


    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            print("spuskaemsya", path+i)
            traversal(path+'/'+i, level+1)
#            print("vozvrat v", path)

traversal('../logs')
