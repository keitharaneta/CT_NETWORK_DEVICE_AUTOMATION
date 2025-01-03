from itertools import islice

data1 = {
  "All": {
    "label_es_ES": "Todo",
    "label_it_IT": "Tutto",
    "label_en_EN": "All", 
    "label_fr_FR": "Tout"
  },
  "Searchprofile": {
    "label_es_ES": "Perfil de búsqueda",
    "label_it_IT": "Profilo di ricerca",
    "label_en_EN": "Search profile", 
    "label_fr_FR": "Profil de recherche"
  }
}


def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

     
for item in chunks({i:i for i in range(10)}, 3):
    print(item)
    
    
chunks(data1)