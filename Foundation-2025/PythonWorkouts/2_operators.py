print(1 + 2) # arithmatic operator
print(1 - 2)
print(1 * 2)
print(4 / 0.5) # convert the result to float
print(5 / 2)  # exactly dividing
print(5 // 2) # quotient - floor division
print(5 % 2)  # remainder
print(10 ** 3) # power

a = 5 # assignment operator
a = a + 3
a += 3 # this shortcut works with any operator mentioned above
print(a)

# comparison operator
print(10 == 5)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 <= 10)
print(10 >= 10)

c = 5
d = 6
print(c < d and c > d )
print(c < d or c > d )
print(not(c < d and c > d ))

# identity operator
e = 100.0
f = 1.0 * e
print(id(e)) # prints the memory address
print(id(f))
print(e is f) # false
print(e is e)
print(e == f) # true
print(e is not f)

# membership operator
numbers = [1, 2, 3, 4, 5]
print(1 in numbers) # checking element is in the list
print(10 in numbers)
print(10 not in numbers) 
