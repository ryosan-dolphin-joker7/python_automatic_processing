import win32com.client as com
import os

# ファイルは絶対パスで指定する必要がある
scr_file = os.path.abspath(__file__)
scr_dir = os.path.dirname(scr_file)
in_file = scr_dir+'/date-sample.xlsx'

# Excelを起動する
app = com.Dispatch("Excel.Application")
app.Visible = False
app.DisplayAlerts = False
try: # --- (*1)
    # Excelでブックを読み込む
    book = app.Workbooks.Open(in_file)
    # ここで何かしらのエラー
    raise Exception('何かしらのエラー')
except:
    # エラーが起きたときの処理をここに
    print("Error")
finally:
    # Exelを終了させる処理
    app.Quit()
    print('Excelを正しく終了しました')
