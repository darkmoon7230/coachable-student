// Link to problem: https://leetcode.com/problems/3sum/description/
// Loom explaining solution you wrote (5m):
// Solution:
// Description:
// Sort the array first and iterate through every element and hold the remaining
// as a two-sum problem Key ideas Two-sum (hashmap/ two pointer) Difficulty:
// Hard

class Solution {
  struct VectorHash {
    size_t operator()(const std::vector<int> &v) const {
      std::hash<int> hasher;
      size_t seed = 0;
      for (int i : v) {
        seed ^= hasher(i) + 0x9e3779b9 + (seed << 6) + (seed >> 2);
      }
      return seed;
    }
  };

public:
  vector<vector<int>> threeSum(vector<int> &nums) {
    // N log N
    sort(nums.begin(), nums.end());

    // N^2
    vector<vector<int>> s;
    for (auto i = 0; i < nums.size() - 1; ++i) {
      int target = nums[i] * -1;
      int lo = i + 1, up = nums.size() - 1;
      while (lo != up) {
        auto sum = nums[lo] + nums[up];
        if (sum == target) {
          // vector<int> trip = {nums[lo], nums[up], nums[i]};
          // sort(trip.begin(), trip.end());
          s.push_back({nums[lo], nums[up], nums[i]});

          do {
            lo += 1;
          } while (lo < up && nums[lo] == nums[lo + 1]);
          wi
        } else if (sum > target) {
          up -= 1;
        } else {
          lo += 1;
        }
      }
    }

    // N
    return vector<vector<int>>(s.begin(), s.end());
  }
};