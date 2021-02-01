import dhash
from PIL import Image

def get_dhash(img_path, s):
    image = Image.open(img_path)
    row, col = dhash.dhash_row_col(image, size=s)
    hh = dhash.format_hex(row, col)
    return hh


h1 = get_dhash('img.png', 8)
print(h1)
print(len(h1))#32
# to binary
print(format(int(h1, 16), "0128b"))# 32*4=128, so is 0128b


h2 = get_dhash('img.png', 16)
print(h2)
print(len(h2))#121
# to binary
print(format(int(h2, 16), "0484b"))# 121*4=484, so is 044b
