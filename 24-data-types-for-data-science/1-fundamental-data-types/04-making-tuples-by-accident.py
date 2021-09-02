'''
Making tuples by accident

Tuples are very powerful and useful, and it's super easy to make one by accident. All you have to do is create a variable and follow the assignment with a comma. This becomes an error when you try to use the variable later expecting it to be a string or a number.

You can verify the data type of a variable with the type() function. In this exercise, you'll see for yourself how easy it is to make a tuple by accident.

INSTRUCTIONS

*   Create a variable named normal and set it equal to 'simple'.
*   Create a variable named error and set it equal 'trailing comma',.
*   Print the type of the normal and error variables.
'''

# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = 'trailing comma',

# Print the types of the variables
print(type(normal))
print(type(error))