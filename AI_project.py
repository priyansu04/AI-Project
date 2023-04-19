import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("AI project")
root.config(bg="#d1fdfb")


def getText():
    input = searchBox.get(1.0, "end-1c")
    matchingDisease(input)


def infoDisease(search):
    infoDisease = tk.Tk()
    infoDisease.geometry("500x200")
    infoDisease.title("Disease details")
    infoDisease.config(bg="#d1fdfb")
    labeltitle = tk.Label(infoDisease, text="RESULT FOR : " + (search),bg='#d1fdfb')
    labeltitle.pack()
    file = open('D:\Python\\'+search+'.txt', 'r')
    padding1Label = tk.Label(infoDisease,text="",bg='#d1fdfb')
    padding1Label.pack()
    diseaseLabel = tk.Label(infoDisease, text='' , bg='#d1fdfb')
    diseaseLabel.config(text=str(file.read()))
    diseaseLabel.pack()
    infoDisease.mainloop()


def matchingDisease(input):
    disease = ["Influenza","Common cold","Pneumonia","Tuberculosis","Malaria","Dengue fever",
               "Measles","Chickenpox","Polio","Rabies","Meningitis","Encephalitis"]
    
    for i in range(0, len(disease), 1):
        flag1 = False
        if disease[i] in input:
            infoDisease(disease[i])
            break
        else:
            flag1 = True
    if (flag1):
        matchingSystoms(input)

def Didntgetthat():
    infoDisease = tk.Tk()
    infoDisease.geometry("200x100")
    infoDisease.title("Disease details")
    infoDisease.config(bg="#ce847f")
    labeltitle = tk.Label(infoDisease, text="Sorry!!, I Didn't get that !!",bg="#ce847f")
    labeltitle.place(x=30,y=30)
    infoDisease.mainloop()

def matchingSystoms(input):
    listOfSymtoms = [["Influenza", "Fever", "cough", "sore throat", "runny nose", " body aches", "fatigue"],
                     ["Common cold", "Sneezing", "runny nose",
                         "sore throat", "cough", "congestion"],
                     ["Pneumonia", "Cough with phlegm", " fever",
                         "chills", "shortness of breath", "chest pain"],
                     ["Tuberculosis", "Cough that lasts for weeks",
                         "chest pain", "fatigue", "weight loss", "night sweats"],
                     ["Malaria", "Fever, headache, muscle pain,fatigue, nausea, vomiting "],
                     ["Dengue fever", "Fever, severe headache, joint pain, rash, nausea, vomiting"],
                     ["Measles", "High fever", "cough", "runny nose", "red","watery eyes", "rash "],
                     ["Chickenpox","Fever", "itchy rash with blisters","headache", "tiredness"],
                     ["Polio", "Fever", "fatigue"," headache", "stiffness in the neck"," muscle weakness or paralysis"],
                     ["Rabies","Fever", "headache","muscle weakness","tingling or numbness", "anxiety","confusion"],
                     ["Meningitis","Fever", "headache"," neck stiffness","nausea", "vomiting", "sensitivity to light"],
                     ["Encephalitis" ,"Fever", "headache", "confusion","seizures", "weakness or paralysis","sensory disturbances"]]
    for i in range(0, len(listOfSymtoms)):
        for j in range(1, len(listOfSymtoms[i])):
            flag = False
            if (listOfSymtoms[i][j] in input):
                flag = True
        if (flag):
            infoDisease(listOfSymtoms[i][0])
            break
    else:
        Didntgetthat()


label1 = tk.Label(root, text="AI in healthcare", font=("Helvetica", 14),bg="#d1fdfb")
label1.pack(ipadx=10, ipady=10)

searchBox = tk.Text(root, width=40, height=15,bg="#daf9f4")
searchBox.pack(ipadx=20, ipady=0)

searchButton = tk.Button(root, text="Search", command=getText,bg="#daf9f4")
searchButton.place(x=230, y=300)

root.mainloop()
