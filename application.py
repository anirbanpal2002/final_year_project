# Imports
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

# Configuration extraction from JSON
class Config_for_mail:
    def __init__(self) -> None:
        self.sender_email = "noreplyasddetection@gmail.com"
        self.password = "oriv wqnc skrn jsgw" 

# Centering Windows class
class Center_window:
    def center_window(root, window_width, window_height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Coordinates of the upper left corner of the window to make the window appear in the center
        x_coordinate = int((screen_width/2) - (window_width/2))
        y_coordinate = int((screen_height/2) - (window_height/2))
        root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Framing around the window
class Framing:
    def create_frame(root, frame_width, frame_height):
        frame1 = Frame(root, highlightbackground="blue", highlightthickness=1,width=frame_width, height=frame_height, bd=2)
        frame1.pack(pady=10, padx=10)

# Menubar Class for all windows
class Menubar:
    def create_menu(root):
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
        root.config(menu=menubar)
        
# Input Form Class
class Input_Form:
    def __init__(self):
        self.window_width=380
        self.window_height=490
        self.root = Tk()
        self.root.geometry(f'{self.window_width}x{self.window_height}')
        self.root.title('Input Form')
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file = '.images/form-icon.png') )
        
        # Field Variables
        self.name = ''
        self.dob = ''
        self.gender = ''

        # Frame Outline
        Framing.create_frame(self.root, 370, 590)

        # Menu Bar
        Menubar.create_menu(self.root)
        
        # Widgets
        ## NAME SECTION ##
        def name_clicked():
            self.name = name_entry.get()
            if self.name=='':
                messagebox.showerror('Error', 'Name is empty!')
            else:
                name_button.config(state='disabled')
                name_entry.config(state='disabled')
                name_button.config(background=confirm_color)
                messagebox.showinfo('Information', "Candidate\'s Name will not be recorded!")
        
        ## AGE AND DOB SECTION ##
        current_date = datetime.now()
        reverse_date_upper = current_date + relativedelta(months=-18)
        reverse_date_lower = current_date + relativedelta(months=-70)
        def dob_clicked():
            self.dob = cal.get()
            self.dob  = self.dob.split('/')
            if date(year=reverse_date_lower.year, month=reverse_date_lower.month, day=reverse_date_lower.day)< date(year=int(self.dob[2]), day=int(self.dob[0]), month=int(self.dob[1])) < date(year=reverse_date_upper.year, month=reverse_date_upper.month, day=reverse_date_upper.day):
                dob_button.config(state='disabled')
                cal.config(state='disabled')
                dob_button.config(background=confirm_color)
            else:
                messagebox.showerror("Age Error", "Date range should be from 18 months to 5 years!") 

        # Labels configuration
        name_label = Label(self.root, text="Name:")
        dob_label = Label(self.root, text="DOB:")
        gender_label = Label(self.root, text="Gender:")
        
        # Entry field configuration
        name_entry = Entry(self.root, borderwidth=.5, relief="solid")
        name_entry.focus_force()
        cal = DateEntry(self.root, borderwidth=1, relief="solid", width=12, date_pattern='dd/mm/y', year = current_date.year, month = current_date.month, day = current_date.day, background='darkblue', foreground='white')
        gender_drop = Combobox(state="readonly", values=["None", "Male", "Female"], width=29)
        gender_drop.current(0)
        
        
        
        # Button configuration
        name_button = Button(self.root, text='Confirm', command=name_clicked, relief='groove')
        dob_button = Button(self.root, text='Confirm', command=dob_clicked, relief='groove')

        # Placing the widgets
        name_label.place(x=30, y=50)
        name_entry.place(x=85, y=50, width=197)
        name_button.place(x=290, y =47)
        
        dob_label.place(x=30, y=90)
        cal.place(x=85, y=90, width=197)
        dob_button.place(x=290, y =88)
        
        # Centering the window
        Center_window.center_window(self.root, self.window_width, self.window_height)
        self.root.mainloop()
        
    
        
    
# Questionnaire Class
# Download Model
# Model Loading and Evaluation Class
# Calling main function
if __name__=='__main__':
    Input_Form()
