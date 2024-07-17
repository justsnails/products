import os # operating system

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line: 
                continue # 繼續，跳到下一回
            name, price = line.strip().split(',')
            products.append([name, price])
        print(products)
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        print('請問要購買什麼商品?')
        buy = input('請輸入購買的商品 : ')
        if buy == 'q':
            print('歡迎再度光臨!')
            break
        price = input('請輸入商品價格 : ')
        products.append([buy, price]) 
    print(products)
    return products

# 印出所有購物紀錄 
def print_products(products):
    for p in products:
        print(p[0], '的價格為:', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    if os.path.isfile('products.csv'): # 檢查檔案在不在
        print('yeah! 找到檔案了!')
        products = read_file('products.csv')
    else:
        products = []
        print('檔案找不到!')
        
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()