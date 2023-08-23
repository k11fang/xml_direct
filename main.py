import requests

videoforme_cities = [
    'moskva',
    'almaty',
    'arhangelsk',
    'astana',
    'astrahan',
    'barnaul',
    'belgorod',
    'bishkek',
    'bryansk',
    'vladivostok',
    'volgograd',
    'voronezh',
    'ekaterinburg',
    'ivanovo',
    'izhevsk',
    'irkutsk',
    'kazan',
    'kaliningrad',
    'kemerovo',
    'krasnodar',
    'krasnoyarsk',
    'lipetsk',
    'mahachkala',
    'minsk',
    'nizniy-novgorod',
    'novokuznetsk',
    'novosibirsk',
    'omsk',
    'online',
    'orenburg',
    'penza',
    'perm',
    'rostov-na-donu',
    'ryazan',
    'samara',
    'saratov',
    'smolensk',
    'surgut',
    'tashkent',
    'tver',
    'tolyatti',
    'tomsk',
    'tula',
    'tumen',
    'ulyanovsk',
    'ufa',
    'khabarovsk',
    'cheboksary',
    'chelyabinsk',
    'yaroslavl',
    'online'
]

ecolespb_cities = [
    'moscow',
    'arhangelsk',
    'balashikha',
    'barnaul',
    'vladivostok',
    'volgograd',
    'voronezh',
    'ekb',
    'ivanovo',
    'izhevsk',
    'irkutsk',
    'kazan',
    'kaliningrad',
    'kemerovo',
    'kirov',
    'krasnodar',
    'krasnoyarsk',
    'lipetsk',
    'nizniy-novgorod',
    'novokuznetsk',
    'novosibirsk',
    'omsk',
    'orenburg',
    'penza',
    'perm',
    'rostov-na-donu',
    'ryazan',
    'samara',
    'saratov',
    'stavropol',
    'surgut',
    'tver',
    'tolyatti',
    'tomsk',
    'tula',
    'tumen',
    'ulyanovsk',
    'ufa',
    'cheboksary',
    'chelyabinsk',
    'yaroslavl',
    'almaty',
    'astana',
    'minsk'
]

def main():
    #  Цикл МШП

    for city in videoforme_cities:
        xml = requests.get(f'https://videoforme.ru/spbsot_{city}_yml.xml')
        xml.encoding = 'utf-8'
        with open(f'mshp/spbsot_{city}_yml.xml', 'wb') as f:
            f.write(xml.content)
    xml = requests.get('https://videoforme.ru/spbsot_yml.xml')
    xml.encoding = 'utf-8'
    with open(f'mshp/spbsot_yml.xml', 'wb') as f:
        f.write(xml.content)

    #  Цикл Эколь

    for city in ecolespb_cities:
        xml = requests.get(f'https://ecolespb.ru/spbsot_{city}_yml.xml', verify=False)
        xml.encoding = 'utf-8'
        with open(f'ecole/spbsot_{city}_yml.xml', 'wb') as f:
            f.write(xml.content)
    xml = requests.get('https://ecolespb.ru/spbsot_yml.xml', verify=False)
    xml.encoding = 'utf-8'
    with open('ecole/spbsot_yml.xml', 'wb') as f:
        f.write(xml.content)

if __name__ == '__main__':
    main()


