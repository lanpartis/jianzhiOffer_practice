newCoder上的《剑指Offer》练习题

结题思路：
1. 杨氏矩阵
2.
3. 递归
4. 利用中序遍历的结果确认父节点，再利用父节点分割前序遍历。因此可以使用分治法解决。
5. 利用另一个空栈倒置当前栈
6. 二分查找
40. 通过异或运算找到a,b的异或值，取异或值中不为1的的位作为区分，将数组分为两组，a和b会分别在两个组中，再对两个数组进行异或运算，每组剩下的一个就是目标数值
41. 动态规划
42. 两个指针一个从头向后一个从尾向前
43. cheat with Python
44. 栈
45. 可以凑成顺子的特性：0以外数字的最大值最小值差小于等于4，最大值最小值的差加上0的个数大于等于4，0以外没有重复数组。
46. 计算每一周之后的余数来模拟循环
47. 使用 and（逻辑与）的短路特性，即当and前部为假时不执行后部。从未控制递归的进行，间接完成判断和循环。
48. 使用位运算完成加法器，注意Python的负数不是补码所以需要额外处理。
49. 使用标志位
50. 把B[i]拆分成前后两个数的乘积，分别用动态规划计算前后两个数组的值。
51. 列出匹配时所有的情况即可
52. 分别判断底数位和指数位
53. 用数组记录各字符的数量
54. 用两个指针，一个每次移动一个Node，一次每个移动两个Node，相遇Node会在环中且由于速度是两倍关系，路程也是两倍关系，可以计算出相遇点到
Entry的距离等于起点到Entry的距离。此时只需要起点与相遇点同时开始走，走到两个指针相同时即为entry
55. 简单题
56. 分为有无右子树两种情况，有右子树时，寻找右子树中左下脚的节点，没有右子树时，需找先祖节点中第一个，given节点或该节点先祖是其left child的先祖。
57. 一棵树是镜像的：一个树左child 和右child的val相等且左child的左子树和右child的右子树对称，左child的右子树和右child的左子树对称.
