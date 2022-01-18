# Add the necessary import statement in order to make this script
# produce output. Don't change any of the existing code.
# All the necessary variables and functions are
# already defined in the `codingnomads/` folder.




#digestible = i.prepare(i.potato)
#mix = i.carrot + i.potato + i.salt
#soup = s.make_soup(mix)
#print(soup)

import sys
sys.path.append( 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-201-main_jsiu\\python-201-main\\06_advanced-python-concepts\\codingnomads\\recipes')
sys.path.append( 'C:\\Users\\jsiu\\Documents\\codingnomads\\python-201-main_jsiu\\python-201-main\\06_advanced-python-concepts\\codingnomads')
import soup as s

import ingredients as i

digestible = i.prepare(i.potato)
mix = i.carrot + i.potato + i.salt
soup = s.make_soup(mix)
print(soup)
