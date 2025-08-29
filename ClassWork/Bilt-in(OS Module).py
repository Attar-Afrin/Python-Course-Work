import os
os.mkdir('PFS-31')

#To check for the directory is present or not then os.path.exists is used
import os
if not os.path.exists('PFS-31'):
    os.mkdir('PFS-31')
os.rmdir('PFS-31')

#To create for the sub directory
os.makedirs('PFS-31\subchild')

#If u have the directory and also sub directory in it then we cannot delete pfs directory
#In this case we should have to go for shutil
import shutil
shutil.rmtree('PFS-31')

#os.mkdir('PFS-31')
print(os.getcwd())
os.chdir('Sets.py')
print(os.getcwd())

#To show the number of files in the directory or folder
print(os.listdir('.'))

#Adding file inside the folder
import os
filepath=os.path.join('PFS-31','demo.txt')
os.remove(filepath)
with open(filepath,'w+') as f:
    f.write("Hello World")
    f.close()