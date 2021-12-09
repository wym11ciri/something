#include<iostream>
#include<vector>
using namespace std;
vector<string> ans;
void dfs(string s, int k){
    if(k == s.size() - 1) ans.push_back(s);
    for(int i = k; i < s.size(); i++){
        swap(s[i], s[k]);
        dfs(s, k+1);
        swap(s[i], s[k]);
    }
}
int main(){
    string s = "abc";
    dfs(s, 0);
    for(int i = 0; i < ans.size(); i++){
        cout<<ans[i]<<" ";
    }
}
