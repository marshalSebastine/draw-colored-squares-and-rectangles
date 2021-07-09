from canvas import Canvas
from square_n_rectangle import Square,Rectangle

#Asking User canvas width and height
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])
m=1
while m==1:
    shape_typ=input("what do you like to draw ? Enter to quit")
    if shape_typ.lower() == 'rectangle':
         rec_x=int(input("Enter x of your rectangle:  "))
         rec_y=int(input("Enter y of your rectangle:  "))
         rec_width=int(input("Enter the width of your rectangle:"))
         rec_height=int(input("Enter the height of your rectangle:"))
         red = int(input("Enter the intensity of red in scale 0-255:"))
         green = int(input("Enter the intensity of green in scale 0-255:"))
         blue = int(input("Enter the intensity of blue in scale 0-255:"))

         ## creating rectangle
         r1=Rectangle(x=rec_x,y=rec_y,height=rec_height,width=rec_width,color=(red,green,blue))
         r1.draw(canvas)
     ##Asking user if he/she wants square
    if shape_typ.lower() == 'square':
         sqr_x=int(input("Enter the x of square"))
         sqr_y=int(input("Enter the y of square"))
         sqr_side=int(input("Enter the side of your square:"))
         red = int(input("Enter the intensity of red in scale 0-255:"))
         green = int(input("Enter the intensity of green in scale 0-255:"))
         blue = int(input("Enter the intensity of blue in scale 0-255:"))
         ##creating square
         s1=Square(x=sqr_x,y=sqr_y,side=sqr_side,color=(red,green,blue))
         s1.draw(canvas)
    if shape_typ == 'quit':
        break
canvas.make('canvas.png')
