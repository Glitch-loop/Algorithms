#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
      int num_to_zero = nums[0];

      // for(int i = 0; i < nums.size(); i++) {
      //   if((abs(nums[i]) <= abs(num_to_zero) && nums[i] > 0) || nums[i] == 0) {
      //     num_to_zero = nums[i];
      //   }  
      // }
      for(int i = 0; i < nums.size(); i++) {
        if(nums[i] == 0) {
          num_to_zero = nums[i];
        } else {
          if((abs(nums[i]) <= abs(num_to_zero))) {
            if(abs(nums[i]) == abs(num_to_zero)) {
              if(nums[i] > num_to_zero) {
                num_to_zero = nums[i];
              }
            } else {
              num_to_zero = nums[i];
            }
          }  
        }
      }

      return num_to_zero;
    }
};


int main() { 
  Solution s;
  vector<int> arr = {-1, 1, 0, 0};
  // vector<int> arr = {2, 1, -1};

  cout << s.findClosestNumber(arr) << endl;

  return 0;
}