# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Jeef", color="#3C932A")


# The game starts here.

define config.name = _('Guys, guys, the ugandan knuckles is meme is still funny XXXXXXXXXXXXXDDDDDDDDDDDDDDDDD. Wait where are you going? Please come back')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Made by Capn Commie.")
#Rough start to test the engine and see what it can do
label start:  

 
  


    python:
        a=['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers',
        'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged man', 'death',
        'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world']
        for i in range(1):
            from random import randint
            x= randint(0,1)
            first="1"
            first = (a[x])
           
           
       
jump test
label test:
    if first== "fool":
        show 0
        "1"
        
    if first== "magician":
        show 1
        "2" 
        
    if first== "high priestess":
        "3" 
        show 2
    if first== "empress":
        "4" 
        show 3
    if first== "emperor":
        "5" 
        show 4
    if first== "hierophant":
        "6" 
        show 5
    if first== "lovers":
        "7"  
        show 6
    if first== "chariot":
        "whoops"
        show 7
    if first== "strength":
        "8" 
        show 8
    if first== "hermit":
        "9" 
        show 9
    if first== "wheel of fortune":
        "10" 
        show 10
    if first== "justice":
        "11"
        show 11
    if first== "hanged man":
        "12" 
        show 12
    if first== "death":
        "13"
        show 13
    if first== "temperance":
        "14" 
        show 14
    if first== "devil":
        "15" 
        show 15
    if first== "tower":
        "16" 
        show 16
    if first== "star":
        "17" 
        show 18
    if first== "moon":
        "18" 
        show 19
    if first== "sun":
        "19" 
        show 20
    if first== "judgement":
        "20" 
        show 21
    if first== "world":
        "21" 
        show 22