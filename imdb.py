import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/search/title/?at=0&genres=animation&keywords=anime&num_votes=1000,&sort=user_rating&title_type=tv_series"
page = requests.get(url)
soup = BeautifulSoup(page.text)

df = pd.DataFrame(columns=["Rank", "Name", "Date", "Genre", "Rate", "Vote"])

rank = soup.find_all("span", class_="lister-item-index unbold text-primary")
name = soup.find_all("h3", class_="lister-item-header")
date = soup.find_all("span", class_="lister-item-year text-muted unbold")
genre = soup.find_all("span", class_="genre")
rate = soup.find_all("strong")
vote = soup.find_all("p", class_="sort-num_votes-visible")

for i in range(len(rank)):
    ranks = rank[i].text.replace(".", "").strip()
    names = name[i].a.text.strip()
    dates = date[i].text.strip()
    genres = genre[i].text.strip()
    rates = rate[i + 2].text.strip()
    votes = vote[i].text[8:].strip()
    rows = [ranks, names, dates, genres, rates, votes]
    df.loc[len(df)] = rows

df.to_csv("Anime Imdb.csv", index=False)
