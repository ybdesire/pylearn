import logging

logging.basicConfig(level=logging.ERROR) # only show error
logger = logging.getLogger(__name__)


def main():
    logger.info('Start reading database')
    # read database here
    records = {'john': 55, 'tom': 66}
    logger.debug('Records: %s', records) 
    logger.info('Updating records ...')
    # update records here
    logger.info('Finish updating records')
    logger.error('Sth error here')


if __name__=='__main__':
    main()


