struct SuffixAutomaton {
  vector<map<char,int>> edges; // edges[i]  : the labeled edges from node i
  vector<int> link;            // link[i]   : the parent of i
  vector<int> length;          // length[i] : the length of the longest string in the ith class
  vector<int> endposCard;      // endposCard[i] : Cardinality of the endpos in the ith class
  int last;                    // the index of the equivalence class of the whole string

  vector<int> toposort;

  void topodfs(vector<map<char,int>> &G, vector<bool> &visited, int u){
      visited[u] = true;
      map<char,int>::iterator it = G[u].begin()
      for (it ; it != G[u].end() ; it++){
          int v = it->second;
          if(not visited[it->second]) topodfs(G, visited, v);
      }
      toposort.push_back(u);
  }

  void endposCardinalities(){
      vector<map<char,int>> G = edges;
      int n = G.size(), u;
      vector<int> endposCardi(n, 1); toposort.clear();
      topodfs(G, vector<bool>(n, false), 0);
      for(int i = 0 ; i < toposort.size() ; i++){
          u = toposort[i];
          endposCardi[link[u]] += endposCardi[u];
      }
      endposCard = endoposCardi;
  }



  SuffixAutomaton(string s) {
    // add the initial node
    edges.push_back(map<char,int>());
    link.push_back(-1);
    length.push_back(0);
    last = 0;

    for(int i=0;i<s.size();i++) {
      // construct r
      edges.push_back(map<char,int>());
      length.push_back(i+1);
      link.push_back(0);
      int r = edges.size() - 1;

      // add edges to r and find p with link to q
      int p = last;
      while(p >= 0 && edges[p].find(s[i]) == edges[p].end()) {
        edges[p][s[i]] = r;
        p = link[p];
      }
      if(p != -1) {
        int q = edges[p][s[i]];
        if(length[p] + 1 == length[q]) {
          // we do not have to split q, just set the correct suffix link
          link[r] = q;
        } else {
          // we have to split, add q'
          edges.push_back(edges[q]); // copy edges of q
          length.push_back(length[p] + 1);
          link.push_back(link[q]); // copy parent of q
          int qq = edges.size()-1;
          // add qq as the new parent of q and r
          link[q] = qq;
          link[r] = qq;
          // move short classes pointing to q to point to q'
          while(p >= 0 && edges[p][s[i]] == q) {
            edges[p][s[i]] = qq;
            p = link[p];
          }
        }
      }
      last = r;
    }
  }
};

//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------