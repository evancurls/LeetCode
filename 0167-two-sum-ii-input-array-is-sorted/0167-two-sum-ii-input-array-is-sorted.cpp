class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int a = 0, b = numbers.size() - 1;
        while (a < b){
            int sum = numbers[a] + numbers[b];
            if(sum > target){
                b--;
            } else if (sum < target){
                a++;
            } else{
                return vector<int> {a + 1, b+ 1};
            }
        }
        return {}; //shouldnt appear
    }
};