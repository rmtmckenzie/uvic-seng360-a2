game_type = 'input_output'

source_language = 'C'

parameter_list = [
	['$n','int'],['$x0','int'],['$x1','int'],['$x2','int'],
	['$y0','string'],['$y1','string'],['$y2','string'],
]

tuple_list = [
	['delete_',	
		# base tuple
		# [3, 0,1,2, 'E D F','D F','B'],
		[3, 0,1,2, None, None, None], # forward
		[3, None,None,None, 'E D F','D F','B'], # backward
		[3, 0,None,2, 'E D F',None,'B'], # mixed

		# base tuple
		# [3, 2,0,1, 'B','D F','B'],
		[3, 2,0,1, None,None,None], # forward
		[3, None,None,None, 'B','D F','B'], # backward
		[3, 2,None,1, 'B',None,'B'], # mixed

		# base tuple
		# [3, 1,2,0, 'D F','B','B'],
		[3, 1,2,0, None,None,None], # forward
		[3, None,None,None, 'D F','B','B'], # backward
		[3, 1,None,0, 'D F',None,'B'], # mixed
	]
]

global_code_template = '''\
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
dx	
dx	struct node {
dx		int x;
dx		struct node *next;
dx	};
dx	
dx	struct node *head = NULL;
dx	
dx	void list_add(int x0)
dx	{
dx		struct node *p;
dx	
dx		p = malloc(sizeof(struct node));
dx		p->x = x0;
dx		p->next = head;
dx		head = p;
dx	}
dx	
dx	void delete(int x)
dx	{
dx		struct node *current, *prev;
dx	
dx		// list length 0
dx		if (head == NULL) {
dx			printf("A\\n");
dx			return;
dx		}
dx	
dx		// x in first node
dx		current = head;
dx		if (current->x == x) {
dx			printf("B\\n");
dx			head = current->next;
dx			free(current);
dx			return;
dx		}
dx	
dx		// list length == 1
dx		if (head->next == NULL) {
dx			printf("C\\n");
dx			return;
dx		}
dx	
dx		// general case: length >= 2 and x not in first node
dx		prev = head;
dx		current = head->next;
dx		while (current != NULL) {
dx			if (current->x == x) {
dx				printf("D ");
dx				prev->next = current->next;
dx				free(current);
dx				current = prev->next;
dx				break;
dx			} else {
dx				printf("E ");
dx				prev = current;
dx				current = current->next;
dx			}
dx		}
dx		printf("F\\n");
dx	}
'''

main_code_template = '''\
dx	
dx		int i;
dx		for (i = 0; i < $n; i++)
dx			list_add(i);
dx
dx		delete($x0);
dx		delete($x1);
dx		delete($x2);
dx
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
$y1
$y2
'''
