# import requests
url = str(input("> ")) #api du skriver in i terminalen kallas url

# def lamao(url):
#     r = requests.lamao(url)
#     response_dictionary = r.json()
#     print(response_dictionary)

from lol import lamao # från lol så importerar vi lamao
lamao(url) # och så anropar vi funktionen lamao och kastar in url en