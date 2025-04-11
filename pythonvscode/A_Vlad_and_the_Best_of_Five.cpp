#include<bits/stdc++.h>
using namespace std;
#define lli long long int
 
int main(){
ios::sync_with_stdio(0);cin.tie(0);
    int T; T=1;
    cin>>T;
    while(T--){
        string s;
        cin>>s;
        int cnt1=0,cnt2=0;
        for(int i=0;i<5;i++){
            if(s[i]=='A') cnt1++;
            else cnt2++;
        }
        if(cnt1>cnt2){
            cout<<"A"<<endl;
        }else{
            cout<<"B"<<endl;
        }
    }
    return 0;
}