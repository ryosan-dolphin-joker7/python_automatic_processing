import msoffcrypto
import openpyxl as excel

# 暗号化されたExcelファイルを指定 --- (*1)
fin = open("uriage-encrypt.xlsx", "rb")
msfile = msoffcrypto.OfficeFile(fin)
# パスワードを指定 --- (*2)
msfile.load_key(password="abcd")
# 復号化したファイルを保存 --- (*3)
fout = open("uriage-decrypt.xlsx", "wb")
msfile.decrypt(fout)

# ワークブックを開いて内容を表示 --- (*4)
book = excel.load_workbook("uriage-decrypt.xlsx")
sheet = book.active
for row in sheet["A2:F99"]:
    values = [v.value for v in row]
    if values[0] is None: break
    print(values)

