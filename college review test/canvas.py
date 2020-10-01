from tkinter import* 

#create the root window
root = Tk()

root.title("canvas")

#create the canvas
c = Canvas(root,bg="blue", height= 500, width = 600, cursor="pencil")
c.pack()

#create a line
l = c.create_line(50,50,200,50,200,150, width = 4 ,fill = "white")#(x0,y0,x1,y1,.......,xn,yn)
r=c.create_rectangle(500,200,300,400, width = 2 , fill = "grey",outline="black",activefill="yellow")
r = c.create_arc(500,100,800,300, width=2, start=90, extent=180, outline="black", style="arc")
root.mainloop()
                  
                  
