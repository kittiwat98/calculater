import tkinter as tk

calculation = ""    #string

def add_num_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)  #index,cha

def square():
    global calculation
    try:
        calculation = str(eval(f"{calculation}**2"))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)   #index,cha
    except:
        clear()
        text_result.insert(1.0, "Error")   #index,cha

def sqrt():
    global calculation
    try:
        calculation = str(eval(f"{calculation}**0.5"))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)   #คำสั่งเพิ่มข้อมูลลงใน List สามารถกำหนดลำดับได้
    except:
        clear()
        text_result.insert(1.0, "Error")   #index,cha


def evaluate_calculation():    
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)   #index,cha
    except:
        clear()
        text_result.insert(1.0, "Error")   #index,cha

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")   


root = tk.Tk()
root.geometry("425x450+500+200")
root.configure(background="pink")
root.resizable(False,False)

text_result = tk.Text(root, height=2, width=16, font=("Arial",24)) #หน้าจิอสดงตัวเลข
text_result.grid(columnspan=5)


def num_create(): #สร้างปุ่มตัวเลข 0-9
    btn_1 = tk.Button(root, text="1", command=lambda:add_num_calculation(1), width=5, font=("Arial",24),bg="#BEBEBE")
    btn_1.grid(row = 3,column=1)
    btn_2 = tk.Button(root, text="2", command=lambda:add_num_calculation(2), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_2.grid(row = 3,column=2)
    btn_3 = tk.Button(root, text="3", command=lambda:add_num_calculation(3), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_3.grid(row = 3,column=3)
    btn_4 = tk.Button(root, text="4", command=lambda:add_num_calculation(4), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_4.grid(row = 4,column=1)
    btn_5 = tk.Button(root, text="5", command=lambda:add_num_calculation(5), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_5.grid(row = 4,column=2)
    btn_6 = tk.Button(root, text="6", command=lambda:add_num_calculation(6), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_6.grid(row = 4,column=3)
    btn_7 = tk.Button(root, text="7", command=lambda:add_num_calculation(7), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_7.grid(row = 5,column=1)
    btn_8 = tk.Button(root, text="8", command=lambda:add_num_calculation(8), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_8.grid(row = 5,column=2)
    btn_9 = tk.Button(root, text="9", command=lambda:add_num_calculation(9), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_9.grid(row = 5,column=3)
    btn_0 = tk.Button(root, text="0", command=lambda:add_num_calculation(0), width=5, font=("Arial",24),bg="#BEBEBE" )
    btn_0.grid(row = 6,column=2)

def tool_crate():#สร้างปุ่มเครื่องมือต่างในเครื่องคิดเลข
    btn_plus = tk.Button(root, text="+", command=lambda:add_num_calculation("+"), width=5, font=("Arial",24) )
    btn_plus.grid(row = 4,column=4)
    btn_minus = tk.Button(root, text="-", command=lambda:add_num_calculation("-"), width=5, font=("Arial",24) )
    btn_minus.grid(row = 3,column=4)
    btn_mul = tk.Button(root, text="x", command=lambda:add_num_calculation("*"), width=5, font=("Arial",24) )
    btn_mul.grid(row = 5,column=4)
    btn_div = tk.Button(root, text="/", command=lambda:add_num_calculation("/"), width=5, font=("Arial",24) )
    btn_div.grid(row = 1,column=4)
    btn_dot =tk.Button(root, text=".", command=lambda:add_num_calculation("."), width=5 ,font=("Arial",24), )
    btn_dot.grid(row = 6,column=1)

    btn_open_bracket = tk.Button(root, text="(", command=lambda:add_num_calculation("("), width=5, font=("Arial",24) )
    btn_open_bracket.grid(row = 6,column=3)
    btn_close_bracket = tk.Button(root, text=")", command=lambda:add_num_calculation(")"), width=5, font=("Arial",24) )
    btn_close_bracket.grid(row = 6,column=4)

    btn_clear = tk.Button(root, text="c", command= clear, width=5 ,font=("Arial",24),bg="#FFDAB9" )
    btn_clear.grid(row = 1,column=1 )
    btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial",24),bg="#FFDAB9" )
    btn_equals.grid(row = 7,column=3, columnspan = 2,sticky="e")

    btn_square = tk.Button(root, text="x\u00b2", command=square, width=5, font=("Arial",24),bg="#FF9933" )
    btn_square.grid(row = 1,column=2)
    btn_sqrt = tk.Button(root, text="\u221ax", command=sqrt, width=5, font=("Arial",24),bg="#FF9933" )
    btn_sqrt.grid(row = 1,column=3)

num_create()
tool_crate()
root.mainloop()