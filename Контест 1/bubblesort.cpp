#include <iostream>
#include <vector>

void BubbleSort(std::vector<int> &vec)
{
  int n;
  n = vec.size();
  for (int i = 0; i < n - 1; i++)
  {
    bool swapped = false;
    for (int j = 0; j < n - i - 1; j++)
      if (vec[j] < vec[j + 1])
      {
        std::swap(vec[j], vec[j + 1]);
        swapped = true;
      }
    if (!swapped)
    {
      break;
    }
  }
}

int main()
{
  int x;
  std::vector<int> arr;
  while (std::cin >> x)
  {
    arr.push_back(x);
  }

  BubbleSort(arr);

  for (int i = 0; i < arr.size(); i++)
  {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}