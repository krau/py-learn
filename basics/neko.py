class Neko:
    '''模拟猫猫'''
    def __init__(self,name,color,gender):
        '''初始化猫猫属性'''
        self.name = name
        self.color = color
        self.gender = gender
        self.age = 0

    def get_descriptive(self):
        '''返回描述猫猫的信息'''
        long_name = f'{self.name} {self.color} {self.gender} {self.age}'
        return long_name.title()

    def eat(self):
        '''猫猫吃饭'''
        print(f'{self.name.title()} 饿饿，饭饭')


class Goodneko(Neko):
    '''好猫！'''
    def __init__(self, name, color, gender):
        '''初始化父类属性'''
        super().__init__(name, color, gender)

    def nya(self):
        '''好猫会喵喵叫！'''
        print('喵~')

    def eat(self):
        '''好猫不需要吃饭！'''
        print(f'{self.name.title()} 不饿，不用吃饭')