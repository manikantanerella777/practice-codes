#lord shiva pattern

n = int(input("Enter a number: "))
for i in range(n):
    print(" " * n + "*" * n) 

for i in range(n):
    print(" " * i + "*" * (n - i + n + n - i) + " " * i + "*" * (n - i)) 

for i in range(n):
    print(" " * (n - i) + "*" * (2 * i + n)) 
