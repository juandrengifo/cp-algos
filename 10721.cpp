#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef long long ll;


ll solve(ll N, ll K, ll M, ll n, ll k, ll m, ll ac, vector<vector<vi>> &memo){
	ll ans = memo[n][k][m];
	if(n == N and k < K) ans = 0;
	else if(n == N and k == K) ans = ac;
	else if(ans == -1){
		ans = 0;
		//change color
		if(k < K) ans += solve(N, K, M, n+1, k+1, 0, ac+1, memo);
		//continue with color
		if(m < M) ans += solve(N, K, M, n+1, k, m+1, ac+1, memo);
	}
	memo[n][k][m] = ans;
	cout << n << " " << k << " " << m << " " << ans << endl;
	return ans;
}


int main(){
	ll N, K, M;
	while(cin >> N >> K >> M){
		vector<vector<vi>> memo(N+1, vector<vi>(K+1, vi(M+1, -1)));
		solve(N, K, M, 0, 1, 1, 1, memo);
		cout << memo[N][K][M] << endl;
	}
	return 0;
}