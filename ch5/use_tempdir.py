import tempfile, subprocess, os

# テンポラリディレクトリを作成
with tempfile.TemporaryDirectory() as tmp:
    # テンポラリフォルダ以下に一時ファイルを作成
    fname = os.path.join(tmp, 'test.txt')
    with open(fname, 'wt') as fp:
        fp.write('こんにちは。\r\n一時ファイル。')
    # メモ帳を起動
    subprocess.run(['notepad', fname])

# この時点ではテンポラリディレクトリは削除される
print("ok.")
