menuList = []
systemMenu = {'burger': 30, 'cake': 25, 'drink': 10, 'noodle': 20.5, 'chicken': 15.5}

def showBill():
    totalPrice = 0
    print('========My Menu========')
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += float(menuList[number][1])
    print('========Thank You========')
    print('Total:', totalPrice)

while True:
    menuName = input('Please Enter Menu:')
    if (menuName.lower() == 'exit'):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()
