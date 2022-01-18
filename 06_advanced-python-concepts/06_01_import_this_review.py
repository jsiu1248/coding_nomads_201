# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.

import sys
sys.path.append( 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-201-main_jsiu\\python-201-main\\06_advanced-python-concepts\\codingnomads\\recipes')
sys.path.append( 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-201-main_jsiu\\python-201-main\\06_advanced-python-concepts\\codingnomads')
import soup

import ingredients
made_soup = soup.make_soup(ingredients.potato)

print(dir(soup))
print(dir(ingredients))

print(soup)
print(made_soup)