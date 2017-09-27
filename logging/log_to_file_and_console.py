import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s, %(levelname)s, %(funcName)s,(%(lineno)d), %(message)s')

# create a file handler and add the handlers to the logger
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)#

# create a console handler and add the handlers to the logger
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)



def main():
    logger.info('Hello baby')

    
if __name__=='__main__':
    main()
    
    
