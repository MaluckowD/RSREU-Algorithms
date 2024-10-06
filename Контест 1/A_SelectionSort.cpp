#include <iostream>
#include <vector>

void SelectionSort(std::vector<int> &vec)
{
  int n;
  n = vec.size();
  for (int i = 0; i < n - 1; i++)
  {
    int key = vec[i];
    int ind = i;
    for (int j = i + 1; j < n; j++)
      if (vec[j] > key)
      {
        key = vec[j];
        ind = j;
      }
    if (i != ind)
    {
      std::swap(vec[i], vec[ind]);
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

  SelectionSort(arr);

  for (int i = 0; i < arr.size(); i++)
  {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}