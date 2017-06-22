import os, ftplib


# download file from srcpath at ftp
srcpath_ftp = '/ftpsrc/' # the file path at ftp server 
file_name_ftp = 'file.txt'# the file name at ftp server 
dstfile = '/local/dst/file.txt'# the dst path at local

ftp = ftplib.FTP("10.12.13.14")
ftp.login('username', 'password')

ftp.cwd(srcpath_ftp)
ftp.retrbinary("RETR " + file_name_ftp ,open(dstfile, 'wb').write)