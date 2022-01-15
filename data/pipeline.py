import logging
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)
delivery_sites_uid = ['ifood']

def main():
    _extract()
    _transform()

def _extract():
    for delivery_sites in delivery_sites_uid:
        logger.info('Starting extract process')
        subprocess.run(['python3', 'main.py', delivery_sites], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(delivery_sites), '-exec' , 'mv' , '{}' , '../raw/{}_.csv'.format(delivery_sites), ';'], cwd='./extract')
def _transform():
    for delivery_sites in delivery_sites_uid:
        logger.info('Starting transform process')
        dirty_data_filename = '{}_.csv'.format(delivery_sites)
        clean_data = '{}_clean'.format(delivery_sites)
        subprocess.run(['python3', 'main.py', '../raw/{}'.format(dirty_data_filename)], cwd='./transform')
        subprocess.run(['mv', '../raw/{}.csv'.format(clean_data) , '../transform/{}.csv'.format(delivery_sites)], cwd='./transform')
        subprocess.run(['rm', '../raw/{}'.format(dirty_data_filename).format(delivery_sites)], cwd='./transform')
        logger.info('Process finished')
if __name__ == '__main__':
    main()