from tkinter import *
from tkinter import ttk
from PIL import Image
import requests
import string
import json
import datetime

c0 = "#000000" # black
c1 = "#cc1d4e" # red
c2 = "#feffff" # white
c3 = "#0074eb" # blue
c4 = "#435e5a" # grey
c5 = "#59b356" # green
c6 = "#d9d9d9" # grey

window = Tk()

window.resizable(width=FALSE, height=FALSE)
window.geometry('835x400')
window.title('')
window.configure(bg=c6)

app_name_frame = Frame(window, width = 840, height = 50, bg = c2, relief = "flat")
app_name_frame.grid(row = 0, column = 0, columnspan = 3, sticky = NSEW)

show_frame_infecteds = Frame(window, width = 220, height = 100, bg = c2, relief = "flat")
show_frame_infecteds.grid(row = 1, column = 0, sticky = NW, pady = 5, padx = 5)

show_frame_recovered = Frame(window, width = 220, height = 100, bg = c2, relief ="flat")
show_frame_recovered.grid(row = 1, column = 1, sticky = NW, pady = 5, padx = 5)

show_frame_deads = Frame(window, width = 220, height = 100, bg = c2, relief = "flat")
show_frame_deads.grid(row = 1, column = 2, sticky = NSEW, pady = 5)

select_frame = Frame(window, width = 840, height = 50, bg = c6, relief = "flat")
select_frame.grid(row = 2, column = 0, columnspan = 3, sticky = "n", pady = 10)

img = Image.open("covid.jpeg")
img = img.resize([225, 150,])
img = img.save("covid.png")
image = PhotoImage(file = "covid.png")

app_image = Label(app_name_frame, image = image, text = "Covid-19", width = 350, pady = 20, relief = "flat", anchor = NE, bg = c2)
app_image.grid(row = 0, column = 0, pady = 5)

app_name = Label(app_name_frame, text = "Covid-19", width = 20, height = 1, pady = 20, relief = "flat", anchor = NW, font = ("Helvetica 25 bold"), bg = c2, fg = c0)
app_name.grid(row = 0, column = 1, pady = 5)

response = requests.get("https://covid19.mathdro.id/api")
info = response
info = json.loads(info.text)

infecteds = info["confirmed"]["value"]
recovereds = info["recovered"]["value"]
deads = info["deaths"]["value"]
day = info["lastUpdate"]
day = datetime.datetime.strptime(day, "%Y-%m-%dT%H:%M:%S.000Z")
day = day.strftime("%c")

label_infecteds = Label(show_frame_infecteds, text = "infecteds", width = 20, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 15 bold"), bg = c2, fg = c0)
label_infecteds.grid(row = 0, column = 0, pady = 1, padx = 13)

show_infecteds = Label(show_frame_infecteds, text = infecteds, width = 12, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 25 bold"), bg = c2, fg = c0)
show_infecteds.grid(row = 1, column = 0, pady = 1)

show_info = Label(show_frame_infecteds, text = str(day), width = 25, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 11 bold"), bg = c2, fg = c0)
show_info.grid(row = 2, column = 0, pady = 1)

show_info = Label(show_frame_infecteds, text = "Total cases of Covid-19", width = 33, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 8 bold"), bg = c2, fg = c0)
show_info.grid(row = 3, column = 0, pady = 1, padx = 13)

show_blue = Label(show_frame_infecteds, text = "", width = 19, height = 1, pady = 1, padx = 0, relief = "flat", anchor = NW, font =("Courier 1 bold"), bg = c3, fg = c0)
show_blue.grid(row = 4, column = 0, padx = 0, sticky = NSEW)

label_recovereds = Label(show_frame_recovered, text = "recovereds", width = 20, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 15 bold"), bg = c2, fg = c0)
label_recovereds.grid(row = 0, column = 0, pady = 1, padx = 13)

show_recovereds = Label(show_frame_recovered, text = recovereds, width = 12, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 25 bold"), bg = c2, fg = c0)
show_recovereds.grid(row = 1, column = 0, pady = 1)

show_info = Label(show_frame_recovered, text = str(day), width = 25, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 11 bold"), bg = c2, fg = c0)
show_info.grid(row = 2, column = 0, pady = 1)

show_info = Label(show_frame_recovered, text = "Total cases recovereds of Covid-19", width = 34, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 8 bold"), bg = c2, fg = c0)
show_info.grid(row = 3, column = 0, pady = 1, padx = 13)

show_green = Label(show_frame_recovered, text = "", width = 19, height = 1, pady = 1, padx = 0, relief = "flat", anchor = NW, font = ("Courier 1 bold"), bg = c5, fg = c0)
show_green.grid(row = 4, column = 0, pady = 0, padx = 0, sticky = NSEW)

label_deads = Label(show_frame_deads, text = "Deads", width = 20, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 15 bold"), bg = c2, fg = c0)
label_deads.grid(row = 0, column = 0, pady = 1, padx = 13)

show_deads = Label(show_frame_deads, text = deads, width = 12, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 25 bold"), bg = c2, fg = c0)
show_deads.grid(row = 1, column = 0, pady = 1)

show_info = Label(show_frame_deads, text = str(day), width = 25, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 11 bold"), bg = c2, fg = c0)
show_info.grid(row = 2, column = 0, pady = 1)

show_info = Label(show_frame_deads, text = "Total cases of Dies for Covid-19", width = 33, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 8 bold"), bg = c2, fg = c0)
show_info.grid(row = 3, column = 0, pady = 1, padx = 13)

show_red = Label(show_frame_deads, text = "", width = 19, height = 1, pady = 1, padx = 0, relief = "flat", anchor = NW, font = ("Courier 1 bold"), bg = c1, fg = c0)
show_red.grid(row = 4, column = 0, pady = 0, padx = 0, sticky = NSEW)

label_country = Label(select_frame, text = "Select Country", width = 20, height = 1, pady = 7, padx = 0, relief = "flat", anchor = NW, font = ("Courier 12 bold"), bg = c6, fg = c0)
label_country.grid(row = 0, column = 0, pady = 1, padx = 13)

countries = ["Global","Brazil", "USA", "France", "Spain", "Portugal", "India"]

combo = ttk.Combobox(select_frame, width = 15, font = ("Ivy 8 bold"))
combo["values"] = (countries)
combo.grid(row = 0, column = 1, padx = 0, pady = 13)

def selected(eventObject):

    if combo.get() == "Global":
        response = requests.get("https://covid19.mathdro.id/api")
        info = response
        info = json.loads(info.text)

        infecteds = info["confirmed"]["value"]
        recovereds = info["recovered"]["value"]
        deads = info["deaths"]["value"]

        show_infecteds.configure(text = infecteds)
        show_recovereds.configure(text = recovereds)
        show_deads.configure(text = deads) 

    else:

        sel_country = combo.get()
        response = requests.get("https://covid19.mathdro.id/api/countries/{}".format(sel_country))
        info = response
        info = json.loads(info.text)

        infecteds = info["confirmed"]["value"]
        recovereds = info["recovered"]["value"]
        deads = info["deaths"]["value"]
        day = info["lastUpdate"]
        day = datetime.datetime.strptime(day, "%Y-%m-%dT%H:%M:%S.000Z")
        day = day.strftime("%c")

        show_infecteds.configure(text = infecteds)
        show_recovereds.configure(text = recovereds)
        show_deads.configure(text = deads)

    print(infecteds, recovereds, day)

combo.bind("<<ComboboxSelected>>", selected)


window.mainloop()