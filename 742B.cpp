#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
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
int logo2(int number){
	return (int)log2(number);
}
int main(){
	int n, x;
	Input(n,x);
	vector<int> lista(n);
	for (int i = 0; i < n; i++) {
		cin>>lista[i];
	}
	sort(lista.begin(),lista.end());
	int limit =logo2(lista.back());
	int poto=0;
	int res=0;
	size_t q;
	for (q = 0; q < lista.size() && logo2(lista[q])<logo2(x); q++) {}//hola
	for (size_t k = 0; k < q+1; k++) {
		for (size_t l = k+1; l < q+1; l++) {
			if((lista[k] ^ lista[l]) ==x){
				//Output("Tengo, ",lista[k] ,"^", lista[l]," ==" ,x);
				res++;
			}
		}
	}
	for (size_t i = q+1; i < lista.size(); i++) {
		if(lista[i]==x){
			continue;
		}
		if (lista[i]==0){
			for (size_t j = i+1; j < lista.size() && lista[j]<x+1; j++) {
				if(lista[j]==x){
					res++;
				}
			}
		}else{
			poto=logo2(i);
			size_t j;
			for (j = i+1; j < lista.size() && logo2(lista[j])==poto; j++) {}//hola
			for (size_t k = i; k < j+1; k++) {
				for (size_t l = k+1; l < j+1; l++) {
					if((lista[k] ^ lista[l]) ==x){
						//Output("Tengo, ",lista[k] ,"^", lista[l]," ==" ,x);
						res++;
					}
				}
			}
			i=j-1;
		}
	}
	Output(res);
}
