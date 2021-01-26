import re
import os
from os.path import join, getsize
from decimal import Decimal

_REGEX = re.compile("[-+]?\d*\.\d+|\d+") 


def values_mem_peak(path, pattern, split_sym):
    values = []
    with open(path, "r") as rfile:
        lines = rfile.readlines()
        for x in lines:
            if re.search(pattern, x, re.IGNORECASE):
                values.append(float(re.search(_REGEX, x.split(split_sym)[1]).group(0)))
        return values


def traversal(path, level=1):
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
                                           rep.write(root.split('/').pop()+'/'+x+": missing 'Solver finished at'\n")

                                # taking max 'Memory Working Set Peak' & 'Total' bricks
                                # from files with diff between them
                                ft_run_max_mem_peak = max(values_mem_peak(root+'/'+x, "Memory Working Set Peak", ','))
                                ft_reference_max_mem_peak = max(values_mem_peak((root+'/'+x).replace('ft_run', 'ft_reference'), "Memory Working Set Peak", ','))
                                ft_run_bricks_total = values_mem_peak(root+'/'+x, "MESH::Bricks: Total=", ' ')
                                ft_reference_bricks_total = values_mem_peak((root+'/'+x).replace('ft_run', 'ft_reference'), "MESH::Bricks: Total=", ' ')
                                rel_diff_mem_peak = Decimal(max(ft_run_max_mem_peak, ft_reference_max_mem_peak)) /\
                                        Decimal(min(ft_run_max_mem_peak, ft_reference_max_mem_peak))
                                rel_diff_bricks_total = abs(Decimal(ft_run_bricks_total[-1]) - Decimal(ft_reference_bricks_total[-1])) / Decimal(ft_reference_bricks_total[-1]) 

                                if rel_diff_mem_peak > 5:
                                    with open(path+'/'+'report.txt', "a") as rep:
                                        rep.write(root.split('/').pop()+ '/'+x+": different 'Memory Working Set Peak' (ft_run="+str(ft_run_max_mem_peak)+", ft_reference="+str(ft_reference_max_mem_peak)+", rel.diff="+str("%.2f" % rel_diff_mem_peak)+", criterion=4)\n")

                                if rel_diff_bricks_total > 0.10:
                                    with open(path+'/'+'report.txt', "a") as rep:
                                        rep.write(root.split('/').pop()+'/'+x+": different 'Total' of bricks (ft_run="+str(ft_run_bricks_total[-1])+', ft_reference='+str(ft_reference_bricks_total[-1])+', rel.diff='+("%.2f"%rel_diff_bricks_total)+', criterion=0.1)\n')


                                           
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            traversal(path+'/'+i, level+1)

def make_report(path):
    with open("../result.txt", "a") as res:
        for root, dirs, files in os.walk(path):
            if "report.txt" in files:
                if os.stat(root+'/report.txt').st_size == 0:
                    res.write("OK: "+root.replace(path,'')+'\n')
                else:
                    with open(root+'/report.txt', "r") as rep:
                        for x in rep.readlines():
                            res.write("FAIL: "+root.replace(path, '')+'\n'+x)


def main():
    traversal('../logs')
    make_report('../logs/')

if __name__ == '__main__':
    main()

