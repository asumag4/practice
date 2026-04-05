-- UNSOLVED!!
SELECT
 CASE 
   WHEN parent_node IS NULL THEN child_node
   ELSE parent_node
 END AS 'id',
 CASE 
   WHEN child_node is NULL THEN "Leaf"
   WHEN parent_node is NULL THEN "Root"
   ELSE "Inner"
 END
FROM (
 SELECT bst1.n parent_node, bst2.n child_node
 FROM BST bst1
   LEFT JOIN BST bst2 on bst1.n = bst2.p
     WHERE bst1.p IS NOT NULL OR (bst1.p IS NULL AND bst2.p IS NULL)
 UNION
 SELECT bst1.n parent_node, bst2.n child_node
 FROM BST bst1
   RIGHT JOIN BST bst2 on bst1.n = bst2.p
     WHERE bst1.p IS NOT NULL OR (bst1.p IS NULL AND bst2.p IS NULL)
) tmp
GROUP BY parent_node
ORDER BY id;