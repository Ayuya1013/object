# 
def say_hello():
        print("こんにちは")
        print("本日は良い天気ですね")

say_hello()
say_hello()
# 
def function_a():
        print("関数aの処理です")

def function_b():
        print("関数bの処理です")


function_a()
function_b()

# 
def function_a():
        print("関数aの処理です")


function_a()
function_b()
def function_b():
        print("関数bの処理です")


# 
def function_a():
        print("関数aの処理です")


def function_b():
        print("関数bの処理です")
        function_a()
        print("関数bの終了")



print("function_bを呼び出します")
function_b()

# 
def function_a():
        a = 10
        print(a)
print(a)


# 
a = 10
def function_a():
        global a
        a=5

function_a()
print(a)

# 
a=19
def function_a():
        a = 5

function_a()
print(a)

# 
def countdown(start):
    print("関数が受け取った値: ",start)
    print("カウントダウンをします")
    counter = start
    while counter >= 0:
            print(counter)
            counter -= 1

countdown(3)
countdown(10)

# 
def countdown(start, end):
    print("一つ目の引数で受け取った値: ",start)
    print("二つ目の引数で受け取った値", end)
    print("カウントダウンをします")
    counter = start
    while counter >= end:
            print(counter)
            counter -= 1

countdown(7, 3)

# 
def countdown(start, end = 0):
    print("一つ目の引数で受け取った値: ",start)
    print("二つ目の引数で受け取った値", end)
    print("カウントダウンをします")
    counter = start
    while counter >= end:
            print(counter)
            counter -= 1

countdown(7)

# 
def func_a(*args):
       for a in args:
              print(a)

func_a(1, 2)
func_a(1,2,3,4)

def func_b(**kwargs):
    for k, v in kwargs:
        print(k, v)


func_b(a=1, b=2)
func_b(c=3, d=4, e=5, f=6)

