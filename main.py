import pandas as pd
df = pd.read_csv (r'/Users/juanmarin/IronHack/pipeline-proj/data/ordered.csv')

def query_identifier(query_word_list):
    #Will get a string of a query and will decide what type of query user wants
    #wether stat leaders or player specific stats, and then call corresponding function
    if query_word_list[0] == "stat":
        query_word_list.pop(0)
        retrieve_stats(query_word_list)
    elif query_word_list[0] == "player":
        query_word_list.pop(0)
        retrieve_player_stats(query_word_list)


def retrieve_player_stats(query_word_list):
    #return the corresponding dataframe row for the wanted player
    playername = query_word_list[0] + " " + query_word_list[-1]
    print(playername)
    try:
        print(df[df['name'] == playername])
    except:
        print("Sorry I couldnt find a player with that name, please try with a different query")


def retrieve_stats(query_word_list):
    #will break down input array into desired order, stat and number of players
    #then return corresponding rows from dataframe
    order = query_word_list[0] == "worst"
    number_of_stats = int(query_word_list[1])
    stat = query_word_list[2]
    print(order, number_of_stats, stat)

    try:
        print(df.sort_values(by=[f"{stat}"], ascending = order).head(number_of_stats))
        return df.sort_values(by=[f"{stat}"], ascending = order).head(number_of_stats)##order by stat (cant put quote marks)
    except:
        print("Sorry couldnt find a result for your query, please try again")







#Introduce program
print("Welcome to the stat query program!")
print("You can either query a player by their full name by indicating the keyword 'player' (eg:player LeBron James) or look for the n leaders for any stat by indicating the word 'stat' (eg:stat top 5 Points)")
#Get first query
query = str(input("Please enter your first query: "))
query_list = query.split(" ")
query_identifier(query_list)
#check if they still want to query dataset
want_more_query = str(input("Would you like to query more? (y/n): "))

#Get more querys and run functions with new queries
while want_more_query == "y":
    query = str(input("Please enter your new query: "))
    query_list = query.split(" ")
    query_identifier(query_list)
    want_more_query = str(input("Would you like to query more? (y/n): "))

#goodbye message
if want_more_query == "n":
    print("Hope you enjoyed using this program.\nBye!")






    
    
