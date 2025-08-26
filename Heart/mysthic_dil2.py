import math
import turtle

#  SETUP
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("A Heart in Motion")
screen.tracer(0)

heart_pen = turtle.Turtle()
heart_pen.color("red")
heart_pen.pensize(3)
heart_pen.hideturtle()

text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()


#  HEART FUNCTIONS
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

def draw_heart(scale=20, color="red", fill=True):
    """Draw a scaled heart with optional fill."""
    heart_pen.color(color)
    heart_pen.penup()
    if fill:
        heart_pen.begin_fill()
    for i in range(361):
        t = math.radians(i)
        x = hearta(t) * scale
        y = heartb(t) * scale
        if i == 0:
            heart_pen.goto(x, y)
            heart_pen.pendown()
        else:
            heart_pen.goto(x, y)
    if fill:
        heart_pen.end_fill()
    heart_pen.penup()

#  ANIMATION STATE
pulse_angle = 0
messages = [
    "🌌 I BUILT WORLDS AROUND YOU… ONLY TO WATCH THEM COLLAPSE 💔",
    "💓 EVERY BEAT REMEMBERS YOU ~ 🕰️",
    "🌙 BETWEEN REALITY AND MEMORY, YOU EXIST 🌫️",
    "📖 A STORY NO_ONE UNDERSTOOD 🔥"
]
colors = ["#ff1744", "#f10909", "red", "#ff4081"]  # optional: each line can have its own color


#  TEXT FUNCTIONS
def typewriter_text(i=0, j=0, display_text=""):
    """Draw typewriter-style text, one char at a time."""
    if i >= len(messages):
        glow_text()
        return

    message = messages[i]
    if j < len(message):
        display_text += message[j]
        text_pen.clear()
        for k in range(i):
            text_pen.goto(0, -250 - k*40)
            text_pen.color(colors[k % len(colors)])
            text_pen.write(messages[k], align="center", font=("Arial", 16, "bold"))
        text_pen.goto(0, -250 - i*40)
        text_pen.color(colors[i % len(colors)])
        text_pen.write(display_text, align="center", font=("Arial", 16, "bold"))
        screen.ontimer(lambda: typewriter_text(i, j+1, display_text), 80)
    else:
        screen.ontimer(lambda: typewriter_text(i+1, 0, ""), 500)

def glow_text(size=14, growing=True):
    """Glowing text animation loop."""
    text_pen.clear()
    for i, message in enumerate(messages):
        text_pen.goto(0, -250 - i*40)
        text_pen.color(colors[i % len(colors)])
        text_pen.write(message, align="center", font=("Arial", size, "bold"))
    next_size = size + 1 if growing else size - 1
    if next_size > 22: growing = False
    if next_size < 14: growing = True
    screen.ontimer(lambda: glow_text(next_size, growing), 100)


#  MAIN HEARTBEAT LOOP (NO THREADS)
def animate():
    global pulse_angle
    heart_pen.clear()
    scale = 20 + 2 * math.sin(pulse_angle)
    intensity = int(180 + 70 * math.sin(pulse_angle))
    color = f"#{intensity:02x}2020"
    draw_heart(scale, color, fill=True)
    pulse_angle += 0.15
    screen.update()
    screen.ontimer(animate, 30)


#  OUTLINE ANIMATION
def draw_outline_animation(i=0):
    if i > 360:
        # After outline done, fill heart and start animations
        draw_heart(scale=20, color="red", fill=True)
        animate()
        typewriter_text()
        return

    t = math.radians(i)
    x = hearta(t) * 20
    y = heartb(t) * 20
    if i == 0:
        heart_pen.penup()
        heart_pen.goto(x, y)
        heart_pen.pendown()
    else:
        heart_pen.goto(x, y)
    screen.update()
    screen.ontimer(lambda: draw_outline_animation(i+1), 8)  # speed of drawing

# Start the heart outline animation
draw_outline_animation()
turtle.done()