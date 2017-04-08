import ftplib

dir_path = '/ftp_root/code/'

ftp = ftplib.FTP('server_ip')
ftp.login('username', 'password')

ftp.cwd('.')

# delete files in dir
files = list(ftp.nlst(dir_path))
for f in files:
    ftp.delete(f)

# delete this dir (empty)
ftp.rmd(dir_path)