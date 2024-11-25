import random
import time
import numpy as np

random.seed(42)

def benchmark_sorting():
    data_python = [random.random() for _ in range(10_000_000)]
    # Δημιουργία αντιγράφων δεδομένων με το numpy για να διαφασλιστεί ότι χρησιμοποιούνται όμοια δεδομένα
    data_numpy = np.array(data_python)

    # Χρονομέτρηση της built-in συνάρτησης sorted
    start_time = time.perf_counter()
    sorted_python = sorted(data_python)
    python_time = time.perf_counter() - start_time

    # Χρονομέτρηση της NumPy συνάρτησης sort
    start_time = time.perf_counter()
    sorted_numpy = np.sort(data_numpy)
    numpy_time = time.perf_counter() - start_time

    print(f"Χρόνος της sorted() της Python : {python_time:.4f} sec")
    print(f"Χρόνος της sort του NumPy: {numpy_time:.4f} sec")
    print(f"Η sort() της NumPy ήταν {python_time/numpy_time:.2f}x ταχύτερη")

    # Επιβεβαίωση ότι οι δύο αλγόριθμοι ταξινόμησης δίνουν τα ίδια αποτελέσματα
    python_first_few = sorted_python[:5]
    numpy_first_few = sorted_numpy[:5]
    print("\nΠρώτα 5 στοιχεία για επαλήθευση ταξινόμησης:")
    print(f"Python sort: {python_first_few}")
    print(f"Numpy sort: {numpy_first_few}")


if __name__ == "__main__":
    benchmark_sorting()
