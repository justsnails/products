products = []
print('歡迎來到好事多!')
while True:
    print('請問要購買什麼商品?')
    buy = input('請輸入購買的商品 : ')
    if buy == 'q':
        print('歡迎再度光臨!')
        break
    price = input('請輸入商品價格 : ')
    products.append([buy, price]) 
for p in products:
    print(p[0], '的價格為:', p[1])

with open('products.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')