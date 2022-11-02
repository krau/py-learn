#存储数据
#json格式使用
import json

nums = [2,3,4,5,6]
jsonname = 'nums.json'
with open(jsonname,'w') as f:
    json.dump(nums,f)

with open(jsonname) as f:
    numbers = json.load(f)
print(numbers)

#存储数据很有用，例如让程序记住用户
username = input('请输入你的名字：')
filename = 'username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f'我们等你回来，{username}')
#然后就可以通过读取username.json来欢迎用户下一次到来