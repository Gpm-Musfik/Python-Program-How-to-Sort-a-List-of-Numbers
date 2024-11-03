# Accessing Dictionary Values
# Values in a dictionary are accessed using their keys.
# If a key is not found, a KeyError will be raised unless you use the get() method, which returns None.

# Example dictionary
my_dict = {'name': 'Musfik', 'age': 25, 'city': 'Shanghai', 'Occupation': 'Data Engineer'}

# Accessing values using keys
name = my_dict['name']
Occupation = my_dict.get('Occupation')

# Printing accessed values
print('Name:', name)
print('Occupation:', Occupation)