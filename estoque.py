produtos = {
    "Notebook": 10,
    "Mouse": 25,
    "Teclado": 15
}


def adicionar_produto(nome, quantidade):
    produtos[nome] = quantidade


print("Produtos disponíveis no estoque:")

for produto, quantidade in produtos.items():
    print(f"{produto}: {quantidade} unidades")


adicionar_produto("Monitor", 8)

print("\nEstoque atualizado:")

for produto, quantidade in produtos.items():
    print(f"{produto}: {quantidade} unidades")
print("Sistema atualizado com sucesso!")
