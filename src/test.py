import os
#print([x for x in os.listdir('../logs/13-ROTATED_FLOWS') if os.path.isdir(x)])
'''for i in os.listdir('../logs/'):
    if os.path.isdir(os.path.join('../logs/', i)):
        print(i)

print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))] == ['ft_reference', 'ft_run'])
with open("../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/report.txt", "a") as rep:
    rep.write('directory missing: '+' '.join([x for x in ['ft_reference','ft_run'] if x not in os.listdir('../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/')]))
    
'''
print(list(set(['1', '2', '3']) - set(['1', '2'])))

        else:
            if os.listdir(path+'/ft_reference') != os.listdir(path+'/ft_run'):
               # if len(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run')))) != 0:
               if list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path+'/ft_run'))) != []:
                   print(' '.join(list(set(os.listdir(path+'/ft_reference')) - set(os.listdir(path + '/ft_run')))) + '/\n\n\n\n\n\nFOUND\n\n\n')

               if list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path+'/ft_reference'))) != []:
                   print(' '.join(list(set(os.listdir(path+'/ft_run')) - set(os.listdir(path + '/ft_reference')))) + '/\n\n\n\n\n\nFOUND\n\n\n')        

