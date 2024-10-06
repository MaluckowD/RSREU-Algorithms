#include <iostream>
#include <vector>

void InsertionSort(std::vector<int> &vec)
{
  int n;
  n = vec.size();
  for (int i = 0; i < n; i++)
  {
    int key = vec[i];
    int j = i;

    while ((j >= 1) && (vec[j-1] > key)){
      vec[j] = vec[j-1];
      j--;
    }
    
    vec[j] = key;
 
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

  InsertionSort(arr);

  for (int i = 0; i < arr.size(); i++)
  {
    std::cout << arr[i] << " ";
  }
  std::cout << std::endl;

  return 0;
}