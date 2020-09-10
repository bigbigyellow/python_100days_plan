name = "dahuang"
print(name.title())
print(name)
name2 = "dadahuang"
name3 = name2 + name
print(name3)

# ----------------------------
print(0.2 + 1)

b = ['a', 'ab', 'ac']
print(b)
print(b[0])
print(b[1])
print(b[-1])
b[0] = 'modify'
print(b)
b.append('append')
print(b)

b.insert(1, 'huang_1')
print(b)
del (b[2])
print(b)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
print(b[0:3])
print(b[0:])
print(b[-3:])
for bb in b[:3]:
    print(bb)
b2 = b
b3 = b[:]
print(b2)
print(b3)

# -------------------
cars = ['0', '1', '2', '3', '4']
for car in cars:
    if car == '1':
        print(car.upper())
    else:
        print('哎呀')

ages = [1, 21, 232]
for age in ages:
    if (age > 2) and (age < 200):
        print(age)

temp = [1, 'a', [2, '2']]
print(temp)
run = [[1, 2], [1, 2]]
print(run)

# -------------
alien = {1, 2, 3, 4, 1, 2, 3, 4}
print(alien)
alien2 = {4, 2, 321, 23, 5, 123}
print(alien2)
att = {'a': 1, 'b': 2, 'v': 3, 'asd': 2}
print(att)
print(att['v'])
del (att['v'])
print(att)

for key, value in att.items():
    print(key)
    print(value)

message = input("please input something:")
print('hello,' + message + '!')

# -------------------------------------
my_list = ['1', '12', '3s', '24sa']
while my_list:
    print(my_list.pop())


# ------------函数-------------------------
def greet_user():
    print('hello!')


def greet_user(username):
    print(username + 'hello!')


# greet_user()
# python中是不能重载的，可以看到这里的第二个函数greet_user覆盖了上一个函数

greet_user("huang")



