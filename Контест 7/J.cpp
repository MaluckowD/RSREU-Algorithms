
#include <iostream>
#include <vector>
#include <limits>
#include <queue>

using namespace std;

long long dijkstra(const vector<vector<pair<int, int>>>& graph, int n, int start, int end) {
    vector<long long> dist(n + 1, numeric_limits<long long>::max());
    dist[start] = 0;

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, start});

    while (!pq.empty()) {
        long long d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (u == end) {
            return dist[end];
        }

        if (d > dist[u]) {
            continue;
        }

        for (const auto& edge : graph[u]) {
            int v = edge.first;
            int weight = edge.second;
            long long newDist = d + weight;
            if (newDist < dist[v]) {
                dist[v] = newDist;
                pq.push({newDist, v});
            }
        }
    }
    return -1;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<vector<pair<int, int>>> graph(n + 1);
    for (int i = 0; i < k; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({v, w});
        graph[v].push_back({u, w});
    }

    int start_node, end_node;
    cin >> start_node >> end_node;

    long long result = dijkstra(graph, n, start_node, end_node);
    cout << result << endl;

    return 0;
}