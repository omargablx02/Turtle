
# from turtle import Turtle, Screen

# turtle_obj = Turtle()
# screen_obj = Screen()

# ? نستخدم ال shape لتغير شكل المؤشر بداخل الشاشه
# turtle_obj.shape("turtle")

# ? لتغير لون الخلفيه bgcolor
# screen_obj.bgcolor("black")

# ? لتغير لون المؤشر
# turtle_obj.color("blue")

# for o in range(4):
#     turtle_obj.color("blue")
#     turtle_obj.forward(100)  # ? لتحريك المؤشر بالشكل الصحيح
#     # turtle_obj.backward(150) # ? لتحريك المؤشر بشكل عكسي
#     turtle_obj.right(90)  # ? لتغير اتجاه المؤشر اتجاه اليمن
#     # turtle_obj.left(90) # ? لتغير اتجاه المؤشر اتجاه الشمال
#     # turtle_obj.speed('slow') # ? للتحكم في السرعه

# for o in range(4):
#     turtle_obj.color("red")
#     turtle_obj.backward(100)
#     turtle_obj.left(90)

# for o in range(4):
#     turtle_obj.color("green")
#     turtle_obj.forward(100)
#     turtle_obj.left(90)

# for o in range(4):
#     turtle_obj.color("gray")
#     turtle_obj.backward(100)
#     turtle_obj.right(90)

# # ? نستخدم exitonclick لكي يمكننا فتح الشاشه المستخدمه وعند الضغط عليها يتم قفلها
# screen_obj.exitonclick()
# >-----------------------------------------------------------------------------------------------------------------
# import turtle as turtle_object
# import random as random_object

# color_list = ['dark blue', 'dark green', 'gold', 'deep pink',
#               'indigo', 'yellow', 'chocolate', 'firebrick', 'dark slate gray', 'gray']

# Screen = turtle_object.Screen()
# Turtle = turtle_object.Turtle()
# # Turtle.shape("turtle")

# for i in range(1, 11):
#     Turtle.circle(40)
#     Screen.bgcolor(random_object.choice(color_list))
#     # Turtle.color(random_object.choice(color_list))

# # @@ نستخدم stamp لترك شكل المؤشر في اخر اتجاه له
#     # Turtle.stamp()
#     Turtle.forward(200)

# # ? لعمل نقطه عند مكان النهايه الذي سوف يقف به المؤشر نستخدم dot
# #!   (اللون      , حجم النقطه)
#     Turtle.dot(10, random_object.choice(color_list))
#     Turtle.right(200)
#     print(f"Color of round {i} is : {Screen.bgcolor()}")

# Screen.exitonclick()
# >-----------------------------------------------------------------------------------------------------------------
# from turtle import Turtle, Screen
# import random as random_object

# Turtle_object = Turtle()
# Screen_object = Screen()

# count = 1

# color_list = ['dark blue', 'dark green', 'gold', 'deep pink',
#               'indigo', 'yellow', 'chocolate', 'firebrick',
#                'dark slate gray', 'gray', '#2c9f45', '#00a4e4'
#               , '#ffc845', '#009f4d', '#b4a996', '#537b35', '#6a67ce'
#               , '#00b2a9', '#b3dcff']

# # P# تستخدم لتغير مكان بدايه المؤشر
# Turtle_object.goto(-50, 180)

# def draw_shapes(shape_sides):
#     degree = 360 / shape_sides

#     for q in range(shape_sides):
#         Turtle_object.forward(100)
#         Turtle_object.right(degree)

# for num in range(3, 15):

#     Screen_object.bgcolor('black')
#     Turtle_object.color(random_object.choice(color_list))
#     print(f"At Round {count} Num of Shape sides : {num}")
#     count += 1
#     draw_shapes(num)
# Screen_object.exitonclick()
# >-----------------------------------------------------------------------------------------------------------------
# from turtle import Turtle, Screen

# Screen_object = Screen()
# Turtle_object = Turtle()

# def go_forward():
#     Turtle_object.forward(10)

# def go_backward():
#     Turtle_object.backward(10)

# def turn_left():
#     # تستخدم لكي يتم تغير المؤشر بتجاه الشمال
#     new_heading = Turtle_object.heading() + 10
#     Turtle_object.setheading(new_heading)

# def turn_right():
#     # تستخدم لكي يتم تغير المؤشر بتجاه اليمين
#     new_heading = Turtle_object.heading() - 10
#     Turtle_object.setheading(new_heading)

# def clean_screen():
#     # ? لتنظيف الشاشه
#     Turtle_object.clear()

# # ? لمسح الخط الذي يكون خلف المؤشر من فوق
#     Turtle_object.penup()

# # ? لاسترجاع المؤشر الي المكان 0 علي الشاشه
#     Turtle_object.home()

# # ? لمسح الخط الذي يكون خلف المؤشر من تحت
#     Turtle_object.pendown()

# def clean_place():
#     Turtle_object.clear()
#     Turtle_object.penup()
#     Turtle_object.pendown()

# # ? تستخدم للانتظار منك كتابه شي معين ولكي تشتغل نستخدم بعدها ال onkey
# Screen_object.listen()

# Screen_object.onkey(go_forward, 'w')
# Screen_object.onkey(go_backward, 's')
# Screen_object.onkey(turn_left, 'a')
# Screen_object.onkey(turn_right, 'd')
# Screen_object.onkey(clean_place, 'p')
# Screen_object.onkey(clean_screen, 'c')

# Screen_object.exitonclick()
# >-----------------------------------------------------------------------------------------------------------------
# from turtle import Turtle, Screen

# Turtle_object = Turtle()
# Screen_object = Screen()

# Screen_object.bgcolor("black")
# Turtle_object.color("green")

# Turtle_object.forward(150)
# Turtle_object.left(45)
# Turtle_object.forward(200)
# # ? لمعرفه مكان ال المؤشر (x , y) >> (0.00,0.00) نستخدم pos
# start_position = Turtle_object.pos()
# print(start_position)

# # ? لمعرفه مكان المؤشر ال x فقط
# x_coor = Turtle_object.xcor()
# # ? لمعرفه مكان المؤشر ال y فقط
# y_coor = Turtle_object.ycor()

# print(x_coor)
# print(y_coor)

# Screen_object.exitonclick()
# >-----------------------------------------------------------------------------------------------------------------
from turtle import Turtle, Screen
import random

Screen_object = Screen()

bg_color_list = ['#cf8d2e', '#371777', '#52325d', '#005670', '#48a9c5', '#222',
                 '#6a67ce', '#2a5934', '#f67828', '#84754e', '#566127', '#d4c99e', '#464646', '#6b0f24',
                 '#005be2', '#212a3e', '#ccc900', '#3949ab', '#2f6f7e', '#0b2d27', '#394956']

color_list = ['red', 'orange', 'yellow', 'green',
              'blue', 'purple', 'brown', 'gray', 'silver', 'lime']

Screen_object.bgcolor(random.choice(bg_color_list))

x_positions = [300, 230, 160, 90, 20, -50, -120, -190, -260, -330]

turtle_list = []

flag = 0

# ^^ لتحديد عرض وطول الشاشه
Screen_object.setup(width=800, height=500)

# B~ لوضع input علي الشاشه حين بداء البرنامج
winner_color = Screen_object.textinput(
    title="Choose Color", prompt="ENter Winner Color")
if winner_color in color_list:
    
    print(f"You Choose : ( {winner_color} ) Color ")

    for turtle_index in range(10):

        new_turtle = Turtle(shape="turtle")
        new_turtle.left(90)
        new_turtle.color(color_list[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=x_positions[turtle_index], y=-230)
        turtle_list.append(new_turtle)

    if winner_color:
        flag = 1

        while flag:
            for turtle in turtle_list:
                if turtle.ycor() > 230:
                    flag = 0
                    winning_color = turtle.pencolor()

                    if winning_color == winner_color:
                        print(
                            f"You've Win!! , the {winning_color} turtle is the winner")
                    else:
                        print(f"You've Lost!! , the {winning_color} is the Winner")

                random_dis = random.randint(0, 10)
                turtle.forward(random_dis)

    Screen_object.exitonclick()
else:
    print(f"False .. Choose Any Color In {color_list} And Try Again")