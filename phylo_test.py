from ete3 import Tree, TreeStyle

# Example Newick tree format
newick_tree = "(A:0.1,B:0.2,(C:0.3,D:0.4):0.5);"

# Load tree
tree = Tree(newick_tree)

# Customize tree style
ts = TreeStyle()
ts.show_leaf_name = True

# Show tree
tree.show(tree_style=ts)
