import matplotlib.pyplot as plt
import random


class DirectedGraph:
    def __init__(self, n=None, e=None):
        if n is None:
            self.nodes = set()
        else:
            self.nodes = set(n)

        if e is None:
            self.edges = dict()
        else:
            self.edges = dict([(v, set()) for v in self.nodes])
            for i in e:
                self.add_edge(i[0], i[1])

    def count_nodes(self):
        return len(self.nodes)

    def count_edges(self):
        return sum([self.degree(node) for node in self.nodes])

    def neighbors(self, node):
        return self.edges[node]

    def degree(self, node):
        neighbors = self.neighbors(node)
        res = len(neighbors)
        return res

    def add_edge(self, u, v):
        if u not in self.nodes:
            self.nodes.add(u)
            self.edges[u] = set()
        if v not in self.nodes:
            self.nodes.add(v)
            self.edges[v] = set()
        if v not in self.edges[u]:
            self.edges[u].add(v)

    def edges_list(self):
        edges = set()
        for v in self.edges.keys():
            for u in self.edges[v]:
                edges.add((v, u))
        return edges

    def strong_components(self):
        indexes = dict()
        links = dict()
        visited = set()
        done = set()
        stack_component = []
        components = dict()
        counter = 0
        comp_counter = 0

        for node in self.nodes:
            if node not in done:
                stack_nodes = [node]

                while stack_nodes:
                    s = stack_nodes[-1]
                    unvisited_node = None

                    if s not in visited:
                        counter += 1
                        indexes[s] = counter
                        links[s] = counter
                        visited.add(s)

                    for t in self.neighbors(s):
                        if t not in visited:
                            unvisited_node = t
                            stack_nodes.append(t)
                            break

                    if not unvisited_node:
                        stack_nodes.pop()

                        for v in self.neighbors(s):
                            if v not in done:
                                links[s] = min([links[s], links[v]])

                        stack_component.append(s)

                        if links[s] == indexes[s]:
                            comp_counter += 1

                            while stack_component:
                                node = stack_component.pop()

                                if indexes[node] < indexes[s]:
                                    stack_component.append(node)
                                    break
                                else:
                                    if comp_counter not in components.keys():
                                        components[comp_counter] = {node}
                                    else:
                                        components[comp_counter].add(node)
                                    done.add(node)

        return components

    def number_strongly_components(self):
        return len(self.strong_components().keys())

    def strongly_comp_with_max_power(self):
        max_len = 0
        max_comp = -1
        components = self.strong_components()
        for i in components.keys():
            if len(components[i]) > max_len:
                max_len = len(components[i])
                max_comp = i
        return components[max_comp]

    def nodes_in_strongly_comp_with_max_power(self):
        return len(self.strongly_comp_with_max_power()) / self.count_nodes()

    def meta_graph(self):
        scc = self.strong_components()
        new_nodes = set(scc.keys())
        new_edges = set()
        indexes = dict()
        for node, values in scc.items():
            for value in values:
                indexes[value] = node
        for edge in self.edges_list():
            u = indexes[edge[0]]
            v = indexes[edge[1]]
            if u != v:
                new_edges.add((u, v))
        meta = DirectedGraph(new_nodes, new_edges)
        return meta
