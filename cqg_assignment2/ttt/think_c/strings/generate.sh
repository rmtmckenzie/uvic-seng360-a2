q=../../../question_library/think_c/strings

rm -rf $q/*

# ***** functions
code_activator_generate.py strlen.py $q
code_activator_generate.py strcpy.py $q
code_activator_generate.py strcmp.py $q

code_activator_generate.py strlen_base.py $q
code_activator_generate.py strcpy_base.py $q

code_activator_generate.py strlen_raw.py $q
code_activator_generate.py strcpy_raw.py $q

code_activator_generate.py strcmp_code.py $q
