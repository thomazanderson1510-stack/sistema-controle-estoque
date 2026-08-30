from estoque import produtos

print("RELATÓRIO DE ESTOQUE")
print("-" * 30)

for produto, quantidade in produtos.items():
    print(f"{produto}: {quantidade} unidades")
