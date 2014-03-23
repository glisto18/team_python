import csv

def get_batters():
    player_list = []
    remove_list = []
    f = open('standard_batting_final.csv')
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        player_list.append(row)
    f.close()

    for player in player_list:
        player["Age"] = int(player["Age"])
        player["Total Batting Average"] = float(player["Total Batting Average"])
        player["Total On Base Percentage"] = float(player["Total On Base Percentage"])
        player["Total Slugging Percentage"] = float(player["Total Slugging Percentage"])
        player["Total Games"] = int(player["Total Games"])
        player["Total Plate Appearances"] = int(player["Total Plate Appearances"])
        player["Total At Bats"] = int(player["Total At Bats"])
        player["Total Runs"] = int(player["Total Runs"])
        player["Total Hits"] = int(player["Total Hits"])
        player["Total Doubles"] = int(player["Total Doubles"])
        player["Total Triples"] = int(player["Total Triples"])
        player["Total Home Runs"] = int(player["Total Home Runs"])
        player["Total Runs Batted In"] = int(player["Total Runs Batted In"])
        player["Total Stolen Bases"] = int(player["Total Stolen Bases"])
        player["Total Caught Stealing"] = int(player["Total Caught Stealing"])
        player["Total Walks"] = int(player["Total Walks"])
        player["Total Strikeouts"] = int(player["Total Strikeouts"])
        player["Total Hit by Pitch"] = int(player["Total Hit by Pitch"])
        player["Total Sacrifice Hits"] = int(player["Total Sacrifice Hits"])
        player["Total Sacrifice Flies"] = int(player["Total Sacrifice Flies"])
        player["Total Intentional Walks"] = int(player["Total Intentional Walks"])
    #By now, player_list is a list of dicts, each dict a single player
    #Total stats are now floats and ints appropriately
    #The list contains ALL players and must be pruned

    for player in player_list:
        if player['Total Games'] < 80 or player['Total At Bats'] < 400:
            remove_list.append(player)
            
    print "Starting with '" + str(len(player_list)) + "' players."

    for player in remove_list:
        player_list.remove(player)

    print "Ended with '" + str(len(player_list)) + "' players."

    for player in player_list:
        player["Total Bases"] = player["Total Hits"]\
                                + (2 * player["Total Doubles"])\
                                + (3 * player["Total Triples"])\
                                + (4 * player["Total Home Runs"])
        player["Fantasy Points"] = player["Total Bases"]\
                                   + player["Total Runs"]\
                                   + player["Total Stolen Bases"]\
                                   + player["Total Walks"]\
                                   + player["Total Runs Batted In"]\
                                   - player["Total Strikeouts"]
        player["Batting Average on Balls in Play"] = \
                        float((player["Total Hits"] - player["Total Home Runs"]))\
                        / float((player["Total At Bats"] - player["Total Strikeouts"]\
                           - player["Total Home Runs"] + player["Total Sacrifice Flies"]))
        player["Secondary Average"] = float(player["Total Walks"]\
                                      + (player["Total Bases"] - player["Total Hits"])\
                                      + (player["Total Stolen Bases"] - player["Total Caught Stealing"]))\
                                      / float(player["Total At Bats"])
        player["On Base Plus Slugging"] = player["Total On Base Percentage"]\
                                          + player["Total Slugging Percentage"]
        player["Goodness"] = (float(player["Batting Average on Balls in Play"])/.300)\
                             + (float(player["Secondary Average"])/.275)\
                             + (float(player["Total On Base Percentage"])/.340)\
                             + (float(player["Total Slugging Percentage"])/.420)\
                             + (float(player["On Base Plus Slugging"])/.760)

    player_list.sort(key=lambda x: x["Goodness"])
    player_list.reverse()
    f = open('batters.txt', 'w')
    for player in player_list:
        f.write(player["Name2"] + "\n")
        f.write("OBP: " + str(player["Total On Base Percentage"]) + "\n")
        f.write("BABIP: " + str(round(player["Batting Average on Balls in Play"], 3)) + "\n")
        f.write("TB: " + str(player["Total Bases"]) + "\n")
        f.write("AB: " + str(player["Total At Bats"]) + "\n")
        f.write("AVG: " + str(player["Total Batting Average"]) + "\n")
        f.write("SO: " + str(player["Total Strikeouts"]) + "\n")
        f.write("Risk-Reward: " + str(player["Total Stolen Bases"]) + "/" + str(player["Total Caught Stealing"]\
                                                                                + player["Total Stolen Bases"]) + "\n\n")

    f.close()

def get_pitchers():
    print ""
