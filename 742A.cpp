#include <string>
#include <iostream>
#include <vector>

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
int main(){
	unsigned long long n;
	int res;
	Input(n);

	switch( n%4){
		case(0):
		res=6;
		break;
		case(1):
		res=8;
		break;
		case(2):
		res=4;
		break;
		case(3):
		res=2;
		break;
	}
	if(n==0){
		res=1;	
	}
	Output(res);
}
