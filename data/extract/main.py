from this import d
from yaml import parse
from common import config
import delivery_sites_object as deliverys
from urllib3.exceptions import MaxRetryError
from requests.exceptions import HTTPError
import requests
from bs4 import BeautifulSoup
import re
import argparse
import logging
import os
import pandas as pd
import datetime
import json
from os import write
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$')
other = re.compile(r'^https?://.+$')
is_root_path = re.compile(r'^/.+$')


def delivery_scraper(delivery_sites_uid):
    host= config()['delivery_sites'][delivery_sites_uid]['url_bog_rest']
    logging.info('Beginning scraper for {}'.format(host))
    restaurant_page = deliverys.RestaurantPage(delivery_sites_uid)
    restaurants = []
    restaurant_info = []
    for info in restaurant_page.restaurant_info:
        link = info[1]
        restaurant = _fetch_restaurant(delivery_sites_uid, _builder_link(link, host))
        if restaurant != None:
            logging.info('Restaurant {} found and fetched'.format(info[1]))
            restaurants.append(restaurant)
            restaurant_info.append(info[0])
        else:
            logging.info('Restaurant {} not available'.format(link))
    _save_restaurant(restaurants, restaurant_info ,delivery_sites_uid)


def _save_restaurant(restaurants, restaurant_info, delivery_sites_uid):

    objRestaurant = {
        'dish_name': [],
        'details': [],
        'categories': [],
        'unitMinPrice': [],
        'restaurant_name': [],
        'valoration': [],
        'delivery_fee': [],
        'delivery_time_min': [],
        'delivery_time_max': [],
        }
    for aux in range(len(restaurants)):
        menu_aux = restaurants[aux]
        categories = [x['name'] for x in menu_aux ]
        for i in range(len(categories)):
            number_products = len(menu_aux[i]['itens'])
            for j in range(number_products):
                objRestaurant['categories'].append(menu_aux[i]['name'])
                objRestaurant['dish_name'].append( menu_aux[i]['itens'][j]['description'])
                try:
                    objRestaurant['details'].append(menu_aux[i]['itens'][j]['details'])
                except KeyError:
                    objRestaurant['details'].append('whitout info')
                objRestaurant['unitMinPrice'].append(menu_aux[i]['itens'][j]['unitMinPrice'])
                objRestaurant['restaurant_name'].append(restaurant_info[aux]['name'])
                objRestaurant['valoration'].append(restaurant_info[aux]['userRating'])
                try:
                    objRestaurant['delivery_fee'].append(restaurant_info[aux]['deliveryInfo']['fee'])
                except KeyError:
                    objRestaurant['delivery_fee'].append('whitout info')
                try:
                    objRestaurant['delivery_time_min'].append(
                        restaurant_info[aux]['deliveryInfo']['timeMinMinutes'])
                except KeyError:
                    objRestaurant['delivery_time_min'].append(0)
                try:
                    objRestaurant['delivery_time_max'].append(
                        restaurant_info[aux]['deliveryInfo']['timeMaxMinutes'])
                except KeyError:
                    objRestaurant['delivery_time_max'].append(0)

    df_restaurant = pd.DataFrame(objRestaurant)

    df_restaurant.to_csv('{}_'.format(delivery_sites_uid), sep=',', index=False , encoding='utf-8')

def _fetch_restaurant(homepage_url , link):
    logging.info('Beginning fetching restaurant {}'.format(link))
    try:
        response = requests.get(link)
        response.raise_for_status()
        restaurant = BeautifulSoup(response.text, 'lxml').find('script', attrs={'id': '__NEXT_DATA__'}).get_text()
        res_data = json.loads(restaurant)
        data_menu = res_data['props']['initialState']['restaurant']['menu']
        if data_menu == []:
            return None
        else:
            return data_menu
    except (HTTPError, MaxRetryError) as e:
        logging.error('Error while trying to fetch article: {}'.format(e))
        return None

def _builder_link(link, host):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    elif other.match(link):
        return '{}/{}'.format(host, link)
    else:
        return None



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    delivery_sites_choices = list(config()['delivery_sites'].keys())
    parser.add_argument('delivery_site', help='The delivery site uid, must be one of: {}'.format(delivery_sites_choices), type=str, choices=delivery_sites_choices)
    args = parser.parse_args()
    delivery_scraper(args.delivery_site)
