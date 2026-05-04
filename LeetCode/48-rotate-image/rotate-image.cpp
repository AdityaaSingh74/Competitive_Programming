class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int col = matrix[0].size();
        int row = matrix.size();
        int temp;
        for(int i=0;i<row;i++){
            for(int j=i+1;j<col;j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        int n=col-1;
        for(int i=0;i<col/2;i++){
            for(int j=0;j<(row);j++){
                temp = matrix[j][i];
                matrix[j][i] = matrix[j][n];
                matrix[j][n] = temp;
            }
            n--;
        }

    }
};