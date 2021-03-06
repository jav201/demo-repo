from collections import deque
# Find the shortest path on a graph with non weighted edges
r"""GRAPH:
YOU - Alice - Peggy
    \       /
       Bob   - Anuj
  \
   Claire - Thom
        \
         Jonny
"""
# First, declare the nodes on a hash table
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['jonny', 'thom']
graph['anuj'] = []
graph['peggy'] = [] # she will be the chosen one
graph['thom'] = []
graph['jonny'] = []


def breadth_first(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # Already searched nodes
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person[0] == 'p':
                print('P-erson found!', person)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

breadth_first('you')

    