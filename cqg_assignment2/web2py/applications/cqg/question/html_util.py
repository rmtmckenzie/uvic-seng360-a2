# will any users of this function need <option>s of the form
# <option value='submit_value'>Display Value</option>
# ? If so, allow options to be a dictionary
#
# multiple selection, table
# terms
# HTML forms terminololgy
#
#	<input type="text" ...
#		an input text field
#		"name": unique id of input element; key in answer dictionary
#		"value": initial value
#		"size": text width in characters; default: 20
#
#	<input type = "checkbox"
#		generates a single check box; checkbox groups have same name
#		"value": in answer dictionary, specifies the pressed button(s)
#	<input type = "radio" ...
#		generates a single radio button; button groups have same name
#		"value": in answer dictionary, specifies the pressed button
#	<select name = ...
#		<option value = value0> label0 </option>
#		<option value = value1> label1 </option>
#		...
#		<option value = valueK selected> labelK </option>
#		...
#		drop down list with current selection showing
#		default current selection is label0
#		user overrides default with "selected"
#	<select multiple="multiple" ...
#		allows multiple items to be selected concurrently
#		entire list always displayed
#	<table name = ...

def get_text(name,value,size=3):
	'''
	purpose
		returns a string containing an HTML text input element
		of width size characters and containing value
	preconditions
		name is a string
		value is a string
		size is a positive int
	'''
	return ("<input type='text' name='%s' value='%s' size ='%i'/>"
	 % (name,value,size))

def get_submit(name,value,disabled=False):
	'''
	purpose
		returns a string containing an HTML submit input element
		 containing value
		button is enabled iff disabled is False
	preconditions
		name is a string
		value is a string
		disabled is a boolean
	'''
	if disabled:
		flag = "disabled"
	else:
		flag = ""
	return ("<input type='submit' name='%s' value='%s' %s>"
	 % (name,value,flag))

def get_select(name,options,selected):
	'''
	purpose
		return a string containing an HTML select element containing
		 options
	preconditions
		name is a string
		options is a non-empty list of strings without duplicates
		selected is one of the strings in options
	'''
	html_string = "<select name='%s'>" % name
	for option in options:
		if option == selected:
			flag = "selected"
		else:
			flag = ""
		html_string += ("<option value='%s' %s>%s</option>"
		 % (option,flag,option))
	html_string += "</select>"
	return html_string

def get_select_multiple(name,options,selected,size=None):
	'''
	purpose
		return a string containing an HTML select element of height
		 size rows, supporting multiple selections, and containing
		 options
		default size: len(options)
	preconditions
		name is a string
		options is a non-empty list of strings without duplicates
		selected is a sublist of options, without duplicates
		size, if present, is a positive int
	'''
	if size == None:
		size = len(options)
	html_string = ("<select name='%s' size='%i' multiple='multiple'>"
	 % (name,size))
	for option in options:
		if option in selected:
			flag = "selected"
		else:
			flag = ""
		html_string += ("<option value='%s' %s>%s</option>"
		 % (option,flag,option))
	html_string += "</select>"
	return html_string

def get_radio_button(name,value,checked):
	'''
	purpose
		returns a string containing a single radio button <input> tag
		if checked is True, the button will be in its checked state
		(i.e. selected)
	preconditions
		name is a string
		value is a string
	'''
	if checked:
		checked = " checked='checked'"
	else:
		checked = ""
	return ("<input type='radio' name='%s' value='%s'%s />"
	 % (name,value,checked))

def get_radio_button_set(name,options,selected_value):
	'''
	purpose
		returns a list of radio buttons for the items in options
		if selected_value is not None, the radio button for that value
		 is checked
	preconditions
		name is a string
		value is of a type supporting str()
		options is a list of items supporting str()
	'''
	radio_buttons = []
	for i in options:
		radio_buttons.append(
		 get_radio_button(name,str(i),
		  (selected_value != None and str(i) == str(selected_value))))
	return radio_buttons

def get_checkbox(name,value,checked):
	'''
	purpose
		returns a string containing a single checkbox <input> tag
		if checked is True, the box will be in its checked state
		(i.e. selected)
	preconditions
		name is a string
		value is a string
	'''
	if checked:
		checked = " checked='checked'"
	else:
		checked = ""
	return ("<input type='checkbox' name='%s' value='%s'%s />"
	 % (name,value,checked))

def get_checkbox_set(name,options,selected_values):
	'''
	purpose
		returns a list of checkboxes for the items in options
		if selected_value is not None, the checkbox for that value
		 is checked
	preconditions
		name is a string
		value is of a type supporting str()
		options is a list of items supporting str()
	'''
	checkboxes = []
	if selected_values is not None:
		selected_values = [str(i) for i in selected_values]
	for i in options:
		checkboxes.append(
		 get_checkbox(name,str(i),
		  (selected_values != None and str(i) in selected_values)))
	return checkboxes

def make_css_borders(thickness,table_id=''):
	'''
	purpose
		if table_id is not given, returns a string containing the
		following CSS classes, for use with get_table:
			top_border
			left_border
			right_border
			bottom_border
			all_borders
		if table_id is given with value X, returns a CSS rule that
		turns on all cell borders for the table which has the
		attribute "id='X'"
	precondition
		thickness is an integer
		table_id is a string or not specified
	'''
	if table_id == '':
		css = '\n'
		for i in ['top','left','right','bottom']:
			css += ('td.%s_border { border-%s: %ipx solid black }\n'
			 % (i,i,thickness))
		css += ('td.all_borders { border: %ipx solid black; }\n'
		 % thickness)
		return css
	else:
		return ( '\n'
		 '#%s { border: %ipx solid black; }\n' % (table_id,thickness) +
		 '#%s td { border: %ipx solid black; }\n' % (table_id,thickness)
		)

def get_table(array,attributes=''):
	'''
	purpose
		return a string containing an HTML table.
		opening <table> tag is constructed as <table %s>, where %s
		 is replaced by the value of attributes.
		each value X in array results in:
			if X is a string: <td>X</td>
			if X is a 2-tuple: <td class='X[1]'>X[0]</td>
	precondition
		values is a list of lists of strings or 2-tuples
		attributes is a string
	'''
	html_string = "<table %s>\n" % attributes
	for row in array:
		html_string += "\t<tr>\n"
		for cell in row:
			if type(cell) is tuple:
				html_string += "\t\t" \
				 "<td class='%s'>%s</td>\n" % (cell[1],cell[0])
			else:
				html_string += "\t\t<td>%s</td>\n" % cell
		html_string += "\t</tr>\n"
	html_string += "</table>\n"
	return html_string
