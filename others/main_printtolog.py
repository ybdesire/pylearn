import datetime

def printtolog(msg):
    with open('log.txt', 'a') as fw:
        fw.write( '{0}, {1}\n'.format(datetime.datetime.now(), msg) )

if __name__=='__main__':
	printtolog('hello')
	printtolog('world')
	printtolog('wh')