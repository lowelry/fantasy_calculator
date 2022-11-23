#from urllib.request import urlopen
#html = urlopen('https://fantasy.espn.com/basketball/team?leagueId=1013716421&teamId=1&seasonId=2023.html')
#print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://fantasy.espn.com/basketball/team?leagueId=1013716421&teamId=1&seasonId=2023')
bs = BeautifulSoup(html.read(), 'html.parser')


print(bs)
#//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div[3]/div/div/div/div/table[2]/tbody/tr[1]/td[2]/div
#jsx-1925058086 team-page