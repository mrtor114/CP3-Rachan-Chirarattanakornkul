uName = input("Username:")
pWord = input("Password:")

blackCoffee = 2
espresso = 3.5
latte =5
mocha =5.5
hotCocoa = 4

if uName == "rachan" and pWord =="1234":
    print("------WELCOME TO STARDUCK------")
    print("-------------MENU--------------")
    print("1.Black Coffee               $2")
    print("2.Espresso                 $3.5")
    print("3.Latte                      $5")
    print("4.Mocha                    $5.5")
    print("5.Hot Cocoa                  $4")
    print("---------Please Select---------")
    item = int(input("What can I get you today? >>"))
    quanti = int(input("How many? >>"))

    if item == 1:
        item = blackCoffee
        print("You Selected: Black Coffee", quanti,"Cup(s)")
    elif item == 2:
        item = espresso
        print("You Selected: Espresso", quanti,"Cup(s)")
    elif item == 3:
        item = latte
        print("You Selected: Latte", quanti,"Cup(s)")
    elif item == 4:
        item = mocha
        print("You Selected: Mocha", quanti,"Cup(s)")
    elif item == 5:
        item = hotCocoa
        print("You Selected: Hot Cocoa", quanti,"Cup(s)")

    print("Your total is             ", "$", float(item*quanti))
    print("------THANK YOU : STARDUCK-------")

else:
    print("Invalid Username or Password")

