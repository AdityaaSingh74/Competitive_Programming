class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s1;

        for (int i = 0; i < operations.size(); i++) {
            if (operations[i] == "C") {
                s1.pop();
            }
            else if (operations[i] == "D") {
                s1.push(s1.top() * 2);
            }
            else if (operations[i] == "+") {
                int top1 = s1.top(); 
                s1.pop();
                int top2 = s1.top();
                s1.push(top1);
                s1.push(top1 + top2);
            }
            else {
                s1.push(stoi(operations[i]));
            }
        }

        int sum = 0;
        while (!s1.empty()) {
            sum += s1.top();
            s1.pop();
        }

        return sum;
    }
};