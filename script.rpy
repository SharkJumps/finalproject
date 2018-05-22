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
    show asd
    scene velvetr
  


    python:
        a=['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers',
        'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged man', 'death',
        'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world']
        for i in range(1):
            from random import randint
            
            size=len(a)-1
            x= randint(0,size)
            first="1"
            first = (a[x])
            del a[x] 
            
            size = len(a)-1
            x= randint(0,size)
            second="1"
            second = (a[x])
            del a[x]
            
            size=len(a)-1
            x= randint(0,size)
            third="1"
            third = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            forth="1"
            forth = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            fifth="1"
            fifth = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            sixth="1"
            sixth = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            seventh="1"
            seventh = (a[x])
            del a[x]  
            
            size=len(a)-1
            x= randint(0,size)
            eighth="1"
            eighth = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            ninth="1"
            ninth = (a[x])
            del a[x] 
            
            size=len(a)-1
            x= randint(0,size)
            tenth="1"
            tenth  = (a[x])
            
            
          
jump test
label test:
    "Shuffling..."
    "Would You Like to Shuffle Again?" 
    menu: 
        "Yes":
            jump test
        "No":
            jump heh
    "Your Current Situation is:"
label heh:    
    if first== "fool":
        show 0 at truecenter
        "Fool"
        
    if first== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if first== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if first== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if first== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if first== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if first== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if first== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if first== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if first== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if first== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if first== "justice":
        show 11 at truecenter 
        "Justice"
        
    if first== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if first== "death":
        show 13 at truecenter 
        "Death"
        
    if first== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if first== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if first== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if first== "star":
        show 18 at truecenter 
        "Star" 
        
    if first== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if first== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if first== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if first== "world":
        show 22 at truecenter 
        "The World" 

############################################
    "The Current Challenge is:"
    if second== "fool":
        show 0 at truecenter
        "Fool"
        
    if second== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if second== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if second== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if second== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if second== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if second== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if second== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if second== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if second== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if second== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if second== "justice":
        show 11 at truecenter 
        "Justice"
        
    if second== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if second== "death":
        show 13 at truecenter 
        "Death"
        
    if second== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if second== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if second== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if second== "star":
        show 18 at truecenter 
        "Star" 
        
    if second== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if second== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if second== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if second== "world":
        show 22 at truecenter 
        "The World" 
#####################################
    "The Basis of the Situation is:"
    if third== "fool":
        show 0 at truecenter 
        "Fool"
        
    if third== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if third== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if third== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if third== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if third== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if third== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if third== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if third== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if third== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if third== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if third== "justice":
        show 11 at truecenter 
        "Justice"
        
    if third== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if third== "death":
        show 13 at truecenter 
        "Death"
        
    if third== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if third== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if third== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if third== "star":
        show 18 at truecenter 
        "Star" 
        
    if third== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if third== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if third== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if third== "world":
        show 22 at truecenter 
        "The World" 
#################################### 
    "The Relevant Past is:"
    if forth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if forth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if forth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if forth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if forth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if forth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if forth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if forth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if forth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if forth== "hermit":
        show 9 at truecenter 
        "Hermit" 
       
    if forth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if forth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if forth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if forth== "death":
        show 13 at truecenter 
        "Death"
        
    if forth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if forth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if forth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if forth== "star":
        show 18 at truecenter 
        "Star" 
        
    if forth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if forth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if forth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if forth== "world":
        show 22 at truecenter 
        "The World" 
################################## 
    "The Present is:"
    if fifth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if fifth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if fifth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if fifth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if fifth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if fifth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if fifth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if fifth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if fifth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if fifth== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if fifth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if fifth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if fifth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if fifth== "death":
        show 13 at truecenter 
        "Death"
        
    if fifth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if fifth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if fifth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if fifth== "star":
        show 18 at truecenter 
        "Star" 
        
    if fifth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if fifth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if fifth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if fifth== "world":
        show 22 at truecenter 
        "The World" 
#################################
    "The Near Future is:"
    if sixth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if sixth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if sixth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if sixth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if sixth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if sixth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if sixth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if sixth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if sixth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if sixth== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if sixth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if sixth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if sixth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if sixth== "death":
        show 13 at truecenter 
        "Death"
        
    if sixth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if sixth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if sixth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if sixth== "star":
        show 18 at truecenter 
        "Star" 
        
    if sixth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if sixth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if sixth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if sixth== "world":
        show 22 at truecenter 
        "The World" 
#################################
    "Your Power in the Situation is:"
    if seventh== "fool":
        show 0 at truecenter 
        "Fool"
        
    if seventh== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if seventh== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if seventh== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if seventh== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if seventh== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if seventh== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if seventh== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if seventh== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if seventh== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if seventh== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if seventh== "justice":
        show 11 at truecenter 
        "Justice"
        
    if seventh== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if seventh== "death":
        show 13 at truecenter 
        "Death"
        
    if seventh== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if seventh== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if seventh== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if seventh== "star":
        show 18 at truecenter 
        "Star" 
        
    if seventh== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if seventh== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if seventh== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if seventh== "world":
        show 22 at truecenter 
        "The World" 
#################################
    "The Effect on People Around you is:"
    if eighth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if eighth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if eighth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if eighth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if eighth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if eighth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if eighth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if eighth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if eighth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if eighth== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if eighth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if eighth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if eighth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if eighth== "death":
        show 13 at truecenter 
        "Death"
        
    if eighth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if eighth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if eighth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if eighth== "star":
        show 18 at truecenter 
        "Star" 
        
    if eighth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if eighth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if eighth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if eighth== "world":
        show 22 at truecenter 
        "The World" 
#######################################
    "Your Hopes and Fears are:"
    if ninth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if ninth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if ninth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if ninth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if ninth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if ninth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if ninth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if ninth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if ninth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if ninth== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if ninth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if ninth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if ninth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if ninth== "death":
        show 13 at truecenter 
        "Death"
        
    if ninth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if ninth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if ninth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if ninth== "star":
        show 18 at truecenter 
        "Star" 
        
    if ninth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if ninth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if ninth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if ninth== "world":
        show 22 at truecenter 
        "The World" 
#################################
    "The Outcome is:"
    if tenth== "fool":
        show 0 at truecenter 
        "Fool"
        
    if tenth== "magician":
        show 1 at truecenter 
        "Magician" 
        
    if tenth== "high priestess":
        show 2 at truecenter 
        "High Priestess" 
        
    if tenth== "empress":
        show 3 at truecenter 
        "Empress" 
        
    if tenth== "emperor":
        show 4 at truecenter 
        "Emperor" 
        
    if tenth== "hierophant":
        show 5 at truecenter 
        "Hierophant" 
        
    if tenth== "lovers":
        show 6 at truecenter 
        "Lovers"  
        
    if tenth== "chariot":
        show 7 at truecenter 
        "Chariot"
        
    if tenth== "strength":
        show 8 at truecenter 
        "Strength" 
        
    if tenth== "hermit":
        show 9 at truecenter 
        "Hermit" 
        
    if tenth== "wheel of fortune":
        show 10 at truecenter 
        "Wheel of Fortune" 
        
    if tenth== "justice":
        show 11 at truecenter 
        "Justice"
        
    if tenth== "hanged man":
        show 12 at truecenter 
        "Hanged Man" 
        
    if tenth== "death":
        show 13 at truecenter 
        "Death"
        
    if tenth== "temperance":
        show 14 at truecenter 
        "Temperance" 
        
    if tenth== "devil":
        show 15 at truecenter 
        "Devil" 
       
    if tenth== "tower":
        show 16 at truecenter 
        "Tower" 
        
    if tenth== "star":
        show 18 at truecenter 
        "Star" 
        
    if tenth== "moon":
        show 19 at truecenter 
        "Moon" 
        
    if tenth== "sun":
        show 20 at truecenter 
        "Sun" 
        
    if tenth== "judgement":
        show 21 at truecenter 
        "Judgement" 
        
    if tenth== "world":
        show 22 at truecenter 
        "The World" 







