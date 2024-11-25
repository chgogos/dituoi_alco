import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

class Student {
    String name;
    int grade;

    Student(String name, int grade) {
        this.name = name;
        this.grade = grade;
    }

    @Override
    public String toString() {
        return name + " - " + grade;
    }
}

public class SortingExample2 {
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Alice", 85));
        students.add(new Student("Bob", 92));
        students.add(new Student("Charlie", 78));
        students.add(new Student("David", 90));

        System.out.println("Πριν την ταξινόμηση:");
        for (Student student : students) {
            System.out.println(student);
        }

        // Ταξινόμηση κατά βαθμό (φθίνουσα σειρά)
        students.sort(Comparator.comparingInt((Student s) -> s.grade));
        System.out.println("\nΜετά την ταξινόμηση κατά βαθμό:");
        for (Student student : students) {
            System.out.println(student);
        }

        // Ταξινόμηση κατά όνομα (φθίνουσα αλφαβητική σειρά)
        students.sort(Comparator.comparing((Student s) -> s.name).reversed());
        System.out.println("\nΜετά την ταξινόμηση κατά όνομα (φθίνουσα):");
        for (Student student : students) {
            System.out.println(student);
        }
    }
}
