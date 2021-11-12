import requests as req

api_url = "https://swapi.dev/api"

data = req.get(api_url+"/planets").json()

unq = set()
for i in data['results']:
    if (i['climate']=="arid"):
        for j in i['films']:
            unq.add(j)

print("a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?")
print(len(unq))



data = req.get(api_url+"/species").json()
movie = req.get(api_url+"/films/").json()

per = []
for i in movie['results']:
    if (i['episode_id']==6):
        for j in i['characters']:
            per.append(j)

count = 0
for i in data['results']:
    if (i['name']=="Wookie"):
        for j in i['people']:
            if j in per:
                count +=1


print("b) ¿Cuántos Wookies aparecen en la sexta película?")
print(count)


nave = req.get(api_url+"/starships").json()

sz = {}
for i in nave['results']:
    sz[i['name']] = float(i['length'].replace(",",''))


print("c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?")
print(max(sz, key=sz.get))
