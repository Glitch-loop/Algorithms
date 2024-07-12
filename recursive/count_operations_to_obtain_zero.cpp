#include <iostream>

using namespace std;

class Solution {
public:
    int countOperations(int num1, int num2) {
        if(num1 == 0 || num2 == 0) {
            return 0;
        } 

        if(num1 >= num2) {
            num1 = num1 - num2;
        } else {
            num2 = num2 - num1;
        }
        
        return countOperations(num1, num2) + 1;
    }
};


int main() { 
  Solution s;

  cout << s.countOperations(3, 1) << endl;

  return 0;
}