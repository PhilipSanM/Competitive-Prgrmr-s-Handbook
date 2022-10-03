#include<bits/stdc++.h>
#include<iostream>
using namespace std;

class node{
public:
    int data;
    node* next;

    node(int data){
        this->data = data;
        next = NULL;
    }
};

bool containsCycle(node *head){
    unordered_map<node*, bool> hashtable;
    node *temp = head;
    while(temp!=NULL){

        // Check if temp already exists in the hashtable
        if(hashtable.count(temp) != 0){
            return true;
        }
        // Insert in the hashtable
        hashtable[temp] = true;
        temp = temp->next;

    }
    return false;

}

void insertAtHead(node *head, int data){
    if(head == NULL){
        head = new node(data);
        return;
    }

    //Otherwise

    node *n = new node(data);
    n->next=head;
    head=n;


}

int main(){

    node * a = NULL;
    insertAtHead(a,34);
    insertAtHead(a,2);
    insertAtHead(a,4);
    insertAtHead(a,8);
    insertAtHead(a,10);
    insertAtHead(a,11);

    containsCycle(a)? cout << "Cycle found" : cout << "Cycle not found";

    return 0;
}