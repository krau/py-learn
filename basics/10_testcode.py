#使用unittest测试代码
import unittest

'''下面的函数用作示例，接下来将对它进行测试'''
def get_formatted_name(first,last):
    '''格式化姓名'''
    full_name = f'{first} {last}'
    return full_name.title()

#单元测试，核实某函数某方面没有问题
class NamesTestCase(unittest.TestCase): #这里的类名可以随意命名，但必须继承unittest.TestCase类
    '''测试示例的函数'''

    def test_first_last_name(self):#测试方法必须以test_开头
        '''能否正确处理像Acher Krau这样的姓名？'''
        formatted_name = get_formatted_name('acher','krau')
        self.assertEqual(formatted_name,'Acher Krau')#unittest最有用的方法之一：断言

if __name__ == '__main__':
    unittest.main()