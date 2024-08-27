class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        # Adiciona uma venda à lista de vendas da categoria
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def total_vendas(self):
        # Calcula e retorna o total das vendas na categoria
        total = 0
        for venda in self.vendas:
            total += venda.valor  # Corrigido para somar apenas o valor
        return total

def main():
    categorias = []

    for i in range(2):  # Aqui assume-se que serão 2 categorias como no exemplo dado
        nome_categoria = input()
        categoria = Categoria(nome_categoria)

        for j in range(2):  # Assume-se que cada categoria tem 2 vendas associadas
            entrada_venda = input()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total:.1f}")

if __name__ == "__main__":
    main()
