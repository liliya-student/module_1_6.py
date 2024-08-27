my_dict = {'Liliya': 2001, 'Liza': 2003, 'Ivan': 1999, 'Anna': 1997}
print('Dict', my_dict)
print('Year of birth Liza:', my_dict['Liza'])
print('Not existing value:', my_dict.get('Fedor'))
my_dict.update({'Sasha': 2005, 'Zhenya': 2000})
removed_year = my_dict.pop('Zhenya')
print('Deleted value \'Женя\':', removed_year)
print('Modified dictionary:', my_dict)

print()

my_set = {1, 2, 3, 7, 2, 'Apple', True, 1, 17.25}
print('Set:', my_set)
my_set.add('text')
my_set.add('8,3')
my_set.discard('Apple')
print('Modified set:', my_set)
