def merge_sort(arr):
    """
    Υλοποίηση του αλγορίθμου merge sort.
    Args:
        arr: λίστα προς ταξινόμηση
    Returns:
        Ταξινομημένη λίστα
    """
    # Βασική περίπτωση: λίστα μήκους 0 ή 1
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Αναδρομική κλήση των δύο μισών
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Συγχώνευση των ταξινομημένων μισών
    return merge(left, right)

def merge(left, right):
    """Βοηθητική συνάρτηση για συγχώνευση δύο ταξινομημένων λιστών"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Προσθήκη όσων στοιχείων δεν προστέθηκαν με τον παραπάνω βρόχο
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quicksort(arr):
    """
    Υλοποίηση της quicksort που χρησιμοποιεί το αριστερότερο κάθε φορά στοιχείο ως pivot.
    Args:
        arr: λίστα προς ταξινόμηση
    Returns:
        Ταξινομημένη λίστα
    """
    def partition(low, high):
        """Βοηθητική συνάρτηση για διαμερισμό του πίνακα"""
        pivot = arr[low]  # Επιλογή του αριστερότερου στοιχείου ως pivot
        i = low + 1
        
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        # Τοποθέτηση του pivot στην τελική του θέση
        pivot_pos = i - 1
        arr[low], arr[pivot_pos] = arr[pivot_pos], arr[low]
        return pivot_pos
    
    def quick_sort_helper(low, high):
        """Βοηθητική συνάρτηση για την quicksort"""
        if low < high:
            # Διαμερισμός πίνακα και λήψη της θέσης του pivot
            pivot_pos = partition(low, high)
            
            # Αναδρομική ταξινόμηση στοιχείων πριν και μετά του pivot
            quick_sort_helper(low, pivot_pos - 1)
            quick_sort_helper(pivot_pos + 1, high)
    
    quick_sort_helper(0, len(arr) - 1)
    return arr


# Παράδειγμα χρήσης
arr = [64, 34, 25, 12, 22, 11, 90]
print("ΑΡΧΙΚΗ ΛΙΣΤΑ ΤΙΜΩΝ: ", arr)
sorted_arr = merge_sort(arr)
print("Merge-Sort : ", sorted_arr)

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_quick = quicksort(arr)
print("Quick-Sort : ", sorted_arr)
