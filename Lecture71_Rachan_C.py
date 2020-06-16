menuList = []
priceList = []

def showBill():
    print('========My Menu========')
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    totalValue()

def totalValue():
    totalPrice = 0
    print('========Thank You========')
    for i in priceList:
        totalPrice = i + totalPrice
    print('Total:', totalPrice)

while True:
    menuName = input('Please Enter Menu:')
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = float(input('Enter price:'))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
