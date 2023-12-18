
def storeData (playerData):
    file = open('data.txt', 'w')
    for item in playerData:
        file.write (f"{item}\n")

def loadData ():
    newData = []
    file = open('data.txt', 'r')
    for item in file:
        newData.append (item)
    return newData

def storeInv (playerData):
    file = open('inventory.txt', 'w')
    for item in playerData:
        file.write(f"{item}\n")

def loadInv ():
    newInv = [] 
    file = open('inventory.txt', 'r')
    for item in file:
        newInv.append (item)
    return newInv




# Inventory = ['Health Potion', 'Attack Potion', 'Defense Potion']

# storeInv (Inventory)



# inv = loadInv ()
# updatedInv = []
# for item in inv:
#     updatedInv.append (item.strip('\n'))
# print (updatedInv)



