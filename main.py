import requests
import json
import pprint


def get_data():

    cookies = {
        '__lhash_': '63406e0ea2e228a27471cb4e8b24681e',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_2_exp_in_1': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20976020647',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'flacktory': 'no',
        'searchType2': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '_gid': 'GA1.2.689043707.1656654161',
        '_ym_uid': '1656654163424992695',
        '_ym_d': '1656654163',
        'st_uid': 'd0bf2e140aede4c136e2b2dbc648bfbe',
        'advcake_track_id': 'e23e1b30-ce8a-4fb1-7651-d2e00ce99388',
        'advcake_session_id': 'c7a319fc-f248-9daa-f49b-823ec0a9c1fb',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'b2ae55d5-0245-48fb-b308-1f486d36bb9c',
        'afUserId': '32d7b2a1-810d-4819-a860-5720f14eddb5-p',
        'AF_SYNC': '1656654164488',
        'uxs_uid': 'a1949bf0-f900-11ec-bc53-293842a45e6b',
        '_ym_isad': '2',
        'flocktory-uuid': '6ba20a21-7e02-4423-89fc-1abf905e1b69-3',
        'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
        'bIPs': '-826759811',
        'adrdel': '1',
        'adrcid': 'A98chvnR6iJfOu1b_F7US7w',
        'authError': '',
        'SMSError': '',
        'MVID_CITY_ID': 'CityCZ_7173',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_REGION_ID': '14',
        'MVID_REGION_SHOP': 'S921',
        'ADRUM_BT': 'R:133|g:d61638bb-3811-4b72-a4cf-fb2c34a88fe64471796',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'JSESSIONID': 'vhy1v2Kc5ltBXRtGgdjypbJRBbWQTS1YhZyJVHrvWlWv3prLt4vy!-1370321511',
        'MVID_CITY_CHANGED': 'false',
        'MVID_KLADR_ID': '3600000100000',
        'mindboxDeviceUUID': '73b019fe-708a-469c-a2f7-6e19b34a8665',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2273b019fe-708a-469c-a2f7-6e19b34a8665%22%7D',
        '_ga_CFMZTSS5FM': 'GS1.1.1656654162.1.1.1656654366.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1656654162.1.1.1656654366.58',
        '_ga': 'GA1.2.1005873918.1656654161',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__lhash_=63406e0ea2e228a27471cb4e8b24681e; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MVID_2_exp_in_1=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20976020647; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _gid=GA1.2.689043707.1656654161; _ym_uid=1656654163424992695; _ym_d=1656654163; st_uid=d0bf2e140aede4c136e2b2dbc648bfbe; advcake_track_id=e23e1b30-ce8a-4fb1-7651-d2e00ce99388; advcake_session_id=c7a319fc-f248-9daa-f49b-823ec0a9c1fb; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=b2ae55d5-0245-48fb-b308-1f486d36bb9c; afUserId=32d7b2a1-810d-4819-a860-5720f14eddb5-p; AF_SYNC=1656654164488; uxs_uid=a1949bf0-f900-11ec-bc53-293842a45e6b; _ym_isad=2; flocktory-uuid=6ba20a21-7e02-4423-89fc-1abf905e1b69-3; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; adrdel=1; adrcid=A98chvnR6iJfOu1b_F7US7w; authError=; SMSError=; MVID_CITY_ID=CityCZ_7173; MVID_GEOLOCATION_NEEDED=false; MVID_REGION_ID=14; MVID_REGION_SHOP=S921; ADRUM_BT=R:133|g:d61638bb-3811-4b72-a4cf-fb2c34a88fe64471796; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; JSESSIONID=vhy1v2Kc5ltBXRtGgdjypbJRBbWQTS1YhZyJVHrvWlWv3prLt4vy!-1370321511; MVID_CITY_CHANGED=false; MVID_KLADR_ID=3600000100000; mindboxDeviceUUID=73b019fe-708a-469c-a2f7-6e19b34a8665; directCrm-session=%7B%22deviceGuid%22%3A%2273b019fe-708a-469c-a2f7-6e19b34a8665%22%7D; _ga_CFMZTSS5FM=GS1.1.1656654162.1.1.1656654366.0; _ga_BNX5WPP3YK=GS1.1.1656654162.1.1.1656654366.58; _ga=GA1.2.1005873918.1656654161; MVID_ENVCLOUD=prod2',
        'Referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429/f/graficheskii-kontroller=geforce-rtx-3060,geforce-rtx-3060-ti',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.4.904 Yowser/2.5 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Yandex";v="22"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-set-application-id': '7518b924-c3db-421d-be48-39316872a39b',
    }

    params = {
        'categoryId': '5429',  # Категории
        'offset': '0',  # Пагинация
        'limit': '24',
        'filterParams': 'WyLQk9GA0LDRhNC40YfQtdGB0LrQuNC5INC60L7QvdGC0YDQvtC70LvQtdGAIiwiNjIwIiwiR2VGb3JjZSBSVFggMzA2MCIsIkdlRm9yY2UgUlRYIDMwNjAgVGkiXQ==',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_ids = response.get('body').get('products')

    with open('1_product_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids) #Получили id товаров со скидкой

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products'))) # Количество товаров

    # Склеиваем список id в одну строку
    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_price.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_total': item_bonus
        }

    with open('4_items_price.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        product_data = json.load(file)

    with open('4_items_price.json') as file:
        product_price = json.load(file)

    products_data = product_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in product_price:
            prices = product_price[product_id]

            item['item_base_Price'] = prices.get('item_basePrice')
            item['item_sale_Price'] = prices.get('item_salePrice')
            item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def base_info():
    info_list = []
    with open('5_result.json') as file:
        product_data = json.load(file)

    for item in product_data:
        item_name = item.get('modelName')
        item_baseprice = item.get('item_base_Price')
        item_saleprice = item.get('item_sale_Price')
        item_bonus = item.get('item_bonus')
        item_spercent = (int(item_saleprice) / int(item_baseprice)) * 100
        discount  = round(100 - item_spercent, 2)
        info_list.append([item_name, item_baseprice, item_saleprice, '-' if discount == 0.0 else discount, item_bonus])
    return info_list


if __name__ == "__main__":
    get_data()
    get_result()
    pprint.pprint(base_info())
