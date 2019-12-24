import glob
import re

# config
srcPath = 'src/'
listFilePattern = '*.txt'
passwordListFilePath = 'list.txt'
passwordListFilePath_azAZ09 = 'list_azAZ09.txt'
passwordListFilePath_azAZ09_8 = 'list_azAZ09_8.txt'
passwordListFilePath_azAZ09Special_8 = 'list_azAZ09Special_8.txt'
specialCharacters = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]') 

# setup variables
passwordList = []
passwordList_azAZ09 = []
passwordList_azAZ09_8 = []
passwordList_azAZ09Special_8 = []

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

# remove empty elements
passwordList = list(filter(None, passwordList))

# save passwordList to passwordListFile by passwordListFilePath
with open(passwordListFilePath, mode='wt') as passwordListFile:
    passwordListFile.write('\n'.join(passwordList))

# check password strenght
for password in passwordList:
    if(any(x.isupper() for x in password) and
       any(x.islower() for x in password) and
       any(x.isdigit() for x in password)):
       passwordList_azAZ09.extend(password.splitlines())

       if(len(password) >= 8):
           passwordList_azAZ09_8.extend(password.splitlines())
           
           if(specialCharacters.search(password) != None):
            passwordList_azAZ09Special_8.extend(password.splitlines())

# save passwordList_azAZ09 to passwordListFile by passwordListFilePath_azAZ09
with open(passwordListFilePath_azAZ09, mode='wt') as passwordListFile:
    passwordListFile.write('\n'.join(passwordList_azAZ09))


# save passwordList_azAZ09_8 to passwordListFile by passwordListFilePath_azAZ09_8
with open(passwordListFilePath_azAZ09_8, mode='wt') as passwordListFile:
    passwordListFile.write('\n'.join(passwordList_azAZ09_8))


# save passwordList_azAZ09Special_8 to passwordListFile by passwordListFilePath_azAZ09Special_8
with open(passwordListFilePath_azAZ09Special_8, mode='wt') as passwordListFile:
    passwordListFile.write('\n'.join(passwordList_azAZ09Special_8))