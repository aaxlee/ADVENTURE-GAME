import random as rand
import time
import sys
import data
import functions

def main():
    while True:
        try:
            hero = functions.characterCreation ()

            time.sleep (1)
            functions.slowPrint ('Successfully created character', 0.05)
            time.sleep (0.5)
            break
        except:
            functions.slowPrint ('An error occurred while trying to load your save. Your save-file is either corrupted or empty\n', 0.05)
            time.sleep (1.5)

    while hero.lives > 0:

        time.sleep (0.5)
        print (
            f"""

******************
1. Check inventory
2. Explore
3. Check stats
4. Map
5. Save game
******************

""")
        
        choice = input("What do you want to do? ")

        if choice == "1":
            functions.inventory (hero.Inventory, 'no')
        elif choice == "2":
            functions.explore (hero)
        elif choice  == "3":
            functions.stats(hero)
        elif choice == "4":
            functions.map (hero)
        elif choice == "5":
            data_to_store = [hero.lives, hero.name, hero.element, hero.defense, hero.attack, hero.money, hero.level, hero.reputation]
            time.sleep (0.5)
            functions.slowPrint ('Saving game...' , 0.05)
            data.storeData (data_to_store)
            data.storeInv (hero.Inventory)
            time.sleep (0.5)
            functions.slowPrint ('Successfully saved game', 0.05)
            time.sleep (0.5)
        else:
            print("Choose 1, 2, 3, 4 or 5!")
    functions.slowPrint ('\nGame over', 0.05) 

main()