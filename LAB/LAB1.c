#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node* next;
} Node;

typedef struct DoubleNode {
  int data;
  struct DoubleNode* bottom;
  struct DoubleNode* next;
} DoubleNode;

Node* head = NULL;
DoubleNode* dhead = NULL;

int deleterepeated(){
  if (head == NULL){
    return 0;
}

  Node* ptr = head;
  Node* pptr = NULL;

  while (ptr->next != NULL){
    pptr = ptr;
    ptr = ptr->next;
    if (pptr->data == ptr->data){
      pptr->next = ptr->next;
      free(ptr);
      ptr = pptr;
    }
  }
  return 0;
}

void deleteathalf(){
  if (head == NULL){
    return;
}

  Node* ptr = head;
  Node* pptr = NULL;
  int cnt = 0;

  while (ptr != NULL){
    cnt++;
    ptr = ptr->next;
  }

  cnt = cnt / 2;
  int i = 0;
  ptr = head;

  while (i < cnt){
    pptr = ptr;
    ptr = ptr->next;
    i++;
  }
  if (pptr != NULL){
    pptr->next = ptr->next;
    free(ptr);
  }
}

void ConvertArrayToLinkedList(int arr[], int n){
  Node* new = NULL;
  for (int i = n - 1; i >= 0; i--){
    new = (Node*)malloc(sizeof(Node));
    new->data = arr[i];
    new->next = head;
    head = new;
  }
}

void sortlinkedlist(){
  Node* ptr = head;
  Node* pptr = NULL;
  int temp;

  while (ptr != NULL){
    pptr = ptr->next;
    while (pptr != NULL){
      if (ptr->data > pptr->data){
        temp = ptr->data;
        ptr->data = pptr->data;
        pptr->data = temp;
      }
      pptr = pptr->next;
    }
    ptr = ptr->next;
  }
}

void printsingle(Node* ptr){
  while (ptr != NULL){
    printf("%d -> ", ptr->data);
    ptr = ptr->next;
  }
  printf("NULL\n");
}


DoubleNode* merge(DoubleNode* a, DoubleNode* b){
  DoubleNode* result = NULL;
  if (a == NULL){
    return b;
}
  if (b == NULL)
    return a;

  if (a->data < b->data){
    result = a;
    result->bottom = merge(a->bottom, b);
  }

  else{
    result = b;
    result->bottom = merge(a, b->bottom);
  }

  result->next = NULL;
  return result;
}



DoubleNode* flatten(DoubleNode* dhead){
  if (dhead == NULL || dhead->next == NULL)
    return dhead;
  dhead->next = flatten(dhead->next);
  dhead = merge(dhead, dhead->next);
  return dhead;
}

DoubleNode* createnode(int data){
  DoubleNode* new = (DoubleNode*)malloc(sizeof(DoubleNode));
  new->data = data;
  new->next = NULL;
  new->bottom = NULL;
  return new;
}

void printlist(DoubleNode* ptr){
  while (ptr != NULL){
    printf("%d -> ", ptr->data);
    ptr = ptr->bottom;
  }
  printf("NULL\n");
}

int main(){
  int arr1[] = {1,2,3,4,5};
  ConvertArrayToLinkedList(arr1, 5);
  printsingle(head);
  head = NULL;
  int arr2[] = {4,2,5,1,3};

  ConvertArrayToLinkedList(arr2, 5);

  sortlinkedlist();

  printsingle(head);

  head = NULL;
  int arr3[] = {1,1,2,2,3,3};

  ConvertArrayToLinkedList(arr3, 6);
  deleterepeated();
  printsingle(head);

  head = NULL;
  int arr4[] = {1,2,3,4,5};
  ConvertArrayToLinkedList(arr4, 5);
  deleteathalf();
  printsingle(head);

  head = NULL;
  int arr5[] = {1,2,3,4};
  ConvertArrayToLinkedList(arr5, 4);
  deleteathalf();
  printsingle(head);

  dhead = createnode(5);
  dhead->bottom = createnode(7);
  dhead->bottom->bottom = createnode(8);
  dhead->bottom->bottom->bottom = createnode(30);
  dhead->next = createnode(10);
  dhead->next->bottom = createnode(20);
  dhead->next->next = createnode(19);
  dhead->next->next->bottom = createnode(22);
  dhead->next->next->bottom->bottom = createnode(50);
  dhead->next->next->next = createnode(28);
  dhead->next->next->next->bottom = createnode(40);
  dhead->next->next->next->bottom->bottom = createnode(45);
  dhead = flatten(dhead);
  printlist(dhead);


  return 0;
}

