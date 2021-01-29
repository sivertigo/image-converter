from PIL import Image, ImageFilter
import sys

# TODO:引数型チェック
if(len(sys.argv) != 5):
  print('引数は4つ必要です. 元ファイル名 出力ファイル名 横比率 縦比率')
  sys.exit()

# 引数取得
fileNm = sys.argv[1]
fileOutputNm = sys.argv[2]
W = int(sys.argv[3])
H = int(sys.argv[4])

# 元ファイル取得
im = Image.open(fileNm)
width, height = im.size
bgWidth, bgHeight = im.size
newim = im.resize((width, height))

# 枠のピクセル数作成
if  bgWidth < bgHeight:
  bgWidth = round(bgHeight * W / H)
else:
  bgHeight = round(bgWidth * H / W)

# 枠作成
bg = Image.new("RGB",[bgWidth,bgHeight],(255,255,255,255))

# 枠の中央に元画像を移動
bg.paste(im,(int((bgWidth-newim.size[0])/2),int((bgHeight-newim.size[1])/2)))

# ファイル出力
bg.save(fileOutputNm)