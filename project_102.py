import os
import shutil
source='audio'
destination='audio_2'

nameoffile=os.listdir(source)
# print(nameoffile)
for i in nameoffile:

    name,extension=os.path.splitext(i)
    # print('name of file:',name)
    # print("Extension of file",extension)

    if extension=='':
        continue

    if extension in ['.mp3','.FUR','.MTM','.ABC']:
        path1=source+'/'+i
        path2=destination+'/'+'audio_1'
        path3=destination+'/'+'audio_1'+'/'+i
        
        if os.path.exists(path2):
            print("moving",i,'...')
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("moving",i,'...')
            shutil.move(path1,path3)