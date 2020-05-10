import requests
import json
from prettytable import PrettyTable

#RAPID API USED: https://rapidapi.com/api-sports/api/api-football
#API-FOOTBALL Documentation: https://www.api-football.com/documentation#standings-parameters

linkEPL = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/524" #Premier League Standings
linkLaLiga = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/775" #La Liga Standings
linkLigue1 = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/525" #Ligue 1 Standings
linkBuLi = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/754" #Bundesliga Standings
linkSerieA = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/891" #Serie A Standings

def getLeagueInfo(link, name): #calls api for league info, turns to json
    
    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "b161a95968mshc503b44905f5835p1c6209jsna8d9417d557f"
    }
    
    info = requests.request("GET", link , headers=headers)
    record = json.loads(info.content)
    print("Current " + name + " standings for the 2019-2020 season")
    return record


def makeLeagueTable(record): #takes in json for league, makes table from league json
    
    leagueTable = PrettyTable(['Rank', 'Team Name', 'Points', 'Goal Diff.', 
                               'Form', 'Last Updated'])
    for team in record['api']['standings'][0]:        
        leagueTable.add_row([team['rank'], team['teamName'], team['points'], 
                             team['goalsDiff'], team['forme'], team['lastUpdate'] ])
        
    print(leagueTable)

#function calls for output    
makeLeagueTable(getLeagueInfo(linkEPL, "Premier League (England)"))
makeLeagueTable(getLeagueInfo(linkLaLiga, "Primera Division (Spain)"))
makeLeagueTable(getLeagueInfo(linkLigue1, "Ligue 1 (France)"))
makeLeagueTable(getLeagueInfo(linkBuLi, "Bundesliga (Germany)"))
makeLeagueTable(getLeagueInfo(linkSerieA, "Serie A (Italy)"))


#api links for 2 teams upcoming fixtures
barcaFixtLink = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/529/next/5?timezone=Europe/London"
liverpoolFixLink = "https://api-football-v1.p.rapidapi.com/v2/fixtures/team/40/next/5?timezone=Europe/London"

def getFixtures(link, team): #takes in api link, creates table for upcoming fixtures (up to 5)

    headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "b161a95968mshc503b44905f5835p1c6209jsna8d9417d557f"
    }
    
    fixtures = requests.request("GET", link, headers=headers)
    fixt = json.loads(fixtures.content)
    
    fixtTable = PrettyTable(['Date', 'Home', 'Away', 'Competition', 'Status'])


    print("Upcoming " + team + " Fixtures")
    
    for match in fixt['api']['fixtures']:
        fixtTable.add_row([match['event_date'][:10], match['homeTeam']['team_name'], 
                           match['awayTeam']['team_name'], match['league']['name'],
                           match['status']])
    
    print(fixtTable)

#fixture calls
getFixtures(barcaFixtLink, "FC Barcelona")
getFixtures(liverpoolFixLink, "Liverpool FC")



#links for top scorers for 5 leagues
linkPDScore = "https://api-football-v1.p.rapidapi.com/v2/topscorers/775"
linkEPLScore = "https://api-football-v1.p.rapidapi.com/v2/topscorers/524"
linkSAScore = "https://api-football-v1.p.rapidapi.com/v2/topscorers/891"
linkL1Score = "https://api-football-v1.p.rapidapi.com/v2/topscorers/525"
linkBLScore = "https://api-football-v1.p.rapidapi.com/v2/topscorers/754"

def getTopScorers(link, leagueName): #takes in api link and league name, outputs table with scorers
    
    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "b161a95968mshc503b44905f5835p1c6209jsna8d9417d557f"
        }

    scorersInfo = requests.request("GET", link, headers=headers)
    scorers = json.loads(scorersInfo.content)
    
    scorersTable = PrettyTable(['Rank:', 'Player Name', 'Position', 'Goals', 
                                'Team', 'Nationality'])

    
    print(leagueName + " top scorers")
    counter = 0
    
    for player in scorers['api']['topscorers']:
        counter = counter + 1
        scorersTable.add_row([counter, player['player_name'], player['position'], 
                              player['goals']['total'], player['team_name'], 
                              player['nationality']])
    
    print(scorersTable)
    
getTopScorers(linkPDScore, "Primera Division (Spain)")    
getTopScorers(linkEPLScore, "Premier League (England)")
getTopScorers(linkSAScore, "Serie A (Italy)")
getTopScorers(linkL1Score, "Ligue 1 (France)")
getTopScorers(linkBLScore, "BundesLiga (Germany)")

