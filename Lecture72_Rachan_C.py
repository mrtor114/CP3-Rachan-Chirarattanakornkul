menuList = []

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
        menuPrice = input('Enter price:')
        menuList.append([menuName,menuPrice])


showBill()
