import fitz  # PyMuPDF
import docx
import re

# ファイルのGUIで指定してpdfファイルを読み込む
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()
fTyp = [("", "*.pdf")]
iDir = r"C:\\Users\\ryoak\\Downloads"
file_path = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
print(file_path)

# PDFファイルの読み込み
pdf_doc = fitz.open(file_path)
text = ""
for page in pdf_doc:
    text += page.get_text()

print(text)

# 制御文字を削除
text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

# テキスト情報をwordにして保存
doc = docx.Document()
doc.add_paragraph(text)
doc.save('C:\\Users\\ryoak\\Downloads\\whitepaper2023.docx')