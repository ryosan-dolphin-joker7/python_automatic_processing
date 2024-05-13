import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if file_path:
        try:
            # pandasを使ってExcelファイルの特定の範囲を読み込む
            #cols = [chr(i) for i in range(ord('B'), ord('V'))]  # B列からU列までのリスト
            cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # B列からU列までの列番号
            df = pd.read_excel(file_path, usecols=cols, skiprows=3, nrows=28)

            display_window = tk.Toplevel(root)
            display_window.title("File Contents")

            table = ttk.Treeview(display_window)
            table.pack(pady=10)

            table["columns"] = tuple(df.columns)
            table["show"] = "headings"

            for col in table["columns"]:
                table.heading(col, text=col)

            for index, row in df.iterrows():
                table.insert("", "end", values=tuple(row))

        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")

root = tk.Tk()
root.title("ファイルアップロード")

open_button = tk.Button(root, text="Excelファイルを開く", command=open_file)
open_button.pack(pady=10)

root.mainloop()