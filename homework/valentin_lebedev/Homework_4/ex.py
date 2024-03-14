my_dict: dict = {
    'one': (1, 2, 3, 4, 5), 
    'two': [7, 8, 9, 10, 11], 
    'three': {
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4, 
        'five': 5
        }, 
    'four': {11, 12, 13, 14, 15}
    }

my_dict['two'].append('a')
my_dict['two'].pop(1)
my_dict['three']['i am a tuple'] = 'hello'
my_dict['three'].pop('four')
my_dict['four'].pop()
my_dict['four'].add('sixteen')

print(my_dict['one'][-1], my_dict, sep='\n')
