from logging import debug
from common import config
import json


class DeliverySite:
    def __init__(self, delivery_sites_uid,):
        self.__config = config()['delivery_sites'][delivery_sites_uid]
        self._queries = self.__config['queries']
        self._data = None
        self.url_bog_res = self.__config['url_bog_rest']
        self._readingData()

    def _readingData(self):
        try:
            jsonFile = open('../../backend_scraper/src/data/data.json', 'r')
            self._data = json.load(jsonFile)
            return self._data
        except Exception as e:
            debug(e)

class RestaurantPage(DeliverySite):
    def __init__(self, delivery_sites_uid):
        super().__init__(delivery_sites_uid )


    @property
    def restaurant_info(self):
        info_restaurantes_bogota = []
        for info in self._data[5]['data']['contents']:
            slug = info['action'].split('%2F')[-1]
            info_restaurantes_bogota.append(
                [info, self.url_bog_res + slug + '/' + info['id']])

        return info_restaurantes_bogota
