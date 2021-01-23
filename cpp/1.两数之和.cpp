#include <vector>
#include <map>
using namespace std;

/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */
// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 遍历数组，用目标值减去后的值，看是否在hashmap里,
        // 如果在就返回数组下标，如果不在就把当前值和数组下标插入hashmap里
        map<int, int> marks;
        typedef map<int, int>::iterator ittype;
        for (int i = 0; i < nums.size(); i++)
        {
            int remain = target - nums[i];
            ittype it = marks.find(remain);
            if (it != marks.end())
            {
                vector<int> result = {it->second, i};
                return result;
            }
            else
            {
                marks.insert(pair<int, int>(nums[i], i));
            }
        }
        
        return vector<int>();
    }
};
// @lc code=end

