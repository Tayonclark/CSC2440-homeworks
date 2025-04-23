def inputOfgraph():
    n = int(input("Enter the amount of nodes within graph:"))
    print("Enter the adjacency matrix:")
    adjacent_matrix = []
    for i in range(n):
        rows = list(map(int, input(f"row{i}: ").split()))
        adjacent_matrix.append(rows)
    return adjacent_matrix

def display_graph(adjacent_matrix):
    print("Adjacent matrix:")
    for rows in adjacent_matrix:
        print(" ".join(map(str, rows)))
    print()


def delete_nodes(adjacent_matrix, index_of_node):
    adjacent_matrix.pop(index_of_node)
    for rows in adjacent_matrix:
        rows.pop(index_of_node)
    return adjacent_matrix

print("input of graph:")
graph = inputOfgraph()

print("The graph before deleting node 2:")
display_graph(graph)

GAD = delete_nodes(graph, 2)

print("The graph after deleting the node 2:")
display_graph(GAD)



