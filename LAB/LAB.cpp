#include <iostream>
using namespace std;
// Implementation of a stack using Array & Linkdlist

/* typedef struct node{
    int val;
    struct node *next;
    node(int a = 0){
        val = a;
        next = NULL;
        }
        } node;
        
class StackLL{
    public:
    node *head = NULL;

    int peek(){
        if (head == NULL){
            cout<<"No elements to show";
            return -1;
        }
        return head->val;
    }

    void push(int val=0){
        node* neww = new node(val);
        if (head == NULL){
            head = neww;
            return;
        }
        neww->next = head;
        head->next = neww;
    }

    int pop(){
        if (head==NULL){
            cout<<"UNDERFLOW";
            return -1;
        }
        int val = head->val;
        node* ptr = head;
        head = head->next;
        delete ptr;
        return val;
    }

    bool isempty(){
        if head==NULL{return True}
        else{return False}
    }

}; */

/* 

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

};

void insertAtBottom(int x){
    
    if (top==-1){
        arr[++top]=x;
        return;
    }
    int temp=arr[top--];
    insertAtBottom(x);
    arr[++top]=temp;
}

void reverseStack(){
    if (top==-1) return;
    int temp=arr[top--];
    
    reverseStack();
    insertAtBottom(temp);
} */

/* class Stack{
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
int main(){
    int a[]={4, 8, 5, 2, 25},n=5, ans[5];
    Stack arrr;
    for(int i=n-1; i>=0; i--){
        while(arrr.empty()!=NULL){
            arrr.pop();
        }

        if(arrr.empty()){ 
        ans[i]=-1;
        }else {
        ans[i]=arrr.peek();
        }
        arrr.push(a[i]);
    }
    for(int i=0;i<n;i++)
        cout<<ans[i];

    return 0;
}
 */

#include<iostream>
using namespace std;

class Stack{
public:
    int arr[50];
    int top=-1;

    void push(int x){
        arr[++top]=x;
    }

    int pop(){
        return arr[top--];
    }

    int empty(){
        return top==-1;
    }
};

int main(){
    Stack st;
    string s;
    cin>>s;

    int c=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='('){
            c++;
            st.push(c);
            cout<<c;
        }
        else{
            int x=st.pop();
            cout<<x;
        }
    }
}
