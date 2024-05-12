rem --- 作業フォルダをバッチファイルのパスに設定 ---
cd /d　%~dp0
rem --- プログラムの実行 ---
python3 %~dp0\get_tenki.py

