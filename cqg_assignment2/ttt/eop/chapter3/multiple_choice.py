question_groups = [

['multiple_choice_3_1_', # state-oriented programming ----------------

['The C language best supports',
	[
	'logic programming',
	'state-oriented programming',
	'functional programming',
	],
	1],
['Which of the following is a definition in the C language?',
	[
	'<t>x = y;</t>',
	'<t>scanf("%d %d", &x, &y);</t>',
	'<t>int x;</t>',
	'<t>#include &lt;stdio.h></t>',
	],
	2],
],

['multiple_choice_3_2_', # assignment --------------------------------

['How many variables are defined in Figure 3.1?',
	[ '0', '1', '2', '3', '4', ],
	3],

['How many assignment statements are there in Figure 3.1?',
	[ '0', '1', '2', '3', '4', ],
	3],

['What is the type of the variable <t>z</t> in Figure 3.1?',
	[
	'double',
	'int',
	'string',
	'float',
	],
	1],
],

# ['multiple_choice_3_3_', # sequencing --------------------------------
# ],

['multiple_choice_3_4_', # selection----------------------------------

['Which of the values below, when viewed as a condition, evaluates to true?',
	[
	'0',
	'5+3',
	'1/5',
	'7/5',
	],
	[1,3]],
['Which of the values below, when viewed as a condition, evaluates to false?',
	[
	'5+3',
	'7/5',
	'0',
	],
	2],
['Based on Figure 3.3, how many two-sorts (swaps) will be performed if <t>a</t> is 1, <t>b</t> is 2, and <t>c</t> is 3?',
	[ '0', '1', '2', '3', '4', ],
	0],
['Based on Figure 3.3, how many two-sorts (swaps) will be performed if <t>a</t> is 3, <t>b</t> is 2, and <t>c</t> is 1?',
	[ '0', '1', '2', '3', '4', ],
	3],
['Based on Figure 3.3, how many two-sorts (swaps) will be performed if <t>a</t> is 2, <t>b</t> is 1, and <t>c</t> is 3?',
	[ '0', '1', '2', '3', '4', ],
	1],
['Based on Figure 3.3, what is the minimum number of two-sorts (swaps) which will be performed?',
	[ '0', '1', '2', '3', '4', ],
	0],
['Based on Figure 3.3, what is the maximum number of two-sorts (swaps) which will be performed?',
	[ '0', '1', '2', '3', '4', ],
	3],
],

['multiple_choice_3_5_', # functions ---------------------------------
['How many function defintions are there in Figure 3.4?',
	[ '0', '1', '2', '3', '4', ],
	2],
['How many function calls are there in Figure 3.4?',
	[ '0', '1', '2', '3', '4', '5', '6', '7', '8', ],
	6],
['In Figure 3.4, how many parameters does <tt>intcmp</tt> take?',
	[ '0', '1', '2', '3', '4', ],
	2],
['In Figure 3.4, what is the return value type of <tt>intcmp</tt>?',
	[ 'float', 'int', 'char *', ],
	1],
],

['multiple_choice_3_6_', # iteration ---------------------------------
['In figure 3.5, if the while condition is changed to <tt>mpg <= 50<tt>,' +
	'how many times is the loop body executed?',
	['0', '1', '2', '3', '4', '5', '6', '7', '8', ],
	8],
['In figure 3.5, if the while condition is changed to <tt>mpg <= 10<tt>,' +
	'how many times is the loop body executed?',
	['0', '1', '2', '3', '4', '5', '6', '7', '8', ],
	0],
],

['multiple_choice_3_7_', # arrays ------------------------------------
['Given the definition <tt>int a[10]</tt>, ' + 
'what is the largest legal index in <tt>a</tt>?',
	['5', '6', '7', '8', '9', '10', '11', ],
	4],
['Given the definition <tt>int a[100]</tt>, ' + 
'what is the largest legal index in <tt>a</tt>?',
	['97', '98', '99', '100', '101', ],
	2],
],

]
