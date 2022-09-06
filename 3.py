def function_pangram(x):
    return set('abcdefghijklmnopqrstuvwxyz') == set(x.lower().replace(' ', ''))

text = input("Введите строку: \n")


print(function_pangram(text))
