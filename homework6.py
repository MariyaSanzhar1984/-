my_dict={'Name': 'Mariya', 'Date': 1984}
print(my_dict)
print(my_dict['Name'])# вывести одно по существующему ключу
my_dict['Anton'] = 89197777777#выводим одно по несуществующему в словаре
print(my_dict)
my_dict.update({'Name':'Sasha', 'Date': 1986,
                'Name':'Katy', 'Date': 1985})
print(my_dict)
my_dict.pop('Name', 'Date')
print(my_dict)
my_set={1,2,2,3,4, 'Mariya', (1,2,2,3,)}#переменная множество
print(my_set)
print(my_set.add(5))
print(my_set)
print(my_set.add(6))
print(my_set)
print(my_set.discard(1))
print(my_set)