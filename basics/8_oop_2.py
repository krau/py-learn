#使用类和实例
class Neko:
    '''模拟猫猫'''
    def __init__(self,name,color,gender):
        '''初始化猫猫属性'''
        self.name = name
        self.color = color
        self.gender = gender
        self.age = 0
        #这里给猫猫了一个age属性，我们认为该属性无需在形参中定义，年龄的默认值为0

    def get_descriptive(self):
        '''返回描述猫猫的信息'''
        long_name = f'{self.name} {self.color} {self.gender} {self.age}'
        return long_name.title()

    def eat(self):
        '''猫猫吃饭'''
        print(f'{self.name.title()} 饿饿，饭饭')

my_new_cat = Neko('dada','white','female')
print(my_new_cat.get_descriptive())
my_new_cat.eat()


#继承
'''
编写类时，并非总是要从空白开始。
如果要编写的类是另一个现成类的特殊版本，可使用继承。
一个类继承另一个类时，将自动获得另一个类的所有属性和方法。
原有的类称为父类 ，而新类称为子类 。
子类继承了父类的所有属性和方法，同时还可以定义自己的属性和方法。
'''
class Goodneko(Neko):
    '''好猫！'''
    def __init__(self, name, color, gender):
        '''初始化父类属性'''
        super().__init__(name, color, gender)#使用super()调用父类方法

    def nya(self): #可编写子类独有，父类不具有的方法
        '''好猫会喵喵叫！'''
        print('喵~')

    def eat(self): #可在子类中重写父类的方法，若不重写则沿用父类
        '''好猫不需要吃饭！'''
        print(f'{self.name.title()} 不饿，不用吃饭')

my_good_cat = Goodneko('anhe','orange','female')
my_good_cat.nya()
my_good_cat.eat()