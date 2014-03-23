import csv

def read_and_create(f):
    player_dict = csv.DictReader(f)
    return player_dict

def best_batters(master_dict):
    player_list = []
    for row in master_dict:
        player_list.append((row.get("Name2"), float(row.get("Total Batting Average")),\
                            int(row.get("Total At Bats")), int(row.get("Total Hits")),\
                            float(row.get("Total On Base Percentage")), int(row.get("Total Plate Appearances"))\
                            , int(row.get("Total Stolen Bases")), int(row.get("Total Caught Stealing"))\
                            , int(row.get("Total Walks")), int(row.get("Total Intentional Walks")), \
                            int(row.get("Total Strikeouts")), float(row.get("Total Slugging Percentage"))\
                            , int(row.get("Total Runs"))))
    return player_list

def prompt():
    usr_quit = False
    f = open('standard_batting_final.csv')
    player_list = best_batters(read_and_create(f))
    f.close()
    stats_available = ["Total Batting Average", "At Bats", "Total Hits", "Total On Base Percentage", "Total Plate Appearances", "Total Stolen Bases",\
                       "Total Caught Stealing", "Total Walks", "Total Intentional Walks", "Total Strikeouts", "Total Slugging Percentage", "Total Runs"]

    while not usr_quit:
        top_amount = raw_input("How many top players do you want to display?")
        print '\n'
        if top_amount.isdigit() and int(top_amount) < len(player_list):

            for kind in stats_available:
                print "\t" + kind

            stat_kind = raw_input("\n\nWhich stat do you want to analyze? CASE SENSITIVE:")

            if stat_kind in stats_available:
                player_list.sort(key=lambda x: x[stats_available.index(stat_kind) + 1])
                sorted_list = sorted(player_list, key=lambda player: stat_kind)
                sorted_list.reverse()
                for player in sorted_list[0:int(top_amount)]:
                    print "\nName:" + player[0]
                    print stat_kind + ":" + str(player[stats_available.index(stat_kind) + 1]) + '\n'
            else:
                print "\nInvalid statistic.  Try again.\n"
                
        elif top_amount.lower() == "quit":
            usr_quit = True

        else:
            print "Invalid input, try again."

def generator():
    f = open('standard_batting_final.csv')
    player_list = best_batters(read_and_create(f))
    f.close()
    remove_list = []

    for player in player_list:
        if player[1] <= .399 and player[2] > 500:
            player + ("Production", player[11] + player[4])
            player + ("Runs/AB", float(player[12])/float(player[2]))
        else:
            remove_list.append(player)

    for player in remove_list:
        player_list.remove(player)
            
    player_list.sort(key=lambda x: x[11])
    sorted_list = sorted(player_list, key=lambda player: "Production")
    sorted_list.reverse()
    f = open('results.txt', 'w')
    for player in sorted_list[0:49]:
        #print "\nName: " + str(player[0])
        f.write("\n\nName: " + str(player[0]))
        
        #print "Production: " + str(player[11])
        f.write("\nProduction: " + str(player[11]))
        
        #print ("Hits/AB: " + str(player[3]) + "/" + str(player[2]))
        f.write("\nHits/AB: " + str(player[3]) + "/" + str(player[2]))

        #print ("Strikeouts/AB: " + str(player[10]) + "/" + str(player[2]))
        f.write("\nStrikeouts/AB: " + str(player[10]) + "/" + str(player[2]))
        
        #print "Stolen Risk-Reward: " + str(player[6]) + "/" + str(player[6] + player[7])
        f.write("\nStolen Risk-Reward: " + str(player[6]) + "/" + str(player[6] + player[7]))

    f.close()
