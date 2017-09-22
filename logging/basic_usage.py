import logging

logging.basicConfig(level=logging.INFO) # only show info & error
logger = logging.getLogger(__name__)


def main():
    logger.info('Start reading database')
    # read database here
    records = {'john': 55, 'tom': 66}
    logger.debug('Records: %s', records) # debug cannot show since config
    logger.info('Updating records ...')
    # update records here
    logger.info('Finish updating records')


if __name__=='__main__':
    main()


