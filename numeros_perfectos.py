while True:
    num = int(input("\nIntroduzca un número:  "))
    sum = 0
    if num < 0:
        break
    for i in range(1, num):
        if num % i == 0:
            sum += i
    
    if sum == num:
        print("Número perfecto.")
    else:
        print("Número imperfecto")