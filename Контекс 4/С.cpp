#include <iostream>
#include <vector>
#include <string>

class MinHeap
{
public:
  MinHeap() {}

  void clear()
  {
    heap.clear();
  }

  void add(int n)
  {
    heap.push_back(n);
    siftUp(heap.size() - 1);
  }

  std::string extract()
  {
    if (heap.empty())
    {
      return "CANNOT";
    }
    int minVal = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    siftDown(0);
    return std::to_string(minVal);
  }

private:
  std::vector<int> heap;

  void siftUp(int index)
  {
    while (index > 0 && heap[parent(index)] > heap[index])
    {
      std::swap(heap[parent(index)], heap[index]);
      index = parent(index);
    }
  }

  void siftDown(int index)
  {
    int minIndex = index;

    int left = leftChild(index);
    if (left < heap.size() && heap[left] < heap[minIndex])
    {
      minIndex = left;
    }

    int right = rightChild(index);
    if (right < heap.size() && heap[right] < heap[minIndex])
    {
      minIndex = right;
    }

    if (index != minIndex)
    {
      std::swap(heap[index], heap[minIndex]);
      siftDown(minIndex);
    }
  }

  int parent(int index)
  {
    return (index - 1) / 2;
  }

  int leftChild(int index)
  {
    return 2 * index + 1;
  }

  int rightChild(int index)
  {
    return 2 * index + 2;
  }
};

int main()
{
  MinHeap heap;
  std::string command;

  while (std::getline(std::cin, command))
  {
    if (command.substr(0, 5) == "CLEAR")
    {
      heap.clear();
    }
    else if (command.substr(0, 3) == "ADD")
    {
      int number = std::stoi(command.substr(4));
      heap.add(number);
    }
    else if (command.substr(0, 7) == "EXTRACT")
    {
      std::cout << heap.extract() << std::endl;
    }
  }

  return 0;
}
