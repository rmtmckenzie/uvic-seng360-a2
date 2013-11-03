import question_template

game_type = 'bullseye'
source_language = 'C'

parameter_list = [
	['$t0','target'],['$x1','int'],
]

tuple_list = [
	['list_lib_find_two_',
		[True,None],
	]
]

global_code_template = '''\
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
d	#include &lt;stdio.h>
x	#include <stdio.h>
dx
dx	#define LL_SUCCESS 1
dx	#define LL_RANGE_ERROR -1
dx	#define LL_MEMORY_ERROR -2
dx
dx	struct node {
dx		int x;
dx		struct node * next;
dx	};
dx
dx	struct node* ll_find(struct node*, int);
dx	int ll_add_at(struct node**, int, int);
dx	int ll_remove(struct node**, int);
dx	void ll_free(struct node**);
dx
dx	int ll_add_at(struct node** head_ptr,int x,int i)
dx	{
dx		struct node *new,*current;
dx
dx		// if i < 0 or i > n, out of range
dx		if (i < 0 || (*head_ptr == NULL && i > 0)) {
dx			return LL_RANGE_ERROR;
dx		}
dx
dx		// if the list is empty or add the new node at the front
dx		if (*head_ptr == NULL || i == 0) {
dx			// create and initialize a new node
dx			new = (struct node*)malloc(sizeof(struct node));
dx			if (new == NULL) {
dx				return LL_MEMORY_ERROR;
dx			}
dx			new->x = x;
dx
dx			// link in the new node
dx			new->next = *head_ptr; // may be NULL
dx			*head_ptr = new;
dx			return LL_SUCCESS;
dx		}
dx
dx		// iterate current to position i-1
dx		for (current = *head_ptr; i > 1; i--) {
dx			// i > n, out of range
dx			if (current->next == NULL) {
dx				return LL_RANGE_ERROR;
dx			}
dx			current = current->next;
dx		}
dx
dx		// create and initialize a new node
dx		new = (struct node*)malloc(sizeof(struct node));
dx		if (new == NULL) {
dx			return LL_MEMORY_ERROR;
dx		}
dx		new->x = x;
dx
dx		// link in the new node
dx		new->next = current->next; // may be NULL
dx		current->next = new;
dx
dx		return LL_SUCCESS;
dx	}
dx
dx	int ll_remove(struct node** head_ptr,int x)
dx	{
dx		struct node *previous,*current;
dx
dx		// the list is empty, nothing can be removed
dx		if (*head_ptr == NULL) {
dx			return LL_RANGE_ERROR;
dx		}
dx
dx		// if x is found in the first node
dx		if ((*head_ptr)->x == x) {
dx			current = *head_ptr;
dx
dx			// free the first node; update *head_ptr
dx			*head_ptr = (*head_ptr)->next;
dx			free(current);
dx			return LL_SUCCESS;
dx		}
dx
dx		// for each node
dx		current = *head_ptr;
dx		previous = *head_ptr;
dx		while (current != NULL) {
dx			// if x is found
dx			if (current->x == x) {
dx				// exclude the node containing x
dx				previous->next = current->next;
dx
dx				// free the node
dx				free(current);
dx				return LL_SUCCESS;
dx			}
dx
dx			// move to next node
dx			previous = current;
dx			current = current->next;
dx		}
dx
dx		// if we get here, then x is not found
dx		return LL_RANGE_ERROR;
dx	}
dx
dx	struct node* ll_find(struct node* head,int x)
dx	{
dx		// if the list is empty
dx		if (head == NULL) {
dx			return NULL;
dx		}
dx
dx		// for each node
dx		for (; head != NULL; head = head->next) {
dx			// if x is found
dx			if (head->x == x) { $t0
dx				return head;
dx			}
dx		}
dx
dx		// if we get here, then x is not found
dx		return NULL;
dx	}
'''

main_code_template = '''\
dx		struct node *list_head = NULL;
dx	
dx		ll_add_at(&list_head,1,0);
dx		ll_add_at(&list_head,3,1);
dx		ll_find(list_head,$x1);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
