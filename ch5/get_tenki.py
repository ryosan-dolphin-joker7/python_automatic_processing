import requests, os, platform

# デスクトップのパスを得る
save_file = os.path.expanduser('~/Desktop/天気.txt')

# クジラ気象情報APIから天気予報を得る
api_url = 'https://api.aoikujira.com/tenki/week.php?fmt=ini&city=319'
tenki = requests.get(api_url).text

# デスクトップに保存
with open(save_file, 'wt', encoding='utf-8') as f:
    f.write(tenki)

