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
    std::vector<int> v(3,100);
    v.insert(v.begin() +1,3);
    for(int i :v){
        cout<<i<<endl;
    }
    return;
    unsigned long long int n,a,b,c;
    n=1;
    a=2;
    b=3;
    c=4;
    Input(n,a,b,c);
    unsigned long long int resto = n%4;
    if (resto==0){
        cout<<resto<<"\n";
        return 0;
    }
    unsigned long long int mincho;
    if(resto ==2){
        mincho =min(2*a,b);
        mincho = min(mincho,2*c);
        mincho= min(mincho,a+b+c); //1+2+3 = 6=> 6+2=8
    }else if(resto==1){
        mincho = min(3*a,c);//1+3=4
        mincho= min(mincho,a+b);//1+1+2=4
        mincho= min(mincho,a+2*b+c);//1+2*2+3==8
    }else{ //resto==3
        mincho=min(a,b+c);//2+3=5=> 5+3=8 divisible por 4 bitch
        mincho=min(mincho,3*c);//3*3 = 9=> 9+3=12
    }
    cout<<mincho<<"\n";
    return 0;
}




//R a b c
//1 10 1 27
