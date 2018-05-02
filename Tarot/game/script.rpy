# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    python: 
        a = ['fool', 'magician', 'high priestess', 'empress', 'emperor', 'hierophant', 'lovers',
            'chariot', 'strength', 'hermit', 'wheel of fortune', 'justice', 'hanged man', 'death',
            'temperance', 'devil', 'tower', 'star', 'moon', 'sun', 'judgement', 'world']
        for i in range(10):
            from random import randint
            x= randint(0, 21)
            y = (a[x])
             
            
    if y==1:
        jump yee
    else: 
        jump yee
                    
label yee:
    if y==fool:
        e "gotem"

    
    return
