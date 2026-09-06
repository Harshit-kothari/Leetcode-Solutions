// Last updated: 9/6/2026, 7:46:03 PM
class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int l = 0, h = n-1;
        int p = 0;
        while(l<=h){
            p = l+(h-l)/2;
            if(nums[p]==target)
                return p;
            if(target<nums[p])
                h = p-1;
            else
                l = p+1;
        }
        return -1;
    }
}