import csv

import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4

# pip install lxml

count = 1
while count <= 317:
    url = f'https://stroydata.ru/services/building?page={count}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    block = BeautifulSoup(data, 'lxml')
    heads = block.find('ul', class_='list-firms list-unstyled').find_all('li')
    print(len(heads))
    for i in heads:
        w = i.find_next('a').get('href')
        # print('https://stroydata.ru'+w)
        get_url = ('https://stroydata.ru' + w)
        r = requests.get(get_url, headers=headers).text
        soup = BeautifulSoup(r, 'lxml')
        params = soup.find('dl', class_='list-space-plus').find_all('dd')
        print(params[0].text.strip())
        name = (params[0].text.strip())
        print(params[1].text.strip())
        adress = (params[1].text.strip())
        print(params[2].text.strip())
        phone = (params[2].text.strip())
        print(params[3].text.strip())
        email = (params[3].text.strip())
        try:
            print(params[4].text.strip())
            site = (params[4].text.strip())
        except:
            print('None')
            site = ('None')
        print('\n')

        storage = {'name': name, 'adress': adress, 'phone': phone, 'email': email, 'site': site}
        with open('all_companies.csv', 'a+', encoding='utf-16') as file:
            pisar = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\r')
            pisar.writerow([storage['name'], storage['adress'], storage['phone'], storage['email'], storage['site']])

    count += 1
    print(count)
