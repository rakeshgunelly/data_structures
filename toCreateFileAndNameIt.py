import os


rawFileName = 'XYZ ABC DEF GHI JKL MNO PQR'
inputString = '_'.join(rawFileName.split(' '))+'_leetcode_'+'Number'+'.py'
fileName =inputString.lower()

path  = 'D:\DS_Algo\DS_Programs'

dir_list = os.listdir(path) 
print("List of directories and files before creation:")
print(dir_list)
print()
  
with open(os.path.join(path, fileName), 'w') as fp:
    
    fp.write("# "+fileName)
