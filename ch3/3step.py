# 三つのプログラムをモジュールとして取り込む
import read_files, split_list, gen_invoice_matome
# モジュールの関数を実行
read_files.read_files() # 1.部署ごとのExcelブックを一つにまとめる
split_list.split_list() # 2.ブックを顧客ごとに分割して集計
gen_invoice_matome.gen_invoice() # 3.顧客ごとの請求書を作成
