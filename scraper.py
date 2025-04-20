import requests
from bs4 import BeautifulSoup
import json

def scrape_restaurant(url, name_selector, location_selector, menu_selector, hours_selector, contact_selector):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve {url}. Status code: {response.status_code}")
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.select_one(name_selector).text.strip() if soup.select_one(name_selector) else "N/A"
    location = soup.select_one(location_selector).text.strip() if soup.select_one(location_selector) else "N/A"
    menu_items = []
    for item in soup.select(menu_selector):
        item_name = item.select_one('.item-name').text.strip() if item.select_one('.item-name') else "N/A"
        price = item.select_one('.price').text.strip() if item.select_one('.price') else "N/A"
        description = item.select_one('.description').text.strip() if item.select_one('.description') else "N/A"
        tags = [tag.text.strip() for tag in item.select('.tag')]
        menu_items.append({
            'item_name': item_name,
            'price': price,
            'description': description,
            'tags': tags
        })
    operating_hours = soup.select_one(hours_selector).text.strip() if soup.select_one(hours_selector) else "N/A"
    contact = soup.select_one(contact_selector).text.strip() if soup.select_one(contact_selector) else "N/A"
    return {
        'name': name,
        'location': location,
        'menu': menu_items,
        'operating_hours': operating_hours,
        'contact': contact
    }

# Define restaurants and their specific selectors (adjust based on actual HTML)
restaurants = [
    {
        'url': 'https://theoriginaldenver.com/menu',
        'name_selector': 'h1.restaurant-name',
        'location_selector': 'div.location',
        'menu_selector': 'div.menu-item',
        'hours_selector': 'div.hours',
        'contact_selector': 'div.contact'
    },
    # Add more restaurants with their specific selectors
]

def main():
    scraped_data = []
    for restaurant in restaurants:
        try:
            data = scrape_restaurant(**restaurant)
            scraped_data.append(data)
        except Exception as e:
            print(f"Error scraping {restaurant['url']}: {e}")
    with open('restaurants.json', 'w') as f:
        json.dump(scraped_data, f, indent=4)

if __name__ == '__main__':
    main()