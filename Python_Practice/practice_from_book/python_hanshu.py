def welcome(username='huang', usertime='2020'):
    print('hello,' + username + ',' + usertime)
    return username


a1 = welcome()
a2 = welcome('xv')
a3 = welcome(usertime='2016')

print(a1)
print(a2)
print(a3)


# 对于任意数量的参数的函数传递
def undefined(*toppings):
    print(toppings)


undefined('huang')
undefined('huang', '2', '2342', 'sd', ['s', 's'])
undefined()
