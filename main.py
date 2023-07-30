# To-Do-List with sqlite

# libraries
import flet
from flet import *
from datetime import datetime
import sqlite3


# Form class for data collection
class FormContainer(UserControl):
    
    def __init__(self, func):
        self.func = func
        super().__init__()
    
    def build(self):
        return Container(
            width=280, height=80, bgcolor="bluegrey500", border_radius=40, 
            margin=margin.only(left=-20, right=-20), animate=animation.Animation(200, "decelerator"), # type: ignore
            animate_opacity=200, padding=padding.only(top=45, bottom=45), 
            opacity=0, # change to 1 only when form is opened
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=45, width=255, filled=True, bgcolor="transparent", text_size=13,
                        hint_text="Description...", hint_style=TextStyle(size=11, color='black')
                    ),
                    IconButton(
                        content=Text("Add Task"), width=180, height=44,
                        on_click=self.func, 
                        style=ButtonStyle(
                            bgcolor={"": "black"}, shape={"": RoundedRectangleBorder(radius=8)},
                        )
                    )
                ]
            )
        )

# CRUD Clases
class CreateTask(UserControl):
    
    def __init__(self, task:str, date:str):
        self.task = task
        self.date = date
        super().__init__()
    
    def TaskDeleteEdit(self, name, color):
        return IconButton(
            icon=name, width=30, height=18, icon_color=color, opacity=0, animate_opacity=200,
            on_click=None
        )
    
    def build(self):
        return Container(
            width=280, height=60, border=border.all(0.85, "white45"),
            border_radius=8, on_hover=None, #change later
            clip_behavior=ClipBehavior.HARD_EDGE, padding=10, 
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        spacing=1, alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value=self.task, size=10),
                            Text(value=self.date, size=9, color="white54")
                        ]
                    ),
                    # Edit & Delete Icons
                    Row(
                        spacing=0, alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.TaskDeleteEdit(icons.DELETE_ROUNDED, "red500"),
                            self.TaskDeleteEdit(icons.EDIT_ROUNDED, "white70"),
                        ]
                    )
                ]
            )
        )

def main(page: Page):  
    page.horizontal_alignment = "center" # type: ignore
    page.vertical_alignment = "center" # type: ignore
    
    # Add new created task to screen
    def AddTaskToScreen(e):
        pass

    # to hide and show form container
    def CreateToDoTask(e):
        # when ADD icon button is clicked
        if form.height != 200:
            form.height = 200
            form.opacity = 1
            form.update()
        else:
            form.height = 80
            form.opacity = 0
            form.update()

    # Main column
    _main_column_ = Column(
        scroll="hidden", expand=True, alignment=MainAxisAlignment.START, # type: ignore
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # Title
                    Text("To-Do Items", size=18, weight="bold"), # type: ignore
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED, icon_size=18, on_click=lambda e: CreateToDoTask(e),
                        visible=True,
                    ),
                    IconButton(
                        icons.CLOSE_ROUNDED, icon_size=18, on_click=lambda e: CreateToDoTask(e),
                        visible=False,
                    ),
                ]
            ),
            Divider(height=8, color="white24")
        ]
    )

    # background and main container
    # general mobile UI
    page.add(
        # background container
        Container(
            width=1500, height=800, margin=-10, bgcolor="orange100", alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER, vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    # Main container
                    Container(
                        width=280, height=600, bgcolor="#0f0f0f", border_radius=40,
                        border=border.all(0.5, "white"), padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE, # clips contents to container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER, expand=True,
                            controls=[
                                # main column
                                _main_column_,
                                # Form class
                                FormContainer(lambda e: AddTaskToScreen(e)),
                            ]
                        )
                    )
                ]
            )
        )
    )

    page.update()
    # we can set the long element index (path) of the form container as variable so that we can 
    # call it easily and quickly whenever needed.     
    form = page.controls[0].content.controls[0].content.controls[1].controls[0] # type: ignore


if __name__ == "__main__":
    flet.app(target=main)