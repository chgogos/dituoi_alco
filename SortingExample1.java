import java.util.Arrays;
import java.util.Collections;

public class SortingExample1 {
    public static void main(String[] args) {
        Integer[] arr = {42, 17, 8, 99, 23};

        System.out.println("Πριν την ταξινόμηση:");
        System.out.println(Arrays.toString(arr));

        // Ταξινόμηση σε αύξουσα σειρά
        Arrays.sort(arr);
        System.out.println("Μετά την ταξινόμηση (αύξουσα σειρά):");
        System.out.println(Arrays.toString(arr));

        // Ταξινόμηση σε φθίνουσα σειρά
        Arrays.sort(arr, Collections.reverseOrder());
        System.out.println("Μετά την ταξινόμηση (φθίνουσα σειρά):");
        System.out.println(Arrays.toString(arr));
    }
}
