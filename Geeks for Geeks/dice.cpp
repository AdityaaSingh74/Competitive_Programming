// User function Template for C++
class Solution {
  public:
    int oppositeFaceOfDice(int n) {
        // Write Your Code here
        switch(n){
            case 1: return 6 ; break;
            case 2: return 5 ; break;
            case 3: return 4 ; break;
            case 4: return 3 ; break;
            case 5: return 2 ; break;
            case 6: return 1 ; break;
        }
    }
};