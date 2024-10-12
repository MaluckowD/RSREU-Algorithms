#include <iostream>
#include <vector>
#include <cmath>

bool good(int x, int k, const std::vector<int> &a){
  int cnt = 0;
  for (int i = 0; i < a.size(); ++i)
  {
    cnt += a[i] / x;
  }

  return cnt >= k;
}

int main()
{
  int n, k;
  std::cin >> n >> k;

  std::vector<int> a(n);
  for (int i = 0; i < n; ++i)
  {
    std::cin >> a[i];
  }

  int l = 0;
  int r = pow(10,7) + 1;

  for (int i = 0; i < 100; i++){
    int m = (l + r) / 2;
    if (good(m, k, a))
    {
      l = m;
    }
    else
    {
      r = m;
    }
  }
  std::cout << l << std::endl;
  return 0;
}