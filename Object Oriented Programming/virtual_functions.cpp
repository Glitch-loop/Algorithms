#include <iostream>

class Base {
public:
    virtual void show() { // Virtual function
        std::cout << "Base class show function called." << std::endl;
    }
    virtual ~Base() {} // Virtual destructor
};

class Derived : public Base {
public:
    void show() override { // Overriding the virtual function
        std::cout << "Derived class show function called." << std::endl;
    }
};

int main() {
    Base* basePtr;
    Derived derivedObj;
    basePtr = &derivedObj;

    // Calls Derived class show function
    basePtr->show();

    return 0;
}
