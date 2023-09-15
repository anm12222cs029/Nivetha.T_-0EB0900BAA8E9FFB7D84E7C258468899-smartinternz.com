def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


# Get input from the user
num = int(input("Enter a number: "))

# Calculate and display the factorial
result = factorial(num)
print(f"The factorial of {num} is {result}")
