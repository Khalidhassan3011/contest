# Presentation
"""
    -> Array
    -> Linked
"""

# Types
"""
    Linear -> Tree
    Non Linear -> Array, Stack, Queue, Linked List
"""

# Traverse
"""
    ----------------------------------------------------------------------
    |     previous node link     |     DATA     |      next node link    |
    ----------------------------------------------------------------------
"""

# Types of Binary Tree
"""
    1-> Full or Strict
            All node have either 2 or 0 children
    
            1               1                   1
           / \             / \                 / \
          2   3           2   3               2   3
                         / \                 / \   \
                        4   5               4   5   6
                          
          FIG:1           FIG:2                FIG:3
          
          FIG:1 -> yes
          FIG:2 -> yes
          FIG:3 -> no  [3 has only one child]
          
          
    2-> Perfect
            i)   All internal node have exact 2 child
            ii)  All leaf nodes are on same level
    
            1               1                   1
           / \             / \                 / \
          2   3           2   3               2   3
                         / \                 / \   \
                        4   5               4   5   6
                          
          FIG:1           FIG:2                FIG:3
          
          FIG:1 -> yes
          FIG:2 -> no  {mismatch rule i and ii} [3 has no child]
          FIG:3 -> no  {mismatch rule i } [3 has only one child]
          
          
    3-> Complete
            i)   All levels are completely filled except last level
            ii)  Last level all nodes in left
    
            1                 1                    1
           / \             /    \                 / \
          2   3           2      3               2   3
         / \             / \    /               / \   \
        4  5            4   5  6               4   5   6
                          
          FIG:1           FIG:2                FIG:3
          
          FIG:1 -> yes
          FIG:2 -> yes
          FIG:3 -> no  {mismatch rule ii } [3 has right side child]
          
          
    4-> Degenerate
            i)   Parent node has only one child except leaf
    
            1                 1                    1
           / \                 \                 / 
          2   3                 3               2   
         / \                                   /     
        4  5                                 4       
                          
          FIG:1           FIG:2                FIG:3
          
          FIG:1 -> no {mismatch rule i } [1 and 2 has two child]
          FIG:2 -> yes
          FIG:3 -> yes  
          
    
    5-> Skewed
            i)   All children in same side
                 Left -> All child on left side
                 Right -> All child in right side
    
            1                 1                    1
           / \                 \                 / 
          2   3                 3               2   
         /                                    /     
        4                                    4       
                          
          FIG:1           FIG:2                FIG:3
          
          FIG:1 -> no [1 has two child]
          FIG:2 -> right
          FIG:3 -> left 
"""
