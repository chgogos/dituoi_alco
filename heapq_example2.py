'''Εύρεση N μεγαλύτερων ή Ν μικρότερων τιμών με το heapq  module'''
import heapq

vathmoi = [7.2, 3.1, 6.7, 4.1, 9.9, 1.0, 2.0, 5.0, 8.0, 9.1]

three_largest = heapq.nlargest(3, vathmoi)
print(three_largest)

three_smallest = heapq.nsmallest(3, vathmoi)
print(three_smallest)

# [9.9, 9.1, 8.0]
# [1.0, 2.0, 3.1]