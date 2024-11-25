#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Student {
  std::string name;
  int grade;
};

// Συνάρτηση για εμφάνιση της λίστας μαθητών
void print_students(const std::vector<Student>& students) {
  for (const auto& student : students) {
    std::cout << student.name << " - " << student.grade << "\n";
  }
}

int main() {
  std::vector<Student> students = {
      {"Alice", 85}, {"Bob", 92}, {"Charlie", 78}, {"David", 90}};

  std::cout << "Πριν την ταξινόμηση:\n";
  print_students(students);

  // Ταξινόμηση κατά βαθμό (φθίνουσα σειρά)
  std::sort(
      students.begin(), students.end(),
      [](const Student& a, const Student& b) { return a.grade < b.grade; });

  std::cout << "\nΜετά την ταξινόμηση κατά βαθμό:\n";
  print_students(students);

  // Ταξινόμηση κατά όνομα (αλφαβητικά σε φθίνουσα σειρά)
  std::sort(students.begin(), students.end(),
            [](const Student& a, const Student& b) { return a.name > b.name; });

  std::cout << "\nΜετά την ταξινόμηση κατά όνομα (αλφαβητικά σε φθίνουσα σειρά):\n";
  print_students(students);

  return 0;
}
