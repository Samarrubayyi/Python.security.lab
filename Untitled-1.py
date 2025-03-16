#home/work 

numbers = input("Enter 4 to 20 float numbers (separated by spaces): ").split()

 
while len(numbers) < 4 or len(numbers) > 20:
    print("Error! Enter between 4 and 20 numbers.")
    numbers = input("Try again: ").split()

 
numbers = [float(x) for x in numbers]

 
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
squares = [x * x for x in numbers]

 
print("Sum:", total)
print("Max:", maximum)
print("Min:", minimum)
print("Squares:", squares)