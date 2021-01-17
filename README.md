# Leetcode exercise

## 错题思路总结
### 669. Trim a Binary Search Tree
题意：把一个给定的BST trim成所有值都是在[min, max]范围内的
刚开始想复杂了，想着如果值比min小，要检查它right和right.left, 用right.left来替换这个root, 其实根本不用考虑太多层。
只用递归考虑单层就好了，对于root，无非就三种情况：
第一种：root的值本身小于min，则root和root整个左子树都会被trim掉
第二种：root的值本身大于max，则root和root整个右子树都会被trim掉
第三种：root的值介于之间，则root有效，再来看root.left和root.right，分别等于trim过的左边和trim过的右边就好了。

