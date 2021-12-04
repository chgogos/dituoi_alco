#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    // σταδιακή προσθήκη τιμών στην ουρά προτεραιότητας
    // priority_queue<int, vector<int>, greater<int>> pq; // MINHEAP
    // for (int x : {21, 5, 17, 12, 3, 9, 16})
    // {
    //     pq.push(x);
    // }

    vector<int> vec{21, 5, 17, 12, 3, 9, 16};
    priority_queue<int, std::vector<int>, std::greater<int>> pq(vec.cbegin(), vec.cend()); // heapify

    while (!pq.empty())
    {
        cout << pq.top() << " ";
        pq.pop();
    }
}

// 3 5 9 12 16 17 21 