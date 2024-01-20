#Definir Nós 
class TreeNode:
    def __init__(self, value): #self = usado para se referir a instacia da classe atual
        self.value = value
        self.left = self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return TreeNode(value)
        
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)

        return root

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self._remove(root.left, value)
        elif value > root.value:
            root.right = self._remove(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.value = self._min_value(root.right)
            root.right = self._remove(root.right, root.value)

        return root

    def _min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.value

    def pre_order(self):
        return self._pre_order(self.root)

    def _pre_order(self, root):
        if root is None:
            return ""
        return str(root.value) + " " + self._pre_order(root.left) + self._pre_order(root.right)

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, root):
        if root is None:
            return ""
        return self._in_order(root.left) + str(root.value) + " " + self._in_order(root.right)

    def post_order(self):
        return self._post_order(self.root)

    def _post_order(self, root):
        if root is None:
            return ""
        return self._post_order(root.left) + self._post_order(root.right) + str(root.value) + " "

    def position(self, x):
        return self._position(self.root, x, 1)

    def _position(self, root, x, current_position):
        if root is None:
            return -1
        if x < root.value:
            return self._position(root.left, x, current_position)
        elif x > root.value:
            return self._position(root.right, x, current_position + self._count_nodes(root.left) + 1)
        else:
            return current_position + self._count_nodes(root.left)

    def _count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self._count_nodes(root.left) + self._count_nodes(root.right)

    def median(self):
        nodes_count = self._count_nodes(self.root)
        if nodes_count % 2 == 0:
            mid_left = nodes_count // 2
            mid_right = mid_left + 1
            return min(self._kth_smallest(self.root, mid_left), self._kth_smallest(self.root, mid_right))
        else:
            mid = nodes_count // 2 + 1
            return self._kth_smallest(self.root, mid)

    def _kth_smallest(self, root, k):
        count_left = self._count_nodes(root.left)
        if k == count_left + 1:
            return root.value
        elif k <= count_left:
            return self._kth_smallest(root.left, k)
        else:
            return self._kth_smallest(root.right, k - count_left - 1)

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, root, level):
        if root is not None:
            self._print_tree(root.right, level + 1)
            print("  " * level + str(root.value))
            self._print_tree(root.left, level + 1)   
    
def main():
    abb = ABB()

    # Leitura do arquivo de entrada
    with open("entrada.txt", "r") as input_file:
        values = map(int, input_file.readline().split())
        for value in values:
            abb.insert(value)

    # Leitura do arquivo de comandos
    with open("comandos.txt", "r") as command_file:
        for line in command_file:
            command = line.strip()
            if command == "PREORDEM":
                print(abb.pre_order())
            elif command == "EMORDEM":
                print(abb.in_order())
            elif command == "POSORDEM":
                print(abb.post_order())
            elif command == "IMPRIMEARVORE":
                abb.print_tree()
            # Adicione outros casos conforme necessário

if __name__ == "__main__":
    main()
