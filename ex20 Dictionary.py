person = {
    "name": "Alice",
    "age": 25,
    "ocupation": "Engineer",
    "earnings": 5500
} # it is a simple dictionay

print(person)
print(person["name"])
print(person["age"])
print("Changing the age...")
person["age"] = 29
print(person["age"])
# adding a new key
person["city"] = "Campina Grande"
print(person)
# removing a key
del person["ocupation"]
print(person)

for key in person: # key iteraction
    print(key)

for key, value in person.items(): # key and values iteractions
    print(f"{key}: {value}")

for value in person.values (): # values iteractions
    print(value)

idade = person.get("idade", "Dado não disponível")
pais = person.get("pais", "Brasil")  # Retorna "Brasil" se "pais" não existir

estoque = {
 "notebook": {"preco": 3500.00, "quantidade": 5},
 "mouse": {"preco": 50.00, "quantidade": 25},
 "teclado": {"preco": 150.00, "quantidade": 12}
}

# Acessando informações aninhadas
preco_notebook = estoque["notebook"]["preco"]

# Atualizando quantidade
estoque["mouse"]["quantidade"] -= 1