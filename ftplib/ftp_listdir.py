import os, ftplib


def listdir(path):
    files = []
    ftp = ftplib.FTP("10.12.13.14")
    ftp.login('username', 'password')
    tmp = list(ftp.nlst(path))
    for f in tmp:
        if(is_file(f)):
            files.append(os.path.join(path, f))
    return files

def is_dir(path):
    if(len(path.split('.'))<2):
        return True
    else:
        return False

def is_file(path):
    if(is_dir(path)):
        return False
    else:
        return True