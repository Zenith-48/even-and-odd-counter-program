n = int(input("How many numbers do you want to enter? "))
even_count = 0
odd_count = 0

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("\nTotal Even Numbers:", even_count)
print("Total Odd Numbers:", odd_count)
