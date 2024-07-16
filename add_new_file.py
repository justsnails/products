# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line: 
            continue # 繼續，跳到下一回
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

print('歡迎來到好事多!')
# 讓使用者輸入
while True:
    print('請問要購買什麼商品?')
    buy = input('請輸入購買的商品 : ')
    if buy == 'q':
        print('歡迎再度光臨!')
        break
    price = input('請輸入商品價格 : ')
    products.append([buy, price]) 
print(products)

# 印出所有購物紀錄 
for p in products:
    print(p[0], '的價格為:', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')