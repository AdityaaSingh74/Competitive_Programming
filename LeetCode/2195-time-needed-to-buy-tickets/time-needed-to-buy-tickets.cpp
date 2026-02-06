class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int n= tickets.size();
        int cnt= 0;
        while(true) {
            for(int i=0;i<n;i++){
                if(tickets[i]>0) {
                    tickets[i]= tickets[i]-1;
                    cnt++;
                }
                if(i==k && tickets[i]==0 ){
                    return cnt;}
            }
        }
        return 0;
    }
};