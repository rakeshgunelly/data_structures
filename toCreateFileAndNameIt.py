import os


rawFileName = 'A Number After a Double Reversal'
inputString = '_'.join(rawFileName.split(' '))+'_leetcode_'+'2119'+'.py'
fileName ='12'+inputString.lower()

path  = 'D:\DS_Algo\DS_Programs'

# dir_list = os.listdir(path) 
# print("List of directories and files before creation:")
# print(dir_list)
# print()
  
with open(os.path.join(path, fileName), 'w') as fp:
    
    fp.write("# "+rawFileName)

print("File with custom name "+ fileName + ' is created')

