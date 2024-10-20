class myHeap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        # Προσθήκη τιμής στον σωρό και αποκατάσταση της ιδιότητας του σωρού
        self.heap.append(value)
        self._upheap(len(self.heap) - 1)

    def removeMin(self):
        # Αφαίρεση και επιστροφή της μικρότερης τιμής (ρίζα του σωρού)
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        # Ανταλλαγή του πρώτου (μικρότερου) στοιχείου με το τελευταίο και αφαίρεσή του
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Αποκατάσταση της ιδιότητας του σωρού
        self._downheap(0)
        return root

    def _upheap(self, index):
        # Μετακίνηση του στοιχείου στην κατάλληλη θέση προς τα πάνω
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            # Ανταλλαγή αν το παιδί είναι μικρότερο από τον γονέα
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._upheap(parent_index)

    def _downheap(self, index):
        # Μετακίνηση του στοιχείου στην κατάλληλη θέση προς τα κάτω
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            # Ανταλλαγή και συνέχεια της διαδικασίας heapify προς τα κάτω
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._downheap(smallest)

    def heapify(self, arr):
        # Μετατροπή ενός τυχαίου πίνακα σε σωρό
        self.heap = arr[:]
        # Ξεκινάμε το heapify από τον τελευταίο μη-φύλλο κόμβο προς τη ρίζα
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._downheap(i)

    def __str__(self):
        return str(self.heap)


h = myHeap()

h.add(10)
h.add(4)
h.add(15)
h.add(2)
h.add(7)
h.add(1)

print("Σωρός μετά τις προσθήκες:", h)

# Αφαίρεση της μικρότερης τιμής
min_element = h.removeMin()
print("Αφαιρέθηκε το μικρότερο στοιχείο:", min_element)
print("Σωρός μετά την αφαίρεση:", h)

# Αφαίρεση ξανά της μικρότερης τιμής
min_element = h.removeMin()
print("Αφαιρέθηκε το μικρότερο στοιχείο:", min_element)
print("Σωρός μετά την αφαίρεση:", h)

# Δημιουργία ενός πίνακα και μετατροπή του σε σωρό
arr = [20, 15, 30, 40, 50, 10, 5]
h.heapify(arr)
print("Νέος σωρός μετά από heapify πίνακα:", h)
