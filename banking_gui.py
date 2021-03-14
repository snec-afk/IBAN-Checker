from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv

#Main class
class IBAN_Check:

    def __init__(self, window):
        window.title("IBAN checker")
        mainframe = ttk.Frame(window, padding="3 3 12 12")
        mainframe.grid(column=0, row=0)
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        #Output box
        self.my_stuff = Text(window, width=30,height=12)
        self.my_stuff.grid(column=0,row=3, pady=10)

        #Enter a code for evaluation
        self.iban = StringVar()
        iban_entry = ttk.Entry(mainframe, width=24, textvariable=self.iban)
        iban_entry.grid(column=2, row=1, sticky=(W,E))

        #Executes check_iban function
        ttk.Button(mainframe, text='Check', command=self.check_iban).grid(column=3, row=1, sticky=W)

        #Open text file button
        open_file = ttk.Button(mainframe, text="Open", command=self.openfile)
        open_file.grid(column=3, row=4)

    #Check bank if IBAN is valid and which bank group it belongs to
    def check_iban(self):
        iban_string = self.iban.get() #Get value from widget
        seb_group = '70440'           ##
        swed_group = '73000'          ## Bank branches
        citadele_group = '72900'      ##

        if len(iban_string) == 20:    # Check if the number is at least 20 char long
            correct_value = '\nThe number is correct'
            self.my_stuff.insert(END, correct_value)    #Pass the output into the textbox
            with open('IBAN_valid.csv', mode='a') as iban_file:     #Write to CSV file
                bank_writer = csv.writer(iban_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                bank_writer.writerow([f'{iban_string}' + correct_value])

            if iban_string[4:8] == seb_group[0:4]:      #Check if the code belongs to SEB bank group
                seb_value = '\nSEB bank group;'
                seb_value.rstrip()
                self.my_stuff.insert(END, seb_value)

            elif iban_string[4:8] == swed_group[0:4]:       # Same code as above for 2nd bank
                swed_value = '\nSwedbank group;'
                swed_value.rstrip()
                self.my_stuff.insert(END,swed_value)

            elif iban_string[4:8] == citadele_group[0:4]:       # Same as above for 3rd bank
                citadele_value = '\nCitadele bank group;'
                self.my_stuff.insert(END, citadele_value)

        #If string isn't 20 char long, write to textbox and CSV file
        elif len(iban_string) != 20:
            incorrect_value = '\nThe number is incorrect'
            self.my_stuff.insert(END, incorrect_value)
            with open('IBAN_valid.csv', mode='a') as iban_file:
                bank_writer = csv.writer(iban_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                bank_writer.writerow([f'{iban_string}' + incorrect_value])

    #Open a text file
    def openfile(self):
        seb_group = '70440'  ##
        swed_group = '73000'  ## Bank branches
        citadele_group = '72900'  ##
        text_file = filedialog.askopenfilename(
            title="Open Text file",
            filetypes=(("Text Files", "*.txt"),)
        )
        file_value = open(text_file, 'r')
        for line in file_value.readlines():
            line = line.strip()
            if len(line) == 20:
                correct_value = '\nThe number is correct'
                self.my_stuff.insert(END, correct_value)
                if line[4:9] == seb_group:  # Check if the code belongs to SEB bank group
                    seb_value = '\nSEB bank group;'
                    seb_value.rstrip()
                    self.my_stuff.insert(END, seb_value)
                elif line[4:9] == swed_group:  # Same code as above for 2nd bank
                    swed_value = '\nSwedbank group;'
                    swed_value.rstrip()
                    self.my_stuff.insert(END, swed_value)
                elif line[4:9] == citadele_group:  # Same as above for 3rd bank
                    citadele_value = '\nCitadele bank group;'
                    self.my_stuff.insert(END, citadele_value)
            # If string isn't 20 char long print incorrect
            elif len(line) != 20:
                incorrect_value = '\nThe number is incorrect'
                self.my_stuff.insert(END, incorrect_value)

window = Tk()
window.geometry("300x300")
IBAN_Check(window)
window.mainloop()
