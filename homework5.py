immutable_var = 1, 2, 3, 4
print(immutable_var)
# immutable_var[0] = 5# попытка изменить список, картеж не изменяемый
mutable_list = ["apple", "banane", "please"]
print(mutable_list)
mutable_list.append ("coconut")# добавление значения в изменяемый список
print(mutable_list)
mutable_list.extend ("str")# добавление значения в изменяемый список по буквенно
print(mutable_list)
mutable_list.extend (["str"])# добавление значения в изменяемый список по буквенно
print(mutable_list)
mutable_list.remove ("str")# добавление значения в изменяемый список по буквенно
print(mutable_list)