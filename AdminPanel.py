#import modules
 
from os import curdir
from tkinter import *
import os
import tkinter.filedialog
import numpy as np
from numpy.lib.polynomial import polyfit
from pandas.core import frame
from styleframe import StyleFrame, utils

import pandas as pd
import numpy as np
import csv

from tkmagicgrid import *
from tkinter import ttk
import threading
import json
from pathlib import Path
try:
    sys.stdout.write("\n")
    sys.stdout.flush()
except:
    class dummyStream:
        ''' dummyStream behaves like a stream but does nothing. '''
        def __init__(self): pass
        def write(self,data): pass
        def read(self,data): pass
        def flush(self): pass
        def close(self): pass
    # and now redirect all default streams to this dummyStream:
    sys.stdout = dummyStream()
    sys.stderr = dummyStream()
    sys.stdin = dummyStream()
    sys.__stdout__ = dummyStream()
    sys.__stderr__ = dummyStream()
    sys.__stdin__ = dummyStream()

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)

    ico_path = curdir+"\media\my_icon.ico"
    register_screen.iconbitmap(ico_path)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    global username_data
    global password_data
    global start_code
    global end_code
    global username_data
    global password_data
    global start_code
    global end_code
    username_data = StringVar()
    password_data = StringVar()
    start_code = StringVar()
    end_code = StringVar()

    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.bind('<Return>', register_user)
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login



def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    ico_path = curdir+"\media\my_icon.ico"
    login_screen.iconbitmap(ico_path)
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.bind('<Return>', login_verify) 
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user(event=None):
 
    username_info = username.get()
    password_info = password.get()
 
    file = open("user_credential_database/" + username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    register_screen.after(700,register_screen.destroy)
 
# Implementing event on login button 
 
def login_verify(event=None):
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    current_directory = os.getcwd()
    user_credential_directory = current_directory + '/'+"user_credential_database/"
 
    list_of_files = os.listdir(user_credential_directory)
    if username1 in list_of_files:
        file1 = open(user_credential_directory + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
 
    login_success_screen = Toplevel(login_screen)
    
    ico_path = curdir+"\media\my_icon.ico"
    login_success_screen.iconbitmap(ico_path)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    
    
    Button(login_success_screen, text="OK", command=del_and_open).pack()
    login_success_screen.after(500, del_and_open)
    
def del_and_open():
    delete_login_success()
    application_window()

  

    
class application_window:

    def __init__(self):
        self.root = Tk()
        frame = self.root
       
      
        ico_path = curdir+"\media\my_icon.ico"
        frame.iconbitmap(ico_path)
        frame.title("Predictive AI Application Window")
        frame.geometry("1024x1024")
        self.current_dir = curdir
        b1 = tkinter.Button(frame, text='Select Master Sheet',width=15, height=2, command=self.get_path_master).place(x=30, y=50)
        b2 = tkinter.Button(frame, text='Select Multiple Test Sheets (use ctrl + click to select)',width=40, height=2, command=self.get_path_test).place(x=300,y=50)
        #las - Label(frame,)
        self.progressbar = ttk.Progressbar(frame, mode='determinate',cursor='spider',length=300)
        self.progressbar.grid(column=1, row=0, sticky=W)
        self.progressbar["maximum"] = 100 
        
        self.progressbar["value"] = 0
        """photo_login = PhotoImage(file = curdir+"\predict.png")
        Button(text = '     Predict Now!', height="80", width="200",  image = photo_login, 
                        compound = LEFT, command = lambda:self.start_submit_thread(None)).place(x=90,y=150)"""

        #ttk.Button(frame, text="Predict Now",
      
        
        b3 = tkinter.Button(frame, text='Predict Now!',width=15, height=2 ,command= lambda:self.start_submit_thread(None)).place(x=90,y=150)
        "b2.pack(fill='x')"


    



        
    def get_path_master(self):
        if not os.path.exists('AI External-Outputs/path_info.txt'):
            check_from = curdir
        else:
            file = open("AI External-Outputs/path_info.txt","r")
            for lines in file.read().splitlines():
                if lines[0] == "M":
                    check_from = os.path.dirname(lines[1:])
            file.close() 
        
        self.master_sheet_filepath = tkinter.filedialog.askopenfilename(parent=self.root, initialdir= check_from ,title='Please Choose Master Sheet',filetypes=[('Excel File', '.xlsx'),('CSV Excel file', '.csv')])


    def get_path_test(self):
        if not os.path.exists('AI External-Outputs/path_info.txt'):
            check_from = curdir
        else:
            file = open("AI External-Outputs/path_info.txt","r")
            for lines in file.read().splitlines():
                if lines[0] == "T":
                    check_from = os.path.dirname(lines[1:])
            file.close() 
        
        self.test_sheet_filepaths = list(tkinter.filedialog.askopenfilenames(parent=self.root, initialdir=check_from,title='Please Choose Test Sheet',filetypes=[('Excel File', '.xlsx'),('CSV Excel file', '.csv')]))
     
                

        """print(f)"""




    def get_prediction(self):
        def read_master_sheet(filepath):
            sf = StyleFrame.read_excel(filepath , read_style=True, use_openpyxl_styles=False)
            return sf

        def df_column_uniquify(df):
            df_columns = df.columns
            new_columns = []
            for item in df_columns:
                counter = 0
                newitem = item
                while newitem in new_columns:
                    counter += 1
                    newitem = "{}_{}".format(item, counter)
                new_columns.append(newitem)
            df.columns = new_columns
            return df


        def read_data(filepath):
            df = pd.read_excel(filepath)
            return df

        def get_standard_matrix(sf):

            f = open('Value-json/hyperparam.json') 
            hyperparam = json.load(f)

            """

            def only_cells_with_red_text(cell):
                if cell!=cell:
                    return hyperparam['empty']
                
                if cell.style.bg_color in {utils.colors.red, 'FFFF0000'}:
                    return 150
            

                if cell.style.font_color in {utils.colors.green, 'FF00B050'}:
                    return hyperparam['green']


                elif cell.style.font_color in {utils.colors.yellow, '00FFFF00'}:
                    return hyperparam['yellow']

                elif cell.style.font_color in {utils.colors.purple, '800080'}:
                    return hyperparam['purple']

                
                elif cell.style.font_color in {utils.colors.red, 'FFFF0000'}:
                    return hyperparam['red']


                elif cell.style.font_color in {utils.colors.blue, 'FF0070C0'}:
                    return hyperparam['blue']
                
                
                elif cell.style.font_color in {utils.colors.black, '00000000'}:
                    return hyperparam['black']

                else:
                    return 100

            
            
            def only_cells_with_red_text_emp(cell):
                if cell!=cell:
                    return 0
                
                if cell.style.bg_color in {utils.colors.red, 'FFFF0000'}:
                    return 150
            
                if cell.style.font_color in {utils.colors.green, 'FF00B050'}:
                    return hyperparam['green']


                elif cell.style.font_color in {utils.colors.yellow, '00FFFF00'}:
                    return hyperparam['yellow']

                elif cell.style.font_color in {utils.colors.purple, '800080'}:
                    return hyperparam['purple']

                
                elif cell.style.font_color in {utils.colors.red, 'FFFF0000'}:
                    return hyperparam['red']


                elif cell.style.font_color in {utils.colors.blue, 'FF0070C0'}:
                    return hyperparam['blue']
                
                
                elif cell.style.font_color in {utils.colors.black, '00000000'}:
                    return hyperparam['black']


                else:
                    return 100


            """
  
            def only_cells_with_red_text(cell):
                if cell!=cell:
                    return hyperparam['empty']

                if '(' in str(cell.value):
                
                    if cell.style.bg_color in {utils.colors.red, 'FFFF0000'}:
                        return 150
                

                    if cell.style.font_color in {utils.colors.green, 'FF00B050'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['green']
                        elif cer[0] == 'V':
                            return int(cer[1])


                    elif cell.style.font_color in {utils.colors.yellow, '00FFFF00'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['yellow']
                        elif cer[0] == 'V':
                            return int(cer[1])
                        

                    elif cell.style.font_color in {utils.colors.purple, '800080'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['purple']
                        elif cer[0] == 'V':
                            return int(cer[1])

                    
                    elif cell.style.font_color in {utils.colors.red, 'FFFF0000'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')

                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['red']
                        elif cer[0] == 'V':
                            return int(cer[1])


                    elif cell.style.font_color in {utils.colors.blue, 'FF0070C0'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['blue']
                        elif cer[0] == 'V':
                            return int(cer[1])
                    
                    
                    elif cell.style.font_color in {utils.colors.black, '00000000'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['black']
                        elif cer[0] == 'V':
                            return int(cer[1])
                    else:
                        return 100

                else:
                    return 100

            
            
            def only_cells_with_red_text_emp(cell):
                if cell!=cell:
                    return 0
                if '(' in str(cell.value):

                    if cell.style.bg_color in {utils.colors.red, 'FFFF0000'}:
                        return 150


                    if cell.style.font_color in {utils.colors.green, 'FF00B050'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['green']
                        elif cer[0] == 'V':
                            return int(cer[1])


                    elif cell.style.font_color in {utils.colors.yellow, '00FFFF00'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['yellow']
                        elif cer[0] == 'V':
                            return int(cer[1])
                        

                    elif cell.style.font_color in {utils.colors.purple, '800080'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['purple']
                        elif cer[0] == 'V':
                            return int(cer[1])

                    
                    elif cell.style.font_color in {utils.colors.red, 'FFFF0000'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['red']
                        elif cer[0] == 'V':
                            return int(cer[1])


                    elif cell.style.font_color in {utils.colors.blue, 'FF0070C0'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['blue']
                        elif cer[0] == 'V':
                            return int(cer[1])
                    
                    
                    elif cell.style.font_color in {utils.colors.black, '00000000'}:
                        check = cell.value
                        check = check[:-1]
                        cert = check.split('(')
                        cer = cert[1].split(',')
                        if cer[0] == 'C':
                            return hyperparam['black']
                        elif cer[0] == 'V':
                            return int(cer[1])

                    else:
                        return 100
                else:
                    return 100
            
            
            sf_2 = StyleFrame(sf.applymap(only_cells_with_red_text))
            sf_3 = StyleFrame(sf.applymap(only_cells_with_red_text_emp))


            # passing a tuple to pandas.dropna is deprecated since pandas 0.23.0, but this can be
            # avoided by simply calling dropna twice, once with axis=0 and once with axis=1
            def get_sum(sf_3):

                sf_3.to_excel(curdir+'/AI Internal-Outputs/output_0.xlsx').save()
                df = read_data(curdir+'/AI Internal-Outputs/output_0.xlsx')
                code_dict = []
                lent = 0
                for col in df.columns:
                    if 'Code' in col:
                        lent = lent + 1
                print(lent)
                for i in range(1,lent):
                    code_dict.append("Code "+str(i))
                qf=[]
                df = df.fillna(0)
                for col in code_dict:
                
                    if any(i == 150 for i in df[col].values):
                        qf.append(col)
                
                qualifying_dict = {}
                df = df.iloc[3:,6:]
                for col_n in qf:
                    idx = int(col_n.split()[1])
                    df_n = df.iloc[:,idx-1]
                    qualifying_dict[col_n] = df_n.values
                standard_matrix = df.values

                def sumColumn(matrix):
                    return np.sum(matrix, axis=0) 

                
                #sum_std_mat = sumColumn(standard_matrix)
                return standard_matrix

            

            #print(qualifying_dict)


            sf_2.to_excel(curdir+'/AI Internal-Outputs/output.xlsx').save()
            df = read_data(curdir+'/AI Internal-Outputs/output.xlsx')
            code_dict = []
            lent = 0
            for col in df.columns:
                if 'Code' in col:
                    lent = lent + 1
            print(lent)
            for i in range(1,lent):
                code_dict.append("Code "+str(i))
            qf=[]
            df = df.fillna(0)
            for col in code_dict:
            
                if any(i == 150 for i in df[col].values):
                    qf.append(col)
            
            qualifying_dict = {}
     
            df = df.iloc[3:,6:]
            for col_n in qf:
                idx = int(col_n.split()[1])
                df_n = df.iloc[:,idx-1]
                qualifying_dict[col_n] = df_n.values
            
            standard_matrix = df.values


            
            
            #print(standard_matrix)
            return standard_matrix,qualifying_dict,get_sum(sf_3)


     




        def get_age_decision(age):
            code_dict = []
            for i in range(1,40):
                code_dict.append("Code "+str(i))
            
            dicte = dict.fromkeys(code_dict, 0)
            prediction_codes = []
            if age<35:
                dicte['Code 1']=120
                prediction_codes.append("Code 1")
            if 30<age<50:
                dicte['Code 2']=100
                prediction_codes.append("Code 2")
            if 10<age<58:
                dicte['Code 3']=100
                dicte['Code 5']=100
                dicte['Code 7']=100
                dicte['Code 13']=100
                dicte['Code 14']=100
                dicte['Code 15']=100
                prediction_codes.append("Code 3")
                prediction_codes.append("Code 5")
                prediction_codes.append("Code 7")
                prediction_codes.append("Code 13")
                prediction_codes.append("Code 14")
                prediction_codes.append("Code 15")
            if age<55:
                dicte['Code 12']=100
                prediction_codes.append("Code 12")

            if 10<age<68:
                dicte['Code 16']=100
                prediction_codes.append("Code 16")

            if age<45:
                dicte['Code 18']=100
                prediction_codes.append("Code 45")

            if 20<age<52:
                dicte['Code 28']=100
                prediction_codes.append("Code 28")

            if 45<age<58:
                dicte['Code 30']=100
                dicte['Code 31']=100
                prediction_codes.append("Code 30")
                prediction_codes.append("Code 31")

            if 12<age<60:
                dicte['Code 33']=100
                prediction_codes.append("Code 33")
            if 12<age<58:
                dicte['Code 35']=100
                prediction_codes.append("Code 35")
            if 10<age<60:
                dicte['Code 37']=100
                dicte['Code 38']=100
                prediction_codes.append("Code 37")
                prediction_codes.append("Code 38")
            if age:
                prediction_codes.append("Code 4")
                prediction_codes.append("Code 6")
                prediction_codes.append("Code 8")
                prediction_codes.append("Code 9")
                prediction_codes.append("Code 10")
                prediction_codes.append("Code 11")
                prediction_codes.append("Code 17")
                prediction_codes.append("Code 19")
                prediction_codes.append("Code 20")
                prediction_codes.append("Code 21")
                prediction_codes.append("Code 22")
                prediction_codes.append("Code 23")
                prediction_codes.append("Code 24")
                prediction_codes.append("Code 25")
                prediction_codes.append("Code 26")
                prediction_codes.append("Code 27")
                prediction_codes.append("Code 29")
                prediction_codes.append("Code 32")
                prediction_codes.append("Code 34")
                prediction_codes.append("Code 36")
                dicte["Code 4"]=100
                dicte["Code 6"]=100
                dicte["Code 8"]=100
                dicte["Code 9"]=100
                dicte["Code 10"]=100
                dicte["Code 11"]=100
                dicte["Code 17"]=100
                dicte["Code 19"]=100
                dicte["Code 20"]=100
                dicte["Code 21"]=100
                dicte["Code 22"]=100
                dicte["Code 23"]=100
                dicte["Code 24"]=100
                dicte["Code 25"]=100
                dicte["Code 26"]=100
                dicte["Code 27"]=100
                dicte["Code 29"]=100
                dicte["Code 32"]=100
                dicte["Code 34"]=100
                dicte["Code 36"]=100

            return dicte,prediction_codes





            

     


        def get_percentile(score_arr,sum_std_mat,idx_file,df_attempt):

            """
            ptile = [ (len(list(np.where(np.array(x)<=i)[0]))/len(x))*100  for i in x]
            """
            cnt = 0
            
            master_attempt = np.where(sum_std_mat ==0,0,1)
            score_mul = np.dot(df_attempt.T,master_attempt)
            score_mul = [i * 120 for i in score_mul]
        
            unique_score = score_mul
            max_v = np.max(score_arr)
            inx = max_v
            comp_std = []
            for inx,val in enumerate(score_arr):
                bck = (val/unique_score[idx_file[-inx-1]])*100
                bck = bck/10
                comp_std.append(bck)
                if val>0:
                    cnt+=1
                    inx = val
            if max_v == 0:
                max_v = 1
            mulk = (max_v - inx)/max_v



            scorecard = [(((i/max_v)*100)-(cnt*mulk)*2.2132) for i in score_arr]
            return scorecard,comp_std

        def get_qualify(attempt,qualify_dict):
            code_dict = []
            for i in range(1,40):
                code_dict.append("Code "+str(i))
            
            hell_dict = dict.fromkeys(code_dict, 1)
            for key,val in qualify_dict.items():

            
                check = np.where(np.logical_and(val==150, attempt==1))[0]
                #print(key)
                #print(check)
                
                if len(check)>0:
    
                    
                    
                    hell_dict[key]= 1
                else:
                    hell_dict[key]= -100000

            #print(hell_dict)

            return hell_dict

        def get_test_output(df, col_number):
            #df = read_data(filepath)

            df_check = df.iloc[4:]
            age = df[col_number].iloc[3]
            ethnicity = df[col_number].iloc[2]

            df_check = df_check.fillna(0)
            to_check_array = df_check[col_number].values
            return to_check_array,age,ethnicity
        def get_top_5_predictions(to_check_array,age,standard_matrix,qualifying_dict,sum_std_mat,ethnicity,col_number):
            
            """ dicte,prediction_codes = get_age_decision(age)
            to_check_array_match = np.where(to_check_array == 0, 0, 1)
            tat_val_match = np.dot(to_check_array_match.T,standard_matrix)
            for idx,val in enumerate(tat_val_match):
            code_idx = "Code "+str(idx+1)
            tat_val_match[idx] = tat_val_match[idx]*dicte[code_idx] 
            to_check_array_n_match = np.where(to_check_array == 0, -0.001, 0)
            tat_val_n_match = np.dot(to_check_array_n_match.T,standard_matrix)

            for idx,val in enumerate(tat_val_n_match):
            code_idx = "Code "+str(idx+1)
            tat_val_n_match[idx] = tat_val_n_match[idx]*dicte[code_idx] 
            tat_val = tat_val_match + tat_val_n_match
            top_2_idx = np.argsort(tat_val)[-5:]
            top_2_val = [tat_val[i] for i in reversed(top_2_idx)]
            accuarcy = [val/sum(top_2_val) for val in top_2_val]
            predictions = ["Code " + str(idx+1) for idx in reversed(top_2_idx)]
            return predictions,accuarcy,get_scores(top_2_val) """

            consumption_dict = {}
            consumption_dict['Finetuning Logic'] = "Not Consumed"
            consumption_dict['Qualifying criteria'] = "Not Used"
            consumption_dict['Age logic'] = "Not Consumed"
            consumption_dict['Insurance settlement history'] = "Not Consumed"
            consumption_dict['Ethnicity Logic'] = "Not Consumed"
            consumption_dict['Layer Logic'] = "Not Consumed"
            f = open('Value-json/hyperparam.json') 
            hyperparam = json.load(f)
            to_check_array = np.where(to_check_array == 0, hyperparam['alpha'], 1)
            tat_val = np.dot(to_check_array.T,standard_matrix)
            dicte,prediction_codes = get_age_decision(age)
            qualify_dict = get_qualify(to_check_array,qualifying_dict)
            col_number =col_number
            intial_logic = {}
            for idx,val in enumerate(tat_val):
                code_idx = "Code "+str(idx+1)
                f = open('Value-json/logic_activation.json') 
                activation = json.load(f)
                if qualify_dict[code_idx] <0:
                    if activation['qualifying_criteria'] == 'active':
                        consumption_dict['Qualifying criteria'] = "Used"
                        tat_val[idx] = -1000000
                    else:
                        pass
                else:
                    if activation['age_logic'] == 'active':
                        if dicte[code_idx] == 0:
                            consumption_dict['Age logic'] = "Consumed"
                            tat_val[idx] = -1000000
                        else:
                            pass
                    else:
                        pass
                intial_logic[code_idx] = tat_val[idx]
            

                   

      
            

            
            f = open('Value-json/logic_activation.json') 
            activation = json.load(f)


            if activation['settlement_logic'] == 'active':

                df = pd.read_excel(os.curdir + '/Logic Container/Insurance settlement history.xlsx')

 
            


                for idx,rows in df.iterrows():

                    if rows['Age']!=rows['Age']:
                        break
                    else:
                        age_r = rows['Age'].split('-')
                    

                        age_start = int(age_r[0])
                        age_end = int(age_r[1])
                        

                        
                        if age_start <= age <= age_end:

                            total = sum(rows[1:].values)




                            for inx,score in enumerate(tat_val):
                                code_idx = "Code "+str(inx+1)

                                if inx!=3122239:


                                        

                                    prob = int(rows[code_idx])/int(total)
                                    consumption_dict['Insurance settlement history'] = "Consumed"
                                    tat_val[inx] = tat_val[inx] * prob
                                  
                                        
                                        
                            
                                         
                                else:
                                    continue
            
            settlement_logic = {}


            for inx,score in enumerate(tat_val):
                code_idx = "Code "+str(inx+1)
                settlement_logic[code_idx] = tat_val[inx]


            f = open('Value-json/logic_activation.json') 
            activation = json.load(f)


            if activation['ethnicity_logic'] == 'active':

                df = pd.read_excel(os.curdir + '/Logic Container/Ethnicity Logic.xlsx')
                #total  = df.iloc[9,:]
                cols = df.columns
                for inx,rows in df.iterrows():
                    if rows['Ethnicity']!=rows['Ethnicity']:
                        break
                    else:
                        if ethnicity == rows['Ethnicity']:
                            
                            for inx,score in enumerate(tat_val):
                                code_idx = "Code "+str(inx+1)

                                if inx!=311229:

                            
                                    prob = rows[code_idx]
                   
                                    consumption_dict['Ethnicity Logic'] = "Consumed"
                                    
                                    
                        
                                    tat_val[inx] = tat_val[inx] * prob 
                                else:
                                    pass
                        else:
                            for inx,score in enumerate(tat_val):
                                code_idx = "Code "+str(inx+1)

                                if inx!=311129:

                            
                                    prob = 1
                        
                                    consumption_dict['Ethnicity Logic'] = "Consumed"
                                    
                                    
                        
                                    tat_val[inx] = tat_val[inx] * prob 
                                else:
                                    pass


                        




            
            ethnicity_logic = {}


            for inx,score in enumerate(tat_val):
                code_idx = "Code "+str(inx+1)
                ethnicity_logic[code_idx] = tat_val[inx]
            
            
            
            f = open('Value-json/logic_activation.json') 
            activation = json.load(f)


            if activation['finetuning_logic'] == 'active':

                df = pd.read_excel(os.curdir + '/Logic Container/Fine tuning logic.xlsx')
                #total  = df.iloc[9,:]
                cols = df.columns
                for inx,rows in df.iterrows():
                    if rows['Age']!=rows['Age']:
                        break
                    else:
                        age_r = rows['Age'].split('-')
                    

                        age_start = int(age_r[0])
                        age_end = int(age_r[1])
                        

                        
                        if age_start <= age <= age_end:
                            
                            for inx,score in enumerate(tat_val):
                                code_idx = "Code "+str(inx+1)

                                if inx!=31119:


                                    if '#' not in str(rows[code_idx]):
                                        
        
                                        prob = rows[code_idx]
                          
                                        consumption_dict['Finetuning Logic'] = "Consumed"

                                        tat_val[inx] = tat_val[inx] * prob
                                    else:
                                        tat_val[inx] = -100000

                            

                                    

                                    
                        

                                else:
                                    continue




            
            finetuning_logic = {}


            for inx,score in enumerate(tat_val):
                code_idx = "Code "+str(inx+1)
                finetuning_logic[code_idx] = tat_val[inx]

            


            f = open('Value-json/logic_activation.json') 
            activation = json.load(f)


            if activation['layer_logic'] == 'active':

                df = pd.read_excel(os.curdir + '/Logic Container/Layer Logic.xlsx')

    
            
                layer = 0

                for idx,rows in df.iterrows():
                    layer = layer + 1
                    if layer == 1:
                        initial_prediction_weight = rows['Weightage']
                    elif layer ==2:
                        settlement_logic_weight = rows['Weightage']
                    elif layer == 3:
                        ethnicity_logic_weight = rows['Weightage']
                    elif layer == 4:
                        finetuning_logic_weight = rows['Weightage']
                    else:
                        pass

                
                for inx,score in enumerate(tat_val):
                    code_idx = "Code "+str(inx+1)
                    tat_val[inx] = intial_logic[code_idx]*(initial_prediction_weight +  settlement_logic_weight*(settlement_logic[code_idx]/intial_logic[code_idx]) + ethnicity_logic_weight*(ethnicity_logic[code_idx]/settlement_logic[code_idx]) + finetuning_logic_weight*(finetuning_logic[code_idx]/ethnicity_logic[code_idx]))
                    consumption_dict['Layer Logic'] = "Consumed"
                
                



                   
                   



        
            
            final_logic = {}


            for inx,score in enumerate(tat_val):
                code_idx = "Code "+str(inx+1)
                final_logic[code_idx] = tat_val[inx]




            




            
            def get_logic_pred(dicte):
                new_dicte = {k: v for k, v in sorted(dicte.items(), key=lambda item: item[1], reverse=True)}
                cnt = 0
                logic_pred = []
                for idx,value in new_dicte.items():
                    cnt = +1

                    
                    logic_pred.append(idx)
                return logic_pred


            intial_logic_pred = get_logic_pred(intial_logic)
            ethnicity_logic_pred = get_logic_pred(ethnicity_logic)
            settlement_logic_pred = get_logic_pred(settlement_logic)
            
            finetuning_logic_pred = get_logic_pred(finetuning_logic)
            final_logic_pred = get_logic_pred(final_logic)
            consumption_metric = [col_number,json.dumps(consumption_dict)]
            prediction_metric = [col_number,json.dumps(intial_logic),intial_logic_pred,json.dumps(settlement_logic),settlement_logic_pred,json.dumps(ethnicity_logic),ethnicity_logic_pred,json.dumps(finetuning_logic),finetuning_logic_pred,json.dumps(final_logic),final_logic_pred]





            
            predictions = list(final_logic_pred)[:5]
            top_2_val = [float(final_logic[i]) for i in (predictions)]
            top_2_idx = []
            for val in predictions:
                wer = val.split()
                top_2_idx.append(int(wer[1]))

            #print(tat_val)
            #accuarcy = [val/sum(top_2_val) for val in top_2_val]
            #predictions = ["Code " + str(idx+1) for idx in reversed(top_2_idx)]

            score_relat,score_std = get_percentile(top_2_val,sum_std_mat,top_2_idx,to_check_array)
            return predictions,score_relat,score_std,prediction_metric,consumption_metric
            


        def save_master_log(master_sheet_filepath):
            df = pd.read_excel(master_sheet_filepath)
            df_w = df.fillna(0)
           
            df_w = df_w.iloc[3:,:]
   
            weightage = list(df_w.iloc[:,4].values)

            df = pd.read_excel(master_sheet_filepath)
            df_s = df.fillna(0)
            df_s = df_s.iloc[3:,:]

            
            scores = df_s.iloc[:,5].values
            scores = np.where(scores == 'B',-1,scores)
            scores = np.where(scores == 'A',1,scores)
            #scores = np.prod(scores)
            #weightage.append(scores)
            np.savetxt('AI Internal-Outputs/master_log_weightage.txt', weightage)
            np.savetxt('AI Internal-Outputs/master_log_score.txt',scores)
            
            


        def execute(df,col_number):

            
            sf = read_master_sheet(self.master_sheet_filepath)
            save_master_log(self.master_sheet_filepath)
            standard_matrix,qualifying_dict,sum_std_mat = get_standard_matrix(sf)
            to_check_array,age,ethnicity = get_test_output(df,col_number)
            predictions,score_relat,score_std,prediction_metric,consumption_metric = get_top_5_predictions(to_check_array,age,standard_matrix,qualifying_dict,sum_std_mat,ethnicity,col_number)
  
            
            #print("Age of the user is = ",age)
            #print("TOP 5 PREDICTIONS ARE :")
            #print(predictions)
            #print("With Cumilitave scores of :")
            #print(scores)
            return age,predictions,score_relat,score_std,ethnicity,prediction_metric,consumption_metric


        def execute_single_files():
            print("____________*** Prediction Al ***_____________________")
            print("Please make sure master sheet and test sheet are uploaded")
            print(" ")

            for test_sheet_filepath in self.test_sheet_filepaths:
                self.test_sheet_filepath = test_sheet_filepath

                file1 = open("AI External-Outputs/path_info.txt", "w")

                file1.write("M"+self.master_sheet_filepath)
                file1.write(" \n") 
            
                file1.write("T"+self.test_sheet_filepath)
                file1.write(" \n")
                file1.close() 
            
                test_df = read_data(self.test_sheet_filepath)
                col_name = test_df.columns
                col_name = col_name
                test_df = read_data(self.test_sheet_filepath)
                test_df = df_column_uniquify(test_df)
                temp_df = test_df.iloc[:,3:]
                col_name = temp_df.columns
                code_values = temp_df.iloc[0].values
                prediction_output = []
                accuracy_1 = 0
                accuracy_2 = 0
                cnt = 0
                
    
                # Progress bar widget 
                prediction_metrics = []
                consumption_metrics = []
            
                for idx,col in enumerate(col_name):
                    age,prediction,score_relat,score_std,ethnicity,prediction_metric,consumption_metric= execute(test_df,col)
                    consumption_metrics.append(consumption_metric)
                    prediction_metrics.append(prediction_metric)
                    prediction_output.append([col,code_values[idx], age,ethnicity, prediction,score_relat,score_std])
                    cnt = cnt+1
                    if code_values[idx] in [prediction[0],prediction[1]]:
                    
                        accuracy_2 = accuracy_2+1
                    if code_values[idx] == prediction[0]:

                        accuracy_1 = accuracy_1+1
                
                df = pd.DataFrame(consumption_metrics, columns =['Column Reference Code','Logic Consumption Dictonary'])
                file = open("AI External-Outputs/path_info.txt","r")
                for lines in file.read().splitlines():
                    if lines[0] == "T":
                        test_filepath = lines[1:]
                file.close() 
                
                t_filename = Path(test_filepath).stem

                df.to_csv("AI External-Outputs/Consumption_metric_{}.csv".format(t_filename))
                
                df = pd.DataFrame(prediction_metrics, columns =['Column Reference Code','Intial Score','Intial Prediction','Settlement Logic','Settlement Prediction','Ethnicity Logic','Ethnicity Prediction','Fine Tuning Logic','FineTuning Prediction','Final Logic','Final Prediction'])  
                
                df.to_csv("AI External-Outputs/Prediction_metric_{}.csv".format(t_filename))
                df = pd.DataFrame(prediction_output, columns =['Column Reference Code','Actual Code','Age','Ethnicity','Predcition Codes','Relative Confidence Percentage','Standard Confidence Percentage'])  
                df.to_csv("AI External-Outputs/Prediction_output_{}.csv".format(t_filename))
                #print("Accurate is ",accuracy)
                self.cnt = cnt
            
                self.accuracy_2 = (accuracy_2/cnt)*100
                self.accuracy_1 = (accuracy_1/cnt)*100

        execute_single_files()

    def exit_the_window():
        self.user_root.destroy()





    def display(self):
        def add_user_verify():
            if not os.path.exists('user_pass_database'):
                os.makedirs('user_pass_database')

            

            username_info = username_data_entry.get()
            password_info = password_data_entry.get()
            start_code_info = start_code_entry.get()
            end_code_info = end_code_entry.get()
        
            file = open("user_pass_database/" + username_info + ".txt", "w")
            file.write(username_info + "\n")
            file.write(password_info + "\n")
            file.write(start_code_info + "\n")
            file.write(end_code_info + "\n")

            file.close()
        
            username_data_entry.delete(0, END)
            password_data_entry.delete(0, END)
            start_code_entry.delete(0, END)
            end_code_entry.delete(0, END)


        
            Label(self.user_root, text="Added Successfully", fg="green", font=("calibri", 11)).pack()
            Button(self.user_root, text="Exit", width=10, height=1, command = self.user_root.destroy()).pack()



        def add_user_data():
            global username_data
            global password_data
            global start_code
            global end_code
            global username_data_entry
            global password_data_entry
            global start_code_entry
            global end_code_entry
            username_data = StringVar()
            password_data = StringVar()
            start_code = StringVar()
            end_code = StringVar()



            self.user_root = tkinter.Tk()
            self.user_root.geometry("500x500")

            Label(self.user_root, text="Username * ").pack()
            username_data_entry = Entry(self.user_root, textvariable=username_data)
            username_data_entry.pack()
            Label(self.user_root, text="").pack()
            Label(self.user_root, text="Password * ").pack()
            password_data_entry = Entry(self.user_root, textvariable=password_data)
            password_data_entry.pack()
            Label(self.user_root, text="").pack()
            Label(self.user_root, text="Start Unique Code").pack()
            start_code_entry = Entry(self.user_root, textvariable=start_code)
            start_code_entry.pack()
            Label(self.user_root, text="").pack()
            Label(self.user_root, text="End Unique Code").pack()
            end_code_entry = Entry(self.user_root, textvariable=end_code)
            end_code_entry.pack()
            Label(self.user_root, text="").pack()
            Button(self.user_root, text="Add user data", width=10, height=1, command = add_user_verify).pack()

        def display_prediction():

            
            root = tkinter.Tk()
            root.geometry("1024x1024")

            ico_path = curdir+"\media\my_icon.ico"
            root.iconbitmap(ico_path)
            grid = MagicGrid(root)
            grid.pack(side="top", expand=2, fill="both")

            # open file
            file = open("AI External-Outputs/path_info.txt","r")
            for lines in file.read().splitlines():
                if lines[0] == "T":
                    test_filepath = lines[1:]
            file.close() 
            
            t_filename = Path(test_filepath).stem
            with open(self.current_dir+"/AI External-Outputs/Prediction_output_{}.csv".format(t_filename), newline = "") as file:
                reader = csv.reader(file)
                parsed_rows = 0

                # r and c tell us where to grid the labels
                for row in reader:
                    if parsed_rows == 0:
                        # Display the first row as a header
                        grid.add_header(*row)
                    else:
                        grid.add_row(*row)
                    parsed_rows += 1

                root.mainloop()
        root = Tk() 


        ico_path = curdir+"\media\my_icon.ico"
        root.iconbitmap(ico_path)

        # specify size of window. 
        root.geometry("1024x1024") 

        # Create text widget and specify size. 
        T = Text(root, height = 5, width = 52) 

        # Create label 
        


        l = Label(root, text = "Prediction by AI are saved") 
        l.config(font =("Courier", 14)) 

        # Create button for next text. 
        b1 = Button(root, text = "Display the Predictions", command = display_prediction) 

        # Create an Exit button. 
        b2 = Button(root, text = "Exit", 
                    command = root.destroy) 

        b3 = Button(root, text = "Add User Data", command = add_user_data) 
        
        T.insert(END, "Total Number of user Tested = ")
        T.insert(END, str(self.cnt)+'\n')
        
        T.insert(END, "Accuracy for being in top 2 predictions = ")
        T.insert(END, str(self.accuracy_2)+'\n')
        T.insert(END, "Accuracy for being the top predictions = ")
        T.insert(END, str(self.accuracy_1)+'\n')

        l.pack() 
        T.pack() 
        b1.pack() 
        b2.pack() 
        b3.pack()





        


        # Insert The Fact. 

        

    def start_submit_thread(self,event):
        global submit_thread
        submit_thread = threading.Thread(target=self.get_prediction)
        submit_thread.daemon = True
        self.progressbar.start()
        submit_thread.start()
        
        self.root.after(100, self.check_submit_thread)

    def check_submit_thread(self):
        if submit_thread.is_alive():
            
            self.progressbar["value"] = int(self.progressbar["value"] + 10)
            Label(self.root,text=(str(self.progressbar["value"])+"/"+"100")).grid(row=1, column=0, columnspan=2, ipadx=50)

            self.progressbar.update()
            self.root.after(100, self.check_submit_thread)
        else:
            #print("yes")
            self.progressbar.stop()
            self.display()
    


        
    


# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)

    ico_path = curdir+"\media\my_icon.ico"
    password_not_recog_screen.iconbitmap(ico_path)
    
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)

    ico_path = curdir+"\media\my_icon.ico"
    login_screen.iconbitmap(ico_path)
    
    
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    user_not_found.after(500, delete_user_not_found_screen)
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()

 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window




   
def main_account_screen():
    if not os.path.exists('user_credential_database'):
        os.makedirs('user_credential_database')
    global main_screen
    main_screen = Tk()

    ico_path = curdir+"\media\my_icon.ico"
    main_screen.iconbitmap(ico_path)
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="PREDECTIVE AI", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()

main_account_screen()

