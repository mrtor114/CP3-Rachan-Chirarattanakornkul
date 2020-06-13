number = int(input())
text = '*'
for x in range(number):
    y =1+2*x
    x = number-x
    print(' ' * x,y * text)
