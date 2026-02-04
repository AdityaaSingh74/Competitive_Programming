class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            int jump = abs(nums[i]) - 1;
            if (nums[jump] < 0) {
                ans.push_back(abs(nums[i]));
                continue;
            }
            nums[jump] = nums[jump] * -1;
        }
        return ans;
    }
};