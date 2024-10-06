#include <iostream>
#include <vector>

int BubbleSort(std::vector<int> &vec,int n)
{
  int count = 0;
  for (int i = 0; i < n - 1; i++)
  {
    bool swapped = false;
    for (int j = 0; j < n - i - 1; j++)
      if (vec[j] > vec[j + 1])
      {
        std::swap(vec[j], vec[j + 1]);
        swapped = true;
        count++;
      }
    if (!swapped)
    {
      break;
    }
  }

  return count;
}

int main()
{
  int x;
  int N;
  std::cin >> N;
  std::vector<int> arr;
  while (std::cin >> x)
  {
    arr.push_back(x);
  }

  std::cout << BubbleSort(arr,N);
  return 0;
}