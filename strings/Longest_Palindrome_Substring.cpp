#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Longest_Palindrome_Substring {
  private:
    int N;
    string str; 
    int **matrix;

    void initializeMatrix(int length) {
      /* It is needed a matrix N * N, where N is the length of the subtring*/
      
      // Dynamically allocate mmory for the matrix
      this->matrix = new int*[length];
      for (int i = 0; i <= length; ++i) {
        this->matrix[i] = new int[length];
      }

      // Initialize and access elements in the matrix
      for(int i = 0; i < length; ++i) {
        for(int j = 0; j < length; ++j) {
          this->matrix[i][j] = 0;
        }
      }
    }

  public:
    Longest_Palindrome_Substring(string text) {
      this->str = text;
      this->N = text.size();
      initializeMatrix(this->N);
    }

    void longest_palindrome_substring() {
      int i = 0;
      int j = 0;
      int substr = this->N - 1; // Variable that indicates the substring to check.
      int startLongestPalindrome = 0;
      int finishLongestPalindrome = 0;
      string longestPalindrome = "";

      /* The first substring: i == j, always are going to be TRUE because the letter always match itself*/
      while(i <= substr) {
        this->matrix[i][j] = 1;
        i += 1;
        j += 1;
      }
      


      /* The second substring: i == j + 1, it is needed to be compared between the current letter and the following letter*/
      i = 0;
      j = this->N - substr;
      substr -= 1;
      while (i <= substr) {
        if(this->str[i] == this->str[j]) {
          this->matrix[i][j] = 1;

            // The longer j, the longer the palindrome will be.
            /*
              In this case it is not necessary to check where the palindrome begins because it is compared pair by pair,
              in short if it is found a palindrome, the maximum length for it is going to be 2.
            */
            if(j > finishLongestPalindrome) {
              startLongestPalindrome = i;
              finishLongestPalindrome = j;
            }
        } else {
          this->matrix[i][j] = 0;
        }
        i += 1;
        j += 1;
      }

      /* 
        From the rest of the substring, it is needed to be compared:
        - Bounderies are equal
        - Non-boundery substring should be a palindrom (if the substring at the middle is a palindrome).

        If both conditions are true, then the position are going to be true.
      */
      i = 0;
      j = this->N - substr;
      substr -= 1;
      while (substr >= 0) {
        while (j < this->N) {
          if(this->str[i] == this->str[j] && this->matrix[i + 1][j - 1] == 1) {
            this->matrix[i][j] = 1;

            /*
              In this case, since we did this process for the second substring, it could be the case where 
              j is greater but in a shorter substring, so, in this case we measure where the string start 
              and where the string ends.
            */
            if(i < startLongestPalindrome && j >= finishLongestPalindrome) {
              startLongestPalindrome = i;
              finishLongestPalindrome = j;
            }
          } else {
            this->matrix[i][j] = 0;
          }
          i += 1;
          j += 1;
        }

        i = 0;
        j = this->N - substr;
        substr -= 1;
      }

      //Print longest palindrom
      cout << "The longest palindrome is: ";

      for(int i = startLongestPalindrome; i <= finishLongestPalindrome; i++) {
        longestPalindrome += this->str[i];
      }

      cout << longestPalindrome << endl;

      cout << "Length is: " << longestPalindrome.length() << endl;
    }

    void print_matrix() {
      // Print matrix
      for (int i = 0; i < this->N; ++i) {
        for (int j = 0; j < this->N; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << "\n";
      }
    }
};

int main(){
  // Longest_Palindrome_Substring obj("geeks");
  // Longest_Palindrome_Substring obj("aaaabbaa");
  // Longest_Palindrome_Substring obj("geeksskeeg");
  Longest_Palindrome_Substring obj("at<tcba");
  obj.longest_palindrome_substring();
  // obj.print_matrix();
  return 0;
}