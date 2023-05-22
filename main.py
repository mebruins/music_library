from tkinter import *
from tkinter import messagebox
import json

window = Tk()
window.title('Music Library')
window.minsize(500, 300)
window.config(padx=20, pady=20)

# canvas = Canvas(width=500,height=500)
# logo = PhotoImage(file='logo1.png')
# canvas.create_image(500,500, image=logo)
# canvas.grid(column=2,row=1)

#---------------------- Save to library -------------------------#
# figure out how to append dictionaries to json file so they can be searchable
def save_to_library():
    title = title_input.get()
    composer = composer_input.get()
    style = style_input.get()
    file = file_input.get()
    performed = performed_input.get()
    title_data = {
            title: {
            'composer': composer,
            'style': style,
            'file': file,
            'performed': performed,       
            }
        }
    composer_data = {
        composer: {
            'title': title,
            'style': style,
            'file': file,
            'performed': performed
        }
    }
    if len(title) == 0 or len(composer) == 0:
        messagebox.showinfo(title='Uh oh.....', message='Title and/or composer must be provided.')
    else:
        try:
            with open('data1.json', 'r') as data_file:
                data1 = json.load(data_file)
            with open('data2.json', 'r') as data_file2:
                data2 = json.load(data_file2)
        except FileNotFoundError:
            with open('data1.json','w') as data_file:
                json.dump(title_data, data_file, indent=4)
            with open('data2.json', 'w') as data_file2:
                json.dump(composer_data, data_file2, indent=4)
        else:
            data1.update(title_data)
            data2.update(composer_data)
            with open('data1.json', 'w') as data_file:
                json.dump(data1, data_file, indent=4)
            with open('data2.json', 'w') as data_file2:
                json.dump(data2, data_file2, indent=4)
        finally:
            title_input.delete(0,END)
            composer_input.delete(0,END)
            style_input.delete(0,END)
            file_input.delete(0,END)
            performed_input.delete(0,END)

#---------------------- Searches --------------------------------#

def search_title():
    title = title_input.get()
    try:
        with open('data1.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Uh oh.....', message='Records do not match your search.')
    else:
        if title in data:
            composer = data[title]['composer']
            style = data[title]['style']
            file = data[title]['file']
            performed = data[title]['performed']
            messagebox.showinfo(title='Found it!', message=f'Title: {title}\nComposer: {composer}\nStyle: {style}\nFiling Number: {file}\nPerformed on: {performed}')
        else:
            messagebox.showinfo(title="Uh oh.....", message='No records match your search.')

def search_composer():
    composer = composer_input.get()
    try:
        with open('data2.json') as data_file2:
            data = json.load(data_file2)
    except FileNotFoundError:
        messagebox.showinfo(title='Uh oh.....', message='Records do not match your search.')
    else:
        if composer in data:
            title = data[composer]['title']
            style = data[composer]['style']
            file = data[composer]['file']
            performed = data[composer]['performed']
            messagebox.showinfo(title='Found it!', message=f'Title: {title}\nComposer: {composer}\nStyle: {style}\nFiling Number: {file}\nPerformed on: {performed}')
        else:
            messagebox.showinfo(title="Uh oh.....", message='No records match your search.')


#---------------Labels, Inputs, Buttons--------------------------#
#labels
title_label = Label(text='Title:', font=('courier', 16))
title_label.grid(column=0,row=0)
composer_label = Label(text='Composer:', font=('courier', 16))
composer_label.grid(column=0,row=1)
style_label = Label(text='Style/Level:', font=('courier', 16))
style_label.grid(column=0,row=2)
file_label = Label(text='Filing Number:', font=('courier', 16))
file_label.grid(column=0, row=3)
performed_label = Label(text='Last Performed:', font=('courier', 16))
performed_label.grid(column=0,row=4)

# inputs
title_input = Entry(width=35)
title_input.grid(column=1,row=0)
composer_input = Entry(width=35)
composer_input.grid(column=1,row=1)
style_input = Entry(width=35)
style_input.grid(column=1,row=2)
file_input = Entry(width=35)
file_input.grid(column=1, row=3)
performed_input = Entry(width=35)
performed_input.grid(column=1,row=4)

# buttons/sorts/searches

search = Button(text='Search by Title', width=20, command=search_title)
search.grid(column=2,row=0)

composer_search = Button(text='Search by Composer', width=20, command=search_composer)
composer_search.grid(column=2,row=1)

add_file = Button(text='Save to Library', width=33, command=save_to_library)
add_file.grid(column=1,row=5)

window.mainloop()