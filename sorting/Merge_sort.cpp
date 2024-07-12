#include <iostream>
#include <vector>

using namespace std;

class Merge_sort {
  private:
    vector<int>* arr;

  void merge(){

  }

  void split(int init, int finish, vector <int>* array){
    if(init >= finish)
      return;

    int mid = 

    split(init, mid, array);
    split(mid + 1, finish, array);
    
  }

  public:
    Merge_sort(vector<int> sample)  { 
      for(auto const &element : sample) {
        this->arr->push_back(element);
      }
    }
    
    void sort() {

    }
};

int main () {
  return 0;
}