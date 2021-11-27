n = int(input("Enter the Number : "))
N = ''

while n > 0 :
    x = n % 2
    n = n // 2
    N = N + ' ' + str(x)
    
print(N[::-1])