# Importa a biblioteca 'json'.
import json

items = [
    {
        "id": 1,
        "name": "Bagulho",
        "description": "Apenas um bagulho",
        "location": "Em uma caixa"
    }, {
        "id": 2,
        "name": "Tranqueira",
        "description": "Apenas uma tranqueira qualquer",
        "location": "Em um gaveteiro"
    }, {
        "id": 3,
        "name": "Bagulete",
        "description": "Um bagulete qualquer",
        "location": "Na esquina"
    }
]

def get_all():# função que le e lista todos os itens da coleção
    return json.dumps(items, indent=2) # Converte a lista 'items' para json e armazena em 'var_json'

def get_one(id):# função que lê um item especifico, identificado pelo indice.
   
    for item in items: 
        if item.get("id") == id:
            return json.dumps(item, indent=2)
 
# chama (call) a função get_all().   
# print(get_all())


# chama a função get_one(), passando o indice como parâmetro.
print(get_one(1))