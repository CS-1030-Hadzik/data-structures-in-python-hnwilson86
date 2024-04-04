# problem 1. print your first and last name`
print ("Holly Wilson")
# `problem 2. In the array.py create an array named 'cars' 
# with the following elements in this order  ---- 
# Ford,Chrysler,Dodge,Ram,Jeep,Chevy,GMC` (use single quotes for each element)
# EX: 'Ford' not "Ford" spelling matters
cars = ['Ford','Chrysler','Dodge','Ram','Jeep','Chevy','GMC',]
# `problem 3. print the array to the console`
print (cars)
# `problem 4. print the length of the array to the console `
print(len(cars))
# `problem 5. Append Buick to the Array`
cars.append('Buick')
# `problem 6. print the array to the console`
print (cars)
# `problem 7. Print the 4th element in the array (Not index 4, element 4)`
print (cars[3])
# `problem 8. Insert 'Toyota' into element 3 in the array`
cars.insert(2,'Toyota')
# `problem 9. print the array to the console`
print (cars)
# `problem 10. Remove element 5 of the array (hint look at options for pop())`
cars.pop(4)
# `problem 11. print the array to the console`
print (cars)
# `problem 12. Sort the array in ascending order`
cars.sort()
# `problem 13. print the array to the console`
print (cars)
# `problem 14. Sort the array in descending order`
cars.sort(reverse=True)
# `problem 15. print the array to the console`
print (cars)
# `problem 16. create a variable called my_array_length with a value of the cars array length (spelling, capitilization, and spaces matter)`
my_array_length =len(cars)
# `problem 17. create a variable called array_string with a value of 'The length of my array is ' (spelling, capitilization, and spaces matter)`
array_string =  'The length of my array is ' 
# `problem 18. print array_string concatenated with my_array_length to the console.`
print(array_string + str(my_array_length))