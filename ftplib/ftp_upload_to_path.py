import os, ftplib


# upload file to ftp dst

srcfile = '/local/src/file.txt'# the src path at local
dst = "/ftpdst_path/file.txt"# dst path at ftp

ftp = ftplib.FTP("10.12.13.14")
ftp.login('username', 'password')

f = open(srcfile, 'rb')
ftp.storbinary("STOR " + dst, f)
f.close()