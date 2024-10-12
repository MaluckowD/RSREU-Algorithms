#include <iostream>
#include <algorithm>

using namespace std;

bool good(int x, int w, int h, int n)
{
  return (x / w) * (x / h) >= n;
}

int main()
{
  int w, h, n;
  cin >> w >> h >> n;

  int l = 0;
  int r = n * max(w, h);

  while (r - l > 1)
  {
    int m = (l + r) / 2;
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