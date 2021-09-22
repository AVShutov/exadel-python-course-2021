tree = {
    "node1": {
        "node11": {
            "node111": [1, 2, 3],
            "node112": [4, 5]
        },
        "node12": [6]
    },
    "node2": [7, 8, 9]
}

flat_tree = [1,2,3]

def my_pow(a,b):
    return(pow(a,b))

def collect_leaves(data):
    if isinstance(data, dict):
        leaves = []
        for value in data.values():
            leaves.extend(collect_leaves(value))
        return leaves
    return data
    
# print(tree.values())
# print(tree.items())

assert collect_leaves(tree) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# edge case: flat tree, i.e. list
assert collect_leaves(flat_tree) == [1, 2, 6]

# assert example
assert my_pow(5, 3) == 125
