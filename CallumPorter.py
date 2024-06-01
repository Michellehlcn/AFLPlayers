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
import pandas as pd
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions


driver = webdriver.Firefox()   
player =[]  
url = "https://www.playhq.com/public/profile/f4b26c9b-6678-4df1-9b6b-def2282e02fc/statistics?tenant=afl"   
driver.get(url)

wait = WebDriverWait(driver, 20)
time.sleep(2)
desc = driver.find_elements(By.XPATH, '//*[contains(@data-testid, "total-statistics")]' )[0]
id="1"
name="Callum Porter"

career_games_played = desc.find_elements(By.TAG_NAME, "div")[0].find_elements(By.TAG_NAME, "span")[0].text
career_total_goals = desc.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[0].text
career_best_player = desc.find_elements(By.TAG_NAME, "div")[2].find_elements(By.TAG_NAME, "span")[0].text
print(career_total_goals)
print(career_games_played )
print(career_best_player)


# season stats
season_statstictics = []
select_year = driver.find_element(By.XPATH, '//*[contains(@id, "season-select")]' ).find_elements(By.TAG_NAME, "option")
for season in range(1,len(select_year)):

    year = select_year[season].text
    print(year)
    select_year[season].click()
    # game_permit = year.split("(")   
    season_stats = driver.find_elements(By.XPATH, '//*[contains(@data-testid, "season-statistics")]' )[0]

    details_of_clubs = season_stats.find_elements(By.CSS_SELECTOR, f"div")
    print(len(details_of_clubs))

    organizations_stats = []
    next_sibiling = True
    sibiling_count = 2
    while next_sibiling:
        print(f"********************************{sibiling_count}")
        time.sleep(1)
        print(season_stats.find_element(By.CSS_SELECTOR, f"div:nth-of-type({sibiling_count})").text)
        season_stats_list = season_stats.find_element(By.CSS_SELECTOR, f"div:nth-of-type({sibiling_count})")
        sibiling_count += 1
        try:
            print(season_stats_list.find_element(By.XPATH, "./following-sibling::div"))
        except:
            next_sibiling = False
            print("No more sibiling")

        try :
        
            club_name = season_stats_list.find_elements(By.TAG_NAME, "div")[1].find_element(By.TAG_NAME, "h3").text
            print(club_name)
            club_type_name= season_stats_list.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "p")[0].text
            print(club_type_name)
            role = season_stats_list.find_elements(By.TAG_NAME, "div")[2].text

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
            details_stats = []
            for details_of_games_ in range(2,len(details_of_games)+1):
                #print(details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").text)
                match_name = details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[0].find_elements(By.TAG_NAME, "span")[0].text
                try:
                    match_time =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[0].find_elements(By.TAG_NAME, "span")[1].text
                except:
                    match_time = "-"
                match_games_played =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[1].find_elements(By.TAG_NAME, "span")[0].text
                match_total_goals =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[2].find_elements(By.TAG_NAME, "span")[0].text
                match_best_player =  details.find_element(By.CSS_SELECTOR, f"tr:nth-of-type({details_of_games_})").find_elements(By.TAG_NAME, "td")[3].find_elements(By.TAG_NAME, "span")[0].text
                print(match_name)
                print(match_time)
                print(match_games_played)
                print(match_total_goals)
                print(match_best_player)
                details_stats.append({
                    "match_name": match_name,
                    "match_time": match_time,
                    "match_games_played": match_games_played,
                    "match_total_goals": match_total_goals,
                    "match_best_player": match_best_player
                })
                print(details_stats)
        except:
            continue
        if club_type_name is not None and club_name is not None and role is not None and games_played is not None and total_goals is not None and best_player is not None:
            organizations_stats.append({
                    "club_type_name": club_type_name,
                    "club_name": club_name,
                    "role": role,
                    "games_played": games_played,
                    "total_goals": total_goals,
                    "best_player": best_player,
                    "details_stats": details_stats
                })
            print(organizations_stats)
    if organizations_stats != []:
        season_statstictics.append({
            "year": year,
            "organizations_stats": organizations_stats
        })
player.append({
    "url": url,
    "id": id,
    "name": name,
    "career_games_played": career_games_played,
    "career_total_goals": career_total_goals,
    "career_best_player": career_best_player,
    "season_stats": season_statstictics
})

print(player)

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['desc', 'id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for key, value in player[0].items():
        if type(value) is list: #[]
            for item1 in value:
                for k1, v1 in item1.items():
                    if type(v1) is list:
                        for item2 in v1:
                            for k2, v2 in item2.items():
                                if type(v2) is list:
                                    for item3 in v2:
                                        for k3, v3 in item3.items():
                                            if type(v3) is list:
                                                for item4 in v3:
                                                    for k4, v4 in item4.items():
                                                        if type(v4) is list:
                                                            for item5 in v4:
                                                                for k5, v5 in item5.items():
                                                                    if type(v5) is list:
                                                                        for item6 in v5:
                                                                            for k6, v6 in item6.items():
                                                                                writer.writerow({'desc': f"{key}.{k1}.{k2}.{k3}.{k4}.{k5}.{k6}", 'id': v6})
                                                                    else:
                                                                        writer.writerow({'desc': f"{key}.{k1}.{k2}.{k3}.{k4}.{k5}", 'id': v5})
                                                        else:
                                                            writer.writerow({'desc': f"{key}.{k1}.{k2}.{k3}.{k4}", 'id': v4})
                                            else:
                                                writer.writerow({'desc': f"{key}.{k1}.{k2}.{k3}", 'id': v3})
                                else:
                                    writer.writerow({'desc': f"{key}.{k1}.{k2}", 'id': v2})
                    else:

                        writer.writerow({'desc': f"{key}.{k1}", 'id': v1})
        else:
            writer.writerow({'desc': key, 'id': value})
  