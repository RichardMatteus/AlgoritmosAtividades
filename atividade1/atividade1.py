produtos = ["Coca", "Pepsi", "Sprite"]
preco = [7,5,6]
quantidade = [20,10,15]

def listarProdutos():
    for indice in range(len(produtos)):
        print('Produto: %s' % (produtos[indice]))

def imprimiProduto(produto):
    print('Produto selecionado: %s --- Preco unidade: %s --- Quatidade do estoque: %s' % (produtos[produto-1],preco[produto-1],quantidade[produto-1]))

def deletaProduto(deletar):
    del produtos[deletar-1]
    del preco[deletar-1]
    del quantidade[deletar-1]

produto = input('Digite o produto que deseja imprimir 1 - Coca, 2 - Pepsi ou 3 - Sprite: ')
imprimiProduto(int(produto))

deletar = input('Digite qual produto deseja deletar 1 - Coca, 2 - Pepsi ou 3 - Sprite: ')
deletaProduto(int(deletar))

listarProdutos()

