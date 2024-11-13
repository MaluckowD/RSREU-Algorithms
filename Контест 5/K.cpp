#include <iostream>
#include <queue>

using namespace std;

struct Node
{
  int data;
  Node *left;
  Node *right;

  Node(int key) : data(key), left(nullptr), right(nullptr) {}
};

class BinarySearchTree
{
public:
  BinarySearchTree() : root(nullptr) {}

  void insert(int key)
  {
    if (root == nullptr)
    {
      root = new Node(key);
      return;
    }

    Node *curr_node = root;
    while (true)
    {
      if (key < curr_node->data)
      {
        if (curr_node->left == nullptr)
        {
          curr_node->left = new Node(key);
          break;
        }
        curr_node = curr_node->left;
      }
      else if (key > curr_node->data)
      {
        if (curr_node->right == nullptr)
        {
          curr_node->right = new Node(key);
          break;
        }
        curr_node = curr_node->right;
      }
      else
      {
        break;
      }
    }
  }

  int next(int key)
  {
    Node *curr_node = root;
    int min_greater = -1;
    while (curr_node)
    {
      if (key <= curr_node->data)
      {
        min_greater = curr_node->data;
        curr_node = curr_node->left;
      }
      else
      {
        curr_node = curr_node->right;
      }
    }
    return min_greater;
  }

  ~BinarySearchTree()
  {
    queue<Node *> nodes;
    nodes.push(root);
    while (!nodes.empty())
    {
      Node *current = nodes.front();
      nodes.pop();
      if (current->left)
        nodes.push(current->left);
      if (current->right)
        nodes.push(current->right);
      delete current;
    }
  }

private:
  Node *root;
};

int main()
{
  int n;
  cin >> n;
  BinarySearchTree bst;
  int last_y = -1;

  for (int i = 0; i < n; ++i)
  {
    string command;
    int num;
    cin >> command >> num;

    if (command == "+")
    {
      if (last_y != -1)
      {
        bst.insert((num + last_y) % (1000000000));
        last_y = -1;
      }
      else
      {
        bst.insert(num);
      }
    }
    else if (command == "?")
    {
      int result = bst.next(num);
      cout << result << endl;
      last_y = result;
    }
  }

  return 0;
}