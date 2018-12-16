import os
import tkinter 
import sh

def main_window():
	main = tkinter.Tk()
	main.title("Access control application")
	main.geometry("400x400")

	frame = tkinter.Frame(main)
	frame.pack()

	cu_dir = tkinter.Button(frame, text="Current directory", command=cu_dir_click)
	cu_dir.pack()

	ch_dir = tkinter.Button(frame, text="Change directory", command=ch_dir_click)
	ch_dir.pack()

	cr_file = tkinter.Button(frame, text="Create file", command=cr_file_click)
	cr_file.pack()

	show_rights = tkinter.Button(frame, text="Show access rights", command=show_rights_click)
	show_rights.pack()

	ch_rights = tkinter.Button(frame, text="Change access rights", command=ch_rights_click)
	ch_rights.pack()

	main.mainloop()
def ch_dir_click():
    def ch_dir_button_click():
        sh.cd(ch_dir_entry.get())
        ch_dir_str = os.popen('pwd').read()
        ch_dir_label2.config(text = (ch_dir_str))
        
    ch_dir_win = tkinter.Tk()
    ch_dir_win.title("Changing directory")
    ch_dir_win.geometry("400x150")
    
    ch_dir_frame = tkinter.Frame(ch_dir_win)
    ch_dir_frame.pack()
    
    ch_dir_label1 = tkinter.Label(ch_dir_frame, text='Enter new directory:')
    ch_dir_label1.pack()
    
    ch_dir_entry = tkinter.Entry(ch_dir_frame)
    ch_dir_entry.pack()
    
    ch_dir_button = tkinter.Button(ch_dir_frame, text = 'Submit', command=ch_dir_button_click)
    ch_dir_button.pack()
    
    ch_dir_label3 = tkinter.Label(ch_dir_frame, text = 'New directory is:')
    ch_dir_label3.pack()	

    ch_dir_label2 = tkinter.Label(ch_dir_frame)
    ch_dir_label2.pack()
    
    ch_dir_win.mainloop()

def cu_dir_click():
    cu_dir_win = tkinter.Tk()
    cu_dir_win.title("Current directory:")
    cu_dir_win.geometry("400x100")
    
    cu_dir_frame = tkinter.Frame(cu_dir_win)
    cu_dir_frame.pack()
    
    cu_dir_label2 = tkinter.Label(cu_dir_frame, text = 'Current directory is:')
    cu_dir_label2.pack()	

    cu_dir_label = tkinter.Label(cu_dir_frame)
    cu_dir_label.pack()
    
    cu_dir_str = os.popen('pwd').read()
    
    cu_dir_label.config(text = (cu_dir_str))
    
def cr_file_click():
	def cr_file_button_click():
		os.system('touch file ' + (cr_file_entry.get()))
		cr_file_label2.config(text = 'File ' + (cr_file_entry.get()) + ' is successfully created!')
        
	cr_file_win = tkinter.Tk()
	cr_file_win.title("Creating file")
	cr_file_win.geometry("400x150")
    
	cr_file_frame = tkinter.Frame(cr_file_win)
	cr_file_frame.pack()
    
	cr_file_label1 = tkinter.Label(cr_file_frame, text='Enter file name:')
	cr_file_label1.pack()
    
	cr_file_entry = tkinter.Entry(cr_file_frame)
	cr_file_entry.pack()
    
	cr_file_button = tkinter.Button(cr_file_frame, text = 'Create', command=cr_file_button_click)
	cr_file_button.pack()
    
	cr_file_label2 = tkinter.Label(cr_file_frame)
	cr_file_label2.pack()
    
	cr_file_win.mainloop()

def ch_rights_click():
	def ch_rights_button_click():
		os.system('chmod ' + (ch_rights_entry2.get()) + ' ' + (ch_rights_entry1.get()))
		ch_rights_label3.config(text='Rights are successfully changed!')

	ch_rights_win = tkinter.Tk()
	ch_rights_win.title("Changing access rights")
	ch_rights_win.geometry("400x150")

	ch_rights_frame = tkinter.Frame(ch_rights_win)
	ch_rights_frame.pack()

	ch_rights_label1 = tkinter.Label(ch_rights_frame, text = 'Enter file name:')
	ch_rights_label1.pack()

	ch_rights_entry1 = tkinter.Entry(ch_rights_frame)
	ch_rights_entry1.pack()

	ch_rights_label2 = tkinter.Label(ch_rights_frame, text = 'Enter new rights:')
	ch_rights_label2.pack()

	ch_rights_entry2 = tkinter.Entry(ch_rights_frame)
	ch_rights_entry2.pack()

	ch_rights_button = tkinter.Button(ch_rights_frame, text = 'Change', command=ch_rights_button_click)
	ch_rights_button.pack()

	ch_rights_label3 = tkinter.Label(ch_rights_frame)
	ch_rights_label3.pack()

	ch_rights_win.mainloop()

def show_rights_click():
	def show_rights_button_click():
		show_rights_str = os.popen('ls -l').read()
		show_rights_label.config(text = (show_rights_str))

	show_rights_win = tkinter.Tk()
	show_rights_win.title("Access rights")
	show_rights_win.geometry("800x600")

	show_rights_frame = tkinter.Frame(show_rights_win)
	show_rights_frame.pack()

	show_rights_button = tkinter.Button(show_rights_frame, text = 'Show', command=show_rights_button_click)
	show_rights_button.pack()

	show_rights_label = tkinter.Label(show_rights_frame)
	show_rights_label.pack()

	show_rights_win.mainloop()

if __name__ == '__main__':
    main_window()
