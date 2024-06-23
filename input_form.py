from tkinter import Tk, PhotoImage, Frame, Menu, Label, Entry, Button, CENTER
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from tkinter import messagebox
from re import match
from webbrowser import open
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import mail_id, password
from subprocess import run
confirm_color = '#90EE90'

window_width = 380
window_height = 490
root = Tk()
root.geometry(f'{window_width}x{window_height}')
root.title('Input Form')
root.resizable(False, False)
icon = PhotoImage(file = '.images/form-icon.png') 
root.iconphoto(False, icon)


def center_screen():
    """ gets the coordinates of the center of the screen """
    global screen_height, screen_width, x_coordinate, y_coordinate
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
center_screen()

## Outline
frame1 = Frame(root, highlightbackground="blue", highlightthickness=1,width=370, height=590, bd=2)
frame1.pack(pady=10, padx=10)


## Menu Bar
menubar = Menu(root)

# About and Help
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label ='Help', menu = help)
def show_about():
    messagebox.showinfo('ASD', "Autism spectrum disorder is a significant developmental condition that hinders communication and social interaction abilities. It affects various aspects of an individual's cognitive, emotional, social, and physical well-being due to its impact on the nervous system. Symptoms can range in severity, commonly including challenges in communication and social interactions, along with repetitive behaviors and intense interests. Early identification and access to behavioral, educational, and family interventions can help alleviate symptoms, promote development, and enhance learning outcomes.\n\nWhile treatment can provide support, autism spectrum disorder cannot be cured. It is a chronic condition that can persist for years or throughout life. Diagnosis typically requires medical evaluation, although lab tests or imaging studies are rarely necessary.")
def show_affect():
    messagebox.showinfo('Effects', 'ASD, or autism spectrum disorder, is a neuro-developmental condition that can lead to various social, communication, and behavioral difficulties in children. While certain children may exhibit ASD symptoms during infancy, others may initially develop typically before later displaying withdrawal or aggression.')
def show_eval():
    messagebox.showinfo('Evaluation effects', "Early evaluation of autism spectrum disorder (ASD) is crucial as it enables timely initiation of targeted intervention programs tailored to a child's specific needs. These interventions, such as speech therapy, occupational therapy, and behavioral interventions, can address communication challenges, improve social interactions, and manage behavioral issues effectively. Additionally, early diagnosis allows families to access education and support services, empowering them to understand ASD better and actively participate in their child's development. Ultimately, early intervention significantly improves long-term outcomes by promoting optimal development, school readiness, and overall well-being for children with ASD.")
def show_q_chat():
    messagebox.showinfo('Q-CHAT-10', "The Q-CHAT measures ASD symptoms and language impairments in toddlers. The Q-CHAT-10 is a uni-dimensional measure of autistic traits.")
def exit_app():
    exit(0)
help.add_command(label ='About', command = show_about)
help.add_command(label ='How it might affect your child?', command = show_affect)
help.add_command(label ='How the evaluation helps?', command = show_eval)
help.add_command(label ='What is Q-Chat-10?', command = show_q_chat)
help.add_separator()
help.add_command(label ='Exit', command = exit_app)

# More Info
info = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Info', menu=info)
def know_more():
    open('https://www.cdc.gov/ncbddd/autism/facts.html')
info.add_command(label='More', command=know_more)


## NAME SECTION ##
name_label = Label(root, text="Name:")
name_label.place(x=30, y=50)
name_entry = Entry(root, borderwidth=.5, relief="solid")
name_entry.place(x=85, y=50, width=197)
name_entry.focus_force()
name = ''
def name_clicked():
    global name
    name = name_entry.get()
    if name=='':
        messagebox.showerror('Error', 'Name is empty!')
    else:
        name_button.config(state='disabled')
        name_entry.config(state='disabled')
        name_button.config(background=confirm_color)
        messagebox.showinfo('Information', "Candidate\'s Name will not be recorded!")
name_button = Button(root, text='Confirm', command=name_clicked, relief='groove')
name_button.place(x=290, y =47)



## AGE AND DOB SECTION ##
current_date = datetime.now()
reverse_date_upper = current_date + relativedelta(months=-18)
reverse_date_lower = current_date + relativedelta(months=-70)
cal = DateEntry(root, borderwidth=1, relief="solid", width=12, date_pattern='dd/mm/y', year = current_date.year, month = current_date.month, day = current_date.day, background='darkblue', foreground='white')
dob_label = Label(root, text="DOB:")
dob_label.place(x=30, y=90)
dob = ''
def dob_clicked():
    global dob
    dob = cal.get()
    dob  = dob.split('/')
    if date(year=reverse_date_lower.year, month=reverse_date_lower.month, day=reverse_date_lower.day)< date(year=int(dob[2]), day=int(dob[0]), month=int(dob[1])) < date(year=reverse_date_upper.year, month=reverse_date_upper.month, day=reverse_date_upper.day):
        dob_button.config(state='disabled')
        cal.config(state='disabled')
        dob_button.config(background=confirm_color)
    else:
        messagebox.showerror("Age Error", "Date range should be from 18 months to 5 years!") 
dob_button = Button(root, text='Confirm', command=dob_clicked, relief='groove')
dob_button.place(x=290, y =88)
cal.place(x=85, y=90, width=197)


## GENDER SECTION ## 
gender_label = Label(root, text="Gender:")
gender_drop = Combobox(state="readonly", values=["None", "Male", "Female"], width=29)
gender_drop.current(0)
gender = ''
gender_label.place(x=30, y=130)
gender_drop.place(x=85, y=130)
def gender_clicked():
    global gender
    gender = gender_drop.get()
    if gender == 'None':
        messagebox.showerror("Gender Error", "Not selected!")
    else:
        gender_button.config(state='disabled')
        gender_drop.config(state='disabled')
        gender_button.config(background=confirm_color)
gender_button = Button(root, text='Confirm', command=gender_clicked, relief='groove')
gender_button.place(x=290, y =128)        


## Ethnicity Selection ##
ethnicity_label = Label(root, text="Ethnicity:")
ethnicity_types = ["None", 'Asian', 'Black', 'Hispanic', 'Latino', 'Middle Eastern', 'Mixed', 'Native Indian', 'Pacifica', 'South Asian', 'White European', 'Others', 'Unknown']
ethnicity_drop = Combobox(state="readonly", values=ethnicity_types, width=29)
ethnicity_drop.current(0)
ethnicity = ''
ethnicity_label.place(x=30, y=170)
ethnicity_drop.place(x=85, y=170)
def ethnicity_clicked():
    global ethnicity
    ethnicity = ethnicity_drop.get()
    if ethnicity == 'None':
        messagebox.showerror("Ethnicity Error", "Not selected!")
    else:
        ethnicity_button.config(state='disabled')
        ethnicity_drop.config(state='disabled')
        ethnicity_button.config(background=confirm_color)
ethnicity_button = Button(root, text='Confirm', command=ethnicity_clicked, relief='groove')
ethnicity_button.place(x=290, y =168)


## Neonatal jaundice Entry ##
jaundice_label = Label(root, text="Neonatal Jaundice:")
jaundice_ans = ["None", "Yes", "No"]
jaundice_drop = Combobox(state="readonly", values=jaundice_ans, width=20)
jaundice_drop.current(0)
jaundice = ''
jaundice_label.place(x=30, y=210)
jaundice_drop.place(x=140, y=210)
def jaundice_clicked():
    global jaundice
    jaundice = jaundice_drop.get()
    if jaundice == 'None' or '':
        messagebox.showerror("Error", "Not selected!")
    else:
        jaundice_button.config(state='disabled')
        jaundice_drop.config(state='disabled')
        jaundice_button.config(background=confirm_color)
jaundice_button = Button(root, text='Confirm', command=jaundice_clicked, relief='groove')
jaundice_button.place(x=290, y =208)

## Family Member with ASD ##
family_label = Label(root, text="Any family member with ASD:")
family_ans = ["None", "Yes", "No"]
family_drop = Combobox(state="readonly", values=family_ans, width=10)
family_drop.current(0)
family = ''
family_label.place(x=30, y=250)
family_drop.place(x=200, y=250)
def family_clicked():
    global family
    family = family_drop.get()
    if family == 'None' or '':
        messagebox.showerror("Error", "Not selected!")
    else:
        family_button.config(state='disabled')
        family_drop.config(state='disabled')
        family_button.config(background=confirm_color)
family_button = Button(root, text='Confirm', command=family_clicked, relief='groove')
family_button.place(x=290, y =248)


## Person Taking the test ##
user_label = Label(root, text="User taking the test:")
user_ans = ["None", "Parent", "Doc/Pediatrician", "Relative"]
user_drop = Combobox(state="readonly", values=user_ans, width=20)
user_drop.current(0)
user = ''
user_label.place(x=30, y=290)
user_drop.place(x=140, y=290)
def user_clicked():
    global user
    user = user_drop.get()
    if user == 'None' or '':
        messagebox.showerror("User Error", "Please select the person taking the test!")
    else:
        user_button.config(state='disabled')
        user_drop.config(state='disabled')
        user_button.config(background=confirm_color)
user_button = Button(root, text='Confirm', command=user_clicked, relief='groove')
user_button.place(x=290, y =288)


## Separator ##
l = Label(root, text = "CONTACT DETAILS")
l.place(relx = 0.5, rely = .7, anchor = CENTER)
l.configure(font=("Courier", 14, 'bold'))

## Email ##
email = ''
email_label = Label(root, text='Email:')
email_entry = Entry(root)
email_entry.config(width=50, relief='solid')
def get_email():
    global email
    email= email_entry.get()
    if match('^[_a-z0-9-]+(\\.[_a-z0-9-]+)*@[a-z0-9-]+(\\.[a-z0-9-]+)*(\\.[a-z]{2,4})$', email):
        email_button.config(state='disabled')
        email_entry.config(state='disabled')
        email_button.config(background=confirm_color)
        if name!='' and len(dob)!=0 and (gender!='None' or gender!='') and (ethnicity!='None' or ethnicity!='') and (jaundice!='None' or jaundice!='') and (family!='' or family!='None') and (user!='None' or user!=''):
            submit_button.configure(state='active')    
    else:
        messagebox.showerror('Mail Error', 'Invalid Email!')
email_button = Button(root, text='Confirm', command=get_email, relief='groove')
email_label.place(x=30, y=380)
email_entry.place(x=85, y=380, width=197)
email_button.place(x=290, y=378)

## Function to calculate age
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age * 12
    
## submit button ##
def submit_action():
    global user, dob, gender, ethnicity, jaundice, family, ethnicity_types, user_ans
    
    sender_email = mail_id
    recipient_email = email
    sender_password = password
    subject = "Welcome to NeuroVantage AI"
    note = 'DISCLAIMER: \nName and email will not be stored and used. Name has been taken so as to address the child in the application and email. Email has been taken for communication and result mailing purposes.'
    body = f"Welcome {user} of {name} for participating in the ASD assessment program. Thank you for connecting with us. We hope to serve you the best cure and help.\n\nThe details filled out are:\nName: {name}\nDOB: {'-'.join(dob)}\nGender: {gender}\nEthnicity: {ethnicity}\nNeonatal Jaundice: {jaundice}\nAny family member diagnosed with ASD: {family}\nUser taking the test: {user}\n\nThanking You,\nTeam Cognitive Healers\n\n{note}"
    
    # Calculating parameters
    age = date(int(dob[2]), int(dob[1]), int(dob[0]))
    age = calculate_age(age)
    gender = 1 if gender == 'Male' else 0
    ethnicity_types =  ethnicity_types[1:]
    ethnicity_types.sort()
    print(ethnicity_types)
    ethnicity = ethnicity_types.index(ethnicity)
    jaundice = 0 if jaundice.lower()=='no' else 1
    user_ans = user_ans[1:]
    user_ans.sort()
    user = user_ans.index(user)
    family = 0 if family.lower()=='no' else 1
    # messagebox.showinfo('Data_Collected', f'Age in Months: {age}\n, DOB: {dob}\n, Gender: {gender}\n, Ethnicity: {ethnicity}\n, Neonatal Jaundice: {jaundice}\n, User taking the test: {user}\n, Any Family member with ASD: {family}\n')
    
    # Create a MIMEText object\
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Send email
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        messagebox.showinfo("Success", "Verification E-mail sent successfully!")
        root.destroy()
        run(['python', 'questionnaire.py', f"{recipient_email}, {age}, {gender}, {ethnicity}, {jaundice}, {user}, {family}, {name}"])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

submit_button = Button(root, text='S  U  B  M  I  T', command=submit_action, state='disabled', relief='groove', font=('Arial', 11, 'bold'), background='#dee9fa')
submit_button.place(x=30, y=420, width=315)

root.config(menu = menubar)
root.mainloop()
print(f'Name: {name}\nDOB: {dob}\nGender: {gender}\nEthnicity: {ethnicity}\nNeonatal Jaundice: {jaundice}\nUser: {user}\nEmail: {email}')
