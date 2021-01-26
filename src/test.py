from decimal import Decimal
import os
import re
#print([x for x in os.listdir('../logs/13-ROTATED_FLOWS') if os.path.isdir(x)])
'''for i in os.listdir('../logs/'):
    if os.path.isdir(os.path.join('../logs/', i)):
        print(i)

print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))] == ['ft_reference', 'ft_run'])
with open("../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/report.txt", "a") as rep:
    rep.write('directory missing: '+' '.join([x for x in ['ft_reference','ft_run'] if x not in os.listdir('../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/')]))
    
'''
#print(list(set(['1', '2', '3']) - set(['1', '2'])))
#
#        else:
#            if os.listdir(path+'/ft_reference') != os.listdir(path+'/ft_run'):
#               # if len(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))) != 0:
#               if list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run'))) != []:
#                   print(' '.join(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path + '/ft_run')))) + '/\n\n\n\n\n\nFOUND\n\n\n')
#
#               if list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path+'/ft_reference'))) != []:
#                   print(' '.join(list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path + '/ft_reference')))) + '/\n\n\n\n\n\nFOUND\n\n\n')        
#

regex = re.compile("[-+]?\d*\.\d+|\d+") 

path = '../logs/'
with open("../result.txt", "a") as res:
    for root, dirs, files in os.walk(path):
        if "report.txt" in files:
            if os.stat(root+'/report.txt').st_size == 0:
                print("OK: "+root.replace(path, ''))
            else:
                with open(root+'/report.txt', "r") as rep:
                    for x in rep.readlines():
                        print("FAIL: "+root.replace(path, '')+'\n'+x)
                

                

#def setPeak(ifile):
#    with open(ifile, "r") as rfile:
#        lines = rfile.readlines()
#        list_of_floats = []
#        for x in lines:
#            if re.search("Memory Working Set Peak", x, re.IGNORECASE):
#                list_of_floats.append(float(re.search(regex, x.split(',')[1]).group(0)))
#        print(list_of_floats)
#    #    for z in list_of_floats:
#        print('max: ', max(list_of_floats))
#        return max(list_of_floats)
#
#run = setPeak('../logs/13-ROTATED_FLOWS/00061-RRF-u_R_0_IW_ref_boundary_lev_2/ft_run/1/1.stdout')
#print('\n')
#reference = setPeak('../logs/13-ROTATED_FLOWS/00061-RRF-u_R_0_IW_ref_boundary_lev_2/ft_reference/1/1.stdout')
#
#print('compare max run on min ref: ', "%.2f" % (Decimal(run) / Decimal(reference)))
#    found = re.findall(r'Memory Working Set Peak', ' '.join(lines))
#    print('found line', found)
#    regex = re.compile(r'([1-9]+)', re.I)
#    print(regex.search(' '.join(lines)).groups())


# os.walk(.../.../..//.//../ft_run/1/1.stdout)
# if files != []:
#       func(root), then comparsion
#       func(root.replace(ft_run->ft_reference) 
