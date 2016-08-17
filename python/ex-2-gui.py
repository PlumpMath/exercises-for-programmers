import tkinter
gui = tkinter.Tk()

message_string_var = tkinter.StringVar()
message_string_var.set('What is the input string?')
input_string_var = tkinter.StringVar()
output_string_var = tkinter.StringVar()

message_label = tkinter.Label(gui, width=30, textvariable=message_string_var)
input_entry = tkinter.Entry(gui, width=30, textvariable=input_string_var)
output_label = tkinter.Label(gui, width=30, textvariable=output_string_var)


def render_label2(event):
    global output_string_var
    input_string = input_string_var.get()
    if input_string:
        output_string = input_string + ' has ' + str(len(input_string)) + ' characters.'
    else:
        output_string = 'Please input something.'
    output_string_var.set(output_string)

message_label.pack()
input_entry.pack()
output_label.pack()
gui.bind('<Key>', render_label2)

gui.mainloop()
