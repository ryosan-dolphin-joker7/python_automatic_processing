import os

# プログラムパスの絶対パスを得る
script_file = os.path.abspath(__file__)
print('script=', script_file)
# プログラムのあるフォルダパスを得る
script_dir = os.path.dirname(script_file)
print('script_dir=', script_dir)
# プログラムと同じフォルダの「result.txt」
result_file = os.path.join(script_dir, 'result.txt')
print('result.txt=', result_file)



