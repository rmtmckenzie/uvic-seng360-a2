q=../../question_library/csc111_hm/

rm -rf $q/csc111_hm/*

multiple_choice_generate.py multiple_choice.py $q

code_activator_generate.py q_2.py $q
code_activator_generate.py q_5.py $q
code_activator_generate.py q_15.py $q
code_activator_generate.py q_16.py $q

