#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <map>
using namespace std;
void Output() {
	std::cout<<std::endl;
}
template<typename First, typename ... Strings>
void Output(First& arg, const Strings&... rest) {
	std::cout<<arg<<" ";
	Output(rest...);
}
void Input() {
}
template<typename First, typename ... Strings>
void Input(First& arg,  Strings&... rest) {
	cin>>arg;
	Input(rest...);
}
vector<int> factors(int n){
	vector<int> fact;
	int check=2;
	int rootn=sqrt(n);
	while (check<rootn){
		if {n%check==0){
			fact.push_back(check);
			fact.push_back(n/check);
		}
		check+=1;
	}
	if (rootn==check){
		fact.push_back(check)
		fact.sort();
	}
	if(fact.empty())
	fact=[n];
	return fact;
}
int main(){
	int n;
	Input(n);
	vector<int> numbers;
	int a;
	for (size_t i = 0; i < n; i++) {
		cin<<a;
		numbers.push_back(a);
	}
	nums = {}
	std::map<int, int> nums;
	for i in numbers{
		nums[i]=0
		for k in nums:
		if(k == i):
		continue
		if(gcd(k,i)==1):
		nums[i]+=1
		nums[k]+=1
	}
	miniCosa = min(nums, key=lambda k: nums[k])
	minLen= nums[miniCosa]
	miniLens=[l for l in nums if nums[l] == minLen]
	primeDecomposition=[]
	for mini in miniLens:
	for i in  factors(mini):
	if i not in primeDecomposition:
	primeDecomposition.append(i)
	sol=0
	for p in primeDecomposition:
	num=sum([1 for i in numbers if i%p==0])
	if(sol<num):
	sol=num
	print(sol)
}
