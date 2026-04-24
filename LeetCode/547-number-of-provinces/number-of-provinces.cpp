#include <vector>
using namespace std;

class Solution {
public:

    int findCircleNum(vector<vector<int>>& cityMatrix) {

        int n = cityMatrix.size();

        vector<int> seenState(n, 0);

        int groupTotal = 0;

        for (int start = 0; start < n; start++) {

            if (seenState[start] == 1) {
                continue;
            }

            vector<int> helperQueue;
            helperQueue.push_back(start);

            int moveIndex = 0;

            while (moveIndex < helperQueue.size()) {

                int currentCity = helperQueue[moveIndex];
                moveIndex++;

                if (seenState[currentCity] == 1) {
                    continue;
                }

                seenState[currentCity] = 1;

                for (int check = 0; check < n; check++) {

                    if (cityMatrix[currentCity][check] == 1 && seenState[check] == 0) {
                        helperQueue.push_back(check);
                    }
                }
            }

            groupTotal++;
        }

        return groupTotal;
    }
};