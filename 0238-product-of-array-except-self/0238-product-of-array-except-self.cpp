class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int size = nums.size(); 
        vector<int> newList (size,1);

        int prod = 1;
        // left pass
        for(int i = 0; i < size; i++){
            newList[i] *= prod;
            prod *= nums[i];
            //cout << "newList[i]: " << newList[i] << "\n";
            //cout << "Prod: " << prod << "\n";
        }
        // right pass
        prod = 1;
        for(int j = size - 1; j >= 0; j--){
            newList[j] *= prod;
            prod *= nums[j];
            //cout << "newList[j]: " << newList[j] << "\n";
            //cout << "Prod: " << prod << "\n\n";
        }
        return newList;
    }
};