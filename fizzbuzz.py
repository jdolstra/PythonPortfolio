# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(1, 101):
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0: 
    print("fizzbuzz")
    continue
  elif fizzbuzz % 3 == 0:
    print("fizz")
    continue
  elif fizzbuzz % 5 == 0:
    print("buzz")
    continue
  print(fizzbuzz)

 