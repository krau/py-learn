#python自定义函数模块化，对应《python编程从入门到实践第二版》第8章8.6(含)以后内容

#将函数存储在模块中
'''
将函数存储在独立文件中，称其为模块。
要创建一个模块，首先创建.py文件，在.py中仅编写函数，这便是一个模块。
然后在同级目录下的其他代码中，便可以使用import导入这个模块。

在本示例中，同级目录下创建了一个名为greet.py的模块。
'''
import greet
greet.hello('krau')
'''
Python读取这个文件时，代码行import greet让Python打开文件 greet.py，并将其中的所有函数都复制到这个程序中。
你看不到复制的代码，因为在这个程序即将运行时，Python在幕后复制了这些代码。
你只需知道，在现在这个文件中，可使用greet.py中定义的所有函数。
使用模块中的函数时，要指定模块名greet和函数名hello，并使用点分割
即 模块名.函数名()
'''

'''
上面的方法是导入了模块中的所有函数，如果不需要全部导入，可以使用下面的语句
from 模块名 import 函数名
'''

'''
如果要导入函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名
类似于外号。要给函数取这种特殊外号，需要在导入它时指定。
import 模块名 as 模块外号
from 模块名 import 函数名 as 函数外号
'''