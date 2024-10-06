#include <iostream>
#include <vector>
#include <algorithm>

void CountSort(std::vector<int> &vec)
{
  int n = vec.size();
  int k = *max_element(vec.begin(), vec.end());
  std::vector<int> counter(k + 1);
  for (int i = 0; i < n; i++)
  {
    counter[vec[i]]++;
  }
  vec.clear();
  for (int i = 0; i < k + 1;i++){
    vec.insert(vec.end(), counter[i], i);
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

  CountSort(arr);

  for (int i = 0; i < arr.size(); i++)
  {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}