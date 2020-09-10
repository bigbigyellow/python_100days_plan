import book

book.read_book(book_name="English Learning", read_time='20200910-1609')


class Dog():
    def __init__(self, name, age, dogtype):
        self.name = name
        self.age = age
        self.dogtype = dogtype

    def sit(self):
        print(self.name + " is now sitting!")

    def roll_over(self):
        print(self.name + "is now rolling!")


dog1 = Dog("xiaohua", "1", "er-ha")
dog1.sit()


# -----------继承---------------------
class erha_Dog(Dog):
    def __init__(self, name, age, dogtype='erha'):
        super().__init__(name, age, dogtype)

    def chaijia(self, time):
        print(self.name + ' broken your home at ' + time)


erha = erha_Dog(name='小黄', age='2')
erha.chaijia('2016')
erha.sit()
