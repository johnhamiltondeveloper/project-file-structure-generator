import os
import datetime

GameDescription = ""
GameName = ""

while len(GameName) <= 4:
    print("-"*30)
    print("Please don't be lazy be kind to your future self")
    print("The Name must be at least 4 characters")
    GameName = input('Game Name: ')
    
while len(GameDescription) < 15:
    print("-"*30)
    print("Please don't be lazy be kind to your future self")
    print("The Description must be longer then 15 characters")
    GameDescription = input('Game Description: ')

print("-"*30)
print("Would you like to setup git files")
EnableGit = input('Y/N:')

os.getcwd()

os.mkdir(GameName)

os.chdir(GameName)

os.getcwd()

f = open('Readme.txt','w')
f.write("Game Name: " + str(GameName) + "\n")
f.write("Date Created: " + str(datetime.datetime.now()) + "\n")
f.write("Description: " + str(GameDescription))
f.close()

f = open('licence.txt','w')
f.close()

os.makedirs("Builds/0.0")

os.makedirs("Documentation/GameDesignDocument/Concept/Story")
os.makedirs("Documentation/GameDesignDocument/Concept/Levels")
os.makedirs("Documentation/GameDesignDocument/Concept/Art")

os.chdir("Documentation/GameDesignDocument")
f = open('Readme.txt','w')
f.write("This GDD is meant for the zim wiki editor (http://zim-wiki.org) but files are keep as .txt files and are written in markdown so you can read them with allmost any text viewer.")
f.close()


