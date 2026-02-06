class MyQueue {
public:
    stack<int> S;        
    stack<int> secS;
    
    MyQueue() {

    }

    void push(int x) {
        while (!(S.empty())) {
            secS.push(S.top());
            S.pop();
        }
        S.push(x);
        while (!secS.empty()) {
            S.push(secS.top());
            secS.pop();
        }
    }

    int pop() {
        int front = S.top();
        S.pop();
        return front;
    }

    int peek() {
        return S.top();
    }

    bool empty() {
        return S.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */