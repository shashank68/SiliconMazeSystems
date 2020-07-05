#include<iostream>
using namespace std;

void pf();
string fg1 = "smz{5tr1ng";
int main() {
    puts("Get ready......");
    string pwd = "x1";
    pwd += "y2";
    pwd += "z3";
    string str;
    printf("Enter the password:  ");
    cin >> str;
    if(str == pwd) {
        puts("You got the flag.");
        pf();
    } else {
        puts("Good Luck, Bye");
    }
    return 0;
}
string fg4 = "_0x01}";

void pf() {
    // smz{5tr1ng5_4re_T4ngleD_0x01}
    string fg2 = "5_4re_T4", fg3 = "ngleD";
    cout << fg1;
    cout << fg2;
    cout << fg3;
    cout << fg4 << endl;; 
}