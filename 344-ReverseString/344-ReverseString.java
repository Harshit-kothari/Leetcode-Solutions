// Last updated: 4/8/2026, 9:14:01 PM
class Solution {
        public void reverseString(char[] s) {
        int left = 0;
        int end = s.length-1;
        while (left < end) {
      //swap
            char temp = s[left];
            s[left] = s[end];
            s[end] = temp;
      
            left ++;
            end --;
    }
}
}