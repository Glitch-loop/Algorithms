#include <iostream>
#include <string.h>

using namespace std;


// Example of simple inheritance
class Vehicle {
  public:
    string brand = "Ford";

    void honk() {
      cout << "honk" << endl;
    }
};

class Car : public Vehicle {
  public:
    string model = "Mustang";
};

// Example of multiple level inheritance
class MyClass {
  public:
    void hello() {
      cout << "Hello world" << endl;
    }
};

class MyChild : public MyClass { };

class MyGrandChild : public MyChild { };

// Example of multiple inheritance
class FatherClass {
  public:
    void fatherGen() {
      cout << "Father's gen" << endl;
    }
};

class MotherClass {
  public:
    void motherGen() {
      cout << "Mother's gen" << endl;
    }
};

class SonClass : public FatherClass, public MotherClass { };

int main() {
  Car myCar;
  myCar.honk();
  cout << myCar.brand + " " + myCar.model << endl;

  MyGrandChild myClass;
  myClass.hello();

  SonClass sonClass;
  sonClass.fatherGen();
  sonClass.motherGen();
  return 0;
}