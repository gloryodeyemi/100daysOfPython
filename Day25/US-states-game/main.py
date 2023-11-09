import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_answer = screen.textinput(title="Guess the state", prompt="Enter a state's name")

screen.exitonclick()

# get x and y coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
