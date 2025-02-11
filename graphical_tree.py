import matplotlib.pyplot as plt
from Bio import Phylo  

tree = Phylo.read("H5_tree_upgma.nwk", "newick")
plt.figure(figsize=(10, 8))
Phylo.draw(tree, do_show=True)

