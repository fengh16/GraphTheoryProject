#include "Algorithm.h"

extern int graph[1419][1419];
int minimum_spanning_tree[1419];	//ÿ��Ԫ�ؼ�¼�ý�������С������ʱ�Ľ������
int g[1419][1419];

void BFS(int G[1419][1419], int edgeNum, int begin, bool *visited, int threshold)
{
	queue<int> Q;
	Q.push(begin);
	visited[begin] = true;
	cout << begin;

	while (!Q.empty())
	{
		int tmp = Q.front();
		Q.pop();
		for (int i = 0; i < edgeNum; i++)
		{
			if (!visited[i] && G[tmp][i] >= threshold)
			{
				Q.push(i);
				visited[i] = true;
				cout << " - " << i;
			}
		}
	}
}

void connected_branch()
{
	int N = 1419;
	int threshold = 0;
	int numSection = 0;
	cout << "��������ֵ:" << endl;
	cin >> threshold;
	bool *visited = new bool[N];
	for (int i = 0; i < N; i++)
		visited[i] = false;
	for (int i = 0; i < N; i++)
	{
		if (!visited[i])
		{
			cout << endl << endl;
			BFS(graph, N, i, visited, threshold);
			numSection++;
		}
	}
}

void prim()
{
	int i, j, last_pos, pos, min, result = 0;
	for (i = 0; i < 1419; i++)
	{
		minimum_spanning_tree[i] = -1;
	}
	int min_length[1419], visited[1419] = { 0 };
	for (i = 0; i < 1419; i++)
	{
		for (j = 0; j < 1419; j++)
		{
			if (graph[i][j] == 0)
				g[i][j] = 1000000;
			else
				g[i][j] = graph[i][j];
		}
	}
	//��ĳ�㿪ʼ���ֱ��Ǻͼ�¼�õ�
	visited[0] = 1;
	pos = 0;
	last_pos = 0;
	//��һ�θ�min_length���鸳ֵ
	for (i = 0; i < 1419; i++)
	{
		if (i != pos)
		{
			min_length[i] = g[pos][i];
			if (min_length[i] != 1000000)
			{
				minimum_spanning_tree[i] = pos;
			}
		}
	}
	//������n-1��
	for (i = 1; i < 1419; i++)
	{
		//�ҳ���СȨֵ����¼λ��
		min = 1000000;
		for (j = 0; j < 1419; j++)
		{
			if (visited[j] == 0 && min > min_length[j])
			{
				min = min_length[j];
				pos = j;
			}
		}
		//��СȨֵ�ۼ�
		result += min;
		//��Ǹõ�
		visited[pos] = 1;
		//����Ȩֵ
		for (j = 0; j < 1419; j++)
		{
			if (visited[j] == 0 && min_length[j] > g[pos][j])
			{
				min_length[j] = g[pos][j];
				if (min_length[j] != 1000000)
				{
					minimum_spanning_tree[j] = pos;
				}
			}
		}
	}
	for (int i = 0; i < 1419; i++)
	{
		cout << minimum_spanning_tree[i] << " -> " << i << endl;
	}
}

/*
d3.dijkstra = function() {
	var dijkstra = {}, nodes, edges, source, dispatch = d3.dispatch("start", "tick", "step", "end");

	dijkstra.run = function(src) {
		source = src;
		var unvisited = [];

		nodes.forEach(function(d) {
			if (d != src) {
				d.distance = Infinity;
				unvisited.push(d);
				d.visited = false;
			}
		});

		var current = src;
		current.distance = 0;

		function tick() {
			current.visited = true;
			current.links.forEach(function(link) {
				var tar = link.target;
				if (!tar.visited) {
					var dist = current.distance + link.value;
					tar.distance = Math.min(dist, tar.distance);
				}
			});
			if (unvisited.length == 0 || current.distance == Infinity) {
				dispatch.end()
					return true;
			}
			unvisited.sort(function(a, b) {
				return b.distance - a.distance
			});

			current = unvisited.pop()

				dispatch.tick();

			return false;
		}

		d3.timer(tick);
	};

	dijkstra.nodes = function(_) {
		if (!arguments.length)
			return nodes;
		else {
			nodes = _;
			return dijkstra;
		}
	};

	dijkstra.edges = function(_) {
		if (!arguments.length)
			return edges;
		else {
			edges = _;
			return dijkstra;
		}
	};

	dijkstra.source = function(_) {
		if (!arguments.length)
			return source;
		else {
			source = _;
			return dijkstra;
		}
	};

	dispatch.on("start.code", dijkstra.run);

	return d3.rebind(dijkstra, dispatch, "on", "end", "start", "tick");
};
*/