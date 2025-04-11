#include<bits/stdc++.h>
using namespace std;
#define lli long long int
 
int main(){
ios::sync_with_stdio(0);cin.tie(0);
    int T; T=1;
    cin>>T;
    while(T--){
        int n;
        cin>>n;
        int a[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                char c;
                cin>>c;
                a[i][j]=c-'0';
            }
        }
        int cnt1=0,cnt2=0,flag=0;
        int f,l,k,h;
        for(int i=0;i<n;i++){
            cnt1=0;
            for(int j=0;j<n;j++){
                if(a[i][j]==1) cnt1++; f=i;l=j;
            }
            if(cnt1>1){
                for(k=f;k<n;k++){
                    if(a[k][l]==1) cnt2++;
                }
            }
        }
        if(flag==1){
            cout<<"SQUARE"<<endl;
        }
    }
    return 0;
}