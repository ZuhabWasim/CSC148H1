"""
treat a filesystem as a tree
"""
from os import scandir, path
from tree import Tree


def path_to_tree(path_name: str) -> Tree:
    """
    Return a Tree representing filesystem starting from pathname.
    """
    return Tree((path_name, [f.name for f in scandir(path_name)]),
                [path_to_tree(path.join(path_name, f.name))
                 for f in scandir(path_name)
                 if f.is_dir()])

if __name__ == '__main__':
    d = scandir(".")
    print([f.name for f in d])
    t = path_to_tree(".")
    print(t)
    from tree_func_sol import leaf_count, arity
    print(leaf_count(t))
    print(arity(t))
