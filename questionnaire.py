from tkinter import Tk, Label, PhotoImage, Frame, Radiobutton, IntVar, Button
from sys import argv
from tempfile import gettempdir
from uuid import uuid4
from subprocess import run

questions = {"Does your child look at you when you call his/her name?": ['Always', 'Usually', 'Sometimes', 'Rarely', 'Never'], 
             "How easy is it for you to get eye contact for your child?": ['Very easy', 'Quite easy', 'Quite difficult', 'Very difficult', 'Impossible'],
             "Does your child point to indicate that he/she wants something? (e.g. a toy\nthat is out of reach)": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"],
             "Does your child point to share interest with you? (e.g. pointing at an\ninteresting sight)": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"],
             "Does your child pretend? (e.g. care for dolls, talk on a toy phone)": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"],
             "Does your child follow where you're looking?": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"],
             "If you or someone else in the family is visibly upset, does your child\n show signs of wanting to comfort them? (e.g. stroking hair, hugging them)": ['Always', 'Usually', 'Sometimes', 'Rarely', 'Never'],
             "Would you describe your child's first words as:": ["Very typical", "Quite typical", "Slightly unusual", "Very unusual", "My child doesn't speak"],
             "Does your child use simple gestures? (e.g. wave goodbye)": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"],
             "Does your child stare at nothing with no apparent purpose?": ["Many times a day", "A few times a day", "A few times a week", "Less than once a week", "Never"]
}
times_new_roman = 'Times New Roman'
ans_values = [0,0,0,0,0,0,0,0,0,0]
accept_ans = [0,0,0,0,0,0,0,0,0,0]
weights = [9,10,8,8,7,7,6,6,7,5]
temp = gettempdir()
hex_val = str(uuid4())

# Accepting from input form
data = argv[1]
data = data.split(', ')
email = data[0]
age = int(data[1])
sex = int(data[2])
ethnicity = int(data[3])
jaundice = int(data[4])
user = int(data[5])
family = int(data[6])

# Creating a window
root = Tk()
root.title("Data form")
icon = PhotoImage(file = '.images/form-icon.png') 
root.iconphoto(False, icon)
window_width = 700
window_height = 400
root.geometry(f'{window_width}x{window_height}')
root.resizable(False, False)


# Centering the main window
def center_screen():
    global screen_height, screen_width, x_coordinate, y_coordinate
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Coordinates of the upper left corner of the window to make the window appear in the center
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
center_screen()

frame1 = Frame(root, highlightbackground="blue", highlightthickness=1,width=680, height=680, bd=2)
frame1.pack(pady=10, padx=10)
key_vals = list(questions.keys())
c = 0

# Question Numbers and Questions
q_no = Label(root, text=f'{c+1}.', font=(times_new_roman, 14, 'bold'))
q = Label(root, text=key_vals[c], font=(times_new_roman, 15), justify='left')
q_options = questions[key_vals[c]] # Options

ans = 0
# Radio Button function on click
def select_value():
    global ans, var, accept_ans
    ans = var.get()
    accept_ans [c] = var.get()
    if c==9 and (ans==1 or ans==2 or ans==3):
        ans_values[c] = 1
    elif c!=9 and (ans==3 or ans==4 or ans==5):
        ans_values[c] = 1
    else:
        ans_values[c] = 0
    # var.set(0)
var = IntVar()
# Radio buttons
r1 = Radiobutton(root, text=q_options[0], variable=var, value=1, command=select_value, font=(times_new_roman, 14, 'italic'))
r2 = Radiobutton(root, text=q_options[1], variable=var, value=2, command=select_value, font=(times_new_roman, 14, 'italic'))
r3 = Radiobutton(root, text=q_options[2], variable=var, value=3, command=select_value, font=(times_new_roman, 14, 'italic'))
r4 = Radiobutton(root, text=q_options[3], variable=var, value=4, command=select_value, font=(times_new_roman, 14, 'italic'))
r5 = Radiobutton(root, text=q_options[4], variable=var, value=5, command=select_value, font=(times_new_roman, 14, 'italic'))

r1.place(x=80, y=100)
r2.place(x=80, y=140)
r3.place(x=80, y=180)
r4.place(x=80, y=220)
r5.place(x=80, y=260)

q_no.place(x=30, y=40)
q.place(x=80, y=40)
# q_part.place(x=30, y=50)

def update_question():
    global q_no, q, q_options, c
    q_no.config(text=f'{c+1}.')
    q.config(text=key_vals[c])
    
def update_options():
    global q_options, r1, r2, r3, r4, r5
    q_options= questions[key_vals[c]] # Extract Options 
    
    # Reinitialize the radio-buttons 
    r1.config(text=q_options[0])
    r2.config(text=q_options[1])
    r3.config(text=q_options[2])
    r4.config(text=q_options[3])
    r5.config(text=q_options[4])
    
def next_question():
    print('Ans 0/1:', ans_values, 'Ans options:', accept_ans)
    global ans, c, var
    if ans!=0:
        if c!=9:
            prev.configure(state='active', command=prev_question)
            var.set(0)
            c+=1
            update_question()
            update_options()
            if accept_ans[c] != 0:
                var.set(accept_ans[c])
                if var.get() != accept_ans[c]:
                    accept_ans[c] = var.get()
            if c==9:
                submit.config(state='active')
                next.configure(command='none', state='disabled')
            select_value()


def prev_question():
    print('Ans 0/1:', ans_values, 'Ans options:', accept_ans)
    
    global c
    if c!=0:
        if c == 9:
            next.configure(command=next_question, state='active')
            submit.configure(state='disabled')
        c-=1
        update_question()
        update_options()
        var.set(accept_ans[c])
        if c==0:
            prev.config(command='none', state='disabled')        
        select_value()
        
prev_img = PhotoImage(file=r'.images/prev.png').subsample(3,3)
prev = Button(root, command='none', state='disabled', image=prev_img, borderwidth=0)
prev.place(x=80,y=325)
next_img = PhotoImage(file=r'.images/next.png').subsample(3,3)
next = Button(root, command=next_question, state='active',  image=next_img, borderwidth=0)
next.place(x=580,y=325)
submit_img = PhotoImage(file=r'.images/submit.png').subsample(3,3)


def create_file(data):
    file = open(f'{temp}/data_{hex_val}.csv', 'w')
    data = ','.join(data)
    file.write(f'A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,Qchat-10-Score,Age_Mons,Sex,Ethnicity,Jaundice,Who completed the test,Family_mem_with_ASD\n{data}\n')
    file.close()
    
    file = open(f'{temp}/data_{hex_val}.csv', 'r')
    for i in file:
        print(i)


def submit_action():
    root.destroy()
    global ans_values
    print('Ans 0/1:', ans_values, 'Ans options:', accept_ans)
    q_chat_10_sum = sum(ans_values)
    weight_sum = 0
    for i in range(len(ans_values)):
        if ans_values[i] == 1:
            weight_sum += weights[i]
    ans_values = list(map(str, ans_values))
    ans_values1 = list(map(str, [q_chat_10_sum, age, sex, ethnicity, jaundice, user, family]))
    name = data[7]
    create_file(ans_values+ans_values1)
    run(['python', 'model_loading_output.py', name, f'{temp}/data_{hex_val}.csv', str(weight_sum), email])

submit = Button(root, command=submit_action, state='disabled', image=submit_img, borderwidth=0)
submit.place(x=275, y=325)
root.mainloop()
