class Solution {
   public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> hashmap;

        for (int& item : nums) {
            if (hashmap.find(item) == hashmap.end())
                hashmap.insert({item, 0});
            else {
                return true;
            }
        }

        return false;
    }
};