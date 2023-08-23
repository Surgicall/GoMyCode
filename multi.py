import numpy
def multiply_numbers(list):
   return numpy.prod(list)
given_list = [2,3,6]
print('The list is:',given_list)
print("The product is: ")
print(multiply_numbers(given_list))
