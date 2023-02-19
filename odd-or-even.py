def oe(a):
    if a%2 == 0:
        return('Even')
    else:
        return('Odd')
B= int(input('Enter a number'))
result = oe(B)
print(result)
