import customtkinter

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
app.title("Mr.Doctor")
app.minsize(1000,650)



from CTkAnimation import AutoTextWriter,Panel



frame = customtkinter.CTkFrame(app,width=0)
frame.pack_propagate(False)




c = Panel.Panel(frame,300,10,10)

a = customtkinter.CTkFrame(frame)

c.add_widget(customtkinter.CTkButton(frame,text="",width=50,height=50,corner_radius=25),{"padx":20,"pady":20})
c.add_widget(a,{"padx":10,"pady":10,"fill":"both","expand":1})
c.add_widget(customtkinter.CTkLabel(a,text="hello"))


btn = customtkinter.CTkButton(app,text=".",command=c.run)




btn.pack(fill="y",side="left",padx=10,pady=10)
frame.pack(fill="y",padx=10,pady=10,side="left")



f2 = customtkinter.CTkFrame(app)
f2.pack(fill="both",expand=1,padx=(0,10),pady = 10,side="right")

l = customtkinter.CTkLabel(f2,font=("calibri",20,"bold"),text="")
l.pack(pady=350)

AutoTextWriter.MultiNamesAnimate(l,["BrainTumors","LungCancer","KidneyStone"]).run()


app.mainloop()