#python列表简单使用，对应第三章

#创建列表
friends = ['ah','leao','zhang','wang']
print(friends)

#访问列表元素
print(friends[0])#索引从0开始
print(friends[-1])#反向索引从-1开始

#修改列表元素
friends[0] = 'ahchan'

#添加与删除列表元素
friends.append('zhou')#在末尾添加
friends.insert(1,'cos0')#在指定索引位置添加

del friends[1]#使用del删除指定位置的元素
popped_friends = friends.pop(1)#使用pop”弹出“指定位置的元素
print(friends)
print(popped_friends)

friends.remove('zhou')#根据值删除元素

#组织列表
friends.sort()#按首字母排序,永久性的
print(friends)
friends.sort(reverse=True)#可以传入reverse参数使其逆序
print(friends)

print(sorted(friends))#临时按首字母排序

friends.reverse()#reverse只是反转列表元素的排列顺序
print(friends)

print(len(friends))#使用len()确定列表有多少元素