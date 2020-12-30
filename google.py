import requests
import webbrowser

search = 'vietnam'
queryString = {'q': search}
searchEngine = 'https://www.google.com/search'
result = requests.get(searchEngine, params=queryString)

print(result.url)
webbrowser.open(result.url)
