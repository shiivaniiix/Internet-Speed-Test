from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)

sp = Tk()
sp.title("Internet Speed Test")  # Window Title
sp.geometry("500x650") # Dimensiom
sp.config(bg = "Blue") # Here we have given background color

#bg = background , fg = Font

lab = Label(sp, text="Internet Speed Test", font= ("Time New Romen", 30, "bold"), bg="Blue", fg="White")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download speed", font= ("Time New Romen", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font= ("Time New Romen", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload speed", font= ("Time New Romen", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font= ("Time New Romen", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)


button = Button(sp, text = "Check speed", font= ("Time New Romen", 30, "bold"), relief=RAISED, bg="Red", command=speedcheck)
button.place(x=60, y=460, height=50, width=380)


sp.mainloop()
