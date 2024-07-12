/*
  Author: Renet de Jesús Pérez Gómez
  Date: 02-03-24

  Algorithm to implement: Knuth Morris Pratt (KMP)

  This algorithm finds all the occurrences of a pattern in a text.

  Unlike the naive method, on which you need to compare all the possibilities for the pattern, KMP
  use the "degenerating propierty".

  According to geeksforgeeks degenerating propierty means:
  "(pattern having the same sub-patterns appearing more than once in the pattern)"  
*/

#include <iostream>
#include <vector>

using namespace std;

class z_algoirthm {
  private:
    string pattern_text;
  
  public:
    z_algoirthm(string pattern, string text){
      this->pattern_text = pattern + text;
    }

    void find_pattern() {
      int L = 0; // Left side of the box.
      int R = 0; // Right side of the box.
      vector<int> Z = {0}; // Z array.
      int k = 0; // Variable to compare the pattern, the beginning iteration.
      int i_auxiliar = 0; //Auxiliar variable to compare the pattern for the current iteration.
      int counter = 0; // Variable to store the number of matches found.
      int remaining_substring = 0;
      int explicity_comparision = true;

      for(int i = 1; i < this->pattern_text.length(); i++) {
        if(i <= R) {
          if(Z[i - L] < (pattern_text.length() - i)) {
            //Case: Substring known.
            /*
              This substring was already calculated in previous iteration
            */
            counter = Z[i - L];
            explicity_comparision = false;
          } else {
            //Case: Substring known, but is grater than the current substring
            /*
              This subtring exists, but due to the remaining letters in the string,
              it cannot be possible that the following letters (altogether) have
              the same length of the substring.
            */
            explicity_comparision = true;
          }
        } else {
          explicity_comparision = true;
        }

        //Case: explicity comparision.
        /*
          It is compared one by one.
        */
        k = 0;
        i_auxiliar = i;
        counter = 0;
        while((this->pattern_text[i_auxiliar] == this->pattern_text[k]) && explicity_comparision) {
            counter += 1;
            k += 1;
            i_auxiliar += 1;
        }
        
        // Update Z box
        /*
          Z box is going to be updated, when there was found a substring that 
          matched with the pattern.

          Otherwise, there is not needed to be updated
        */
        if(counter > 0){
          L = i;
          R = k; 
        } else { /* Do Nothing */ } 

        Z.push_back(counter);
      }    

      for(const auto &element : Z) {
        cout << element << endl;
      }
    }
};


int main() {
  // string pattern = "aab";
  // string text = "baabaa";
  // string pattern = "ab";
  // string text = "ababab";
  string pattern = "aba";
  string text = "abab";
  z_algoirthm obj(pattern, text);
  obj.find_pattern();
  return 0;
}