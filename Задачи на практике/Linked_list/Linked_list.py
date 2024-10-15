class Node:
    """Класс узла односвязного списка."""
    def __init__(self, element, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    """Класс односвязного списка."""
    def __init__(self):
        self.head = None

    def get_len(self):
        """Возвращает длину списка."""
        if not self.head:
            return 0

        count = 1
        current = self.head
        while current.next_node:
            count += 1
            current = current.next_node

        return count

    def __str__(self):
        """Возвращает строковое представление списка."""
        if not self.head:
            return "[]"

        result = "["
        current = self.head
        while current.next_node:
            result += str(current.element) + ", "
            current = current.next_node
        result += str(current.element) + "]"
        return result

    def insert(self, element, index):
        """Вставляет элемент в список по заданному индексу."""
        if index == 0:
            self.head = Node(element, self.head)
            return

        count = 0
        current = self.head
        previous = None
        while count < index:
            previous = current
            current = current.next_node
            count += 1

        new_node = Node(element, current)
        previous.next_node = new_node

    def get(self, index):
        """Возвращает элемент по заданному индексу."""
        if index < 0 or index >= self.get_len():
            raise IndexError("Индекс вне диапазона.")

        count = 0
        current = self.head
        while count < index:
            current = current.next_node
            count += 1
        return current.element

    def pop(self, index):
        if index < 0 or index >= self.get_len():
            raise IndexError("Индекс вне диапазона.")

        if index == 0:
            element = self.head.element
            self.head = self.head.next_node
            return element

        count = 0
        current = self.head
        previous = None
        while count < index:
            previous = current
            current = current.next_node
            count += 1

        element = current.element
        previous.next_node = current.next_node
        return element
      
lst = LinkedList()
lst.append(10)
lst.append(20)
lst.insert(24,2)
lst.append(80)
lst.str()