
Dict = dict()
itemDict = dict()
uniqueItems = set()
while True :
    username = input("Username : ")
    if username == 'leave' :
        break

    itemCount = (int(input("Number of Items : ")))
    itemNames = []
    count = 0
    while count < itemCount:
        itemName = input("Item Name : ")
        count += 1
        itemNames.append(itemName)

    itemNames = list(set(itemNames))

    for itemName in itemNames :
        if itemName in itemDict:
            itemDict[itemName] += 1
            uniqueItems.remove(itemName)
        else:
            itemDict[itemName] = 1
            uniqueItems.add(itemName)

    print(username,"'s items :",itemNames)

    Dict[username] = itemNames


print('Users :\n',Dict)
print('Unique Items :\n' , uniqueItems)

mostCount = 0
for item in itemDict:
    if(itemDict[item] > mostCount):
        mostPopular = item
        mostCount = itemDict[item]
print('Most Popular Item :', mostPopular)




