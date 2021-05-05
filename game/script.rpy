# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("darksider")
define m = Character("me")

# The game starts here.

label start:

    # Start by playing some music.
    play music "epic.opus"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene swamp
    show bg2

    show s1l

    "whats that.another body?"
    hide s1l
    show s2r
    with moveinright
    "yes he dead badly.poor stinky maggot"
    hide s2r
    show s1l
    "let him go"
    "may his body can rest in peace in swamp at last"
    hide s1l
    hide bg2
    show swamp

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show swamp

    # These display lines of dialogue.

    d "yess im finally arrive hear ."

    d "after all this months"

    d "im revelanted."

    hide swamp

    show closed eyes

    # These display lines of dialogue.

    d "just whaiting for revenge."

    d "just trying to write some scripts today."
    
    hide closed eyes

    show openeye

    # These display lines of dialogue.

    d "i must findout my stuffs."

    d "i burry them n cementry."
    
    hide openeye

    show swamp rise

    # These display lines of dialogue.

    d "bettr go faster."

    # These display lines of dialogue.

    d "before they find me?."
    hide swamp rise
    show bg15
    with dissolve

    # These display lines of dialogue.

    "cementry is house o demons and ghosts now."
    "creey creatures who living in old cementry eating dead bodies flesh and bones"
    "they can smell alive creatures breath and hear them heart beats"
    "they defence of swamp dragon territory and call swamp dragon to kill you"
    show nomask
    with moveinright

    d "i can feel demons"
    d "they very near to me"
    show bg3
    d "my stuffs is other side of cementry"
    d "i burried them under the cone shape bulding"
    d "in must across betwin ghosts"
    hide bg3
    show bg15
    d "the mask can take me some power i do need"

    d "its beter to put my mask on"

    show mask

    # These display lines of dialogue.

    menu:

        "mask of death do you want to put it on your face?"

        "yes i put i on":
            jump maskon

        "no i dont need it":
            jump nomask

   
label nomask:

    $ nomask = True

    scene cementry
    show bg15
    with fade
    show nomask
    with moveinright
    play music "sooo.opus"
    
    d " i must move very quick and quiet "

    d "if ghostsand and demons can find me i will be in truble "

    hide nomask
    show bg3
    show demon
    with moveinright

    "i can smell humen flesh anlive human is around hear"
    "i must to find it first and call dragon"
    "he is there an alive man"
    hide demon
    hide bg3
    show bg15

    show nomask
    with moveinright
    d "damn! they find me"
    d "i dont have any stuff to kill them"
    show bg17
    show nomask
    d "better run away"
    hide bg17
    show bg3
    show demon2
    with moveinright
    "ghrrrrrrrrrrrrrrr ghrrrrrrrrrrrrrrrrr"


    show dragon1

    "the swamp dragon heard the voice and turn around to kill any alive creatures"
    "on this territory"
    show bg16
    show nomask
    d "there is no way to run away from it "
    d "dragon sat all forrest on fire"
    show dragon2
    "dragon kill every alive creature to feed demons"
    "dead bodies flesh for its territory demons"
    show dragon4
    "rosted human is a good food for my demons"
    show dragonnomask
    "burn in my fire you puny human"
    show udie
    # This ends the game.

    return


label maskon:

    $ maskon = True

    scene cmentry
    show bg15
    with fade

    play music "ff3.mp3"

    show mask6
    with moveinbottom
    d "this mask makes me stronger and invisible in front of demons"
    hide mask6
    show mask11
    d "i must find my stuffs and kill the beasts and demons"
    d "." 

    d "..."

    hide mask11

    show doom
    show weapons
    with moveinbottom

    show mask11
    d "finally find my weapons"
    d "now ill wipe out this forrest of demons and beasts"
    
    show demon

    d "come hear demon  and teast my weapons "

    hide mask11
    hide weapons
    "human? with death mask on his face ? but how?"

    show demon2
    "ghrrrrrrrrrrrrrrrrrrrrrrrrrrr"

    menu:      

        m "demon called the dragon .and it come too burn up me"

        "run away from hear ":
            jump nomask

        "i have a plan too kill dragon":
            jump plan

    hide me

    show sylvie green giggle
    e "die you idiot."

    show blood

    e "this is your end"

    # This ends the game.

    return

label plan:

    $ plan = True

    scene fireforrest

    show dragon1

    "the swamp dragon heard the voice and turn around to kill any alive creatures"
    "on this territory"
    show bg16
    show mask11
    d "dragon sat all forrest on fire"
    hide mask11
    show dragon2
    "dragon kill every alive creature to feed demons"
    "dead bodies flesh for its territory demons"
    show dragon4
    "rosted human is a good food for my demons"
 
    show mask11
    
    d "hey you  big lizzard !"
    d "do you know who am i?"
    d "i am the death"
    d "idont affraid of you"
    d "i have the dragon heart with me.do you want to see?"

    hide mask11

    
    "heart of a dragon?"
    d "do you want tosee?come closer"
    show dragon3
    "well show me now"
    "i want to see that heart"
    hide dragon3
    with dissolve
    show bg14
    show maskarm
    d "hear i must ready it first"
    d "because its in your chest"
    show dragon6

    ""



