class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] count = new int[101];
        for(int i:nums){
            count[i]++;
        }
        int[] ans = new int[nums.length];
        int i=0;
        while(i<nums.length){
            for(int j=1;j<=100;j++){
                if(count[j]>0){
                    ans[i++]=j;
                    count[j]--;
                }
            }
        }
        return ans;
    }
}
