#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

bool good(long long x, int w, int h, int n)
{
  return (x / w) * (x / h) >= n;
}

int main()
{
  int w, h, n;
  cin >> w >> h >> n;

  long long l = 0;
  long long r = (sqrt(n) + 1) * std::max(w, h);

  while (r - l > 1)
  {
    long long m = (l + r) / 2;
    if (good(m, w, h, n))
    {
      r = m;
    }
    else
    {
      l = m;
    }
  }

  cout << r << endl; 

  return 0;
}