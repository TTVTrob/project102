import os
import shutil
source="C:/Users/suyas/Downloads"
destination="C:/Users/suyas/OneDrive/Desktop/test"
list=os.listdir(source)
print(list)
for fileName in list:
    name,extension=os.path.splitext(fileName)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".png",".jpg",".jpeg",".gif",".jfif",".pdf",".docx"]:
        path1=source+"/"+fileName
        path2=destination+"/"+"imagefiles"
        path3=destination+"/"+"imagefiles"+"/"+fileName
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print("moving"+fileName+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            print("moving"+fileName+"...")
            
