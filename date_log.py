import datetime
import logging

date_to_prove = input('Введите дату: ')
logger = logging.getLogger(__name__)

logging.basicConfig(filename='mylog_date.log', filemode='a', encoding='UTF-8', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

date_obj = date_to_prove.split('.')
try:
    date = datetime.date(day=int(date_obj[0]), month=int(date_obj[1]), year=int(date_obj[2]))
    print('True')
except ValueError as e:
    logging.error(msg = e)