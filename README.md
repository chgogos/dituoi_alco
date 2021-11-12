# Αλγόριθμοι και πολυπλοκότητα

<!-- 

## 1. Ανάλυση αλγορίθμων -->


## 5. Ουρές προτεραιότητας και σωροί

* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/Heap.html) δημιουργίας σωρού ελαχίστων (MINHEAP) με διαδοχικές εισαγωγές τιμών: π.χ. χρησιμοποιήστε το πλήκτρο **Insert** για τη διαδοχική εισαγωγή των τιμών 21,5,17,12,3,9,16 σε έναν σωρό ελαχίστων
* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/Heap.html) δημιουργίας σωρού ελαχίστων (MINHEAP) με τη διαδικασία heapify: χρησιμοποιήστε το πλήκτρο **BuildHeap** για τη δημιουργία ενός σωρού ελαχίστων από έναν πίνακα 31 τιμών με τους ακέραιους από 1 μέχρι και 31
* [Οπτικοποίηση](http://btv.melezinek.cz/binary-heap.html) λειτουργιών insert, delete, heapsort, buildheap σε σωρό μεγίστων (MAXHEAP) 

**Ουρά προτεραιότητας στην Python**

[heapq](https://docs.python.org/3/library/heapq.html)

Παράδειγμα: [heapq_example.py](./heapq_example.py)

**Ουρά προτεραιότητας στην C++**

[std::priority_queue](https://en.cppreference.com/w/cpp/container/priority_queue)

Παράδειγμα: [priority_queue_example.cpp](./priority_queue_example.cpp)

**Ουρά προτεραιότητας στην Java**

[PriorityQueue\<E\>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html)

Παραδείγματα: [Java PriorityQueue by Programiz](https://www.programiz.com/java-programming/priorityqueue)

**Ασκήσεις**
  
1. Έστω ένας μηχανισμός παραγωγής πραγματικών τιμών. Όταν παράγεται μια νέα τιμή να υπολογίζεται και να εμφανίζεται η διάμεσος από όλες τις τιμές που έχουν παραχθεί μέχρι εκείνη τη χρονική στιγμή. Γράψτε πρόγραμμα που να υλοποιεί τη λύση.
   * Σημείωση 1: η διάμεσος μιας λίστας παρατηρήσεων είναι η τιμή της μεσαίας παρατήρησης στη διατεταγμένη σε αύξουσα σειρά λίστας παρατηρήσεων όταν το πλήθος των παρατηρήσεων είναι περιττό, και το ημιάθροισμα των δύο μεσαίων παρατηρήσεων στη διατεταγμένη σε αύξουσα σειρά λίστας παρατηρήσεων όταν όταν το πλήθος των παρατηρήσεων είναι άρτιο. 
   * Σημείωση 2: Προσομοιώστε την παραγωγή πραγματικών τιμών με μια λίστα  τυχαίων πραγματικών τιμών. Θεωρείστε ότι στη χρονική στιγμή 0 παράγεται η τιμή που βρίσκεται στη θέση 0 της λίστας, στη χρονική στιγμή 1 παράγεται η τιμή που βρίσκεται στη θέση 1 της λίστας κ.ο.κ. 

    <!-- * [heap_exercise2.py](./heap_exercise2.py) -->

## 6. Πίνακες κατακερματισμού

Χάρτες (maps), ή χάρτες κατακερματισμού (hashmaps) ή λεξικά (dictionaries) ή συσχετιστικοί πίνακες (associative arrays) ή συσχετιστικές μνήμες (associative memories) είναι σύνολα από ζεύγη κλειδί/τιμή. 

**Λεξικά στην Python**

[dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), [υλοποίηση των dictionaries στην Python](https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented)

Παράδειγμα: [dictionary_example.py](./dictionary_example.py) 

**Μη διατεταγμένοι χάρτες στην C++**

[unordered_map](https://en.cppreference.com/w/cpp/container/unordered_map)

Παράδειγμα: [unordered_map_example.cpp](./unordered_map_example.cpp)

**Χάρτες κατακερματισμού στην Java**

[HashMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/HashMap.html)


### Συναρτήσεις κατακερματισμού

**Συναρτήσεις κατακερματισμού για δομές δεδομένων**

* [General Purpose Hash Function Algorithms](http://www.partow.net/programming/hashfunctions/index.html#AvailableHashFunctions)
* [djb2, sdbm](http://www.cse.yorku.ca/~oz/hash.html)
<!-- * [FNV](http://www.isthe.com/chongo/tech/comp/fnv/) -->

**Κρυπτογραφικές συναρτήσεις κατακερματισμού**

* [SHA256 Hash by Blockchain Demo](https://andersbrownworth.com/blockchain/hash)
* [SlavaSoft HashCalc](https://www.slavasoft.com/hashcalc/)

**Παραδείγματα με hash functions στην Python**

* [interactive_py_hash.py](./interactive_py_hash.py)
* [interactive_py_hash2.py](./interactive_py_hash2.py) κρυπτογραφικες συναρτήσεις κατακερματσιμού με το module hashlib

### Ανοικτή διευθυνσιοδότηση (open addressing) - κλειστός κατακερματισμός (closed hashing)

* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/ClosedHash.html) ανοικτής διευθυνσιοδότησης

**Παραλλαγές ανοικτής διευθυνσιοδότησης**

* Γραμμική ανίχνευση (linear probing)
* Τετραγωνική ανίχνευση (quadratic probing)
* Διπλός κατακερματισμός (double hashing)
* Τυχαίος κατακερματισμός (random hashing)

### Κλειστή διευθυνσιοδότηση (closed adressing) - ανοικτός κατακερματισμός (open hashing) - ξεχωριστή αλυσίδωση (separate chaining)

* [Οπτικοποίηση](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html) κλειστής διευθυνσιοδότησης


### Κατακερματισμός κούκου

* [Οπτικοποίηση](https://www.lkozma.net/cuckoo_hashing_visualization/) κατακερματισμού κούκου.

**Ασκήσεις**

1. Γράψτε ένα πρόγραμμα που να δέχεται έναν πίνακα ακεραίων και μια τιμή sum και να εμφανίζει όλα τα ζεύγη τιμών του πίνακα με άθροισμα ίσο με την τιμή sum.
    <!-- * [hash_exercise1.py](./hash_exercise1.py) -->
2. Γράψτε ένα πρόγραμμα που να εντοπίζει σε ένα λεξικό με μεγάλο πλήθος λέξεων όλες τις λέξεις για τις οποίες υπάρχουν τουλάχιστον άλλες 4 λέξεις που είναι αναγραμματισμοί της (π.χ. user -> ['rues', 'ruse', 'suer', 'sure', 'user']).
    <!-- * [hash_exercise2.py](./hash_exercise2.py) -->
3. Γράψτε ένα προγραμμα που να εντοπίζει το πλήθος των διακριτών ακεραίων σε μια μεγάλη λίστα ακεραίων.
   <!-- * [hash_exercise3.py](./hash_exercise3.py) -->

## Συνδυαστικές ασκήσεις

1. Δίνεται μια ακολουθία μεγάλου μεγέθους με τυχαίες ακέραιες τιμές. Ζητείται να βρεθούν οι 10 πλέον συχνές τιμές χρησιμοποιώντας μια ουρά προτεραιότητας. Αναζητήστε την αποδοτικότερη λύση. Γράψτε πρόγραμμα που να υλοποιεί τη λύση.
<!-- * [heap_exercise1a.py](./heap_exercise1a.py)
* [heap_exercise1b.py](./heap_exercise1b.py) -->
