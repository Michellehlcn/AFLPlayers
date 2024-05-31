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
import time
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
time.sleep(2)
desc = driver.find_elements(By.XPATH, '//*[contains(@data-testid, "total-statistics")]' )[0]
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
select_year = driver.find_element(By.XPATH, '//*[contains(@id, "season-select")]' ).find_elements(By.TAG_NAME, "option")
year = select_year[1].text
print(year)
select_year[1].click()
# game_permit = year.split("(")   
season_stats = driver.find_element(By.XPATH, '//*[contains(@data-testid, "season-statistics")]' )


#rint(season_stats.text)

details_of_clubs = season_stats.find_elements(By.TAG_NAME, "div")

for details_of_clubs_ in range(2,len(details_of_clubs)+1):
    print(season_stats.find_element(By.CSS_SELECTOR, f"div:nth-of-type({details_of_clubs_})").text)
    season_stats_list = season_stats.find_element(By.CSS_SELECTOR, f"div:nth-of-type({details_of_clubs_})")
    club_name = season_stats_list.find_elements(By.TAG_NAME, "div")[1].find_element(By.TAG_NAME, "h3").text
    print(club_name)
    club_type_name= season_stats_list.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "p")[0].text
    print(club_type_name)
    role = season_stats_list.find_elements(By.TAG_NAME, "div")[2].text
    #//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]
    #//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/h3
    #//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/h3

#//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]
#//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/span[1]
#//*[@id="root"]/section/main/div/div/div/div/div/div/div[2]/div[2]/div[1]/h2

    print(role)
    total_statistics = season_stats_list.find_elements(By.XPATH, '//*[contains(@data-testid, "total-statistics")]' )[1]

    games_played = total_statistics.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "span")[0].text
    total_goals = total_statistics.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[0].text
    best_player = total_statistics.find_elements(By.TAG_NAME, "div")[2].find_elements(By.TAG_NAME, "span")[0].text

    print(games_played)
    print(total_goals)
    print(best_player)

    #Details of the season
    details = season_stats.find_element(By.TAG_NAME, "table").find_element(By.TAG_NAME, "tbody")
    games = details.find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[0].find_elements(By.TAG_NAME,"span")[0].text
    print(games)
    games_games_played = details.find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[1].find_elements(By.TAG_NAME, "span")[0].text
    print(games_games_played)
    games_total_goals = details.find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[2].find_elements(By.TAG_NAME, "span")[0].text
    print(games_total_goals)
    games_best_player = details.find_elements(By.TAG_NAME, "tr")[0].find_elements(By.TAG_NAME, "td")[3].find_elements(By.TAG_NAME, "span")[0].text
    print(games_best_player)

    #Details of games
    details_of_games = details.find_elements(By.TAG_NAME, "tr")
    for details_of_games_ in range(2,len(details_of_games)+1):
        #print(details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").text)
        match_name = details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[0].find_elements(By.TAG_NAME, "span")[0].text
        match_time =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[0].find_elements(By.TAG_NAME, "span")[1].text
        match_games_played =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[1].find_elements(By.TAG_NAME, "span")[0].text
        match_total_goals =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[2].find_elements(By.TAG_NAME, "span")[0].text
        match_best_player =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[3].find_elements(By.TAG_NAME, "span")[0].text
        print(match_name)
        print(match_time)
        print(match_games_played)
        print(match_total_goals)
        print(match_best_player)

