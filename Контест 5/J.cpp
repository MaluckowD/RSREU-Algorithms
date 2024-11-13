#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node
{
  int data;
  Node *left;
  Node *right;
  int count;

  Node(int key) : data(key), left(nullptr), right(nullptr), count(1) {}
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
        curr_node->count++;
        break;
      }
    }
  }

  void order_up_recursive(Node *node, vector<pair<int, int>> &result)
  {
    if (node != nullptr)
    {
      order_up_recursive(node->left, result);
      result.push_back(make_pair(node->data, node->count));
      order_up_recursive(node->right, result);
    }
  }

  vector<pair<int, int>> order_up()
  {
    vector<pair<int, int>> result;
    order_up_recursive(root, result);
    return result;
  }

  Node *getRoot()
  { 
    return root;
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
  vector<int> numbers;
  int el;
  cin >> el;
  while (el != 0)
  {
    numbers.push_back(el);
    cin >> el;
  }

  BinarySearchTree bst;
  for (int num : numbers)
  {
    bst.insert(num);
  }

  vector<pair<int, int>> result = bst.order_up();
  for (auto item : result)
  {
    cout << item.first << " " << item.second << endl;
  }
  return 0;
}