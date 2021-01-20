import os
#print([x for x in os.listdir('../logs/13-ROTATED_FLOWS') if os.path.isdir(x)])
'''for i in os.listdir('../logs/'):
    if os.path.isdir(os.path.join('../logs/', i)):
        print(i)

print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))] == ['ft_reference', 'ft_run'])
'''
with open("../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/report.txt", "a") as rep:
    rep.write('directory missing: '+' '.join([x for x in ['ft_reference','ft_run'] if x not in os.listdir('../logs/13-ROTATED_FLOWS/00060-RRF-u_R_0_IW/')]))
    
