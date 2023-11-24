#include <iostream>
using namespace std;

int main() {
    
    int guessNum, secterNum;
    string low, high, equal;
    low = false;
    high = false;
    equal = false;
    
    cin >> secterNum;
    srand ( time(NULL) );
    guessNum = rand() % 10 + 1;
    
    cout << guessNum;
    
    if(guessNum > secterNum){
       high = true;
       cout << "your number is high";
    } else if(guessNum < secterNum){
        low = true;
        cout << "you number if is low";
    } else {
        equal = true;
        cout << "congratulation";
    }
    
    return 0;
}