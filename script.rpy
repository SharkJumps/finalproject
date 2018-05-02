# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Jeef", color="#3C932A")


# The game starts here.

define config.name = _('Guys, guys, the ugandan knuckles is meme is still funny XXXXXXXXXXXXXDDDDDDDDDDDDDDDDD. Wait where are you going? Please come back')

define gui.show_name = True

define config.version = "1.0"

define gui.about = _("Made by Big Money.")
#Rough start to test the engine and see what it can do

label start:
    play music "finnawoke.mp3"
    scene bgfrontschool
    with fade
    show pupper
    c "Hello world!"
return 
#Simple beginning understandable and basic- good start 