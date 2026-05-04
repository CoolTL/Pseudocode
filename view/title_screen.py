from nicegui import ui

class title_screen:
    def __init__(self):
        self.controller = None
    def get_controller(self,controller):
        self.controller = controller
    def difficulty_buttons(self):
        ui.button('Easy', on_click=lambda: ui.notify('I have been clicked'))
        ui.button('Normal',on_click=lambda: ui.notify('I have been clicked'))
        ui.button('Hard',on_click=lambda: ui.notify('I have been clicked'))
        ui.button('Variants',on_click=lambda: ui.notify('I have been clicked'))
title_screen()
ui.run()   