# function = block of code that is reusablen and modular
# DRY =  Do not repeat yourself
# usually for performing a specific task

# function can take in parameters or arguments or nothing

def add_numbers(number_1, number_2=10):
    results = number_1 + number_2
    print( 'The sum of' , number_1, '&' , number_2, 'is' , results)

add_numbers(2,3)
add_numbers(4,6)
add_numbers(3)
