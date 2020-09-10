# python_100days_plan
我的100天入门、练习和巩固python计划（始于2020-8-13）

- 目标：基础语法/网络爬虫/web框架/深度学习
- 使用的环境：anaconda中创建一个新的虚拟环境，命名为py36，安装python3.6

## DAY1(8-14)
1. 配置本地的编程环境，安装Anaconda3

2. 创建一个新的python虚拟环境

   ```cmd
   conda create -n python_study  python=3.7
   ```
## DAY2(9-4)
按照pytorch官方教程搭建了一个神经网络和一个图像分类器

（因为自己的操作失误不小心删掉了，后面再写一遍把）

 ## DAY3-DAY4(9-9/9-10)  
 按照《Python编程——从如么到实践》简单的学习了下python的简单语法
 
 我个人觉得比较重要的点：
 
> python中是不能重载的

关于python中的方法和类的构造和使用重点掌握一下
```python
# 类的实现，注意一下属性、初始化函数、自定义函数
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
```
```python
# 类的继承，就是勇哥super().__init()__
# 稍微注意一下细节
class erha_Dog(Dog):
    def __init__(self, name, age, dogtype='erha'):
        super().__init__(name, age, dogtype)

    def chaijia(self, time):
        print(self.name + ' broken your home at ' + time)
```

python可以支持导入模块，也支持导入模块中的方法和类