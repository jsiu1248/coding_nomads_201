# Add an API call to your CLI game that assigns a name to your player.
import requests
from pprint import pprint

base_url = "https://randomuser.me/api/?inc=name"
response = requests.get(base_url)

data = response.json()


"""
Added requests for API
CLI game for figuring out left and right and inventory
And then all of the inventory will be tracked in a file

"""
file1 = open("MyFile.txt","a+")

from datetime import datetime
now=datetime.now()
name= data["results"][0]["name"]["first"]
greeting=input(f"Welcome to the game, {name}. You have the option between the right or left door Left or Right.")

if greeting=="Right":
    print("There is a dragon.")
    dragon=input("Do you wish to fight the dragon? Yes or No.")
    if dragon=="No":
        print("Great choice. You didn't get eaten by the dragon.")
    if dragon=="Yes":
        print("You got eaten because you didn't have a sword.")
elif greeting=="Left":
    print("The room is empty.")
    sword=input("Actually there is a sword in the room. Do you wish to take it? Yes or No.")
    if sword =="Yes":
        print("Go fight the dragon and win!")
        file1.write(f"time: {now} The character {name} has a sword.\n")

    if sword =="No":
        print("You will die when you fight the dragon.")
        file1.write(f"time: {now} The character {name} has no sword.\n")






#new things to add
#file input and output done
#open a write done
#figure out what to write to the file done
#write to the file done
#close the file
#functions
#State - write the state of gameplay to a file and can keep track of your play's inventory across multiple games
