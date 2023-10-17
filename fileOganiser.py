import os 
import shutil
path=input('Enter the name of the folder: ')
destination='folderB'
listOffiles=os.listdir(path)
print(listOffiles)
for file in listOffiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(destination+'/'+ext):
        shutil.move(path+'/'+file,destination+'/'+ext+'/'+file)
    else:
        os.makedirs(destination+'/'+ext)
        shutil.move(path+'/'+file,destination+'/'+ext+'/'+file)
