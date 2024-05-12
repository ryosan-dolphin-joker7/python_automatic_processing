# 挨拶をする関数を定義
def say_hello(name, age):
    print(name, 'さんは', age, '才,よろしく!')

# 普通に関数を呼び出す
say_hello('鈴木', 28)
# 名前付き引数を使って関数を呼び出す
say_hello(name='田中', age=24)

# 表示結果→ 鈴木 さんは 28 才,よろしく!
#            田中 さんは 24 才,よろしく!


