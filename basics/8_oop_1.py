#Python面向对象

#类，同种事物的抽象
#定义一个类，使用class
class Krau: #根据规范，类的首字母应当大写
    '''有一类人叫Krau'''
    def __init__(self,name,age):
        #类中的函数，叫做方法。
        # __init__()是一个特殊方法，创建Krau类的实例时，py会自动运行Krau类中的__init__()方法
        #在__init__()定义中，self形参是必不可少的，而且必须位于第一位。
        '''他们有名字和年龄'''
        #以self.开头命名的变量可供类中所有的方法使用，可以通过类的任何实例访问，这种变量被称为 属性
        self.name = name
        self.age = age

    def eat(self):
        #这里定义的eat()方法不需要额外信息，所以只需要一个形参self，使实例能够访问eat()方法
        '''他们要吃饭'''
        print(f'{self.name.title()} 要吃饭')

    def sleep(self):
        #同上
        '''他们要睡觉'''
        print(f'{self.name.title()} 该睡觉了')


#实例，一类事物的一个具体个体
keluo = Krau('柯罗',18)#创建了Krau类的一个实例，将它赋给keluo
print(keluo.name)
keluo.eat()
keluo.sleep()