#include <stdio.h>
#include <conio.h>
#include <stdlib.h>


struct node
{
    int data;
    struct node *next;

};
struct node *head, *new_node, *temp, *prev_node, *nextnode;
int main()
{
    int ch;
    void create();
    void insert_beg();
    void insert_end();
    void insert_pos();
    void display();
    void delete_beg();
    void delete_end();
    void delete_pos();

    while(1)
    {
        printf("\n\n --------- Singly Linked List --------");
        printf("\n 1.Create\n 2.Insert\n 3.Display \n 4.Delete \n 5.Exit\n\n");
        printf("Enter your choice(1-4):");
        scanf("%d", &ch);

        switch(ch){
            case 1:
                create();
                break;
            case 2:
                printf("\n----- Insert Menu------");
                printf("\n 1.Insert at beginning\n 2.Insert at end\n 3.Insert at specified position");
                printf("\n\n Enter your choice(1-3):");
                scanf("%d",&ch);

                switch(ch)
                {
                    case 1:
                        insert_beg();
                        break;
                    case 2:
                        insert_end();
                        break;
                    case 3:
                        insert_pos();
                        break;
                    default:
                        printf("Wrong choice");
                }
                break;
            case 3:
                display();
                break;
            case 4:
                printf("\n----- Delete Menu------");
                printf("\n 1.Delete from beginning\n 2.Delete from end\n 3.Delete from specified position");
                printf("\n\n Enter your choice(1-4):");
                scanf("%d",&ch);

                switch(ch)
                {
                case 1:
                    delete_beg();
                    break;
                case 2:
                    delete_end();
                    break;
                case 3:
                    delete_pos();
                    break;

                default:
                    printf("Wrong choice");
                }
                break;
             case 5:
                exit(0);
             default:
                printf("Wrong choice.");
        }
    }
    return 0;
}
void create()
{

    new_node = (struct node *)malloc(sizeof(struct node));
    printf("\nEnter data:");
    scanf("%d",&new_node->data);
    new_node->next = 0;
    if(head == NULL)
    {
        head = temp = new_node;
    }
    else
    {
        temp->next = new_node;
        temp = new_node;
    }
}
void insert_beg()
{

    new_node = (struct node*)malloc(sizeof(struct node));
    printf("Enter data:");
    scanf("%d",&new_node->data);
    new_node->next = head;
    head = new_node;

}
void insert_end()
{

    new_node = (struct node*)malloc(sizeof(struct node));
    printf("Enter data:");
    scanf("%d",&new_node->data);
    new_node->next = NULL;
    temp = head;
        while(temp->next!= NULL)
        {
            temp = temp->next;
        }
        temp->next = new_node;
}
 void insert_pos()
{
    int pos, i, count=0;

    new_node = (struct node*)malloc(sizeof(struct node));

    printf("Enter position to insert:");
    scanf("%d",&pos);

    temp = head;
    while(temp != 0)
    {
        temp = temp->next;
        count++;
    }
    if(pos>count)
    {
        printf("Invalid position");
    }
    else
    {
        temp = head;
        for(i=1;i<pos;i++){
            temp = temp->next;
        }
        printf("Enter data:");
        scanf("%d",&new_node->data);
        new_node->next = temp->next;
        temp->next = new_node;
    }

}
void display()
{
    temp = head;
    while (temp != NULL)
    {
        printf("%3d",temp->data);
        temp = temp->next;

    }
}
void delete_beg()
{
    temp = head;
    head = head->next;
    free(temp);
}
void delete_end()
{
    temp = head;
    while (temp->next != NULL)
    {
        prev_node = temp;
        temp = temp->next;
    }
    if(temp = head)
    {
        head = 0;
        free(temp);
    }
    else
    {
        prev_node->next = NULL;

    }
    free(temp);
}
void delete_pos()
{
    int pos,i=1;
    temp = head;
    printf("Enter position:");
    scanf("%d",&pos);
    while (i<pos-1)
    {
        temp = temp->next;
        i++;
    }
    nextnode = temp->next;
    temp->next = nextnode->next;
    free(nextnode);

}


