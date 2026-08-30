produtos = {
    "Notebook": 10,
    "Mouse": 25,
    "Teclado": 15
}

print("Produtos disponíveis no estoque:")

for produto, quantidade in produtos.items():
    print(f"{produto}: {quantidade} unidades")
