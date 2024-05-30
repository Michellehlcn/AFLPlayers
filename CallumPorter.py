# Year
# name 
# organization name
# club type name
# club name
# role
# games played
# total goals
# best player
# player={
#     "id": 1,
#     "name": "Callum Porter",
#     "url": "https://www.playhq.com/public/profile/f4b26c9b-6678-4df1-9b6b-def2282e02fc/statistics?tenant=afl",
#     "type": "AFL",
#     "career_games_played": "5",
#     "career_total_goals": "5",
#     "career_best_player": "136"
#     "season_stats": [
#         {
#             "year": "2022",
#             "game_permit: true,
#             "organizations_stats": [
#                 {
#                     "club_type_name": "BOX HILL HAWKS VFL",
#                     "club_name": "VFL",
#                     "role": "Player",
#                     "games_played": "5",
#                     "total_goals": "5",
#                     "best_player": "136",
#                     "details": [
#                         {
#                             "club_name": "VS Brisbane Lions VFL",
#                             "Round": 9,
#                             "time": "",
#                             "games_played": 8,
#                             "total_goals": 0,
#                             "best_player": "-"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]
# }
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions


driver = webdriver.Firefox()        
driver.get("https://www.playhq.com/public/profile/f4b26c9b-6678-4df1-9b6b-def2282e02fc/statistics?tenant=afl")

wait = WebDriverWait(driver, 20)
desc = driver.find_element(By.XPATH, '//*[contains(@data-testid, "total-statistics")]' )
id="1"
name=""
url = ""

career_games_played = desc.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "span")[0].text
career_total_goals = desc.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[0].text
career_best_player = desc.find_elements(By.TAG_NAME, "div")[2].find_elements(By.TAG_NAME, "span")[0].text
print(career_total_goals)
print(career_games_played )
print(career_best_player)

# season stats
year = driver.find_element(By.XPATH, '//*[contains(@id, "season-select")]' )
# game_permit = year.split("(")   
season_stats = driver.find_element(By.XPATH, '//*[contains(@data-testid, "season-statistics")]' )

season_stats_list = season_stats.find_elements(By.TAG_NAME, "div")[2]
print(season_stats_list.text)
club_name_ = season_stats_list.find_elements(By.TAG_NAME, "div")[0].find_element(By.TAG_NAME, "h3").text
club_type_name= season_stats_list.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "p")[1].text
role = season_stats_list.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "p")[0].text
print(year)
print(club_name)
print(club_type_name)
print(role)

# total_stats_list = season_stats_list .find_element(By.XPATH, '//*[contains(@data-testid, "total-statistics")]' )
# games_played = total_stats_list.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "span")[0]
# total_goals = total_stats_list.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[0]
# best_player = total_stats_list.find_elements(By.TAG_NAME, "div")[2].find_elements(By.TAG_NAME, "span")[0]

# print(games_played)
# print(total_goals)
# print(best_player)