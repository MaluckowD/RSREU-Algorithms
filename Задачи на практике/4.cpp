#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

int merge_and_count(vector<int> &arr, vector<int> &temp_arr, int left, int mid, int right)
{
  int i = left;
  int j = mid + 1;
  int k = left;
  int inv_count = 0;

  while (i <= mid && j <= right)
  {
    if (arr[i] <= arr[j])
    {
      temp_arr[k] = arr[i];
      i++;
    }
    else
    {
      temp_arr[k] = arr[j];
      inv_count += (mid - i + 1);
      j++;
    }
    k++;
  }

  while (i <= mid)
  {
    temp_arr[k] = arr[i];
    i++;
    k++;
  }

  while (j <= right)
  {
    temp_arr[k] = arr[j];
    j++;
    k++;
  }

  for (int i = left; i <= right; i++)
  {
    arr[i] = temp_arr[i];
  }

  return inv_count;
}

int merge_sort_and_count(vector<int> &arr, vector<int> &temp_arr, int left, int right)
{
  int inv_count = 0;
  if (left < right)
  {
    int mid = (left + right) / 2;

    inv_count += merge_sort_and_count(arr, temp_arr, left, mid);
    inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right);
    inv_count += merge_and_count(arr, temp_arr, left, mid, right);
  }
  return inv_count;
}

int count_inversions(vector<int> &arr)
{
  vector<int> temp_arr(arr.size());
  return merge_sort_and_count(arr, temp_arr, 0, arr.size() - 1);
}

int min_transpositions_to_sort_p(int n, vector<int> &p)
{
  vector<int> index_map(n + 1, -1);
  for (int i = 0; i < n; ++i)
  {
    index_map[p[i]] = i;
  }

  vector<int> transformed(n);
  for (int i = 1; i <= n; ++i)
  {
    transformed[i - 1] = index_map[i];
  }

  int min_inv = count_inversions(transformed);
  return min_inv;
}

int main()
{
  int n;
  cin >> n;
  vector<int> p(n);
  for (int i = 0; i < n; ++i)
  {
    cin >> p[i];
  }

  int result = min_transpositions_to_sort_p(n, p);
  cout << result << endl;

  return 0;
}