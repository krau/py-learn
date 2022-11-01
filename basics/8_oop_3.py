#导入类，在模块中存储类
'''
如函数一样，类也可以存储在模块中，在需要的时候导入它们。
在同级目录下存在一个neko.py模块，它包含了Neko和Goodneko类
'''

from neko import Neko #从neko.py中导入Neko类，类的导入与函数的导入方法类似

my_cat_0 = Neko('ah0','black','female')
print(my_cat_0.get_descriptive())

'''
另外，一个模块之中可以导入另外一个模块
'''

