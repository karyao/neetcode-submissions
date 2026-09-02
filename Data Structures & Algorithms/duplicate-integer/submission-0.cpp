#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hashTable; 
        
        for(int i = 0; i < nums.size(); i++) {
            hashTable.insert(nums[i]);
        }

        if(nums.size() != hashTable.size()) {
            return true;
        }
        return false;
    }
};
