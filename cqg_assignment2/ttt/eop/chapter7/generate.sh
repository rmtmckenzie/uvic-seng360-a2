q=../../../question_library/eop/chapter7/

rm -rf $q/*

# ***** structure and value of an expression
code_activator_generate.py abcd_io.py $q
code_activator_generate.py uvwx_io.py $q

code_activator_generate.py inc_dec_easy_io.py $q
code_activator_generate.py inc_dec_harder_io.py $q

code_activator_generate.py conditional_expression_io.py $q

multiple_choice_generate.py multiple_choice.py $q
