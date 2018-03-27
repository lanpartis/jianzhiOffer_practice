//输入一个整数(int型)，输出该数二进制表示中1的个数。其中负数用补码表示。
//python不太适合，故使用c++

class Solution {
public:
     int  NumberOf1(int n) {
         int cur = 1,sum = 0;
         for(int i=0;i<32;i++){
             if(cur&n){
                 sum++;
             }
             cur = cur<<1;
         }
         return sum;
     }
};
