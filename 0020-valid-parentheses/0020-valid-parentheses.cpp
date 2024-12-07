class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char,char> closeToOpen = {
            {')','('}, 
            {'}','{'}, 
            {']','['}
        };

        for(char c : s){
            //check to see if list is an exit bracket
            if(closeToOpen.count(c)){ //if is a close bracket
                if(!stack.empty() && closeToOpen[c] == stack.top()){
                    stack.pop();
                } else {
                    return false;
                }

            } else { //if is an open bracket
                stack.push(c);
            }
        }
        return stack.empty();
    }
};