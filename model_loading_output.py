from pandas import read_csv
from joblib import load
from tkinter import Tk, PhotoImage,Label,Button
from sys import argv
from download_model import download
from sklearn.preprocessing import LabelEncoder
from numpy import log
from time import sleep
from threading import Thread
import firebase_admin
from firebase_admin import credentials, storage
from google.oauth2 import service_account
from google.cloud import storage
from os.path import exists
from os import mkdir, remove
from tkinter import filedialog
from tkinter import messagebox
from subprocess import run


per = 0
dir_name = ''
folder_path = ''


cred = credentials.Certificate(".keys/key.json")
cred_var = service_account.Credentials.from_service_account_file(".keys/key.json")

# Global variables
counter = 3
running = True

name = argv[1]
data_to_eval = argv[2]
weight = int(argv[3])
email_sender = argv[4]
# name = 'John Doe'
# data_to_eval = "C:/Users/USER/AppData/Local/Temp/data_acbd5bcc-2b59-4ad2-8679-4529ce1fd6b3.csv"
# weight = 23

root = Tk()
root.title("Evaluation window")
icon = PhotoImage(file = '.images/result.png') 

window_width = 700
window_height = 400

root.iconphoto(False, icon)
root.geometry(f'{window_width}x{window_height}')
root.resizable(False, False)


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


def encode_labels(data):
    for col in data.columns:
        # Here we will check if datatype
        # is object then we will encode it
        if data[col].dtype == object:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
    return data


label_img_1 = PhotoImage(file=".images/evaluating.png").subsample(2, 2)
label1 = Label(image=label_img_1, state='active')
label1.place(anchor='center', relx=0.5, rely=0.5)


def update_label():
    global counter, running, label1
    while counter > 0 and running:
        counter -= 1
        sleep(1)

def send_treatment_plan():
    global per, dir_name, folder_path
    dir_name = filedialog.askdirectory()
    folder_path = f'{dir_name}/Treatment_Plan'

    if not exists(folder_path):
        mkdir(folder_path)
    if result == [1]:
        if 10<=per<=33:
            storage.Client(credentials=cred_var).bucket(firebase_admin.storage.bucket().name).blob('Mild ASD.pdf').download_to_filename(f'{folder_path}/Mild ASD.pdf')
            run(['python', 'send_treatment_plan.py', email_sender, f'{folder_path}/Severe ASD.pdf'])
            messagebox.showinfo('Info', 'File Downloaded!\nClose the window')
        elif per<=66:
            storage.Client(credentials=cred_var).bucket(firebase_admin.storage.bucket().name).blob('Moderate ASD.pdf').download_to_filename(f'{folder_path}/Moderate ASD.pdf')
            run(['python', 'send_treatment_plan.py', email_sender, f'{folder_path}/Severe ASD.pdf'])
            messagebox.showinfo('Info', 'File Downloaded!\nClose the window')
        else:
            storage.Client(credentials=cred_var).bucket(firebase_admin.storage.bucket().name).blob('Severe ASD.pdf').download_to_filename(f'{folder_path}/Severe ASD.pdf')
            run(['python', 'send_treatment_plan.py', email_sender, f'{folder_path}/Severe ASD.pdf'])
            messagebox.showinfo('Info', 'File Downloaded!\nClose the window')
        remove(folder_path)
    
                    
def evaluate_model():
    global label1, label2, result, running, per
    sleep(3)
    if running:
        file_Path = download()
        loaded_model = load(file_Path)
        df1 = read_csv(data_to_eval)
        df1['Age_Mons'] = df1['Age_Mons'].apply(lambda x: log(x))
        df1 = df1.replace({'yes':1, 'no':0, 'Yes':1, 'No':0, '?':'others', 'Others':'others'})
        df1 = encode_labels(df1)
        # print(name,'\n', df1)
        result = loaded_model.predict(df1)
        text = ''
        per = (weight/73)*100
        
        if per<10:
            text='no'
        elif 10<=per<=33:
            text = 'mild'
        elif 34<=per<=66:
            text = 'moderate'
        else:
            text = 'severe'
        
        b = Button(root, text='Get treatment plan',  font=('Times New Roman', 14, 'italic'), command=send_treatment_plan, relief='groove', state='disabled')
        b.place(anchor='n', relx=0.5, rely=.6)
        
        if result == [0]:
            text += ' chance of'
        else:
            b.configure(state='active')
        
        per = "{:.2f}".format(per)
        label1.configure(text=f'{name} has {per}% {text} ASD.', image="", font=('Times New Roman', 14, 'italic'))
        per = float(per)
        print(folder_path)

# Start the threads
countdown_thread = Thread(target=update_label)
evaluating_thread = Thread(target=evaluate_model)

countdown_thread.start()
evaluating_thread.start()

root.mainloop()
