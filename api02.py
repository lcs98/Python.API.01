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
# função que le e lista todos os itens da coleção
def get_all():
    
    # Converte a lista 'items' para json e armazena em 'var_json'
    return json.dumps(items, indent=2)

# função que lê um item especifico, identificado pelo indice. 
def get_one(id):
    
    # Converte o dicionario "itens[id]" para json e armazena em "var_json"
    var_json = json.dumps(items[id], indent=2)
    
    # imprime o json.
    print(var_json)
 
# chama (call) a função get_all().   
print(get_all())


# chama a função get_one(), passando o indice como parâmetro.
print(get_one(1))