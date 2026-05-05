class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        while( low <= high){
            int midpoint = low + (high -  low) / 2;
            if(nums[midpoint] == target){
                return midpoint;
            }
            else if(nums[midpoint] < target){
                low = midpoint + 1;
            }
            else{
                high = midpoint - 1;
            }

        }
        return -1;
    }
};
