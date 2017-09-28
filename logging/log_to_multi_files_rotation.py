import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(funcName)s,(%(lineno)d), %(message)s')

# create a file handler and add the handlers to the logger
handler = RotatingFileHandler('hello.log', mode='a', maxBytes=5*1024, 
                                 backupCount=15, encoding=None, delay=0)

handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)#

# create a console handler and add the handlers to the logger
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)



def main():
    c = 0
    while(True):
        c += 1
        logger.info('Hello baby {0}'.format(c))

    
if __name__=='__main__':
    main()
    
    
