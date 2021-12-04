#include <string>
#include <iostream>
#include <cctype>
#include <unordered_map>

using namespace std;

int main()
{
    string text = "Mission of the Department is the provision of education, expertise and high level specialization, as well as the development of scientific and technological research in emerging sectors of (Computer Science/)Informatics and Telecommunications with the aim of creating high-level scientific executives. The two-dimensional approach to IT and Telecommunications objects,allows the creation of highly skilled and attractive professionals in the labor market";
    string ENGLISH_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    std::unordered_map<char, int> a_map;

    for (char &c : ENGLISH_CAPS)
    {
        a_map[c] = 0;
    }

    for (char c : text)
    {
        c = toupper(c);
        if (ENGLISH_CAPS.find(c) == string::npos)
            continue;
        a_map[c] += 1;
    }

    for (char &c : ENGLISH_CAPS)
    {
        cout << "Letter = " << c << " occurences " << a_map[c] << endl;
    }

    return 0;
}


// Letter = A occurences 28
// Letter = B occurences 2
// Letter = C occurences 24
// Letter = D occurences 10
// Letter = E occurences 48
// Letter = F occurences 10
// Letter = G occurences 7
// Letter = H occurences 17
// Letter = I occurences 41
// Letter = J occurences 1
// Letter = K occurences 2
// Letter = L occurences 20
// Letter = M occurences 13
// Letter = N occurences 28
// Letter = O occurences 31
// Letter = P occurences 9
// Letter = Q occurences 0
// Letter = R occurences 16
// Letter = S occurences 25
// Letter = T occurences 35
// Letter = U occurences 5
// Letter = V occurences 6
// Letter = W occurences 4
// Letter = X occurences 2
// Letter = Y occurences 1
// Letter = Z occurences 1