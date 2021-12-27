# 日常记账簿

import os #operating system

# 读取档案
def read_file(filename):
    products = []
    if os.path.isfile(filename): #检查档案在不在
        print('找到档案了！')
        with open(filename, 'r', encoding='GB2312') as f: #读取档案
            for line in f:
                if '商品，价格' in line:
                    continue
                s = line.strip().split(',')
                name = s[0]
                price = s[1]
                products.append([name, price])
        print(products)
    else:
        print('没有档案！')
    return products

# 请使用者输入
def user_input(products):
    while True:
        name = input('请输入商品名称： ')
        if name == 'q':
            break
        price = input('请输入商品价格： ')
        p = [name, price]
        products.append(p)
    print(products)
    return products

# 印出所以购买记录
def print_products(products):
    for p in products:
        print(p[0], '的价格是： ', p[1])

# 写入档案
def write_file(filename, products):
    with open(filename, 'w', encoding='GB2312') as f: # 可以使用utf-8作为encoding，并加以转换
        f.write('商品,价格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') #\n为空格符号

products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)