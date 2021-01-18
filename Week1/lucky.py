def check(n):
    summa = 0
    for numero in str(n):
        summa += int(numero)
    return summa % 7 == 0
 
if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True