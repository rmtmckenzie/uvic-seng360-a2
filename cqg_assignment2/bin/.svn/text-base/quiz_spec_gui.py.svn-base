#!/usr/bin/python

import sys
import os
import re

from Tkinter import *
import tkFileDialog
import tkMessageBox
import traceback

import quiz_spec_gui_model

model = quiz_spec_gui_model.model()
question_library_path = ''

def add_scrolling_canvas(window,orientations):
	canvas = Canvas(window)
	if orientations.find("h") != -1:
		xscrollbar = Scrollbar(window,orient="h",command=canvas.xview)
		canvas.configure(xscrollcommand=xscrollbar.set)
		xscrollbar.grid(row=1,column=0,sticky="ew")
	if orientations.find("v") != -1:
		yscrollbar = Scrollbar(window,orient="v",command=canvas.yview)
		canvas.configure(yscrollcommand=yscrollbar.set)
		yscrollbar.grid(row=0,column=1,sticky="ns")
	canvas.grid(row=0,column=0,sticky="nsew")
	window.grid_rowconfigure(0,weight=1)
	window.grid_columnconfigure(0,weight=1)
	canvas.configure(scrollregion=canvas.bbox("all"))
	window.canvas = canvas

#### main window event handling ################################################
def get_focus():
	try:
		widget = main.focus_get()
		return widget.position
	except:
		return None

def update_mark(event):
	entry = event.widget
	model.update_group(entry.position, 0, entry.get())

def update_count(event):
	entry = event.widget
	model.update_group(entry.position, 1, entry.get())

def update_ui_hints(event):
	# disable all context-sensitive commands, then selectively re-enable
	for i in range(4,6):
		groups.entryconfigure(i,state = DISABLED)
	focus = get_focus()
	if focus is None:
		return
	if group_buffer is not None:
		groups.entryconfigure(5, state = NORMAL) # clear group buffer
	groups.entryconfigure(4, state = NORMAL) # delete group
	groups.entryconfigure(6, state = NORMAL) # add directories
	groups.entryconfigure(7, state = NORMAL) # remove directories

def gen_add_callback(position):
	return lambda:add_dirs_dialogue(position,True,None)

def gen_remove_callback(position):
	return lambda:remove_dirs_dialogue(position)

def check_qre_callback(entry,position):
	return lambda:check_question_re(entry,position)

def check_question_re(entry,position):
	re_string = entry.get()
	try:
		re.compile(re_string)
		model.group_update_dir(position,re_string)
		tkMessageBox.showinfo("","Regular expression recorded")
	except:
		tkMessageBox.showerror(title='Illegal regular expression', 
		 message=traceback.format_exc())

def view_question_callback(position):
	return lambda:view_questions(position)

def view_questions(i):
	s = ''
	L = model.get_question_list()
	if type(L[i][2]) == str:
		s = L[i][2] 
	add_dirs_dialogue(i,False,s)
	

def refresh():
	main.canvas.delete(ALL)

	# headers
	mark_header = Label(main.canvas,text = 'Mark')
	main.canvas.create_window(0,0,window=mark_header,anchor=NW)
	count_header = Label(main.canvas,text = 'Count')
	main.canvas.create_window(50,0,window=count_header,anchor=NW)
	dirs_header = Label(main.canvas,text = 'Directories')
	main.canvas.create_window(100,0,window=dirs_header,anchor=NW)

	# widget group rows
	question_list = model.get_question_list()
	for i in range(len(question_list)):
		mark = Entry(main.canvas,width = 4)
		mark.position = i
		mark.insert(0,str(question_list[i][0]))
		mark.bind(sequence='<KeyRelease>',func=update_mark)
		count = Entry(main.canvas,width = 4)
		count.position = i
		count.insert(0,str(question_list[i][1]))
		count.bind(sequence='<KeyRelease>',func=update_count)
		#place widgets 
		main.canvas.create_window(0,30*(i+1),window=mark,anchor=NW)
		main.canvas.create_window(50,30*(i+1),window=count,anchor=NW)
		if type(question_list[i][2]) == str: # a pattern group
			pattern = Entry(main.canvas,width = 24)
			pattern.position = i
			s = ''
			if type(question_list[i][2]) == str:
				s = question_list[i][2]
			pattern.insert(0,s)
			#pattern.bind(sequence='<KeyRelease>',func=update_count)
			main.canvas.create_window(100,30*(i+1),window=pattern,
			 anchor=NW)
			check_button = Button(main.canvas,text="Check",
			 command=check_qre_callback(pattern,i))
			view_button = Button(main.canvas,text="View",
			 command=view_question_callback(i))
			main.canvas.create_window(300,30*(i+1),
			 window=check_button,anchor=NW)
			main.canvas.create_window(370,30*(i+1),
			 window=view_button,anchor=NW)
		else:
			add_button = Button(main.canvas,text="Add",
			 command=gen_add_callback(i))
			main.canvas.create_window(370,30*(i+1),
			 window=add_button,anchor=NW)
		remove_button = Button(main.canvas,text="Remove",
			command=gen_remove_callback(i))
		main.canvas.create_window(430,30*(i+1),window=remove_button,
			anchor=NW)

	main.canvas.config(scrollregion=main.canvas.bbox(ALL))
	update_ui_hints(None)

#### File menu #################################################################
saved_filename = ''

def new():
	global model,saved_filename
	saved_filename = ''
	model = quiz_spec_gui_model.model()

	refresh()

def load():
	global saved_filename
	handle = tkFileDialog.askopenfilename()
	try:
		model.load(handle)
		saved_filename = handle
	except:
		saved_filename = ''

	refresh()

def save_as():
	global saved_filename
	handle = tkFileDialog.asksaveasfile(mode='w')
	if handle:
		saved_filename = handle.name
		model.save(saved_filename)
		update_ui_hints(None)

def save():
	global saved_filename
	if saved_filename == '':
		save_as()
	else:
		model.save(saved_filename)
		update_ui_hints(None)

#### Groups menu ###############################################################
group_buffer = None # holds most recently deleted group, a crude clipboard
dirs_popup = None

def add_group(after,is_list):
	position = get_focus()
	if position is None:
		position = 0
	elif after:
		position += 1
	model.insert_group(position,group_buffer,is_list)

	refresh()

def delete_group():
	global group_buffer
	position = get_focus()
	if position is not None:
		group_buffer = model.remove_group(position)

	refresh()

def clear_group_buffer():
	global group_buffer
	group_buffer = None

fvalue=''
def callback(entry,filter_popup):
	global fvalue
	tmp = entry.get()
	try:
		re.compile(tmp)
		fvalue = tmp
		filter_popup.destroy()
	except:
		tkMessageBox.showerror(title='Illegal regular expression', 
		 message=traceback.format_exc())


def set_add_directory_filter():	
	filter_popup = Toplevel()
	filter_popup.grab_set()
	filter_popup.title("Set add directory filter")

	global fvalue
	label = Label(filter_popup,text="Input your directory filter:")
	label.grid(row=0)
	entry = Entry(filter_popup)
	entry.grid(row = 1)
	entry.insert(0,fvalue)
	button = Button(filter_popup,text = 'OK',command=lambda:callback(entry,filter_popup))
	button.grid(row = 2)	

def process_dir_list(position,action,dir_list,checkbox_values):
	for i in range(len(dir_list)):
		if checkbox_values[i].get():
			if action == 'add':
				model.group_add_dir(position,dir_list[i])
			else:
				model.group_remove_dir(position,dir_list[i])

	dirs_popup.destroy()
	refresh()

def preview_question(q):
	# import question class
	q = os.path.join(question_library_path,q)
	exec(open(os.path.join(q,'types.py'),'r').read())
	exec('import question.'+product_family)
	exec('question_obj = question.'+product_family+'.'+question_type+'(q)')

	# get question preview
	preview = question_obj.get_preview()
	
	# create a popup window to display question preview
	preview_popup = Toplevel()
	preview_popup.title = (q)
	add_scrolling_canvas(preview_popup,"vh")
	preview_popup.geometry("500x500")
	label = Label(preview_popup,text=preview)
	preview_popup.canvas.create_window(0,0,window=label,anchor=NW)
	
def gen_preview_callback(q):
	return lambda:preview_question(q)

def get_question_dirs(base_dir,question_library_path):
	all_questions = []
	L = os.listdir(os.path.join(question_library_path,base_dir))
	for d in L:
		p = os.path.join(base_dir,d)
		t = os.path.join(question_library_path,base_dir,d,'types.py')
		if os.path.isfile(t):
			all_questions.append(p)
		else:
			all_questions += get_question_dirs(p,
			 question_library_path)
	return all_questions

def add_dirs_dialogue(position,is_add,re_pattern):
	global dirs_popup
	dirs_popup = Toplevel()
	dirs_popup.grab_set()
	s = "Add directories"
	if not is_add:
		s = "View directories"
	dirs_popup.title(s)
	add_scrolling_canvas(dirs_popup,"v")
	dirs_popup.geometry("300x500")

	# casting to set type allows us to use set difference to filter out the
	# dirs that are already present:
	d_list = list(set(get_question_dirs(question_library_path,''))-
	 set(model.get_dir_list(position)))
	d_list.sort()
	dir_list = []
	if re_pattern == None:
		re_pattern = fvalue
	for i in range(len(d_list)):
		if re.search(re_pattern,d_list[i]):
			dir_list.append(d_list[i])
	
	checkbox_values = []
	last_row = 0 # need i defined even if there are no rows
	for i in range(len(dir_list)):
		question_dir = dir_list[i]
		if is_add:
			value = IntVar()
			checkbox_values.append(value)
			checkbox = Checkbutton(dirs_popup,variable=value)
			dirs_popup.canvas.create_window(0,30*last_row,
			 window=checkbox, anchor=NW)

		pre_button = Button(dirs_popup.canvas,text="Preview",
		 command=gen_preview_callback(dir_list[i]))
		dirs_popup.canvas.create_window(30,30*last_row,
		 window=pre_button,anchor=NW)

		question_label = Label(dirs_popup,text=question_dir)
		dirs_popup.canvas.create_window(120,30*last_row,
		 window=question_label,anchor=NW)
		last_row += 1
	if is_add:
		add_button = Button(dirs_popup.canvas,text="Add",
		 command=lambda:process_dir_list(position,'add',dir_list,
		 checkbox_values))
		dirs_popup.canvas.create_window(0,30*(last_row+2),
		 window=add_button,anchor=NW)

		cancel_button = Button(dirs_popup.canvas,text="Cancel",
		 command=dirs_popup.destroy)
		dirs_popup.canvas.create_window(100,30*(last_row+2),
		 window=cancel_button,anchor=NW)

		# tell the scroll bars the new size of the canvas:
	dirs_popup.canvas.config(scrollregion=dirs_popup.canvas.bbox(ALL))

def remove_dirs_dialogue(position):
	global dirs_popup
	dirs_popup = Toplevel()
	dirs_popup.grab_set()
	dirs_popup.title("Remove directories")
	add_scrolling_canvas(dirs_popup,"v")
	dirs_popup.geometry("300x500")

	dir_list = model.get_dir_list(position)

	checkbox_values = []
	i = 0 # need i defined even if there are no rows
	for i in range(len(dir_list)):
		question_dir = dir_list[i]
		value = IntVar()
		checkbox_values.append(value)

		checkbox = Checkbutton(dirs_popup,variable=value)
		dirs_popup.canvas.create_window(0,30*i,window=checkbox,
		 anchor=NW)

		question_label = Label(dirs_popup,text=question_dir)
		dirs_popup.canvas.create_window(30,30*i,window=question_label,
		 anchor=NW)

	last_row = i
	remove = Button(dirs_popup.canvas,text="Remove",
	 command=lambda: process_dir_list(position,'remove',dir_list,
	 checkbox_values))
	dirs_popup.canvas.create_window(0,30*(last_row+1),window=remove,
	 anchor=NW)

	cancel = Button(dirs_popup.canvas,text="Cancel",
	 command=dirs_popup.destroy)
	dirs_popup.canvas.create_window(100,30*(last_row+1),window=cancel,
	 anchor=NW)

	# tell the scroll bars the new size of the canvas:
	dirs_popup.canvas.config(scrollregion=dirs_popup.canvas.bbox(ALL))

#### Quiz parameters menu ######################################################
quiz_params_popup = None

def quiz_params_dialogue():
	global quiz_params_popup
	quiz_params_popup = Toplevel()
	quiz_params_popup.title("Quiz Parameters")
	quiz_params_popup.grab_set()

	practice_mode_var = BooleanVar(quiz_params_popup)
	practice_mode_var.set(model.get_practice_mode())
	practice_mode_label = Label(quiz_params_popup,text="Practice mode:")
	practice_mode_label.grid(row = 0,column = 0)
	practice_mode_menu = OptionMenu(quiz_params_popup,practice_mode_var,
	 False,True)
	practice_mode_menu.grid(row = 0,column = 1)

	standalone_var = BooleanVar(quiz_params_popup)
	standalone_var.set(model.get_standalone())
	standalone_label = Label(quiz_params_popup,text="Single-question quiz:")
	standalone_label.grid(row = 1,column = 0)
	standalone_menu = OptionMenu(quiz_params_popup,standalone_var,False,
	 True)
	standalone_menu.grid(row = 1,column = 1)

	logged_var = BooleanVar(quiz_params_popup)
	logged_var.set(model.get_logged())
	logged_label = Label(quiz_params_popup,text="Quiz logging:")
	logged_label.grid(row = 2,column = 0)
	logged_menu = OptionMenu(quiz_params_popup,logged_var,False,True)
	logged_menu.grid(row = 2,column = 1)

	log_dir_label = Label(quiz_params_popup,text='Log directory:')
	log_dir_label.grid(row = 3,column = 0)
	log_dir = Entry(quiz_params_popup)
	log_dir.insert(0, model.get_log_dir())
	log_dir.grid(row = 3,column = 1)
	
	ok = Button(quiz_params_popup,text = "OK",command =
		lambda: set_quiz_params(
			practice_mode_var.get(),
			standalone_var.get(),
			logged_var.get(),
			log_dir.get()
		)
	)
	ok.grid(row = 4,columnspan = 2)

def set_quiz_params(
		practice_mode_var,
		standalone_var,
		logged_var,
		log_dir
	):
	model.set_practice_mode(practice_mode_var)
	model.set_standalone(standalone_var)
	model.set_logged(logged_var)
	model.set_log_dir(log_dir)
	quiz_params_popup.destroy()

#### main code #################################################################
if len(sys.argv) != 2:
	print 'Usage: python '+sys.argv[0]+' <question library path>'
	sys.exit(-1)
# resolve question library path, then try to work out where
# web2py/applications/cqg/ and quiz_specifications/ are
question_library_path = os.path.abspath(sys.argv[1])
try:
	# where are we? (first entry in argv is the called program's path)
	bin_dir = os.path.split(sys.argv[0])[0]
	# resolve relative paths from here
	cqg_dir = os.path.join(bin_dir,"../web2py/applications/cqg")
	quiz_specs_dir = os.path.join(bin_dir,"../quiz_specifications")
	sys.path.append(os.path.abspath(cqg_dir))
	os.chdir(quiz_specs_dir)
except:
	print "Warning: this doesn't look like a complete CQG install,"
	print "so question previewing is unavailable."

# init Tkinter GUI:
main = Tk()
main.geometry("700x200")
main.title("Quiz Specification GUI")
add_scrolling_canvas(main,"hv")

menubar = Menu(main)
# file menu
file_m = Menu(menubar,tearoff = 0)
file_m.add_command(label = 'New',command = new)
file_m.add_command(label = 'Open...',command = load)
file_m.add_command(label = 'Save',command = save)
file_m.add_command(label = 'Save as...',command = save_as)
file_m.add_command(label = 'Exit',command = main.quit)
menubar.add_cascade(label = 'File',menu = file_m)
# groups menu
groups = Menu(menubar,tearoff = 0)
groups.add_command(label = "Add group before:list",
command = lambda:add_group(False,True))
groups.add_command(label = "Add group before:pattern",
command = lambda:add_group(False,False))
groups.add_command(label = "Add group after:list",
command = lambda:add_group(True,True))
groups.add_command(label = "Add group after:pattern",
command = lambda:add_group(True,False))
groups.add_command(label = "Delete group",command = delete_group)
groups.add_command(label = "Clear group buffer",command = clear_group_buffer)
groups.add_command(label = "Set add directory filter",command = lambda:set_add_directory_filter())
menubar.add_cascade(label = "Groups", menu = groups)
# quiz parameters menu
quiz_params = Menu(menubar,tearoff = 0)
quiz_params.add_command(label = 'Set quiz parameters',
 command = quiz_params_dialogue)
menubar.add_cascade(label = 'Quiz parameters',menu = quiz_params)
main.config(menu = menubar)

menubar.bind(sequence = '<Button-1>', func = update_ui_hints)

# run the gui
refresh()
mainloop()
