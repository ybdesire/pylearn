from pathlib import Path
#Pathlib 是 Python3 中的一个默认模块，可以帮助你避免使用大量的 os.path.join

a = Path("dir1")
b = "dir2"
c = a / b
print(c)
print(c.exists())  # 路径是否存在
print(c.is_dir())  # 判断是否为文件夹
print(c.parts)  # 分离路径
print(c.with_name('sibling.png'))  # 只修改拓展名, 不会修改源文件
print(c.with_suffix('.jpg'))  # 只修改拓展名, 不会修改源文件
c.chmod(777)  # 修改目录权限
#c.rmdir()  # 删除目录
