#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>> &graph, vector<bool> &visited, int u, int &visCnt){
    if(not visited[u]){
        visited[u] = true;
        visCnt++;
        vector<int> adjacents = graph[u];

        for(int i = 0 ; i < adjacents.size() ; i++)
            dfs(graph, visited, adjacents[i], visCnt);
    }
}

int main(){
    int cases, c, m, i, u, v, maxVisCnt, maxVis, visCnt;

    cin >> cases;
    for(c = 1 ; c <= cases ; c++){
        cin >> m;

        vector<vector<int>> graph(m, vector<int>(0, 0));

        for(i = 0 ; i < m ; i++){
            cin >> u >> v;
            u--;v--;
            graph[u].push_back(v);
        }


        maxVisCnt = maxVis = 0;
        for(i = 0 ; i < m ; i++){
            vector<bool> visited(m, false);
            visCnt = 0;
            dfs(graph, visited, i, visCnt);
            if(visCnt > maxVisCnt){
                maxVisCnt = visCnt;
                maxVis = i;
            }
        }

        cout << "Case " << c << ": " << maxVis + 1 << endl;
    }
    return 0;
}