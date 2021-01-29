from PIL import Image, ImageFilter
import sys

# TODO:引数型チェック
if(len(sys.argv) != 4):
  print('引数は3つ必要です。元ファイル名 出力ファイル名 縮小率')
  sys.exit()

fileNm = sys.argv[1]
fileOutputNm = sys.argv[2]
ratio = float(sys.argv[3])

# 元ファイル取得
im = Image.open(fileNm)
width, height = im.size
width = round(width * ratio)
height = round(height * ratio)
print(im.size)

# サイズ変換
newim = im.resize((width, height))
newim.save(fileOutputNm)
print(newim.size)