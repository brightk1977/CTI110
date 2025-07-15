# Kristopher Bright
# 7/14/2025
# P5HW1
# An 80s inspired adventure game with lots of little easter eggs and references <3

import random
import sys
import time

print(r"""

                                                                 
                          .*@@@@@@@@@+.                          
                        @@= -         =@%                        
                      @@.**             :@*                      
                     @-:@                 %@                     
                    @:=+                   %@                    
                   @# %                    .@                    
                .:%@:                     :*@@@@@#:.             
            .@@@=. :#@@@@@%*++**#%@@@@@@%=.       .=@@%          
        .%@@-   .                           #@%.       +@@:      
      +@#    :@. :@.    -@@+      -@@#    :@   *%         #@-    
    *@:      @    @.   @:  .@    %+   @.  .@.  #@         -@@+   
   =@+@+      #@@@.    @=  +@    +@  :@.    .++       .#@* +@.   
    @@. .%@@-.           +=        .:           .:@@@-  .@@-     
      =@@=    :-%@@@@#=:              .-+%@@@@=:    -@@@:        
          +@@@@*-.           .....          .-*@@@@+             
                @@=#@@@@@@@@@@@@@@@@@@@@@@%=  +@:                
                  +@@-                     #@@.                  
                     .*@@@@*=-::::-=+#@@@@=                      
                    @-  .                                        
                  %@  :@            :@  @-                       
                 @.  *@              %-  #%                      
                    @+               :@                          
  
 ____      ____  ____  ____  ________  _______     ________   
|_  _|    |_  _||_   ||   _||_   __  ||_   __ \   |_   __  |  
  \ \  /\  / /    | |__| |    | |_ \_|  | |__) |    | |_ \_|  
   \ \/  \/ /     |  __  |    |  _| _   |  __ /     |  _| _   
    \  /\  /     _| |  | |_  _| |__/ | _| |  \ \_  _| |__/ |  
     \/_ \/    _|____||____||________||____|_|___||________|  
 
       _      _____    ____      ______      ____
      / \     |_   \  /   _|     |_   _|    / ___ `.            
     / _ \      |   \/   |         | |     |_/___) |            
    / ___ \     | |\  /| |         | |       /  __.'            
  _/ /   \ \_  _| |_\/_| |_       _| |_      |_|                
 |____| |____||_____||_____|     |_____|     (_)     
 
 ____________________________________________________________
 ____________________________________________________________
 
    """)


    
# ────────────── State Constants ──────────────
STATE_ROOM1   = 1
STATE_ROOM2   = 2
STATE_ROBOT   = 3
STATE_ALIEN   = 4
STATE_ROOM3   = 5
STATE_AIRLOCK = 6
PAUSE         = 0.6

# ────────────── Global Variables ──────────────
state = STATE_ROOM1

player_name = ""

inventory = {
    'door keycard':    False,
    'probing stick':   False,
    'alien cookies':   False,
    'left shoe':       False,
    'right shoe':      False,
    'airlock keycard': False,
    'bomb':            False,
    'sunkist soda':    False,
    'pen':             False,
    
}

events = {
    'robot_defeated':   False,
    'aliens_distracted': False,
}

# Rarity weights for RNG selection (lower => rarer)
RARITY = {
    'left shoe':       3,
    'right shoe':      3,
    'pen':             3,
    'sunkist soda':    3,
    'robot':           7,
    'bomb':            6,
    'airlock keycard': 7,
    'door keycard':    8,
    'probing stick':   8,
    'alien cookies':   8,
    'trash':           9,
    'dust':            9,
}

# ────────────── Utility Functions ──────────────

def game_over(text="Game Over"): 
    print(text)
    sys.exit()


def game_win(text="You Win"):  
    print(text)
    sys.exit()


def weighted_choice(options):
    names, weights = zip(*options)
    return random.choices(names, weights=weights, k=1)[0]


def have_both_shoes():
    return inventory['left shoe'] and inventory['right shoe']

# ────────────── Search Functions ──────────────

ITEM_MESSAGES = {
    'door keycard': "In a drawer you find a small retangular piece of plastic\n'Maybe its a key?'",
    'probing stick': "On the desk you pick up an electric probing rod\nyou shutter to think about what its used for\n'Eww, maybe I shouldn't be touching this'",
    'alien cookies': "-CRUNCH!- \nYou steped on a bag... of alien cookies!\nScanning the label, you don't recognize any of the ingredients\n'psshh.. what's new? Probably full of calories anyway'",
    'left shoe': "You find your left shoe... at least you think its yours\n'Where's my other shoe?'",
    'right shoe': "At last, it's your other shoe!\n'I knew it had to be around here somewhere'",
    'airlock keycard': "Under some trash on the floor you find another key.\nHold on to it, it'll probably save your life",
    'bomb': "Woah! You would recognize this on any planet. This is definitely a bomb!\n'I gotta be careful with this'",
    'sunkist soda': "Inside what you can only assume is a refrigerator\nyou find a full bottle of Orange Sunkist\n'No way! Did I bring this with me?'",
    'pen': "It's just a pen... it kinda looks like your pen, but nahh... you always forget it"
}
def search_room1():
    global state
    pool = []
    for item in ('door keycard','probing stick','alien cookies','left shoe'):
        if not inventory[item]:
            pool.append((item, RARITY[item]))
    pool.append(('dust', RARITY['dust']))
    result = weighted_choice(pool)

    if result == 'dust':
        print("\nYou find some junk - nothing useful.")
    else:
        inventory[result] = True
        print(f"\n{ITEM_MESSAGES.get(result, f'You found {result}.')}")
        if have_both_shoes():
            game_win("You find your other shoe! With both now in hand you put them on\nYou start to remember\n'Oh yeah, my SpaceCast! Well, it's time to go home Charlotte'\nYou and your dog float through the ceiling and blast through the galaxy\n'Welcome back Clancy, how was your adventure?'")



def search_room2():
    global state
    pool = []
    for item in ('right shoe','airlock keycard','bomb','sunkist soda','pen'):
        if not inventory[item]:
            pool.append((item, RARITY[item]))
    if not events['robot_defeated'] and not events['aliens_distracted']:
        pool.append(('robot', RARITY['robot']))
    pool.append(('dust', RARITY['dust']))
    result = weighted_choice(pool)

    if result == 'dust':
        print("\nUggh! More junk\n'Does no one clean around here?'")
    elif result == 'robot':
        state = STATE_ROBOT
    else:
        inventory[result] = True
        print(f"\n{ITEM_MESSAGES.get(result, f'You found {result}.')}")
        if have_both_shoes():
            game_win("With both now in hand you put them on and start to remember\n'Oh yeah, my SpaceCast! Well, it's time to go home Charlotte'\nYou and your dog float through the ceiling and blast through the galaxy\nA robotic voice greets you:\n'Welcome back Clancy, how was your adventure?'")

# ────────────── Item Use Logic ──────────────

def apply_item(item, context):
    global state
    # Bomb -> always game over
    if item == 'bomb':
        game_over("\nExcellent plan, the bomb must be the way out of here\nYou start pushing random buttons until it starts to beep rapidly\n'I wonder how much time I have until*KABOOM*'\nGAME  OVER")

    # Cookies outside hostile -> poison
    if item == 'alien cookies' and context != 'alien_hostile':
        game_over("\nAll this searching around has made you hungry. 'It's my cheat day after all'\nSoon you don't feel so good...\nYour body starts to boil from the inside out!\nSuddenly you spontaniously combust\nAll that's left of you is a little pile of ashes on the floor\nGAME  OVER")

    # Robot encounter context
    if context == 'robot':
        if item == 'probing stick':
            events['robot_defeated'] = True
            print("\nGood thinking! You jam the electrified prob into the robot\nIt's power fades out as it crashes to the floor")
            state = STATE_ROOM2
        else:
            game_over(f"\nThat's not good. That seemed to make it even more upset!\n'ANY LAST WORDS {player_name.upper()}?'\nIt raises its blaster at you and fires\nGAME  OVER")
        return

    # Alien hostile context
    if context == 'alien_hostile':
        if item == 'alien cookies':
            events['aliens_distracted'] = True
            inventory['alien cookies'] = False
            print("\nIn a moment of quick thinking, you toss the cookies their way.\nIt works! They race each other to the bag, giving you time to slip by")
            state = STATE_ROOM3
        else:
            game_over("\n It did't work! The aliens make a strange sound in unison. You've never heard anything like it\n'Was that an alien laugh?'\nThey reach out and hold each side of your head until you lose conciousness\n*GAME  OVER*")
        return

    # Airlock context
    if context == 'airlock':
        if item == 'airlock keycard':
            print("'REPRESSURISING AIR LOCK'\nAfter a brief countdown, the doors open\nOnce inside, they shut behind you")
            state = STATE_AIRLOCK
        else:
            print("\nYep, you're betting this is also a key...")
        return

    # Default room/item interactions
    if item == 'sunkist soda':
        print("\nWhat luck, they have Sunkist on this ship!\nYou finish the whole bottle like it could be your last\n'Delicious!'")
        inventory['sunkist soda'] = False
        return
    print("\n'on second thought, maybe this isn't that useful right now...'")


def prompt_use_item(context):
    owned = [i for i,v in inventory.items() if v]
    if not owned:
        print("\nYou check, but it seems all you have \nin your pockets is a losing lottery ticket\n'I should have at least remembered to bring my towel'")
        return
    for idx,itm in enumerate(owned,1):
        print(f"{idx}. {itm}")
    sel = input("Chose item: ")
    if sel.isdigit() and 1 <= int(sel) <= len(owned):
        apply_item(owned[int(sel)-1], context)
    else:
        print(f"\nWrong {player_name}, Wrong! How are you so bad at this?\n")

# ────────────── Room & Encounter Loops ──────────────

def room1_loop():
    global state
    while state == STATE_ROOM1:
        time.sleep(PAUSE)
        print("\n<Holding Bay>\n")
        time.sleep(PAUSE)
        print("(1) Search the room")
        time.sleep(PAUSE)
        print("(2) Move forward to the next room")
        time.sleep(PAUSE)
        print("(3) Go Back")
        time.sleep(PAUSE)
        print("(4) Use an item in your inventory")
        time.sleep(PAUSE)
        cmd = input(": ")
        if cmd == '1':
            search_room1()
        elif cmd == '2':
            if inventory['door keycard']:
                print("\n'...oh man, I sure hope this works'\nYou approach the large white door and scan the card \nit slides open with a sigh as you enter into the next room\n'I think that door just sighed...'")
                state = STATE_ROOM2
            else:
                print("\nYou push and pull and bang against the large door, but it doesn't budge\n'It must be locked...'")
        elif cmd == '3':
            print("\nThere's no going back from here \n'We're a long way from Kansas, Toto'")
        elif cmd == '4':
            prompt_use_item('room')
        else:
            print(f"\nWe thought you were a inteligent human specimen, {player_name}\nI guess not...\nTry picking a valid option next time")


def robot_encounter():
    print(f"\nUh oh! You must have hit something wrong - a robot wakes up!\n'HEY! YOU AREN'T SUPPOSED TO BE IN HERE {player_name.upper()}!'\nYou'll have to find a way to defend yourself'\n")
    while state == STATE_ROBOT:
        prompt_use_item('robot')


def room2_loop():
    global state
    while state == STATE_ROOM2:
        # re-encounter roll when returning
        if events['aliens_distracted']:
            if random.randint(1,6) == 1:
                state = STATE_ALIEN
                break
                time.sleep(PAUSE)
        print("\n<Laboratory>\n")
        time.sleep(PAUSE)
        print("(1) Search the room")
        time.sleep(PAUSE)
        print("(2) Move forward to the next room")
        time.sleep(PAUSE)
        print("(3) Go Back")
        time.sleep(PAUSE)
        print("(4) Use an item in your inventory")
        time.sleep(PAUSE)
        cmd = input(": ")
        if cmd == '1':
            search_room2()
        elif cmd == '2':
            print("Two large, gray aliens enter the room!\nThey're coming right for ya'!")
            state = STATE_ALIEN
        elif cmd == '3':
            print("\nYou head back to the room you woke up in\n'Maybe I missed something'")
            state = STATE_ROOM1
        elif cmd == '4':
            prompt_use_item('room')
        else:
            print(f"\nYou still haven't learned, {player_name}??\nYou can only make valid choices\nDo better!")


def alien_encounter():
    global state
    # initial check
    if inventory['sunkist soda']:
        if inventory['pen']:
            game_win(f"Both speak simultaniously, perfectly in sync.\n'You are the chosen one'nthe one who will deliver the message\na message of hope for those who chose to hear it\nand a warning for those who do not'\nYou think to yourself 'wow! me - the chosen one- they chose me\nAnd I didn't even graduate from highschool\n***YOU  WIN***")
        else:
            game_over(f"Both speak simultaniously, perfectly in sync.\n'You are the chosen one'nthe one who will deliver the message\na message of hope for those who chose to hear it\nand a warning for those who do not'\nYou think to yourself 'wow! me - the chosen one- they chose me\n...wait! No, I forgot my pen\n***GAME  OVER***")
    # hostile branch
    print("Quick! You have to defend yourself!")
    while state == STATE_ALIEN:
        print("Enter (1) to chose an Item")
        cmd = input(": ")
        if cmd == '1':
            prompt_use_item('alien_hostile')
        else:
            game_over("They make a sound in unison. You've never heard anything like it\n'Was that an alien laugh?'\nThey reach out and hold each side of your head until you lose conciousness\n*GAME  OVER*")


def room3_loop():
    global state
    while state == STATE_ROOM3:
        time.sleep(PAUSE)
        print("\n<Holding Bay>\n")
        time.sleep(PAUSE)
        print("(1) Search the room")
        time.sleep(PAUSE)
        print("(2) Move forward to the next room")
        time.sleep(PAUSE)
        print("(3) Go Back")
        time.sleep(PAUSE)
        print("(4) Use an item in your inventory")
        time.sleep(PAUSE)
        cmd = input(": ")
        if cmd == '1':
            print("\nYou don't have time to look around!\nThose cookies won't hold them off for forever")
        elif cmd == '2':
            if inventory['airlock keycard']:
                state = STATE_AIRLOCK
            else:
                print("\nIt's locked! You're gonna have to sneak back into the lab and find the key")
        elif cmd == '3':
            print("\nYou quietly sneak back in, hoping the aliens are still distracted by the cookies")
            state = STATE_ROOM2
        elif cmd == '4':
            prompt_use_item('room')
        else:
            print("\nAt this point in the game, {player_name}, you really should know that you can't\njust type anything in here. Try again...")


def airlock_loop():
    global state
    while state == STATE_AIRLOCK:
        print("\nSafe! They can't get to you in here, you have the only key card. But... now what?\nYou stare off into the infinite endless abyss of space\nA large red button on the wall is surrounded by what you can only guess\nis alien for \"caution.\" Is this the only way? (y/n)")
        choice = input().lower()
        if choice.startswith('y'):
            game_win("The vaccum of space sucks you into the infinite silence\nIt's peaceful, but it's cold...\n***YOU  WIN!***")
        else:
            print("'No! There must be something else I can do'")
            state = STATE_ROOM3

# ────────────── Main Dispatcher ──────────────

def main():
    global player_name
    player_name = input("What is your name?\n").strip()
    print("\nYou wake up in a strange room. Your head is")
    print("pounding, and your eyes water from the bright")
    print("lights. You can hear the strange, etheral sounds")
    print("of an otherworldly engine.") 
    print("'Where am I?' You ask yourself")
    print("You sit up from the cool metal slab you were")
    print("laying on and look around the room...\n")
    print("How are you going to get out of here?")
    while True:
        if state == STATE_ROOM1:
            room1_loop()
        elif state == STATE_ROBOT:
            robot_encounter()
        elif state == STATE_ROOM2:
            room2_loop()
        elif state == STATE_ALIEN:
            alien_encounter()
        elif state == STATE_ROOM3:
            room3_loop()
        elif state == STATE_AIRLOCK:
            airlock_loop()
        else:
            game_over("[Unknown state]")

if __name__ == "__main__":
    main()

