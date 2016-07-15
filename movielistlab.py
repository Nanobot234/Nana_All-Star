#This code is used to randomly create action titles
from random import randrange

begList = ["The Return Of","Finding","The Last",
           "Uprising of", "Adventures of",
           " The Battle of", "Discovering",
           "Flying with", "Destruction of",
           "Grim Tales of the"]
choice = randrange(len(begList))
       

adjList = ["Ugly Haired","Half-Faced","Red Teethed",
           "Three-Legged","Naked","Gorgeous",
           "Cruel","Clueless","Three eyed", 
           "abominable"]
pick = randrange(len(adjList))

         
nouList = ["pineapple","Nanobot","Pineapple",
           "Iphone","Mattress","Computer","Clown"
           "Alien","Pheonix","Mario",]
take = randrange(len(nouList))
print(begList[choice] + " " + adjList[pick] +  " "  + nouList[take]) 
                                 
 
            
 
 
    