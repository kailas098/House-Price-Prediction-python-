from tkinter import *
import HousePricePredictorApp as hpp

root =Tk()

root.title("Residential Property Price prediction System")

result=""

# frame within root


frame = Frame(root)
frame.pack()

# property-detail frame within frame


data_frame = LabelFrame(frame, text = "Property details")
data_frame.grid(row = 0, column = 0,padx=20, pady=20)

def button_command():
    global result
    result = str(hpp.HousePricePrediction(float(age_entry.get()),float(no_of_B_rooms_entry.get()),float(no_of_B_rooms_entry.get()),float(population_entry.get())))
    result = str(hpp.HousePricePrediction(float(age_entry.get()),float(no_of_B_rooms_entry.get()),float(no_of_B_rooms_entry.get()),float(population_entry.get())))
    output.config(text=result)
    hpp.plot_graph(float(age_entry.get()),float(no_of_B_rooms_entry.get()),float(no_of_B_rooms_entry.get()),float(population_entry.get()),float(current_year_entry.get()))
    
    
    return None

def clear_command():
    age_entry.delete(0,END)
    no_of_rooms_entry.delete(0,END)
    no_of_B_rooms_entry.delete(0,END)
    population_entry.delete(0,END)
    current_year_entry.delete(0,END)

    return None

# Labels in property detail frame

age = Label(data_frame, text="Building age")
# Labels in property detail frame

age = Label(data_frame, text="Building age")
age.grid(row=0,column=0)

no_of_rooms = Label(data_frame, text="No. of rooms")
no_of_rooms.grid(row=1,column=0)

no_of_B_rooms = Label(data_frame,text="No. of Bedrooms")
no_of_B_rooms.grid(row=2,column=0)

population = Label(data_frame,text="Area Population")
population.grid(row=3,column=0)

current_year = Label(data_frame,text="Current year")
current_year.grid(row=4,column=0)

# Entry in property detail frame

# Entry in property detail frame

age_entry = Entry(data_frame, width = 20)
age_entry.grid(row=0,column=1)

no_of_rooms_entry = Entry(data_frame, width = 20)
no_of_rooms_entry.grid(row=1,column=1)

no_of_B_rooms_entry = Entry(data_frame, width = 20)
no_of_B_rooms_entry.grid(row=2,column=1)

population_entry = Entry(data_frame, width = 20)
population_entry.grid(row=3,column=1)

current_year_entry = Entry(data_frame, width = 20)
current_year_entry.grid(row=4,column=1)

#Buttons in property-details frame
#Buttons in property-details frame

Button(data_frame, text="enter",width=16 , command=button_command).grid(row=5,column=0)
Button(data_frame, text="clear",width=16 , command=clear_command).grid(row=5,column=1)

#Output area
output_text = Label(data_frame, text="Estimated price:",height=2,bg="#FFFEE4",width=20)
#Output area
output_text = Label(data_frame, text="Estimated price($):",height=2,bg="#FFFEE4",width=20)
output_text.grid(row=6, column=0,pady=10)

output = Label(data_frame,text="",bg="#FFFEE4",width=20,height=2)
output.grid(row=6,column=1)

root.mainloop()