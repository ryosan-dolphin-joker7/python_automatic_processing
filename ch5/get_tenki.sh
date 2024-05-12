#/bin/bash

# PYTHONのパスを指定 --- (*1)
PYTHON=/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# このファイルがあるパスを取得 --- (*2)
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# プログラムを実行 --- (*3)
$PYTHON $SCRIPT_DIR/get_tenki.py
