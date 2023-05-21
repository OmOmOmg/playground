import os
f = open('treewalk/treewalk_test.txt','w')
for root, dirs, files in os.walk('.'):    
    
    print(root+"/")
    
    if len(files) > 0:
        print(' '.join(files))
    else:
        print('!EMPTY_DIR!')      
        
f.close()
    
