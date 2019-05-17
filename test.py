import requests
import bs4

result = requests.get("https://towardsdatascience.com/the-power-of-visualization-in-data-science-1995d56e4208")
soup = bs4.BeautifulSoup(result.content)
metas = soup.find_all("meta", attrs={'content':'Medium'})

print(metas)
