import question_template

game_type = 'bullseye'
source_language = 'C'

parameter_list = [
	['$t0','target'], ['$t1','target'],['$t2','target'],['$x1','string'],
]

tuple_list = [
	['word_storage_find_bull_',
		[True,False,False,None],
		[False,True,False,None],
		[False,False,True,None],
	]
]

global_code_template = '''\
d	#include &lt;stdlib.h>
x	#include <stdlib.h>
d	#include &lt;stdio.h>
x	#include <stdio.h>
d	#include &lt;string.h>
x	#include <string.h>
dx
dx	#define SUCCESS 0
dx	#define MEMORY_ERROR -1
dx	#define MAX_WORDS 2
dx	static char **word_list;
dx	static int word_list_length;
dx	static int num_words;
dx
dx	int ws_init(void)
dx	{
dx		// create an empty word_list with default space
dx		word_list_length = MAX_WORDS;
dx		num_words = 0;
dx		word_list = malloc(word_list_length * sizeof(char*));
dx		if (word_list == NULL) {
dx			return MEMORY_ERROR;
dx		} else {
dx			return SUCCESS;
dx		}
dx	}
dx
dx	int ws_add_word(char *word)
dx	{
dx		int insert_position,i,n;
dx
dx		// if word_list is full, double its size
dx		if (num_words >= word_list_length) {
dx			word_list_length *= 2;
dx			word_list = realloc(word_list, word_list_length*sizeof(char*));
dx			if (word_list == NULL) {
dx				return MEMORY_ERROR;
dx			}
dx		}
dx
dx		// find position to insert word
dx		for (insert_position = 0;
dx		 insert_position < num_words;
dx		  insert_position++) {
dx			n = strcasecmp(word,word_list[insert_position]);
dx			if (n == 0) { // already in word_list: ignore
dx				return SUCCESS;
dx			} else if (n < 0) { // insert position found
dx				break;
dx			}
dx		}
dx
dx		// shift word_list[i..num_words-1] to the right
dx		num_words++;
dx		for (i = num_words-1; i > insert_position; i--) {
dx			word_list[i] = word_list[i-1];
dx		}
dx
dx		// insert word in place
dx		word_list[insert_position] = malloc(strlen(word)+1);
dx		if (word_list[insert_position] == NULL) {
dx			return MEMORY_ERROR;
dx		}
dx		strcpy(word_list[insert_position],word);
dx
dx		return SUCCESS;
dx	}
dx
dx	int ws_find_word(const char *word)
dx	{
dx		int high,low,mid,compare;
dx
dx		low = 0;
dx		high = num_words - 1;
dx		while (low <= high) {
dx			mid = (low+high)/2;
dx			compare = strcasecmp(word,word_list[mid]);
dx			if (compare < 0) { $t0
dx				high = mid-1;
dx			} else if (compare == 0) { $t1
dx				return 1;
dx			} else { $t2
dx				low = mid+1;
dx			}
dx		}
dx		return 0;
dx	}
'''

main_code_template = '''\
dx		int i;
dx		char* words[] = {"cat"};
dx	
dx		ws_init();
dx		for (i = 0; i < 1; i++)
dx			ws_add_word(words[i]);
dx		ws_find_word($x1);
'''

argv_template = ''

stdin_template = ''

stdout_template = ''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
