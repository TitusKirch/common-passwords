import glob

# config
srcPath = 'src/'
listFilePattern = '*.txt'
passwordListFilePath = 'list.txt'

# setup variables
passwordList = []

# get all passwords once from all lists
for filePath in glob.glob(srcPath + listFilePattern):
    # open file by filePath
    file = open(filePath, 'r')

    # add new passwords to passwordList (without \n)
    passwordList.extend(file.read().splitlines())

    # remove dupicated passwords
    passwordList = list(dict.fromkeys(passwordList))

    #close file
    file.close()

# save passwordList to passwordListFile by passwordListFilePath
with open(passwordListFilePath, mode='wt') as passwordListFile:
    passwordListFile.write('\n'.join(passwordList))
