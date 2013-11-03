question_list = [
	# (mark, 	count, [directories])
	# [5] from tutorial: one of each question type
	(1,	2,	['min_io_*']),
	(1,	1,	['min_bull_*']),
	(1,	1,	['min_ff_*']),
	(1,	1,	['min_ll_*']),

	# [5] loops: basic for & while
	(1,	3,	['for_basic_*']),
	(1,	2,	['while_basic_*']),

	# [6] loops: break & continue: for/while
	(1,	2,	['for_break_forward_io_*']),
	(1,	3,	['for_continue_forward_io_*']),
	(1,	1,	['while_break_forward_io_*']),

	# [2] find: work with a specification
	(1,	2,	['for_ff_*']),

	# [2] 3x+1: 1 forward, 1 backward
	(1,	1,	['three_x_forward_*']),
	(1,	1,	['three_x_backward_*']),
]
practice_mode = False
standalone = False
logged = True
log_dir = 'quiz_log'
