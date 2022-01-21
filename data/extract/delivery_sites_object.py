from logging import debug
from common import config
import json


class DeliverySite:
    def __init__(self, delivery_sites_uid,idx):
        self.__config = config()['delivery_sites']['ifood']
        self._queries = self.__config['queries']
        self._data = None
        self._index = int(idx)
        self._delivery_sites_uid = delivery_sites_uid
        self.url_bog_res = self.__config['url_bog_rest']
        self._readingData()

    def _readingData(self):
        try:
            jsonFile = open('../../backend_scraper/src/data/data{}.json'.format(self._index), 'r')
            self._data = json.load(jsonFile)
            return self._data
        except Exception as e:
            debug(e)

class RestaurantPage(DeliverySite):
    def __init__(self, delivery_sites_uid, idx):
        super().__init__(delivery_sites_uid,idx )
        for i in range(len(self._data)):
            if self._data[i]['cardType'] == 'MERCHANT_LIST_V2':
                self._index = i

    @property
    def restaurant_info(self):
        info_restaurantes_bogota = []
        for info in self._data[self._index]['data']['contents']:
            slug = info['action'].split('%2F')[-1]
            info_restaurantes_bogota.append(
                [info, self.url_bog_res + slug + '/' + info['id']])

        return info_restaurantes_bogota
