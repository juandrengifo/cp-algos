#include <bits/stdc++.h>
using namespace std;

vector<int> concat(vector<int> &a, vector<int> &b){
    vector<int> newVec = a;
    for(int i = 0 ; i < b.size() ; i++)
        newVec.push_back(b[i]);
    return newVec;
}

int main(){
    vector<int> nums;
    int num, n, N;

    while(cin >> num){
        nums.push_back(num);
    }
    N = nums.size();

    pair<int,vector<int>> tab[100000];

    vector<int> lis;


    for(n = 0 ; n <= N ; n++){
        if(n == 0)
            tab[n] = {0,vector<int>(0,0)};
        
        else{
            vector<int> newLis = {nums[n]};
            int ans = 1;
            for(int i = 0 ; i < n ; i++){
                if(nums[i] < nums[n]){
                    if(1+tab[i].first > ans){
                        ans = 1 + tab[i].first;
                        vector<int> aux = concat(newLis, tab[i].second);
                        newLis.clear();
                        newLis = aux;
                    }
                }
            }
            
            if(ans > tab[n-1].first){
                tab[n].first = ans;
                tab[n].second = newLis;
            }
            else{
                tab[n].first = tab[n-1].first;
                tab[n].second = tab[n-1].second;
            }
        }
    }

    cout << tab[N].first << "\n-\n";
    for(int i = 0 ; i < tab[N].second.size() ; i++)
        cout << tab[N].second[i] << endl;

    return 0;
}