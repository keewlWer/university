#include <iostream>
#include <ostream>

using namespace std;
string reverseString(const string& str)
{
    if (str.length() <= 1) {
        return str;
    }
    else {
        return reverseString(str.substr(1)) + str[0];
    }
}
int main(){
    string input, reversed;
    cout << "Enter the string to reverse:" << endl;
    cin >> input;
    reversed = reverseString(input);
    cout <<"Reversed string: "<< reversed << endl;
    return 0;
}
