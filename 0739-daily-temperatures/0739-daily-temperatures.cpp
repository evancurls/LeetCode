class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<pair<int,int>> tempStack;

        std::vector<int> dayTemp (temperatures.size(),0);


        for(int i = 0; i < temperatures.size();i++){
            int n = temperatures[i];

            while(!tempStack.empty() && tempStack.top().first < n){
                pair<int,int> p = tempStack.top();
                tempStack.pop();
                dayTemp[p.second] = i - p.second;
            }

            tempStack.push({n,i});
        }
        return dayTemp;
    }
};