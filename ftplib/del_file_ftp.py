import ftplib

file_path = '/ftp_root/code/main.py'

ftp = ftplib.FTP('server_ip')
ftp.login('username', 'password')

ftp.cwd('.')
ftp.delete(file_path)# delete file