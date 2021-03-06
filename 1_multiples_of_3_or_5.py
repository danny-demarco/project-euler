#Q If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def sumMultiples(upper_limit):
   multip = [i for i in range(upper_limit) if i % 3 == 0 or i % 5 == 0]
   return sum(multip)


print(sumMultiples(1000))