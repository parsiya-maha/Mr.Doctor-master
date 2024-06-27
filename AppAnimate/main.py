import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
app.title("Mr.Doctor")
app.minsize(1000,650)

X = 0
pos = "+"



def click():
    a = True


    global X,pos,l,btn

    if pos=="+":

        if a :
            a = False
            for i,k in l :
                i.pack(**k)


        X+=10

        if X <= 200:
            frame1.configure(width=X)

            app.after(10,click)
        else :
            pos = "-"



    else : 
        X-= 10

        if X >= 0 :
            frame1.configure(width=X)
            app.after(10,click)

        else:
            pos = "+"
            for i,_ in l:
                i.pack_forget()



    



btn = customtkinter.CTkButton(app,text="S\nH\nO\nW",width=30,corner_radius=20,command=click)
btn.pack(side = "left",padx=(10,0),fill="y",pady=10)

frame1 = customtkinter.CTkFrame(app,width=X)
frame1.pack_propagate(False)

l = [
    [customtkinter.CTkLabel(frame1,text="dbfsdf\nassdg\nasvasvd\nagfadg\n"),{"padx":10,"pady":10}],
    [customtkinter.CTkButton(frame1,text="click me"),{"pady":[50,10],"padx":10}]
]


# frame1.pack_propagate(False)
frame1.pack(side="left",fill="y",padx=10,pady=10)


frame2 = customtkinter.CTkFrame(app)
frame2.pack(side="right",padx=(0,10),pady=10,fill="both",expand=1)



app.mainloop()