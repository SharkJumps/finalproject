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
            print size
            size=len(a)
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
#####################################
    if third== "fool":
        show 0
        "1"
        
    if third== "magician":
        show 1
        "2" 
        
    if third== "high priestess":
        show 2
        "3" 
        
    if third== "empress":
        show 3
        "4" 
        
    if third== "emperor":
        show 4
        "5" 
        
    if third== "hierophant":
        show 5
        "6" 
        
    if third== "lovers":
        show 6
        "7"  
        
    if third== "chariot":
        show 7
        "whoops"
        
    if third== "strength":
        show 8
        "8" 
        
    if third== "hermit":
        "9" 
        show 9
    if third== "wheel of fortune":
        show 10
        "10" 
        
    if third== "justice":
        show 11
        "11"
        
    if third== "hanged man":
        show 12
        "12" 
        
    if third== "death":
        show 13
        "13"
        
    if third== "temperance":
        show 14
        "14" 
        
    if third== "devil":
        show 15
        "15" 
       
    if third== "tower":
        show 16
        "16" 
        
    if third== "star":
        show 18
        "17" 
        
    if third== "moon":
        show 19
        "18" 
        
    if third== "sun":
        show 20
        "19" 
        
    if third== "judgement":
        show 21
        "20" 
        
    if third== "world":
        show 22
        "21" 
#################################### 
    if forth== "fool":
        show 0
        "1"
        
    if forth== "magician":
        show 1
        "2" 
        
    if forth== "high priestess":
        show 2
        "3" 
        
    if forth== "empress":
        show 3
        "4" 
        
    if forth== "emperor":
        show 4
        "5" 
        
    if forth== "hierophant":
        show 5
        "6" 
        
    if forth== "lovers":
        show 6
        "7"  
        
    if forth== "chariot":
        show 7
        "whoops"
        
    if forth== "strength":
        show 8
        "8" 
        
    if forth== "hermit":
        "9" 
        show 9
    if forth== "wheel of fortune":
        show 10
        "10" 
        
    if forth== "justice":
        show 11
        "11"
        
    if forth== "hanged man":
        show 12
        "12" 
        
    if forth== "death":
        show 13
        "13"
        
    if forth== "temperance":
        show 14
        "14" 
        
    if forth== "devil":
        show 15
        "15" 
       
    if forth== "tower":
        show 16
        "16" 
        
    if forth== "star":
        show 18
        "17" 
        
    if forth== "moon":
        show 19
        "18" 
        
    if forth== "sun":
        show 20
        "19" 
        
    if forth== "judgement":
        show 21
        "20" 
        
    if forth== "world":
        show 22
        "21" 
################################## 
    if fifth== "fool":
        show 0
        "1"
        
    if fifth== "magician":
        show 1
        "2" 
        
    if fifth== "high priestess":
        show 2
        "3" 
        
    if fifth== "empress":
        show 3
        "4" 
        
    if fifth== "emperor":
        show 4
        "5" 
        
    if fifth== "hierophant":
        show 5
        "6" 
        
    if fifth== "lovers":
        show 6
        "7"  
        
    if fifth== "chariot":
        show 7
        "whoops"
        
    if fifth== "strength":
        show 8
        "8" 
        
    if fifth== "hermit":
        "9" 
        show 9
    if fifth== "wheel of fortune":
        show 10
        "10" 
        
    if fifth== "justice":
        show 11
        "11"
        
    if fifth== "hanged man":
        show 12
        "12" 
        
    if fifth== "death":
        show 13
        "13"
        
    if fifth== "temperance":
        show 14
        "14" 
        
    if fifth== "devil":
        show 15
        "15" 
       
    if fifth== "tower":
        show 16
        "16" 
        
    if fifth== "star":
        show 18
        "17" 
        
    if fifth== "moon":
        show 19
        "18" 
        
    if fifth== "sun":
        show 20
        "19" 
        
    if fifth== "judgement":
        show 21
        "20" 
        
    if fifth== "world":
        show 22
        "21" 
#################################
    if sixth== "fool":
        show 0
        "1"
        
    if sixth== "magician":
        show 1
        "2" 
        
    if sixth== "high priestess":
        show 2
        "3" 
        
    if sixth== "empress":
        show 3
        "4" 
        
    if sixth== "emperor":
        show 4
        "5" 
        
    if sixth== "hierophant":
        show 5
        "6" 
        
    if sixth== "lovers":
        show 6
        "7"  
        
    if sixth== "chariot":
        show 7
        "whoops"
        
    if sixth== "strength":
        show 8
        "8" 
        
    if sixth== "hermit":
        "9" 
        show 9
    if sixth== "wheel of fortune":
        show 10
        "10" 
        
    if sixth== "justice":
        show 11
        "11"
        
    if sixth== "hanged man":
        show 12
        "12" 
        
    if sixth== "death":
        show 13
        "13"
        
    if sixth== "temperance":
        show 14
        "14" 
        
    if sixth== "devil":
        show 15
        "15" 
       
    if sixth== "tower":
        show 16
        "16" 
        
    if sixth== "star":
        show 18
        "17" 
        
    if sixth== "moon":
        show 19
        "18" 
        
    if sixth== "sun":
        show 20
        "19" 
        
    if sixth== "judgement":
        show 21
        "20" 
        
    if sixth== "world":
        show 22
        "21" 
#################################
    if seventh== "fool":
        show 0
        "1"
        
    if seventh== "magician":
        show 1
        "2" 
        
    if seventh== "high priestess":
        show 2
        "3" 
        
    if seventh== "empress":
        show 3
        "4" 
        
    if seventh== "emperor":
        show 4
        "5" 
        
    if seventh== "hierophant":
        show 5
        "6" 
        
    if seventh== "lovers":
        show 6
        "7"  
        
    if seventh== "chariot":
        show 7
        "whoops"
        
    if seventh== "strength":
        show 8
        "8" 
        
    if seventh== "hermit":
        "9" 
        show 9
    if seventh== "wheel of fortune":
        show 10
        "10" 
        
    if seventh== "justice":
        show 11
        "11"
        
    if seventh== "hanged man":
        show 12
        "12" 
        
    if seventh== "death":
        show 13
        "13"
        
    if seventh== "temperance":
        show 14
        "14" 
        
    if seventh== "devil":
        show 15
        "15" 
       
    if seventh== "tower":
        show 16
        "16" 
        
    if seventh== "star":
        show 18
        "17" 
        
    if seventh== "moon":
        show 19
        "18" 
        
    if seventh== "sun":
        show 20
        "19" 
        
    if seventh== "judgement":
        show 21
        "20" 
        
    if seventh== "world":
        show 22
        "21" 
#################################
    if eighth== "fool":
        show 0
        "1"
        
    if eighth== "magician":
        show 1
        "2" 
        
    if eighth== "high priestess":
        show 2
        "3" 
        
    if eighth== "empress":
        show 3
        "4" 
        
    if eighth== "emperor":
        show 4
        "5" 
        
    if eighth== "hierophant":
        show 5
        "6" 
        
    if eighth== "lovers":
        show 6
        "7"  
        
    if eighth== "chariot":
        show 7
        "whoops"
        
    if eighth== "strength":
        show 8
        "8" 
        
    if eighth== "hermit":
        "9" 
        show 9
    if eighth== "wheel of fortune":
        show 10
        "10" 
        
    if eighth== "justice":
        show 11
        "11"
        
    if eighth== "hanged man":
        show 12
        "12" 
        
    if eighth== "death":
        show 13
        "13"
        
    if eighth== "temperance":
        show 14
        "14" 
        
    if eighth== "devil":
        show 15
        "15" 
       
    if eighth== "tower":
        show 16
        "16" 
        
    if eighth== "star":
        show 18
        "17" 
        
    if eighth== "moon":
        show 19
        "18" 
        
    if eighth== "sun":
        show 20
        "19" 
        
    if eighth== "judgement":
        show 21
        "20" 
        
    if eighth== "world":
        show 22
        "21" 
#######################################
    if ninth== "fool":
        show 0
        "1"
        
    if ninth== "magician":
        show 1
        "2" 
        
    if ninth== "high priestess":
        show 2
        "3" 
        
    if ninth== "empress":
        show 3
        "4" 
        
    if ninth== "emperor":
        show 4
        "5" 
        
    if ninth== "hierophant":
        show 5
        "6" 
        
    if ninth== "lovers":
        show 6
        "7"  
        
    if ninth== "chariot":
        show 7
        "whoops"
        
    if ninth== "strength":
        show 8
        "8" 
        
    if ninth== "hermit":
        "9" 
        show 9
    if ninth== "wheel of fortune":
        show 10
        "10" 
        
    if ninth== "justice":
        show 11
        "11"
        
    if ninth== "hanged man":
        show 12
        "12" 
        
    if ninth== "death":
        show 13
        "13"
        
    if ninth== "temperance":
        show 14
        "14" 
        
    if ninth== "devil":
        show 15
        "15" 
       
    if ninth== "tower":
        show 16
        "16" 
        
    if ninth== "star":
        show 18
        "17" 
        
    if ninth== "moon":
        show 19
        "18" 
        
    if ninth== "sun":
        show 20
        "19" 
        
    if ninth== "judgement":
        show 21
        "20" 
        
    if ninth== "world":
        show 22
        "21" 
#################################
    if tenth== "fool":
        show 0
        "1"
        
    if tenth== "magician":
        show 1
        "2" 
        
    if tenth== "high priestess":
        show 2
        "3" 
        
    if tenth== "empress":
        show 3
        "4" 
        
    if tenth== "emperor":
        show 4
        "5" 
        
    if tenth== "hierophant":
        show 5
        "6" 
        
    if tenth== "lovers":
        show 6
        "7"  
        
    if tenth== "chariot":
        show 7
        "whoops"
        
    if tenth== "strength":
        show 8
        "8" 
        
    if tenth== "hermit":
        "9" 
        show 9
    if tenth== "wheel of fortune":
        show 10
        "10" 
        
    if tenth== "justice":
        show 11
        "11"
        
    if tenth== "hanged man":
        show 12
        "12" 
        
    if tenth== "death":
        show 13
        "13"
        
    if tenth== "temperance":
        show 14
        "14" 
        
    if tenth== "devil":
        show 15
        "15" 
       
    if tenth== "tower":
        show 16
        "16" 
        
    if tenth== "star":
        show 18
        "17" 
        
    if tenth== "moon":
        show 19
        "18" 
        
    if tenth== "sun":
        show 20
        "19" 
        
    if tenth== "judgement":
        show 21
        "20" 
        
    if tenth== "world":
        show 22
        "21" 





