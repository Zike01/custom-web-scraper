from steambot import SteamBot
import pandas as pd

bot = SteamBot()
bot.get_website()

# COLUMNS

names_list = bot.get_names()
positive_entries = bot.get_positive()
negative_entries = bot.get_negative()
ratings = bot.get_ratings()
percentage_positive = bot.get_positive_percentage()


steam_data = {
    "Name": names_list,
    "Positive": positive_entries,
    "Negative": negative_entries,
    "Rating": ratings,
    "Positive(%)": percentage_positive,
}

steam_df = pd.DataFrame(steam_data)
steam_df.to_csv('top_rated_games.csv', index=False)
