q=../../../question_library/code_activator/python

echo "------------- control"
rm -rf $q/control/*
code_activator_generate.py control/for_break_io.py $q/control
code_activator_generate.py control/min3_be.py $q/control
code_activator_generate.py control/while_continue_io.py $q/control

echo "------------- lists"
rm -rf $q/lists/*
code_activator_generate.py lists/list_indexing_io.py $q/lists
code_activator_generate.py lists/list_multi_to_one_reference_io.py $q/lists
code_activator_generate.py lists/list_reference_semantics_io.py $q/lists
code_activator_generate.py lists/list_slices_defaultUL_io.py $q/lists
code_activator_generate.py lists/list_slices_out_of_range_io.py $q/lists
code_activator_generate.py lists/list_slices_replace_io.py $q/lists
code_activator_generate.py lists/range_advanced_io.py $q/lists

echo "------------- misc"
rm -rf $q/misc/*
code_activator_generate.py misc/shift_io.py $q/misc
code_activator_generate.py misc/dict_io.py $q/misc

echo "------------- re"
rm -rf $q/re/*
code_activator_generate.py re/date.py $q/re
code_activator_generate.py re/group.py $q/re
code_activator_generate.py re/list.py $q/re
code_activator_generate.py re/nonmatch_group.py $q/re
code_activator_generate.py re/operators.py $q/re

echo "------------- tutorial"
rm -rf $q/tutorial/*
code_activator_generate.py tutorial/min_be.py $q/tutorial
code_activator_generate.py tutorial/min_ff.py $q/tutorial
code_activator_generate.py tutorial/min_io.py $q/tutorial
