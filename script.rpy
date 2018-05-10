# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Jeef", color="#3C932A")


# The game starts here.

define config.name = _('The Velvet Room')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Made by Capn Commie.")
#Rough start to test the engine and see what it can do
label start:  
    play music "yeet.mp3"
 
  


    python:
        a=['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers',
        'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged man', 'death',
        'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world']
        for i in range(1):
            from random import randint
            
            size=len(a)
            x= randint(0,size)
            first="1"
            first = (a[x])
            del a[x] 
            size = len(a)
            print size
            size=len(a)
            x= randint(0,size)
            second="1"
            second = (a[x])
            del a[x]
            size=len(a)
            x= randint(0,size)
            third="1"
            third = (a[x])
            del a[x] 
            size=len(a)
            x= randint(0,size)
            forth="1"
            forth = (a[x])
            del a[x] 
            size=len(a)
            x= randint(0,size)
            fifth="1"
            fifth = (a[x])
            del a[x] 
            size=len(a)
            x= randint(0,size)
            sixth="1"
            sixth = (a[x])
            del a[x] 
            size=len(a)
            x= randint(0,size)
            seventh="1"
            seventh = (a[x])
            
            del a[x]  
            size=len(a)
            x= randint(0,size)
            eighth="1"
            eighth = (a[x])
            
            del a[x] 
            size=len(a)
            x= randint(0,size)
            ninth="1"
            ninth = (a[x])
            
            del a[x] 
            size=len(a)
            x= randint(0,size)
            tenth="1"
            tenth  = (a[x])
            
            
          
jump test
label test:
    if first== "fool":
        show 0
        "1"
        
    if first== "magician":
        show 1
        "2" 
        
    if first== "high priestess":
        show 2
        "3" 
        
    if first== "empress":
        show 3
        "4" 
        
    if first== "emperor":
        show 4
        "5" 
        
    if first== "hierophant":
        show 5
        "6" 
        
    if first== "lovers":
        show 6
        "7"  
        
    if first== "chariot":
        show 7
        "whoops"
        
    if first== "strength":
        show 8
        "8" 
        
    if first== "hermit":
        show 9
        "9" 
        
    if first== "wheel of fortune":
        show 10
        "10" 
        
    if first== "justice":
        show 11
        "11"
        
    if first== "hanged man":
        show 12
        "12" 
        
    if first== "death":
        show 13
        "13"
        
    if first== "temperance":
        show 14
        "14" 
        
    if first== "devil":
        show 15
        "15" 
       
    if first== "tower":
        show 16
        "16" 
        
    if first== "star":
        show 18
        "17" 
        
    if first== "moon":
        show 19
        "18" 
        
    if first== "sun":
        show 20
        "19" 
        
    if first== "judgement":
        show 21
        "20" 
        
    if first== "world":
        show 22
        "21" 

############################################
    
    if second== "fool":
        show 0
        "1"
        
    if second== "magician":
        show 1
        "2" 
        
    if second== "high priestess":
        show 2
        "3" 
        
    if second== "empress":
        show 3
        "4" 
        
    if second== "emperor":
        show 4
        "5" 
        
    if second== "hierophant":
        show 5
        "6" 
        
    if second== "lovers":
        show 6
        "7"  
        
    if second== "chariot":
        show 7
        "whoops"
        
    if second== "strength":
        show 8
        "8" 
        
    if second== "hermit":
        "9" 
        show 9
    if second== "wheel of fortune":
        show 10
        "10" 
        
    if second== "justice":
        show 11
        "11"
        
    if second== "hanged man":
        show 12
        "12" 
        
    if second== "death":
        show 13
        "13"
        
    if second== "temperance":
        show 14
        "14" 
        
    if second== "devil":
        show 15
        "15" 
       
    if second== "tower":
        show 16
        "16" 
        
    if second== "star":
        show 18
        "17" 
        
    if second== "moon":
        show 19
        "18" 
        
    if second== "sun":
        show 20
        "19" 
        
    if second== "judgement":
        show 21
        "20" 
        
    if second== "world":
        show 22
        "21" 

