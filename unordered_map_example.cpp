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
