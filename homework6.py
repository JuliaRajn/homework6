my_dict={'Anton': 1999, 'Flex': 1997}
print(my_dict)
print(my_dict['Flex'])
print(my_dict.get('Masha'))
my_dict.update({'Sasha':1996, 'Polina':2001})
print(my_dict)
del my_dict['Flex']
print(my_dict)
my_set={1,2,3,True,2,3,'a','a'}
print(my_set)
my_set.update({7,'c'})
print(my_set)
print(my_set.discard(1))
print(my_set)