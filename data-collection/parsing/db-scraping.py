from bs4 import BeautifulSoup
import urllib
import json
import re

r = urllib.urlopen('http://www.paulaschoice.com/ingredient-dictionary').read()
soup = BeautifulSoup(r, "html.parser")
ingredientList = soup.findAll("tr", {"class": "ingredient-result"})
dict = {'ingredients' : [] }
regex = re.compile(r'[\r\n\t\t\t\t                \t]')

for ingredient in ingredientList:
    ingredientDict = {'name' : '', 'rating' : '', 'description' : '',
                      'categories' : [], 'link' : '' }

    classListRating = ["col-rating", "ingredient-rating"]
    ingredientDict['name'] = ingredient.find("h2", {"class" : "name ingredient-name"}).text.rstrip()[1:]
    ingredientDict['rating'] = ingredient.find("td", classListRating).text.rstrip()
    ingredientDict['description'] = '' if ingredient.find("p", {"class" : "description ingredient-description"}) is None else ingredient.find("p", {"class" : "description ingredient-description"}).text.rstrip()
    ingredientDict['description'] = '' if len(ingredientDict['description']) == 0 else ingredientDict['description'][23:]
    ingredientDict['link'] = ingredient.find("h2", {"class" : "name ingredient-name"}).find("a")['href']
    catListHTML = ingredient.find("div", {"class" : "categories ingredient-categories"})
    catListHTML = catListHTML.findAll("a")
    catList = []
    for cat in catListHTML:
        s = cat.text.rstrip()
        catList.append(s)
    ingredientDict['categories'] = catList
    dict['ingredients'].append(ingredientDict)


#create json file
with open('paulaschoice.json', 'w') as outfile:
    json.dump(dict, outfile)
