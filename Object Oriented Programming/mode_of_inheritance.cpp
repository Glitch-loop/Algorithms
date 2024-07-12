#include <iostream>
#include <string.h>

using namespace std;

class Base {
  public:
    int publicVar = 0;
  protected:
    int protectedVar = 0;
  private:
    int privateVar = 0;
};

class Derived : protected Base {
  public:
    void method() { }
};

class Further_Derived : public Derived {
  public:
      void method() {
        this->protectedVar = 0;
      }  
};


int main() {
  Further_Derived derived;
  derived.method();
  return 0;
}
