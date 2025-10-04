n = int(input("How many numbers do you want to enter? "))
even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
prime_count = 0
if num > 1:
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                break
        else:
            prime_count += 1
print("\nTotal Even Numbers:", even_count)
print("\nTotal Odd Numbers:", odd_count)
print("\nTotal Prime Numbers:", prime_count)
