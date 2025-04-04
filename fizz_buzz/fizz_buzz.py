#fizz buzz

# Write a function, fizz_buzz, that takes in a number n as an argument. The function should return a list containing numbers from 1 to n, replacing certain numbers according to the following rules:

#     if the number is divisible by 3, make the element "fizz"
#     if the number is divisible by 5, make the element "buzz"
#     if the number is divisible by 3 and 5, make the element "fizzbuzz"

def fizz_buzz(n):
   fizzbuzz = []
   for i in range(1, n+1):
     if i % 15 == 0:
       fizzbuzz.append("fizzbuzz")
     elif i % 3 == 0:
       fizzbuzz.append("fizz")
     elif i % 5 == 0:
       fizzbuzz.append("buzz")
     else:
       fizzbuzz.append(i)
   return fizzbuzz
  
