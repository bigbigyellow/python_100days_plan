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

## DAY5(9-25)

### python的基本语法补充

1. python的import不同于Java，还可以导入其中的变量。
2. 导入时注意绝对导入和相对导入。

### PYTORCH的学习

1. 大致的看明白了pytorch的基本实现，就是官方的[60min快速上手教程](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)，还有部分细节还是需要继续注意，在这记录一下一个简单神经网络的构建、训练和测试流程：
   1. 加载数据集
   2. 定义net结构
   3. 定义loss
   4. 定义自己的optimizer
   5. 训练集上训练自己的网络：
      1. 正向传播
      2. loss反向传播
   6. 使用梯度进行参数更新
   7. 保存模型参数，使用模型进行测试
2. 跑通了一个最简单的net：在MNIST数据集上，一个2层CONV和一层FC的网络。使用min-batch,大致的运行了几次，似乎 batch-size = 100-200的时候效果比较好，最好达到了99以上，batch-size过大和过小时都不是很合适。