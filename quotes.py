import json
import random 

f = open('quotes.json')

quotes_dict = json.load(f)
all_the_quotes = list(quotes_dict["quotes_list"])


""" Fetch a random quote array from the data  
    and return it """
def getRandomQuote(quotes_list):
    random_num = random.randint(0, 5)
    quote_obj = quotes_list[random_num]
    return quote_obj 


""" Plug the information from the random quote array into
    the html and return it """
def printQuote():
    # get random quote
    random_quote = getRandomQuote(all_the_quotes)

    return random_quote 


f.close()