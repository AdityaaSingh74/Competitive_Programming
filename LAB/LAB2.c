/* #include <iostream>
using namespace std;

typedef struct node{
    int val;
    struct node *next;
    node(int a = 0){
        val = a;
        next = NULL;
    }
} node;

node *head = NULL;

void insertAtHead(int data){
    node *neww = new node(data);
    if (head == NULL){
        head = neww;
        return;
    }
    neww->next = NULL;
    head->next = neww;
}

void insertAtLast(int data){
    node *neww = new node(data);
    if (head==NULL){
        insertAtHead(data);
        return;
    }
    node* ptr = head;
    while(ptr->next!=NULL){
        ptr=ptr->next;
    }
    ptr->next = neww;
}

void insertAtPos(int data,int pos){
    node *neww = new node(data);
    if (head==NULL){
        insertAtHead(data);
        return;
    }
    node* ptr = head;
    int cnt = 1;
    while(cnt<pos){
        ptr=ptr->next;
        cnt++;
    }
    neww->next = ptr->next;
    ptr->next = neww;
}

void DeleteAtPos(int data){
    node* ptr = head;
    node* ptr1 = ptr;
    while(ptr->val!=data){
        ptr1=ptr;
        ptr=ptr->next;
    }
    ptr1->next = ptr->next ;
    free(ptr);
}

int get(indx){
    node* ptr=head;
    while(indx>=0){
        ptr = ptr->next;
    }
    return ptr->val;
}

void display(){
    node* ptr=head;
    while(ptr != NULL){
        cout<< ptr->val<<"->";
        ptr = ptr->next;
    }
    cout<<"NULL";
}

int main(){
    int ch;
    while (true){
        cout << "\n1. Insert at head \n2. Insert at Last \n3. Insert at Pos \n. Delete at idx \n7. Display \n8. Exit \nEnter your choice: "<< endl;
        cin >> ch;

        switch (ch){
        case 1:{
            int data;
            cout << "Enter data to insert: ";
            cin >> data;
            insertAtHead(data);
            break;
        }

        case 2:{
            int data;
            cout << "Enter data to insert: ";
            cin >> data;
            insertAtLast(data);
            break;
        }
        
        case 3:{
            int data,pos;
            cout << "Enter data to insert: ";
            cin >> data;
            cout << "Enter position: ";
            cin >> pos;
            insertAtPos(data,pos);
            break;
        }

        case 4:{
            int pos;
            cout << "Enter data: ";
            cin >> pos;
            DeleteAtPos(pos);
            break;
        }
        

        case 7:{
            display();
            break;
        }

        case 8:
            exit(0);
        }
    }
    return 0;
} */

/* #include <iostream>
using namespace std;
int t[300];
int h[300];
void initilizer(){
  for(int i=0;i<300;i++){

    t[i] = 0;
    h[i] = 0;
  }

}

void hit(int ts){
  int idx= ts % 300;
  if(t[idx]!=ts){
    t[idx]=ts;
    h[idx]= 1;
  }else{
    h[idx]++;
  }
}

int getHits(int ts){
  int cnt= 0;
  for(int i= 0; i< 300; i++){
    if(ts-t[i]< 300){
      cnt+= h[i];
    }
  }
  return cnt;
}

int main(){
  initilizer();
  hit(300);
  hit(301);
  cout<<getHits(4)<<endl;
  cout<<getHits(300)<<endl;
  cout<<getHits(301)<<endl;
  return 0;
} */

/* #include <iostream>
using namespace std;

class Node {
public:
    string link;
    
    Node* prev;
    Node* next;
    
    Node(string u) {
        link = u;prev = NULL;
        next = NULL;
    
    }
};

class brow {
    public:
    
    Node* curr;
    brow(string home) {
        
        curr = new Node(home);
    }

    void vis(string link) {
        Node* temp = new Node(link);
        
        curr->next = temp;
        
        temp->prev = curr;

        curr = temp;

    }
    string back(int cnt) {
        while (cnt>0 && curr->prev!=NULL) {
        
            curr = curr->prev;
            cnt--;

        }

        return curr->link;

    }


    string forw(int cnt) {
        while (cnt>0 && curr->next!=NULL) {
        
            curr = curr->next;
        
            cnt--;
        }
        
        return curr->link;
    }
    void display() {
        
        cout<< curr->link<< endl;
    }
};
void main(){
    
    brow b(" adityahandsome.in");
    
    b.display();
    
    cout<<b.back(1);
    
    cout<<b.forw(1);
    
}
 */


/* #include<iostream>

using namespace std;

class counter {

    public:

    int time[300];
    int hit[300];

    counter() {

        for(int i=0; i<300; i++) {
            time[i]=0;
            hit[i]= 0;
        }

    }

    void hit(int ts) {

        int idx= ts%300;

        if(time[idx]!= ts){

            time[idx]= ts;

            hit[idx]= 1;

        }

        else{

            hit[idx]++;

        }

    }

    int getHit(int ts){

        int ans= 0;

        for(int i=0; i<300; i++) {

            if ((ts-time[i])< 300) {

                ans+= hit[i];

                
            }
        
        }
        
        return ans;
    
    }

}; */
typedef struct ListNode {
    int val;
    struct ListNode* next;
}ListNode;

ListNode* reverseList(ListNode* head) {
    ListNode* p = NULL;
    ListNode* c = head;
    ListNode* n = NULL;

    while (c != NULL) {
        n = c->next;   
        c->next = p;   
        p = c;         
        c = n;         
    }
    return p;  
}


/* struct ListNode {
    int val;
    struct ListNode* next;
};

int isPalindrome(struct ListNode* head) {
    struct ListNode *slow = head, *fast = head, *prev = 0;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    prev = slow;
    slow = slow->next;
    prev->next = 0;

    while (slow) {
        struct ListNode* next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    fast = head;
    slow = prev;

    while (slow) {
        if (fast->val != slow->val)
            return 0;
        fast = fast->next;
        slow = slow->next;
    }

    return 1;
}
 */


