# Classe Node, que representa um nó da árvore AVL
class Node:
    def __init__(self, key):
        self.key = key  # Valor armazenado no nó
        self.left = None  # Referência ao nó filho a esquerda
        self.right = None  # Referência ao nó filho a direita
        self.height = 1  # Altura do nó na árvore

# Classe AVLTree, que implementa uma árvore AVL
class AVLTree:
    # Método para inserir um novo nó na árvore
    def insert(self, root, key):
        # Se a raiz é None, cria um novo nó com a chave fornecida
        if not root:
            return Node(key)
        # Se a chave é menor que a chave do nó atual, insere a esquerda
        elif key < root.key:
            root.left = self.insert(root.left, key)
        # Se a chave é maior ou igual a chave do nó atual, insere a direita
        else:
            root.right = self.insert(root.right, key)
        
        # Atualiza a altura do nó atual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Obtém o fator de balanceamento do nó atual
        balance = self.get_balance(root)
        
        # Se o nó está desbalanceado, aplica rotações para balancear
        # Caso 1: Rotação a direita
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Caso 2: Rotação a esquerda
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Caso 3: Rotação dupla (esquerda-direita)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Caso 4: Rotação dupla (direita-esquerda)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        # Retorna o nó (potencialmente modificado)
        return root
    
    # Método para remover um nó da árvore
    def remove(self, root, key):
        # Se a raiz é None, retorna None
        if not root:
            return root
        
        # Procura a chave a ser removida
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            # Nó encontrado, trata os casos de remoção
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = None
                return temp
            # Caso em que o nó tem dois filhos
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.remove(root.right, temp.key)
        
        # Se a árvore tinha apenas um nó, retorna None
        if not root:
            return root
        
        # Atualiza a altura do nó atual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Obtém o fator de balanceamento do nó atual
        balance = self.get_balance(root)
        
        # Se o nó está desbalanceado, aplica rotações para balancear
        # Caso 1: Rotação a direita
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        # Caso 2: Rotação a esquerda
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        
        # Caso 3: Rotação dupla (esquerda-direita)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Caso 4: Rotação dupla (direita-esquerda)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        # Retorna o nó (potencialmente modificado)
        return root
    
    # Método auxiliar para encontrar o nó com o valor mínimo
    def get_min_value_node(self, root):
        current = root
        # Itera para a esquerda até encontrar o nó mais a esquerda
        while current.left:
            current = current.left
        return current
    
    # Método para realizar uma rotação a esquerda
    def left_rotate(self, z):
        y = z.right  # y é o filho a direita de z
        T2 = y.left  # T2 é a subárvore a esquerda de y
        
        # Realiza a rotação
        y.left = z
        z.right = T2
        
        # Atualiza as alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        # Retorna a nova raiz
        return y
    
    # Método para realizar uma rotação a direita
    def right_rotate(self, z):
        y = z.left  # y é o filho a esquerda de z
        T3 = y.right  # T3 é a subárvore a direita de y
        
        # Realiza a rotação
        y.right = z
        z.left = T3
        
        # Atualiza as alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        # Retorna a nova raiz
        return y
    
    # Método para obter a altura de um nó
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    # Método para obter o fator de balanceamento de um nó
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    # Método para percorrer a árvore em pré-ordem
    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    # Método para percorrer a árvore em ordem de nível (BFS)
    def level_order(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.key, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    
    # Método para imprimir a árvore de forma estruturada
    def print_tree(self, root, level=0, prefix="Raiz: "):
        if not root:
            print(" " * (level * 4) + prefix + "None")
            return
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:
                self.print_tree(root.left, level + 1, "E--- ")
            else:
                print(" " * ((level + 1) * 4) + "E--- None")
            if root.right:
                self.print_tree(root.right, level + 1, "D--- ")
            else:
                print(" " * ((level + 1) * 4) + "D--- None")

# Ler nomes do arquivo e retornar uma lista de nomes
def read_names_from_file(filename):
    with open(filename, 'r') as file:
        names = file.read().split()
    return names

# Exibir o menu
def display_menu():
    print("Menu:")
    print("1. Adicionar nome")
    print("2. Remover nome")
    print("3. Mostrar árvore")
    print("4. Sair")


avl = AVLTree()  # Cria uma árvore 
root = None  
#Leitura do arquivo entrada.txt
names = read_names_from_file('entrada.txt')
# Preenchendo arvores
for name in names:
    print(f"Inserindo {name} na árvore AVL:")
    avl.print_tree(root)  # Exibe a árvore antes da inserção
    print()
    root = avl.insert(root, name)  # Insere o nome na árvore
    print(f"Árvore após inserir {name}:")
    avl.print_tree(root)  # Exibe a árvore após a inserção
    print("\n")
# Menu e printar arvore
while True:
    display_menu()  # Exibe o menu de opções
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        name_to_add = input("Digite o nome a ser adicionado: ")
        print(f"Inserindo {name_to_add} na árvore AVL:")
        avl.print_tree(root)  # Exibe a árvore antes da inserção
        print()
        root = avl.insert(root, name_to_add)  # Insere o nome na árvore
        print(f"Árvore após inserir {name_to_add}:")
        avl.print_tree(root)  # Exibe a árvore após a inserção
        print("\n")
    elif escolha == '2':
        name_to_remove = input("Digite o nome a ser removido: ")
        print(f"Removendo {name_to_remove} da árvore AVL:")
        avl.print_tree(root)  # Exibe a árvore antes da remoção
        print()
        root = avl.remove(root, name_to_remove)  # Remove o nome da árvore
        print(f"Árvore após remover {name_to_remove}:")
        avl.print_tree(root)  # Exibe a árvore após a remoção
        print("\n")
    elif escolha == '3':
        print("Árvore AVL:")
        avl.print_tree(root)  # Exibe a árvore
        print()
    elif escolha == '4':
        break  # Sai do loop e termina o programa