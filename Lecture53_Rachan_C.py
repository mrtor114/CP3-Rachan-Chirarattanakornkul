def vatCalculate():
    totalPrice = float(input('How much?'))
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculate())