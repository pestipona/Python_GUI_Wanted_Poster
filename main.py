# import widgets from quizero library
from guizero import App, Text, Picture

# create a container widget
app = App(title="Wanted!")

# change background color
app.bg = "#F8C363"

# add a text widget
Hazel = Text(app, "WANTED!!!")
Hazel.text_size = 50
Hazel.font = "Times New Roman"

# add a picture widget
bunny = Picture(app, image="./images/Hazel.jpg")
bunny.resize(400, 350)

# display the gui app
app.display()