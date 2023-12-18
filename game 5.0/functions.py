
import random as rand
import time
import sys
import data
import string

class Player:
    def __init__ (self, name, element, attack, defense, lives, level, Inventory, money, pity1, pity2, infamy, health='\n===================='):
        self.name = name
        self.element = element
        self.attack = attack
        self.defense = defense
        self.health = health
        self.level = level
        self.bars = 20
        self.lives = lives
        self.Inventory = Inventory
        self.money = money
        self.infamy = infamy
        # to make sure you dont get the same destination twice in a row from the explore and travel function
        self.explorePity = pity1
        self.travelPity = pity2

    def shop (self):
        while True:
            print ("""
                   
---------Welcome to The Shop--------

     --Item--             --Price--                   

1. Health Potion    -    100 credits               
2. Attack Potion    -    100 credits
3. Defense Potion   -    100 credits

4. Leave
------------------------------------
What do you want to buy?""")

            choice = input ('')
            if choice == "1":
                try:
                    potionAmount = int(input('How many Health Potions would you like to buy? '))
                    cost = 100 * potionAmount
                    if self.money - cost < 0:
                        slowPrint ('You dont have enough money. \n', 0.05)
                        continue
                    else:      
                        self.money -= cost

                        for potion in range (0, potionAmount):
                            self.Inventory.append ('Health Potion')

                        time.sleep (0.5)
                        slowPrint (f'You bought {potionAmount} Health Potion(s) for {potionAmount * 100} credits \n', 0.05)
                        time.sleep (0.5)
                        slowPrint (f'Your balance is now {self.money} credits', 0.05)
                        continue                
                except:
                    slowPrint ("Invalid number. \n", 0.05)
                    time.sleep (1)
                    continue
            elif choice == "2":
                try:
                    potionAmount = int(input('How many Attack Potions would you like to buy? '))
                    cost = 100 * potionAmount
                    if self.money - cost < 0:
                        slowPrint ('You dont have enough money. \n', 0.05)
                        continue              
                    self.money -= cost

                    for potion in range (0, potionAmount):
                        self.Inventory.append ('Attack Potion')

                    time.sleep (0.5)
                    slowPrint (f'You bought {potionAmount} Attack Potion(s) for {cost} credits \n', 0.05)
                    time.sleep (0.5)
                    slowPrint (f'Your balance is now {self.money} credits', 0.05)
                    continue
                except:
                    slowPrint ("Invalid number. \n", 0.05)
                    time.sleep (1)
                    continue
            elif choice == "3":
                try:
                    potionAmount = int(input('How many Defense Potions would you like to buy? '))
                    cost = 100 * potionAmount
                    if self.money - cost < 0:
                        slowPrint ('You dont have enough money. \n', 0.05)
                        continue                    
                    self.money -= cost

                    for potion in range (0, potionAmount):
                        self.Inventory.append ('Defense Potion')

                    time.sleep (0.5)
                    slowPrint (f'You bought {potionAmount} Defense Potion(s) for {potionAmount * 100} credits \n', 0.05)
                    time.sleep (0.5)
                    slowPrint (f'Your balance is now {self.money} credits', 0.05)
                    continue
                except:
                    slowPrint ("Invalid number. \n", 0.05)
                    time.sleep (1)
                    continue
            elif choice == "4":
                slowPrint ('Leaving The Shop \n', 0.05)
                return self.money and self.Inventory
            else:
                print ('Invalid input. Choose 1, 2, 3 or 4')
            continue

    def fight (self,enemy, situation):

        # needed for when you reset player's temporarily increased stats to the player's default stats after the battle is over
        defaultAttack = self.attack        
        defaultDefense = self.defense

        print ('\n-----FIGHT!-----')
        print (f"\n{self.name}")
        print (f"ELEMENT: {self.element}")
        print (f"ATTACK: {self.attack}")
        print (f"DEFENSE: {self.defense}")
        print ("\nVS")
        print (f"\n{enemy.name}")
        print (f"ELEMENT: {enemy.element}")
        print (f"ATTACK: {enemy.attack}")
        print (f"DEFENSE: {enemy.defense}")

        time.sleep (2)
        
        # if hero has element advantage
        if self.element == 'Fire' and enemy.element == 'Grass' or self.element == 'Grass' and enemy.element == 'Water' or self.element == 'Water' and enemy.element == 'Fire':
            self.attack *= 2
            heroMessage = 'Its super effective!'
            enemyMessage = 'Its not very effective...'
            counterMessage = 'It was effective'
        
        # if player and enemy element are the same
        elif self.element == enemy.element:
            heroMessage = 'Its not very effective...'
            enemyMessage = 'Its not very effective...'
            counterMessage = 'It was effective'

        # if enemy has element advantage
        else:
            enemy.attack *= 2
            heroMessage = 'Its not very effective...'
            enemyMessage = 'Its super effective!'
            counterMessage = 'It was effective'

        while self.bars > 0 and enemy.bars > 0:
            print (f"\n{self.name} Health: \n{self.health}")
            print (f"\n{enemy.name} Health: \n{enemy.health}")

            time.sleep (1)

            # hero's turn
            while True:
                print ("\nHero's turn: ")
                print ("""

1. Attack       2. Counter
3. Inventory                   

""")
                choice = input('What do you want to do? ')
                if choice == "1":
                    slowPrint (f'\nYou attacked the {enemy.name}\n', 0.05)
                    print (heroMessage)
                    break
                elif choice == "2":
                    # counter does dmg based on your defense stat. supposed to be used when you have element disadvantage
                    crit = rand.randint (0,10)
                    if crit >= 5:
                        slowPrint ('\nYou countered the enemy\n', 0.05)
                        print ('Critical hit!')
                        print (counterMessage)
                        break
                    else: 
                        slowPrint ('\nYou countered the enemy\n', 0.05)
                        print (counterMessage),
                        break
                elif choice == "3":

                    # variable to check if player used a potions or not 
                    while True:

                        # prints your inventory then checks if you have any potions
                        potions = inventory (self.Inventory, 'nono')
                        if potions [0] <= 0 and potions [1] <= 0 and potions [2] <= 0:
                            slowPrint ('\nYou do not have any potions\n', 0.05)
                            break

                        answer = input("""

1. Health Potion
2. Attack Potion
3. Defense Potion                                                                                 
select potion: """)
                        if answer == "1":
                            # check if player has any health potions
                            if potions [0] > 0:
                                    
                                self.bars += 8
                                slowPrint ('\nYou used the healing potion\n', 0.05)
                                # prevents healing over hp cap :)
                                if self.bars > 20:
                                    self.bars = 20
                                self.health = "=" * self.bars
                                inventory (self.Inventory, 'hp')
                                break
                            else:
                                slowPrint ('\nYou do not have any health potions\n', 0.05)
                            
                        elif answer == "2":
                            # check if player has any attack potions
                            if potions [1] > 0:

                                self.attack += 3
                                slowPrint ('\nYou used the attack potion\n', 0.05)
                                inventory (self.Inventory, 'atk')
                                break
                            else:
                                slowPrint ('\nYou do not have any attack potions\n', 0.05)
                            
                        elif answer == "3":
                            # check if palyer has any defense potions
                            if potions [2] > 0:

                                self.defense += 3
                                slowPrint ('\nYou used the defense potion\n', 0.05)
                                inventory (self.Inventory, 'def')
                                break
                            else:
                                slowPrint ('\nYou do not have any defense potions\n', 0.05)
                                break
                        else:
                            print ('Choose 1, 2 or 3'),
                        break
                    break
                
                time.sleep (1)

            if choice == "1":
                enemy.bars -= self.attack
                enemy.health = "=" * enemy.bars
            elif choice == "2":
                enemy.bars -= self.defense
                enemy.health = '=' * enemy.bars

            time.sleep (1)

            print (f"\n{self.name} Health: \n{self.health}")
            print (f"\n{enemy.name} Health: \n{enemy.health}")

            time.sleep (1)

            # check for winner
            if situation == 'normal':
                if enemy.bars <= 0:
                    slowPrint ('\nYou won the battle \n', 0.05)

                    self.bars = 20
                    enemy.bars = 20
                    self.health = '===================='
                    self.attack = defaultAttack
                    self.defense = defaultDefense

                    self.level += 1

                    # randomly generates a potion
                    reward = get_potion ()
                    slowPrint (f'You have been awarded with a(n) {reward}. You added it to your inventory \n', 0.05)
                    
                    self.Inventory.append (reward)
                    

                    return self.level and self.Inventory
            elif situation == 'modified':
                if enemy.bars <= 0:
                    slowPrint ('You won the fight\n', 0.05)

                    return True

            # enemy's turn

            print ("\nEnemy's turn: ")
            enemyChoice = rand.randint (1,2)

            # if enemy attacks
            if enemyChoice == 1:
                slowPrint (f'The {enemy.name} attacked you\n')
                print (enemyMessage)
            elif enemyChoice == 2:
                enemyCrit = rand.randint (7,10)
                if enemyCrit >= 7:
                    slowPrint (f'The {enemy.name} countered you\n', 0.05)
                    print ('Critical hit!')
                    print (counterMessage)
                else:
                    slowPrint (f'The enemy {enemy.name} countered you\n', 0.05)
                    print (counterMessage)
            
            time.sleep (1)

            if enemyChoice == 1:
                self.bars -= enemy.attack
                self.health = "=" * self.bars
            elif enemyChoice == 2:
                self.bars -= enemy.defense
                self.health = '=' * self.bars

            # check for winner
            if situation == 'normal':
                
                if self.bars <= 0:

                    print (f"\n{self.name} Health: \n{self.health}")
                    print (f"\n{enemy.name} Health: \n{enemy.health}")
                    
                    slowPrint ('\nYou lost the battle \n', 0.05)

                    self.bars = 20
                    enemy.bars = 20
                    self.attack = defaultAttack
                    self.defense = defaultDefense
                    self.health = '===================='

                    self.lives -= 1
                    return self.lives
            elif situation == 'modified':
                
                if self.bars <= 0:

                    print (f"\n{self.name} Health: \n{self.health}")
                    print (f"\n{enemy.name} Health: \n{enemy.health}")

                    slowPrint ('\nYou lost the battle \n', 0.05)

                    self.bars = 20
                    enemy.bars = 20
                    self.attack = defaultAttack
                    self.defense = defaultAttack
                    self.health = '===================='

                    self.lives -= 1
                    return self.lives

class Enemy:
    def __init__ (self,name,element,attack,defense,health='\n===================='):
        self.name = name
        self.element = element
        self.attack = attack
        self.defense = defense
        self.bars = 20
        self.health = health

class Riddles:
    def __init__ (self, riddle, alternative1, alternative2, alternative3, correctAnswer):
        self.riddle = riddle
        self.alternative1 = alternative1
        self.alternative2 = alternative2
        self.alternative3 = alternative3
        self.correctAnswer = correctAnswer

def get_potion ():
    healingPotion = 'Health Potion'
    attackPotion = 'Attack Potion'
    defensePotion = 'Defense Potion'
    determinePotion = rand.randint (1,3)
    if determinePotion == 1:
        return healingPotion
    elif determinePotion == 2:
        return attackPotion
    elif determinePotion == 3:
        return defensePotion
    
def map (hero):
    while True:
        print ("""
-----Locations-----

1. The Shop


4. Return to adventure
-------------------

Where do you want to go? 
""")
        answer = input('')
        if answer == "1":            
            slowPrint ('Traveling to the shop...', 0.05)
            time.sleep (1)
            hero.shop ()
            continue
        elif answer == "4":
            slowPrint ('Returning to adventure...', 0.05)
            return
        else:
            print ('Invalid location. Please enter a valid location')
            continue

def inventory (inv,removePot):
    hpPot_count = inv.count ('Health Potion')
    atkPot_count = inv.count ('Attack Potion')
    defPot_count = inv.count ('Defense Potion')
    # removePot parameter controls if you want to check your inventory or remove a potion from inventory
    if removePot == 'no' or removePot == 'nono':
        slowPrint ('Loading inventory...\n', 0.05)
        time.sleep (1)
        print (f"""
---Potions---
Health Potions:  {hpPot_count}
Attack Potions:  {atkPot_count}
Defense Potions: {defPot_count}
""")
        if removePot != 'nono':
            input ('Press any key to return to your adventure: ')
            slowPrint ('Returning to adventure...', 0.05)
            time.sleep (1)
            return
        else:
            return hpPot_count, atkPot_count, defPot_count
    elif removePot == 'hp':
        inv.remove ('Health Potion')
    elif removePot == 'atk':
        inv.remove ('Attack Potion')
    elif removePot == 'def':
        inv.remove ('Defense Potion')
    return hpPot_count, atkPot_count, defPot_count
     
def slowPrint(string, speed=0.05):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)    

def stats (hero):
    slowPrint ('Loading stats...\n', 0.05)
    time.sleep (1)

    life_string = f'You have {hero.lives} lives left'
    if hero.lives == 1:
        life_string = f'You have one {hero.lives} left...'

    print (f"""
--------------------------
Name:       {hero.name}
Level:      {hero.level}
Element:    {hero.element}
Attack:     {hero.attack}
Defense:    {hero.defense}
Money:      {hero.money}
Infamy:     {hero.infamy}

{life_string}
--------------------------
""")
    input('Press any key to return to your adventure: ')
    slowPrint ('Returning to adventure...', 0.05)

def inn (hero):
    slowPrint ('You found an inn and and decided to stay for the night',0.05)
    while True:
        print ("""    
1. Get drunk
2. Gamble
3. Start a fight
4. Leave
What do you want to do?                
""")
        answer = input('')
        if answer == '1':
            print ('drunk :)')
            return
        elif answer == '2':
            casino(hero)
        elif answer == '3':
            barFight (hero)
            slowPrint ('Leaving the inn...', 0.05)
            return
        elif answer == '4':
            slowPrint ('Leaving the inn...', 0.05)
            time.sleep (1)
            break

def drunk (hero):

    slowPrint ('You woke up 12 hours later feeling completely wasted...\n', 0.05)
    moneyLost = round(hero.money * 0.25)
    slowPrint (f'You checked your pockets and realized someone stole {moneyLost} of your credits.\n')

def travel (hero):

    # make sure you dont roll the same function twice in a row (same principle as in explore function)

    # if first time in travel function
    if hero.travelPity == 0:
        next = rand.randint (1,3)

    # if last function was cave function
    elif hero.travelPity == 1:
        next = rand.randint (2,3)

    # if last function was village function
    elif hero.travelPity == 2:
        availableNumber = [1,3]
        next = rand.choice (availableNumber)

    # if last function was inn function
    elif hero.travelPity == 3:
        next = rand.randint (1,2)

    if next == 1:
        cave (hero)
        hero.travelPity = 1
    elif next == 2:
        village (hero)
        hero.travelPity = 2
    elif next == 3:
        inn (hero)
        hero.travelPity = 3

def normalBattle (hero):

    enemyList = ["Ninja", "theif", "Golem"]
    elementList = ['Fire', 'Water', 'Grass']

    enemy = Enemy (rand.choice (enemyList), rand.choice (elementList), rand.randint (hero.attack-1,hero.attack+1), rand.randint (hero.defense-1,hero.defense+1))

    slowPrint ("""
                        __________
                      .~#########%%;~.
                     /############%%;`\\
                    /######/~\/~\%%;,;,\\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@                  .
""", 0.0009)
    
    print (f'\nA {enemy.name} appeared!')

    time.sleep (1.5)                                                                                   

    hero.fight (enemy,'normal')
    slowPrint (f'\nYour level: {hero.level}', 0.05)
    slowPrint (f'\nLives left: {hero.lives}', 0.05)
    slowPrint ('\nLeaving the battlefield...', 0.05)
    time.sleep (1)

def barFight (hero):
    enemyList = ["Drunk man", "Bartender"]
    elementList = ['Fire', 'Water', 'Grass']
  
    enemy = Enemy(rand.choice(enemyList), rand.choice(elementList), rand.randint (hero.attack-1,hero.attack+1), rand.randint (hero.defense-1,hero.defense+1))

    if enemy.name == 'Bartender':
        slowPrint ('You angered the bartender \n', 0.05)
    else:
        slowPrint (f'You found yourself in a fight with a {enemy.name} \n', 0.05)

    time.sleep (1.5)

    hero.fight (enemy, 'normal')
    
    slowPrint (f'\nYour level: {hero.level}', 0.05)
    slowPrint (f'\nLives left: {hero.lives}\n', 0.05)
    time.sleep (1)

def guardBattle (hero, guardAmount):

    defaultAttack = hero.attack
    defaultDefense = hero.defense

    # counts amount of guards defeated
    guardsGone = 1
    
    iterations = 0

    while iterations < guardAmount:
        element = ['Fire', 'Water', 'Grass']
        enemy = Enemy('Guard', rand.choice (element), rand.randint (defaultAttack-2, defaultAttack +1), rand.randint (defaultDefense-2, defaultDefense +1))

        result = hero.fight (enemy,'modified')
        if result == True:
            time.sleep (1)
            slowPrint (f'\n{guardAmount - guardsGone} guard(s) remaining... \n', 0.05)
            time.sleep (0.5)
            guardsGone += 1
            iterations += 1
        else:
            slowPrint ('\nHA!, WEAKLING!\n', 0.05)
            hero.infamy -= 10
            return
    
    slowPrint ('You won against the guards \n', 0.05)
    hero.attack = defaultAttack
    hero.defense = defaultDefense
    hero.infamy += 10*guardAmount
    # if you win against 3 or less guards
    if guardAmount != 4 or guardAmount != 5:
        slowPrint (f'You were awarded with {guardAmount * 1000} credits')
        hero.money += guardAmount * 1000
        return hero.money
    
    # if you win against 4 or more guards
    elif guardAmount == 4 or guardAmount == 5:
        compensation = 10000
        slowPrint (f'You were awarded with {guardAmount * compensation} credits')
        hero.money += guardAmount * compensation
        return hero.money

def village (hero):
    slowPrint ("""
~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '

""", 0.001)
    time.sleep (1)
    slowPrint ('You found a village', 0.05)
    time.sleep (1)
    if hero.infamy > 100:
        slowPrint ('While wandering around the village you saw a few wanted posters with your name on it...', 0.05)
    print ("""
           
1. Plunder village
2. Look around for loot
3. Leave
""")
    answer = input("")
    while True:
        if answer == "1":
            if hero.infamy < 10:
                guardAmount = rand.randint (1,2)
            elif hero.infamy >= 10 and hero.infamy < 100:
                guardAmount = rand.randint (2,5)
            elif hero.infamy >= 100:
                guardAmount = rand.randint (5,10)

            slowPrint (f'While you were plundering you alerted {guardAmount} guard(s)', 0.05)
            time.sleep (2)
            guardBattle (hero, guardAmount)
            time.sleep (1)
            slowPrint ('\nLeaving the village...', 0.05)
            break

        elif answer == "2":
            slowPrint ('You wandered around for a while \n', 0.05)
            slowPrint ('Atlast you found a chest hidden in an old abandoned house \n', 0.05)
            slowPrint ('You opened the chest... \n', 0.05)
            reward1 = get_potion ()
            reward2 = get_potion ()
            reward3 = get_potion ()
            slowPrint (f'You found --{reward1}, {reward2}, {reward3}--. You added them to your inventory \n', 0.05)
            time.sleep (0.5)
            hero.Inventory.append (reward1)
            hero.Inventory.append (reward2)
            hero.Inventory.append (reward3)
            return hero.Inventory
        elif answer == "3":
            slowPrint ('Leaving the village...', 0.05)
            break
        else:
            print ("Invalid input. Enter 1, 2 or 3")

def cave (hero):
    
    slowPrint('You found a beautiful waterfall!\n', 0.05)
    slowPrint("""
                                _____,,,\//,,/,/,
                                /-- --- --- -----
                                ///--- --- -- - ----
                            o////- ---- --- --
                            !!//o/---  -- --
                            o*) !///,~,,\\,\/,,/,//,,
                            o!*!o'(\          
                            | ! o ",) 
                            o  !o! !!|  
                        ( * (  o!'; 
                            o o ! * !`
                        o  |  o 'o|
                            *  o !*!':
                                (o''| `
                                ! *|'`  
                            ' !o!':
                                ( ('|  
    ////\\\,,\///,,,,\,/oO._*  o !*!'`  
    ---- -- ------- - -oO*OoOo (o''|          
        --------  ------ 'oO*OoO!*|'o!!         
    -------  -- - ---- --* oO*OoO *!'| '         
    ---  -   -----  ---- - oO*OoO!!':o!'       
    - -  -----  -  --  - *--oO*OoOo!`       
    \\\\\,,,\\,//////,\,,\\//\/,,\..\n""", 0.002)


    slowPrint('\nBut wait, there is something hidden behind it...\n', 0.05)
    time.sleep(1)

    slowPrint("""                  
                                _____,,,\//,,\\,/,
                                /-- --- --- -----
                                ///--- --- -- - ----
                            o////- ---- --- --
                            !!//o/---  -- --
                            o*) !///,~,,\\,\/,,/,//,,
                            o!*!o'(\          /\\
                            | ! o ",) \/\  /\  /  \/\\
                            o  !o! !!|    \/  \/     /
                        ( * (  o!'; |\   \       /
                            o o ! * !` | \  /       \\
                        o  |  o 'o| | :  \       /
                            *  o !*!': |o|  /      /
                                (o''| `| : /      /
                                ! *|'`  \|/       \\
                            ' !o!':\  \\        \\
                                ( ('|  \  `._______/
    ////\\\,,\///,,,,\,/oO._*  o !*!'`  `.________/
    ---- -- ------- - -oO*OoOo (o''|           /
        --------  ------ 'oO*OoO!*|'o!!          \\
    -------  -- - ---- --* oO*OoO *!'| '         /
    ---  -   -----  ---- - oO*OoO!!':o!'       /
    - -  -----  -  --  - *--oO*OoOo!`         /
    \\\\\,,,\\,//////,\,,\\\/,,,\,,""",0.002)

    slowPrint('\nYou found a hidden cave!\n', 0.05)
    slowPrint ('Press any key to explore the cave\n')
    input("")

    caveExplore (hero)

def caveExplore (hero):
    time.sleep (0.5)
    slowPrint ('\nThe cave is dark and you can barely see a thing...\n', 0.05)
    slowPrint ('You took a step forward but when you put your foot down no ground was to be found...\n', 0.05)
    slowPrint ('You lost your balance and started falling\n', 0.05)
    slowPrint ('After a few seconds you landed on the ground\n', 0.05)
    slowPrint ('The sound you made when you landed alerted a strange creature who lived in the cave\n', 0.05)
    slowPrint ('The creature slowly approached you with a torch in his hand providing light\n', 0.05)

    slowPrint('\nCreature: Welcome, traveler, to the depths of my domain. What brings you to this dark realm?\n', 0.05)
    slowPrint('I am the guardian of these shadows, and to proceed, you must answer a riddle of the abyss.\n', 0.05)
    slowPrint('Listen well, for the echoes of your answer will resonate through these caverns.\n', 0.05)
    slowPrint('Riddle me this:\n', 0.05)

    riddleOne = Riddles("I'm tall and firm, my branches high, In forests deep, against the sky. Birds make nests upon my boughs, What am I?", 'A Mountain', 'A Tree', 'A Tower', 2)
    riddleTwo = Riddles("I'm born in fire, a molten birth, Upon the earth, my spreading girth. As time goes on, I cool and freeze, What am I?", 'Lava', 'Ice', 'Volcano', 1)
    riddleThree = Riddles("I'm a weaver of dreams in the dark of night, With silver threads, I craft visions so bright. Some call me queen, in the sky, I gleam, What am I?", 'Moon', 'Star', 'Cloud', 1)

    generateRiddle = rand.randint (1,3)

    if generateRiddle == 1:
        riddle = riddleOne
    elif generateRiddle == 2:
        riddle = riddleTwo
    elif generateRiddle == 3:
        riddle = riddleThree

    while True:
        time.sleep (1)
        print (f"""
{riddle.riddle}
    1. {riddle.alternative1}
    2. {riddle.alternative2}
    3. {riddle.alternative3}
    4. Run away...
    """)

        try:
            answer = int(input ('Whats your answer traveler? '))
        
            if answer == riddle.correctAnswer:
                slowPrint ('Congratulations... You solved it. You may leave unharmed...\n', 0.05)
                return
            elif answer != riddle.correctAnswer and answer >=1 and answer <= 3:
                slowPrint ('Ha!...Fool...\n', 0.05)
                if hero.money <= 2:
                    slowPrint ('Ha!... seems like you dont have any money...\n')
                    slowPrint ('*The creature stabbed you....*\n', 0.05)
                    slowPrint ('You lost one life...\n', 0.05)
                    hero.lives -= 1
                    return hero.lives
                else:
                    money = rand.randint (1, hero.money)
                    hero.money -= money
                    slowPrint (f'The creature stole {money} credits from you and threw you out of the cave')
                    time.sleep (1)
                    return hero.money
            elif answer == 4:
                slowPrint ('Oh, so you are trying to run away?\n', 0.05)
                slowPrint ('Big mistake......')
                slowPrint ('While running you suddenly felt a sharp pain in your chest...\n', 0.05)
                slowPrint ('The goblin brutally stabbed you and threw you out of the cave...\n', 0.05)
                slowPrint ('You lost one life...\n', 0.05)
                hero.lives -= 1
                time.sleep (1)
                return hero.lives
            else:
                print ('Please choose 1, 2, 3 or 4\n')
        except ValueError:
            print ('Enter a valid number')

def trap (hero):

    # time.time () - returns time in seconds since jan 1 1970 ????????

    print ('You found a dark cave and decided to explore it')
    time.sleep (1.5)
    print ('Suddenly the walls started to close in on you...')
    time.sleep (1.5)
    print ('You have one second to escape...')
    time.sleep (1.5)

    letters = string.ascii_lowercase
    randomLetter = rand.choice (letters)
    
    print (f'type {randomLetter} to escape')
    clock = time.time ()
    
    answer = input('')
    stopwatch = time.time ()

    # counts how many seconds the user took to answer
    timeDiff = (stopwatch - clock) 

    if answer == randomLetter and timeDiff < 1:
        print (f'You escaped the trap with a margin of {1 - timeDiff} seconds')
    else:
        print ('You got caught in the trap')
        if hero.money >= 100:
            hero.money -= 100
            print (f'You lost 100 credits. Your current balance is {hero.money}')
        
def casino(hero):
        print("""

 __          __  _                              _            _   _               _____          _             _ 
 \ \        / / | |                            | |          | | | |             / ____|        (_)           | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___    | |_ ___     | |_| |__   ___    | |     __ _ ___ _ _ __   ___ | |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | __/ _ \    | __| '_ \ / _ \   | |    / _` / __| | '_ \ / _ \| |
    \  /\  /  __/ | (_| (_) | | | | | |  __/   | || (_) |   | |_| | | |  __/   | |___| (_| \__ \ | | | | (_) |_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    \__\___/     \__|_| |_|\___|    \_____\__,_|___/_|_| |_|\___/(_)
                                                                                                                
                                                                                                                
                                                                                                                """)
        print("Press any button to continue...")
        input()
        start_gamble(hero)       

def coin_flip():
    return rand.choice(['Heads', 'Tails'])

def gamble(bet, choice, hero):
    result = coin_flip()
    slowPrint ('Flipping the coin...... \n')
    time.sleep (2)
    slowPrint(f"The coin landed on...... {result}", 0.05)

    if bet > hero.money:
        slowPrint("You don't have enough money for that bet. Betting your remaining money. \n", 0.05)
        bet = hero.money

    if result.lower() == choice.lower():
        hero.money += bet*2    
        slowPrint("""
            .-------.
            |Jackpot|
  _________ |_______| ____________
 |  __    __    ___  _____   __    |  
 | / _\  / /   /___\/__   \ / _\   | 
 | \ \  / /   //  //  / /\ \\ \  25|  
 | _\ \/ /___/ \_//  / /  \/_\ \ []| 
 | \__/\____/\___/   \/     \__/ []|
 |===_______===_______===_______===|
 ||*|\_     |*| _____ |*|\_     |*||  
 ||*|| \ _  |*||     ||*|| \ _  |*||
 ||*| \_(_) |*||*BAR*||*| \_(_) |*||
 ||*| (_)   |*||_____||*| (_)   |*|| __
 ||*|_______|*|_______|*|_______|*||(__)
 |===_______===_______===_______===| ||
 ||*| _____ |*|\_     |*|  ___  |*|| ||
 ||*||     ||*|| \ _  |*| |_  | |*|| ||
 ||*||*BAR*||*| \_(_) |*|  / /  |*|| ||
 ||*||_____||*| (_)   |*| /_/   |*|| ||
 ||*|_______|*|_______|*|_______|*||_//
 |===_______===_______===_______===|_/
 ||*|  ___  |*|   |   |*| _____ |*||
 ||*| |_  | |*|  / \  |*||     ||*||
 ||*|  / /  |*| /_ _\ |*||*BAR*||*||              
 ||*| /_/   |*|   O   |*||_____||*||        
 ||*|_______|*|_______|*|_______|*||
 |lc=___________________________===|
 |  /___________________________\  |
 |   |                         |   |
_|    \_______________________/    |_
(_____________________________________)

""", 0.0005)
        time.sleep (0.5)
        slowPrint(f"You won! You doubled your bet ({bet}). \n", 0.05)
    else:
        slowPrint(f"You lost!", 0.05)
        slowPrint (f"You lost your bet ({bet}) credits \n", 0.05)
        hero.money -= bet
    

    return hero.money

def start_gamble(hero):
    while True:
        try:
            print(f"You have {hero.money} money to bet")
            bet = int(input("Enter your bet (or 0 to quit): "))
            if bet == 0:
                print("Exiting the casino. Goodbye!")
                break
            elif bet < 0:
                print("Please enter a positive number.")
                continue
            elif bet > hero.money:
                print("Hey, you don't have that much money!")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        choice = input("Heads or Tails? ").capitalize()

        if choice not in ['Heads', 'Tails']:
            print("Invalid choice. Please choose 'Heads' or 'Tails'.")
            continue

        hero.money = gamble(bet, choice, hero)    

        
        print(f"Your current balance: {hero.money}\n")        

def explore(hero):
    # randomizes destination but takes into account "hero.exmploreRNG" to make sure you dont get the same destination twice in a row

    # if its your first time entering this function
    if hero.explorePity == 0:
        destination = rand.randint(1, 4)

    # if your last explore was travel function
    elif hero.explorePity == 1:
        destination = rand.randint (3,4)

    # if your last explore was normalBattle function
    elif hero.explorePity == 2:
        availableNumbers = [1,2,4]
        destination = rand.choice(availableNumbers)

    # if your last explore was trap function
    elif hero.explorePity == 3:
        destination = rand.randint (1,3)

    if destination == 1  or destination == 2:
        travel(hero)
        hero.explorePity = 1
    elif destination == 3:
        normalBattle(hero)
        hero.explorePity = 2
    elif destination == 4:
        trap(hero)
        hero.explorePity = 3

def characterCreation ():
    Inventory = ['Health Potion', 'Attack Potion', 'Defense Potion']

    heroLife = 3  
    heroName = ""
    heroElement = "Fire" 
    heroDefense = 4
    heroStrength = 3
    heroMoney = 100
    heroLevel = 1
    heroInfamy = 0
    # used to make sure player doesnt get the same destionation from exloore function twice in a row
    explorePity = 0
    travelPity = 0

    while True:
        slowPrint ('Do you want to load game or start a new one? \n', 0.05)
        time.sleep (0.5)
        print ("WARNING - if it's your first time playing 'Load game' will cause the game to crash\n")
        slowPrint ("""
1. New game
2. Load game
""", 0.05)
        game = input('Answer: ')

        while game == "1":
            slowPrint ('\n---Character creation---', 0.05)
            input(f'\n Press any key to continue: ')
            
            heroName = input('\nYour name: ')
            print (f'\nHello {heroName}')
            slowPrint ("""
---Elements---

Fire            Fire > Grass
Water           Water > Fire
Grass           Grass > Water""", 0.05)
            
            while True:
                heroElement = input ('\nSelect your element: ')
                if heroElement == 'Fire' or heroElement == 'Water' or heroElement == 'Grass':
                    slowPrint (f'\nYou chose {heroElement}, excellent choice! \n', 0.05)
                    hero = Player(heroName, heroElement, heroStrength, heroDefense, heroLife, heroLevel, Inventory, heroMoney, explorePity, travelPity, heroInfamy)
                    return hero      
                else:
                    slowPrint ('Invalid element, please enter a valid element \n', 0.05)

        if game == "2":
            time.sleep (0.5)
            slowPrint ('Loading data...', 0.05)
            time.sleep (0.5)
            data.loadData ()
            updatedData = data.loadData ()
            storedInventory = data.loadInv ()

            heroLife = int(updatedData [0].strip ("\n"))
            heroName = updatedData [1]. strip ("\n")
            heroElement = updatedData [2].strip ("\n")
            heroDefense = int(updatedData [3].strip ("\n"))
            heroStrength = int(updatedData [4].strip ("\n"))
            heroMoney = int(updatedData [5].strip ("\n"))
            heroLevel = int(updatedData [6].strip ("\n"))
            heroInfamy = int(updatedData [7].strip ("\n"))
            
            Inventory = []
            for potion in storedInventory:
                Inventory.append (potion.strip ('\n'))

            hero = Player(heroName, heroElement, heroStrength, heroDefense, heroLife, heroLevel, Inventory, heroMoney, explorePity, travelPity, heroInfamy)       
            return hero
        else:
            print ('Invalid input. Please enter 1 or 2')
            continue
