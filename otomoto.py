import httpx
import bs4


otomoto_url = "https://www.otomoto.pl/osobowe/od-2010?search%5Bfilter_enum_damaged%5D=0&search%5Bfilter_enum_fuel_type%5D%5B0%5D=petrol&search%5Bfilter_enum_fuel_type%5D%5B1%5D=petrol-lpg&search%5Bfilter_float_price%3Afrom%5D=10000&search%5Bfilter_float_price%3Ato%5D=40000&search%5Bfilter_float_year%3Ato%5D=2015&search%5Border%5D=filter_float_price%3Aasc&search%5Badvanced_search_expanded%5D=true"

response = httpx.get(otomoto_url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
data_testid_tags = soup.find("div", attrs={"data-testid": "search-results"})
tags_list = []
for tag in data_testid_tags:
    article_with_h1_tag = tag.find('h1')
    article_with_p_tag = tag.find('p')


    tags_list.append(article_with_h1_tag)
    print(article_with_p_tag.text)
    print(article_with_h1_tag)

print('****'*20)
print(len(tags_list))
