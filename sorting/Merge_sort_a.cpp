#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

class Merge_sort{
  private:
    vector<int> array;

    void merge(int l, int mid, int r, vector<int> array) {
      int left_iterator = l;
      int right_iterator = mid;
      
      for(int i = l; i < r; i++) {
        if(left_iterator < mid && right_iterator <= r) {
          if(this->array[left_iterator] < this->array[right_iterator]) {
            this->array[i] = this->array[left_iterator];
          } else {
            this->array[i] = this->array[right_iterator];
          }
        } 
      }
      // while(left_iterator < mid || right_iterator <= r) {
      //   if(left_iterator < mid && right_iterator <= r) {
      //     if(this->array[left_iterator] < this->array[right_iterator]) {

      //     }
      //   }
      // }

      return;
    }

    void sorting(int l, int r, vector<int> array) {
      if(l >= r) {
        return;
      } else {
        int mid = l + (r - l) / 2;

        this->sorting(l, mid, array);
        this->sorting(mid + 1, r, array);
        cout<<"l = "<< l << " - mid: " << mid << " - r: " << r << endl;
      }
    }

  public: 
    Merge_sort(vector<int> array) {

      // this->array = new vector<int> (array);
      for(const auto &element : array) {
        this->array.push_back(element);  
      }
    }

    void sorting() {
      this->sorting(0, this->array.size(), this->array);
    }

    void printArray() {
      for(int i = 0; i < this->array.size(); i++) {
        cout << this->array[i] << " ";
      }
      cout << endl;
    }

};

int main() {
  // Merge_sort obj({38, 27, 43, 10});
  Merge_sort obj({32, 52, 69, 87, 98, 74, 85});

  obj.printArray();
  obj.sorting();
  return 0;
}