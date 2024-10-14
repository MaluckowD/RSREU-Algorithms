#include <iostream>
#include <vector>

using namespace std;

int get_sum(vector<int> &arr, int div)
{
  int s = 0;
  for (int num : arr)
  {
    s += num / div;
  }

  return s;
}

int main()
{
  int n, k;
  cin >> n >> k;

  vector<int> a(n, 0);
  for (int i = 0; i < n; ++i)
    cin >> a[i];

  int left = 0;
  int right = 1000000000;
  while (left < right - 1)
  {
    int middle = (left + right) / 2;
    if (get_sum(a, middle) < k)
      right = middle;
    else
      left = middle;
  }

  cout << left;

  return 0;
}