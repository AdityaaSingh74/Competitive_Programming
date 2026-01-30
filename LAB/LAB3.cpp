#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Stack{
    public:
    int arr[50];
    int top=-1;

    int peek(){
        if (top==-1){
            cout<<"No elements to show";
            return -1;
        }
        return arr[top];
    }

    void push(int val=0){
        if (top>=50){
            cout<< "OVERFLOW";
            return ;
        }
        arr[++top]= val;
    }

    int pop(){
        if (top==-1){
            cout<<"UNDERFLOW";
            return -1;
        }
        return arr[top--];
    }
    int empty(){
        return top==-1;
    }

};

class Solution {
public:
    int calPoints(vector<string>& operations) {
        Stack s1;
        for(int i=0;i<operations.size();i++){
            if( operations[i] == "C"){
                s1.pop();
            }
            else if(operations[i]=="D"){
                s1.push(s1.peek()*2);
            }else if(operations[i]=="+"){
                int top = s1.pop();
                int newpop = s1.peek() + top;
                s1.push(top);
                s1.push(newpop);
            }else{
                s1.push(std::stoi(operations[i]));
            }
        }
        int sum=0;
        while(!s1.empty()){
            sum+=s1.pop();
        }
        return sum;
    }

    int calculate(string s) {
        if (s.size()==0){
            return 0;
        }
        Stack s1;
        int n = s.size();
        for(int i=0;i<n;i++){
            char curr = s[i];
            switch(curr){
                case '+':   s1.push(stoi(curr));
                            break;
                case '-':   s1.push(stoi(curr) * -1);
                            break;
                case '*':   int a=s1.pop();
                            i++;
                            s1.push(stoi(s[i])*a);
                            break;
                case '/':   int a=s1.pop();
                            i++;
                            s1.push(a/stoi(s[i]));
                            break;
                default:    s1.push(stoi(curr)); 
            }
        }
        int ans=0;
        while(!s1.empty()){
            ans+=s1.pop();
        }
        return ans;
    }
    string removeDuplicateLetters(string s) {
        
    }
    string decodeString(string s) {
        
    }

};