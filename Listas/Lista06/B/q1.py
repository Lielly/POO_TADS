import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def get_id(self):
        return self.__id
    def set_id(self, x):
        if x >= 0: self.__id = x
        else: raise ValueError("Valor não pode ser negativo")

    def get_nome(self):
        return self.__nome
    def set_nome(self, x):
        if len(x) > 0:
            self.__nome = x
        else: raise ValueError("Valor inválido")

    def get_email(self):
        return self.__email
    def set_email(self, x):
        if len(x) > 0:
            self.__email = x
        else: raise ValueError("Valor inválido")

    def get_fone(self):
        return self.__fone
    def set_fone(self, x):
        if len(x) > 0:
            self.__fone = x
        else: raise ValueError("Valor inválido")

    def __str__(self):
        return f"CLIENTE- ID: {self.__id}; NOME: {self.__nome}; EMAIL: {self.__email}; FONE: {self.__fone}"

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def get_id(self):
        return self.__id
    def set_id(self, x):
        if x >= 0: self.__id = x
        else: raise ValueError("Valor não pode ser negativo")
    
    def get_descricao(self):
        return self.__descricao
    def set_descricao(self, x):
        if len(x) > 0:
            self.__descricao = x
        else: raise ValueError("Valor inválido")
    
    def __str__(self):
        return f"CATEGORIA- ID: {self.__id}; DESCRIÇÃO: {self.__descricao};"

class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)

    def get_id(self):
        return self.__id
    def set_id(self, x):
        if x >= 0:
            self.__id = x
        else: raise ValueError("Valor não pode ser negativo")

    def get_descricao(self):
        return self.__descricao
    def set_descricao(self, x):
        if len(x) > 0:
            self.__descricao = x
        else: raise ValueError("Valor inválido")
    
    def get_preco(self):
        return self.__preco
    def set_preco(self, x):
        if x >= 0.0:
            self.__preco = x
        else: raise ValueError("Valor não pode ser negativo")
    
    def get_estoque(self):
        return self.__estoque
    def set_estoque(self, x):
        if x >= 0:
            self.__estoque = x
        else: raise ValueError("Valor não pode ser negativo")
    
    def get_idCategoria(self):
        return self.__idCategoria
    def set_idCategoria(self, x):
        if x >= 0:
            self.__idCategoria = x
        else: raise ValueError("Valor não pode ser negativo")
    
    def __str__(self):
        return f"PRODUTO- ID: {self.__id}; DESCRIÇÃO: {self.__descricao}; PREÇO: R${self.__preco:.2f}; ESTOQUE: {self.__estoque}; ID-CATEGORIA: {self.__idCategoria};"

class Venda:
    def __init__(self, id, data, carrinho, total, idCliente):
        self.set_id(id)
        self.__data = data
        self.__carrinho = carrinho
        self.__total = total
        '''
        self.set_data(data)
        self.set_carrinho(carrinho)
        self.set_total(total)
        '''
        self.__idCliente = idCliente

    def get_id(self):
        return self.__id
    def set_id(self, x):
        if x >= 0:
            self.__id = x
        else: raise ValueError("Valor não pode ser negativo")

    def __str__(self):
        return f"VENDA- ID: {self.__id}; DATA: {self.__data}; CARRINHO: {self.__carrinho}; TOTAL: {self.__total}; ID-CLIENTE:{self.__idCliente};"

class VendaItem:
    def __init__(self, id, qtd, preco, idVenda, idProduto):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_idVenda(idVenda)
        self.set_idProduto(idProduto)

    def get_id(self):
        return self.__id
    def set_id(self, x):
        if x >= 0:
            self.__id = x
        else: raise ValueError("Valor não pode ser negativo")

    def get_qtd(self):
        return self.__qtd
    def set_qtd(self, x):
        if x >= 0:
            self.__qtd = x
        else: raise ValueError("Valor não pode ser negativo")

    def get_preco(self):
        return self.__preco
    def set_preco(self, x):
        if x >= 0.0:
            self.__preco = x
        else: raise ValueError("Valor não pode ser negativo")

    def get_idVenda(self):
        return self.__idVenda
    def set_idVenda(self, x):
        if x >= 0:
            self.__idVenda = x
        else: raise ValueError("Valor não pode ser negativo")
    
    def get_idProduto(self):
        return self.__idProduto
    def set_idProduto(self, x):
        if x >= 0:
            self.__idProduto = x
        else: raise ValueError("Valor não pode ser negativo")

    def __str__(self):
        return f"VENDAITEM- ID: {self.__id}; QUANTIDADE: {self.__qtd}; PREÇO: {self.__preco}; ID-VENDA: {self.__idVenda}; ID-PRODUTO: {self.__idProduto};"

class ClienteDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.get_nome())
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, id):
        x = self.listar_id(id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self):
        self.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                clientes_json = json.load(arquivo)
                for obj in clientes_json:
                    c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"], obj["_Cliente__email"], obj["_Cliente__fone"])
                    self.objetos.append(c)
        except FileNotFoundError:
            self.objetos = []

class CategoriaDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.get_descricao())
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, id):
        x = self.listar_id(id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self):
        self.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                categorias_json = json.load(arquivo)
                for obj in categorias_json:
                    c = Categoria(obj["_Categoria__id"], obj["_Categoria__descricao"])
                    self.objetos.append(c)
        except FileNotFoundError:
            self.objetos = []
    
class ProdutoDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.get_descricao())
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, id):
        x = self.listar_id(id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self):
        self.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                produtos_json = json.load(arquivo)
                for obj in produtos_json:
                    p = Produto(obj["_Produto__id"], obj["_Produto__descricao"], obj["_Produto__preco"], obj["_Produto__estoque"], obj["_Produto__idCategoria"])
                    self.objetos.append(p)
        except FileNotFoundError:
            self.objetos = []

class VendaDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.get_id())
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, id):
        x = self.listar_id(id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self):
        self.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                vendas_json = json.load(arquivo)
                for obj in vendas_json:
                    v = Venda(obj["_Venda__id"], obj["_Venda__data"], obj["_Venda__carrinho"], obj["_Venda__total"])
                    self.objetos.append(v)
        except FileNotFoundError:
            self.objetos = []

class VendaItemDAO:
    def __init__(self):
        self.objetos = []

    def inserir(self, obj):
        self.abrir()
        if len(self.objetos) == 0: 
            id = 1
        else: id = (max(self.objetos, key = lambda x : x.get_id())).get_id() + 1
        obj.set_id(id)
        self.objetos.append(obj)
        self.salvar()

    def listar(self):
        self.abrir()
        self.objetos.sort(key = lambda x : x.get_id())
        return self.objetos

    def listar_id(self, id):
        self.abrir()
        for obj in self.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.get_id())
        if x != None:
            self.objetos.remove(x)
            self.objetos.append(obj)
            self.salvar()

    def excluir(self, id):
        x = self.listar_id(id)
        if x != None:
            self.objetos.remove(x)
            self.salvar()

    def salvar(self):
        with open("vendas_itens.json", mode="w") as arquivo:
            json.dump(self.objetos, arquivo, default = vars)

    def abrir(self):
        self.objetos = []
        try:
            with open("vendas_itens.json", mode="r") as arquivo:
                vendas_itens_json = json.load(arquivo)
                for obj in vendas_itens_json:
                    vi = VendaItem(obj["_VendaItem__id"], obj["_VendaItem__qtd"], obj["_VendaItem__preco"])
                    self.objetos.append(vi)
        except FileNotFoundError:
            self.objetos = []

class UI:
    @staticmethod
    def main(): 
        ce = 0
        while ce != 9:
            ce = UI.menu_principal()
            if ce == 1:
                ocl = 0
                while ocl != 9:
                    ocl = UI.menu_cliente()
                    if ocl == 1: UI.cliente_inserir()
                    if ocl == 2: UI.cliente_listar()
                    if ocl == 3: UI.cliente_atualizar()
                    if ocl == 4: UI.cliente_excluir()
            
            if ce == 2:
                oca = 0
                while oca != 9:
                    oca = UI.menu_categoria()
                    if oca == 1: UI.categoria_inserir()
                    if oca == 2: UI.categoria_listar()
                    if oca == 3: UI.categoria_atualizar()
                    if oca == 4: UI.categoria_excluir()

            if ce == 3:
                opr = 0
                while opr != 9:
                    opr = UI.menu_produto()
                    if opr == 1: UI.produto_inserir()
                    if opr == 2: UI.produto_listar()
                    if opr == 3: UI.produto_atualizar()
                    if opr == 4: UI.produto_excluir()

    @staticmethod
    def menu_principal():
        print("Informe qual CRUD você quer acessar:")
        print("1- CRUD Cliente\n2- CRUD Categoria\n3- CRUD Produto\n9- Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def menu_cliente():
        print("\nCRUD Cliente")
        print("1- Inserir Cliente\n2- Listar Cliente\n3- Atualizar Cliente\n4- Excluir Cliente\n9- Voltar para o menu principal")
        return int(input("Informe uma opção: "))

    @staticmethod
    def menu_categoria():
        print("\nCRUD Categoria")
        print("1- Inserir Categoria\n2- Listar Categoria\n3- Atualizar Categoria\n4- Excluir Categoria\n9- Voltar para o menu principal")
        return int(input("Informe uma opção: "))

    @staticmethod
    def menu_produto():
        print("\nCRUD Produto")
        print("1- Inserir Produto\n2- Listar Produto\n3- Atualizar Produto\n4- Excluir Produto\n9- Voltar para o menu principal")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        print("\nCadastro de Cliente")
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        cl = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(cl)

    @staticmethod
    def categoria_inserir():
        print("\nCadastro de Categoria")
        #id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        ca = Categoria(0, descricao)
        CategoriaDAO().inserir(ca)

    @staticmethod
    def produto_inserir():
        print("\nCadastro de Produto")
        #id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço: R$"))
        estoque = int(input("Informe a quantidade em estoque: "))
        pr = Produto(0, descricao, preco, estoque, 0)
        ProdutoDAO().inserir(pr)

    @staticmethod
    def cliente_listar():
        print("Listagem de Clientes")
        for cl in ClienteDAO().listar(): print(cl)

    @staticmethod
    def categoria_listar():
        print("Listagem de Categorias")
        for ca in CategoriaDAO().listar(): print(ca)

    @staticmethod
    def produto_listar():
        print("Listagem de Produtos")
        for pr in ProdutoDAO().listar(): print(pr)
    
    @staticmethod
    def cliente_atualizar():
        print("Atualização de Cliente\n")
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        cl = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(cl)

    @staticmethod
    def categoria_atualizar():
        print("Atualização de Categoria\n")
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser atualizada: "))
        descricao = input("Informe a nova descrição: ")
        ca = Categoria(id, descricao)
        CategoriaDAO().atualizar(ca)

    @staticmethod
    def produto_atualizar():
        print("Atualização de Produto\n")
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: R$"))
        estoque = int(input("Informe a nova quantidade em estoque: "))
        pr = Produto(id, descricao, preco, estoque, 0)
        ProdutoDAO().atualizar(pr)
    
    @staticmethod
    def cliente_excluir():
        print("Exclusão de Cliente\n")
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        #cl = Cliente(id, "", "", "")
        ClienteDAO().excluir(id)
    
    @staticmethod
    def categoria_excluir():
        print("Exclusão de Categoria\n")
        UI.categoria_listar()
        id = int(input("Informe o id da categoria a ser excluído: "))
        CategoriaDAO().excluir(id)
 
    @staticmethod
    def produto_excluir():
        print("Exclusão de Produto\n")
        UI.produto_listar()
        id = int(input("Informe o id do produto a ser excluído: "))
        ProdutoDAO().excluir(id)    

UI.main()
