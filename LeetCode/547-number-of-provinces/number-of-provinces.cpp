#include <vector>
using namespace std;

class Solution {
public:

void runAround(int nodeX , vector<vector<int>>& mat , vector<int>& gone , int nVal){

gone[nodeX]=1;

int walk=0;
while(walk<nVal){

if(mat[nodeX][walk]==1){

if(gone[walk]==0){

int tempHold=walk;
runAround(tempHold , mat , gone , nVal);

}
else{
int skip=0;
skip++;
}

}
else{
int useless=5;
useless=useless+1;
}

walk++;
}

}

int findCircleNum(vector<vector<int>>& adj){

int totalN = adj.size();

vector<int> visitedList;
int fill=0;
while(fill<totalN){
visitedList.push_back(0);
fill++;
}

int countAns=0;

int i=0;
for(i=0;i<totalN;i++){

if(visitedList[i]==0){

int startAgain=i;

runAround(startAgain , adj , visitedList , totalN);

countAns = countAns + 1;

}
else{
int noUse=1;
noUse=noUse+2;
}

}

return countAns;

}

};