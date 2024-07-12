#include <iostream>
#include <queue>

using namespace std;

struct Node {
  int value;
  Node* left = NULL;
  Node* right = NULL;
};

class Tree {
  public:
    Node* root = NULL;

    void add_node(int value) {
      Node* new_node = new Node();
      new_node->value = value;

      if (this->root == nullptr) {
        root = new_node; 
      } else {
        this->add_node(this->root, new_node);
      }
    }

    void delete_node(int value) {
      if(this->root == nullptr)
        return;
      
      if(this->root->value == value) {
        this->delete_node(this->root, value, true);
        this->root = nullptr;
      } else {
        this->delete_node(this->root, value, false);
      }
    }

    void height() {
      cout << this->height(this->root) << endl;
    }

    void height_balanced() {
      if(this->root == nullptr) {
        cout << "Empty tree" << endl;
        return;
      }

      bool isBalanced = this->height_balanced(this->root);
      if(isBalanced) {
        cout << "Height balanced tree" << endl;
      } else {
        cout << "Not a height balanced tree" << endl;
      }

    }


    void inorder_traverse() {
      this->inorder_traverse(this->root);
      cout << endl;
    }

    void preorder_traverse() {
      this->preorder_traverse(this->root);
      cout << endl;
    }

    void postorder_traverse() {
      this->postorder_traverse(this->root);
      cout << endl;
    }

    void level_order_traversal() {
      queue<Node*> treeQueue;

      if(this->root == nullptr) {
        cout << "Tree empty" << endl;
        return;
      }

      treeQueue.push(this->root);

      this->level_order_traversal(treeQueue);
    }

  private:
    void add_node(Node* current_node, Node* new_node) {
      if(new_node->value <= current_node->value) {
        if (current_node->left == nullptr) {
          current_node->left = new_node;
        } else {
          add_node(current_node->left, new_node);
        }
      } else {
        if (current_node->right == nullptr) {
          current_node->right = new_node;
        } else {
          add_node(current_node->right, new_node);
        }
      }
    }

    void delete_node(Node* current_node, int value, bool delete_branch) {      
      if(current_node == nullptr)
        return;
        
      if(delete_branch == true) {
        // It was found the branch to prone.
        delete_node(current_node->left, value, true);
        delete_node(current_node->right, value, true);
        current_node->left = NULL;
        current_node->right = NULL;
        
      } else {
        // It wasn't found the branch to prone
        if(current_node->left != nullptr) {
          if(current_node->left->value == value) {
            delete_node(current_node->left, value, true);
            current_node->left = NULL;
          }
        }
        
        if(current_node->right != nullptr) {
          if(current_node->right->value == value) {
            delete_node(current_node->right, value, true);
            current_node->right = NULL;
          }
        }
        
        delete_node(current_node->left, value, false);
        delete_node(current_node->right, value, false);
      
      }
    }

    int height(Node* current_node) {
      if (current_node == nullptr)
        return 0;

      return 1 + max(this->height(current_node->left), this->height(current_node->right));
    }

    bool height_balanced(Node* current_node){
      if (current_node == nullptr)
        return false;

      int lh = this->height(current_node->left);
      int rh = this->height(current_node->right);

      if(abs(lh - rh) <= 1 
      && this->height_balanced(current_node->right)
      && this->height_balanced(current_node->left)) {
        return true;
      } else {
        return false;
      }

    }

    void inorder_traverse(Node* current_node) {
      if(current_node == nullptr) 
        return;
      
      this->inorder_traverse(current_node->left);
      cout << current_node->value << " - ";
      this->inorder_traverse(current_node->right);
    }

    void preorder_traverse(Node* current_node) { 
      if(current_node == nullptr)
        return;

      cout << current_node->value << " - ";
      this->preorder_traverse(current_node->left);
      this->preorder_traverse(current_node->right);
    }

    void postorder_traverse(Node* current_node) {
      if(current_node == nullptr)
        return;
      
      this->postorder_traverse(current_node->left);
      this->postorder_traverse(current_node->right);
      cout << current_node-> value <<" - ";
    }

    void level_order_traversal(queue<Node*> treeQueue) {
      
      if(treeQueue.empty())
        return;

      // Getting the first node
      Node* current_node = treeQueue.front();

      // Popping the first node
      treeQueue.pop();

      cout << current_node->value << " - ";

      if(current_node->left != nullptr)
        treeQueue.push(current_node->left);

      if(current_node->right != nullptr)
        treeQueue.push(current_node->right);

      level_order_traversal(treeQueue);      
    } 
};

int main() {
  Tree tree;
  // int arr[] = {5,3,1,4,7,6,8};
  // int arr[] = {8,9,5,4,3};
  int arr[] = {1,2,3,4,5,6,8};
  // int arr[] = {1,2,3,4,5,6,7,8};
  int n = sizeof(arr)/sizeof(arr[0]);

  for(int i = 0; i < n; i++) {
    tree.add_node(arr[i]);
  }

  // tree.level_order_traversal();
  tree.height();
  tree.height_balanced();
  return 0;
}