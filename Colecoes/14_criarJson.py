import json

# Criando um arquivo json
computador_json = """{
  "marca": "Dell",
  "preco": 2000
}"""

# Convertendo a string json para um dicionário
computador = json.loads(computador_json)
print(computador['marca'])

with open('computador.json', 'w', encoding='utf-8') as f:
    json.dump(computador, f, ensure_ascii=False, indent=4)

