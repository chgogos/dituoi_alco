#include <algorithm>  // Για std::sort
#include <functional>
#include <iostream>
#include <vector>

int main() {
  std::vector<int> arr = {42, 17, 8, 99, 23};

  std::cout << "Πριν την ταξινόμηση:\n";
  for (int num : arr) {
    std::cout << num << " ";
  }
  std::cout << "\n";

  // Ταξινόμηση σε αύξουσα σειρά
  std::sort(arr.begin(), arr.end());

  std::cout << "Μετά την ταξινόμηση (αύξουσα σειρά):\n";
  for (int num : arr) {
    std::cout << num << " ";
  }
  std::cout << "\n";

  // Ταξινόμηση σε φθίνουσα σειρά
  std::sort(arr.begin(), arr.end(), std::greater<int>());

  std::cout << "Μετά την ταξινόμηση (φθίνουσα σειρά):\n";
  for (int num : arr) {
    std::cout << num << " ";
  }
  std::cout << "\n";

  return 0;
}
