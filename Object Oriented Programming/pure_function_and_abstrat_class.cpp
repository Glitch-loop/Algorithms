#include <iostream>

// Abstract class with a pure virtual function
class Shape {
public:
    virtual void draw() = 0; // Pure virtual function
    virtual ~Shape() {} // Virtual destructor
};

class Circle : public Shape {
public:
    void draw() override { // Override pure virtual function
        std::cout << "Drawing a Circle" << std::endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override { // Override pure virtual function
        std::cout << "Drawing a Rectangle" << std::endl;
    }
};

void drawShape(Shape* shape) {
    shape->draw(); // Polymorphic call to the appropriate draw() function
}

int main() {
    Circle circle;
    Rectangle rectangle;

    drawShape(&circle);    // Outputs: Drawing a Circle
    drawShape(&rectangle); // Outputs: Drawing a Rectangle

    return 0;
}
