import question_template

game_type = 'input_output'
source_language = 'C'

parameter_list = [
	['$x1','int'],['$x2','int'],['$x3','string'],['$y0','int']
]

tuple_list = [
	['word_storage_find_io_',
		[0,0,'"goose"',None],
		[0,1,'"fox"',None],
		[0,2,'"eagle"',None],
		[0,3,'"dog"',None],
		[0,4,'"cat"',None],
		[0,5,'"goose"',None],
		[2,0,'"fox"',None],
		[2,1,'"eagle"',None],
		[2,2,'"dog"',None],
		[2,3,'"cat"',None],
		[4,0,'"goose"',None],
		[4,1,'"fox"',None],
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
dx			if (compare < 0)
dx				high = mid-1;
dx			else if (compare == 0)
dx				return 1;
dx			else
dx				low = mid+1;
dx		}
dx		return 0;
dx	}
'''

main_code_template = '''\
dx		int i;
dx		char* words[] = {"cat", "dog", "eagle", "fox", "goose"};
dx	
dx		ws_init();
dx		for (i = 0; i < $x2; i++)
dx			ws_add_word(words[i+$x1]);
dx		printf("%d\\n", ws_find_word($x3));
'''

argv_template = ''

stdin_template = ''

stdout_template = '''\
$y0
'''

question = question_template.Question_template(game_type,source_language,
 parameter_list,tuple_list,global_code_template,main_code_template,
 argv_template,stdin_template,stdout_template)
