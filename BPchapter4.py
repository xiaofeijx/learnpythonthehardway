# coding:utf-8

# 4.2创建字典
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# 4.2.1 dict函数
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
d
d['name']

# 或者
d = dict(name = 'Gumby', age = 42)

# 基本字典操作
# len(d)
# d[k]
# d[k] = v
# del d[k]
# k in d 键是否在d中

# x = []
# x[42] = 'foobar'
# 列表不允许这样的操作

x = {}
x[42] = 'Foobar'

# code 4-1 字典示例
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# 描述性标签
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')

request = raw_input('phone number(p) or address(a)?')

if request == 'p':
    key = 'phone'

if request == 'a':
    key= 'addr'

if name in people:
    print "%s's %s is %s." % (name, labels[key], people[name][key])


# 4.2.3 字典的格式化字符串
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
"Cecil's phone number is %(Cecil)s." % phonebook


# 4.2.4 字典方法
# 1.clear
d = {}
d['name'] = 'gumby'
d['age'] = 42
d
returned_value = d.clear()

d #返回{}

returned_value  # d.clear()返回 None

# 情况一
x = {}
y = x
x['key'] = 'value'
x = {}
y

# 情况二
x = {}
y = x
x['key'] = 'value'
x.clear()
y


# 2.copy
# copy为浅拷贝

x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'  # 替换原值，原值不变
y['machines'].remove('bar')  # 修改某个值的话会改变原值
y
x

# deep copy
from copy import deepcopy
d = {}
d['name'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['name'].append('Clive')

# 3.fromkeys
{}.fromkeys(['name', 'age'])

# 4.get
d = {}
d.get('name')  # 返回 None
d.get('name', 'N/A')  # 'N/A'替换None



# code 4-1 字典示例 修订版
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# 描述性标签
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')

request = raw_input('phone number(p) or address(a)?')

if request == 'p':
    key = 'phone'

if request == 'a':
    key= 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not avaiable')

print "%s's %s is %s." % (name, label, result)

# 5.has_key
d = {}
d.has_key('name')

d['name'] = 'Eric'
d.has_key('name')

# 6.items and iteritems
# items 以列表方式返回字典项
d = {'title': 'python web site', 'url': 'http//www.python.org', 'spam': 0}
d.items()

# iteritems 返回迭代器
it = d.iteritems()
it
list(it)

# 7. keys and iterkeys
# 与item类似

# 8.pop
# 获取值，然后将其删除
d = {'x': 1, 'y': 2}
d.pop('x')
d

# 9. popitem
d = {'title': 'python web site', 'url': 'http//www.python.org', 'spam': 0}
d.popitem() # 填出随机的项

# 10. setdefault
# 如果字典中没有此项（键），那么加入
# 如果字典中有此项，就返回对应的值
d = {}
d.setdefault('name', 'N/A')
d
d['name'] = 'Gumby'

# 11. update
# 用一个字典项更新另外一个字典
d = {
    'title': 'Python web site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2008'
}
x = {'title': 'python language website'}

d.update(x)

# 12.values and itervalues
# 返回值
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 4
d[5] = 5
d.values()




