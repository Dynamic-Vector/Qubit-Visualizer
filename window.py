from tkinter import *
import tkinter as tk
import numpy as np
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
from tkinter import LEFT,END,DISABLED,NORMAL
import warnings

warnings.filterwarnings('ignore')


#Initalize the Quantum circuit
def initialize_circuit():
     """
    Initializes the Quantum Circuit
    """
     global circuit
     circuit=QuantumCircuit(1)

initialize_circuit()
theta=0



#Define Display Function

def display_gate(gate_input): 
    """
    Adds a corresponding gate notation in the display to track the operations.
    If the number of operation reach ten,all gate buttons are disabled.
    """
    #Insert the defined gate
    display.insert(END,gate_input)

    #Check if the number of operations has reached ten,if yes,
    #disable all the gate buttons
    input_gates = display.get()
    num_gates_pressed = len(input_gates)
    list_input_gates= list(input_gates)
    search_word = ["R","D"]
    count_double_valued_gates = [list_input_gates.count(i) for i in search_word]
    num_gates_pressed -= sum(count_double_valued_gates)
    if num_gates_pressed == 10:
        gates=[x,y,z,s,sd,h,t,td]
        for gate in gates:
            gate.config(state=DISABLED)


#Define Del Function

def clear(circuit):
    """
   clears the display!
   Reintializes the Quantum circuit for fresh calculation!
   Checks if the gate buttons are disabled,if so,enables the buttons
   """
   #clear the display
    display.delete(0,END)

    #reset the circuit to initial state |0>
    initialize_circuit()  
   
   #Checks if the buttons are disabled and if so,enables them
    if x['state']== DISABLED:
       gates=[x,y,z,s,sd,h,t,td]
       for gate in gates:
           gate.config(state=NORMAL)

def user_input(circuit,key):
    """Take the user input for rotation for paramaterized 
     Rotation gates Rx,Ry,Rz
      """

    #Initialize adn define the properties of window
    get=tk.Tk()
    get.title("Enter theta")
    get.geometry("320x80")
    get.resizable(0,0)


    val1=tk.Button(get,height=2,width=10,text="PI/4",command=lambda:change_theta(0.25,get,circuit,key))
    val1.grid(row=0,column=0)

    val2=tk.Button(get,height=2,width=10,text="PI/2",command=lambda:change_theta(0.50,get,circuit,key))
    val2.grid(row=0,column=1)

    val3=tk.Button(get,height=2,width=10,text="PI",command=lambda:change_theta(1.0,get,circuit,key))
    val3.grid(row=0,column=2)
   
    val4=tk.Button(get,height=2,width=10,text="2*PI",command=lambda:change_theta(2.0,get,circuit,key))
    val4.grid(row=0,column=3,sticky='w')

    val5=tk.Button(get,height=2,width=10,text="-PI/4",command=lambda:change_theta(-0.25,get,circuit,key))
    val5.grid(row=1,column=0)
    
    val6=tk.Button(get,height=2,width=10,text="-PI/2",command=lambda:change_theta(-0.50,get,circuit,key))
    val6.grid(row=1,column=1)

    val7=tk.Button(get,height=2,width=10,text="-PI",command=lambda:change_theta(-1.0,get,circuit,key))
    val7.grid(row=1,column=2)
 
    val8=tk.Button(get,height=2,width=10,text="-2*PI",command=lambda:change_theta(-2.0,get,circuit,key))
    val8.grid(row=1,column=3,sticky='w')
 

    
    get.mainloop()

def change_theta(num,window,circuit,key):

    global theta
    theta = num* np.pi
    if key=='x':
        circuit.rx(theta,0)
        thera=0 
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else :
        circuit.rz(theta,0)
        theta=0
    window.destroy()            

#Attributes

background='#2c94c8'
buttons='#d9d9d9'
special_buttons='#bc3454'
button_font=('Roboto',18,)
display_font=('Roboto',28)


#Define Window

window = tk.Tk()
window.iconbitmap(default='res/logo.ico')
window.title("Quantum Labs")



window.geometry("816x560")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 560,
    width = 816,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"res/background.png")
background = canvas.create_image(
    260, 279,
    image=background_img)


#Add the display
text_box_bg = tk.PhotoImage("res/TextBox_Bg.png")
display_img = canvas.create_image(650.5, 267.5, image=text_box_bg)
display = tk.Entry(bd=0, bg="#bfc0de",font=display_font, highlightthickness=0)
display.place(x=485, y=125, width=270, height=45)


#Add the buttons

x = Button(
    window,
    text = "X",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,

    relief = "ridge",
    command =lambda:[display_gate('X'),circuit.x(0)])
 
x.place(x = 485, y = 200
    , width = 60, height = 30)

y= Button(
    window,
    text = "Y",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('Y'),circuit.y(0)])
     
y.place(x = 590, y = 200
    , width = 60, height = 30)


z= Button(
    window,
    text = "Z",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('Z'),circuit.z(0)])

z.place(x = 695, y = 200
    , width = 60, height = 30)


s= Button(
    window,
    text = "S",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('S'),circuit.s(0)])

s.place(x = 485, y = 275
    , width = 60, height = 30)


sd= Button(
    window,
    text = "SD",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('SD'),circuit.sdg(0)])

sd.place(x = 590, y = 275
    , width = 60, height = 30)

h= Button(
    window,
    text = "H",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('H'),circuit.h(0)])

h.place(x = 695, y = 275
    , width = 60, height = 30) 

rx= Button(
    window,
    text = "RX",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('RX'),user_input(circuit, 'x')])

rx.place(x = 485, y = 350
    , width = 60, height = 30)




ry= Button(
    window,
    text = "RY",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('RY'),user_input(circuit, 'y')])

ry.place(x = 590, y = 350,
        width = 60, height = 30)






rz= Button(
    window,
    text = "RZ",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('RZ'),user_input(circuit, 'z')])


rz.place(x = 695, y = 350,
        width = 60, height = 30)


         
t= Button(
    window,
    text = "T",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('T'),circuit.t(0)])

t.place(x = 485, y = 425
    , width = 60, height = 30)  

td= Button(
    window,
    text = "TD",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:[display_gate('TD'),circuit.tdg(0)])

td.place(x = 590, y = 425,
     width = 60, height = 30)


clean = Button(
    window,
    text = "DEL",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command=lambda:clear(circuit))

clean.place(x = 695, y = 425
    , width = 60, height = 30)


visualize = Button(
    window,
    text = "VISUALIZE",
    font = button_font,
    bg = buttons,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    command =lambda:visualize_transition(circuit,trace=False,saveas=None,spg=2,fpg=100))

visualize.place(x = 540, y = 490
    , width = 160, height = 40)


window.resizable(False, False)
window.mainloop()
