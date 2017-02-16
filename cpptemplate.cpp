#include <algorithm>
#include <iostream>
#include <iterator>
#include <map>
#include <math.h>
#include <string>
#include <vector>
using namespace std;
typedef unsigned int Nat;
typedef unsigned long long longNat;
typedef vector<int> vint;
typedef vector<Nat> vnat;

void Output() { std::cout << std::endl; }
template <typename First, typename... Strings>
void Output(First &arg, const Strings &... rest) {
  std::cout << arg << " ";
  Output(rest...);
}
void Input() {}
template <typename First, typename... Strings>
void Input(First &arg, Strings &... rest) {
  typedef vector<int> vint;
  cin >> arg;
  Input(rest...);
}

template <typename T> void printVector(const T &t) {
  cout << "[";
  copy(t.cbegin(),
       t.cend() -
           1, // -1 because i don't want a comma at the end of the last number
       std::ostream_iterator<typename T::value_type>(std::cout, ", "));
  cout << t.back() << "]";
}

template <typename T> void printVectorInVector(const T &t) {
  for_each(t.cbegin(), t.cend(), printVector<typename T::value_type>);
}
