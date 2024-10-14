import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("sky blue")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    t.color("white")

    i = 3
    while i > 0:
        koch_curve(t, order, size)
        t.right(120)
        i -= 1

    turtle.done()

def main():
    try:
        turtle_deep = int(input("Вкажіть рівень рекурсії>>> "))
        draw_koch_curve(turtle_deep)
    except ValueError:
        print("Потрібно ввести ціле число, спробуйте знову.")

if __name__ == '__main__':
    main()