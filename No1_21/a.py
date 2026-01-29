def circle_area(r):
    return r * r * 3.14

a = circle_area(2.5)
print("半径2.5の円の面積は", a)

def is_positive(i):
    if i > 0:
        return True
    else:
        return False

a = -10
if is_positive(a) == True:
    print('aの値は正です')
else:
    print('aの値は負またはゼロです')


def is_positive(i):
    return i > 0

a = -10
if is_positive(a):
    print('aの値は正です')
else:
    print('aの値は負またはゼロです')

def get_two_numbers():
    return (2,3)
a, b = get_two_numbers()
print(a, b)

# 
def print_price(price, func):
    print('価格は' + func(price))

def price_without_tax(price):
    return f'税抜き{price}円'

def price_with_tax(price):
    return f'税込み{int(price*1.1)}円'

print_price(800, price_without_tax)
print_price(800, price_with_tax)

# 
def price_without_tax(price):
    return f'税抜き{price}円'
lambda price: f'税抜き{price}円'
# 
def print_price(price, func):
    print('価格は' + func(price))

def price_without_tax(price):
    return f'税抜き{price}円'

def price_with_tax(price):
    return f'税込み{int(price*1.1)}円'

print_price(800, price_without_tax)
print_price(800, price_with_tax)
def print_price(price, func):
    print('価格は' + func(price))

print_price(800, lambda price: f'税抜き{price}円')
print_price(800, lambda price: f'税込み{int(price*1.1)}円')
