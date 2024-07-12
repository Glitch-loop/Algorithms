/*
  Author: Renet de Jesús Pérez Gómez
  Date: 01-30-24

  Algorithm to implement: Knuth Morris Pratt (KMP)

  This algorithm finds all the occurrences of a pattern in a text.

  Unlike the naive method, on which you need to compare all the possibilities for the pattern, KMP
  use the "degenerating propierty".

  According to geeksforgeeks degenerating propierty means:
  "(pattern having the same sub-patterns appearing more than once in the pattern)"  
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std; 

class KMP {
    private:
    vector<string> pat;
    vector<int> lps;
    vector<string> text;

    void computeLPSArray() {
      int len = 0;
      
      for(int i = 0; i < this->pat.size(); i++) {
        if(i == 0) {
          // lps[0] always is 0.
          lps.push_back(0);
        } else if(pat[len] == pat[i]) {
          /*
            Both characters are equal.
            
            Explanation:
              Pattern having the same sub-patterns appearing more than once in a pattern
          */
          len += 1;
          lps.push_back(len); 
        } else {
          /*
            It is needed to find another charater that match with the current character,
            this looking in previous values in the array.

            There is 2 cases: There is not a match then len = 0 or there is a match; therefore 0 = n 
          */
          bool findMatch = true;
          while(findMatch) {
            if(pat[len] == pat[i]) {
              len += 1;
              findMatch = false;              
            } else {
              len -= 1;
              if(len > 0) {
                /* Do Nothing */
              } else {
                len = 0;
                findMatch = false;
              }
            }
          }
          lps.push_back(len);
        }
      }
    }

  public:
    KMP(string& pattern, string& text) {      
      for(const auto &element : pattern) {
        this->pat.push_back(string(1, element));
      }

      for(const auto &element : text) {
        this->text.push_back(string(1, element));
      }
    } 

    void solvePattern() {
      int i = 0;
      int j = 0;
      int textLength = this->text.size();
      int pathLenght = this->pat.size();

      this->computeLPSArray();

      // Find pattern in text
      while(i < textLength) {
        if(this->text[i] == this->pat[j]) {
          /*
            It was found a coincidence between the current character in both the pattern 
            and in the text, so we move forward in the iteration.
          */
          i += 1;
          j += 1;
        } else {
          if(j > 0) {
            /*
              That means that the current position is not a prefix for the next coincidence, but it might be
              the previous prefix in lps vector.
            */
            j = lps[j - 1];
          } else {
            /*
              That means that it was not found any match for the current character and there is not a
              useful prefix in lps. 
            */
            i += 1;
          }
        }

        if(j == pathLenght) {
          /*
            It was found a match for the whole pattern.
            
            As it was a match for the entire pattern, j needs to be reset,
            in the new assignation it is only substracted 1, because the current
            suffix can be the prefix of the next pattern.
          */
          cout << "Pattern  found at index: " <<  i - pathLenght << endl;
          
          j = lps[j - 1]; 
        } 
      }
    }
};

int main(){

  // string text = "ABABDABACDABABCABAB";
  // string pattern = "ABABCABAB";

  string text = "AAAAABAAABA";
  string pattern = "AAAA";
  KMP instance(pattern, text);
  instance.solvePattern();
  return 0;
}