import requests
from bs4 import BeautifulSoup


def scrape_product_price(product_id):
    url = f"https://www.amazon.es/dp/{product_id}"
    headers = ({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                      'Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })

    response = requests.get(url, headers=headers)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    price_whole_raw = soup.find('span', {'class': 'a-price-whole'}).get_text()
    price_fraction_raw = soup.find('span', {'class': 'a-price-fraction'}).get_text()
    price_raw = ".".join((price_whole_raw, price_fraction_raw))

    price_cleaned = price_raw.strip().replace('.', '').replace(',', '.')

    return price_cleaned
