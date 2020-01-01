#include <iostream>
#include <string>
#include <vector>

typedef unsigned long long ULL;
typedef ULL value_type; // or big-integer type
using namespace std;

void recursive_build(ULL dmin, ULL d, vector < ULL > & primes, vector < size_t > & exponents, size_t k, value_type & x, value_type & xmin) {
  value_type y = x;
  for (size_t i = 1; i <= exponents[k - 1]; ++i) {
    exponents[k] = i;
    ULL dnext = d * (2 * i + 1);
    y = y * primes[k];

    // quit if bigger than current best
    if (y > xmin) {
      return;
    }

    // quit and save if we have new best
    if (dnext > dmin) {
      xmin = y;
      return;
    }
    recursive_build(dmin, dnext, primes, exponents, k + 1, y, xmin);
  }
}

void euler(ULL N) {

  // we need X such that X^2 has at least this many divisors
  ULL dmin = 2 * N - 1;

  // count how many unique primes until we get # divisors (provides a bound on X)
  size_t nprimes = 1;
  ULL p = 3;
  while (p < dmin) {
    p = p * 3;
    ++nprimes;
  }
  vector < ULL > primes = {
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47
  };
  // gen_primes<ULL>(nprimes); // or generate primes if more required

  // current best estimate is first k primes
  value_type xmin = 1;
  for (size_t i = 0; i < nprimes; ++i) {
    xmin = xmin * primes[i];
  }

  // recursively build up number by slowly increasing exponents
  vector < size_t > exponents(nprimes, 0);
  value_type y = 1;
  recursive_build(dmin, 1, primes, exponents, 0, y, xmin);

  // solution
  cout << xmin << std::endl;

}

int main() {
  euler(1000);
}
