from nicegui import ui

class Titlescreen:
    def __init__(self):
        self.controller = None
        self.setup()
    def get_controller(self,controller):
        self.controller = controller
    def setup(self):
        with ui.column().classes('w-full h-screen items-center justify-center -mt-32'):
            ui.label('Sudoku TOR').classes('text-8xl')
            ui.button('Easy', on_click=lambda: ui.navigate.to('/easy')).classes('text-xl py-4 w-64')
            ui.button('Medium', on_click=lambda: ui.navigate.to('/medium')).classes('text-xl py-4 w-64')
            ui.button('Hard', on_click=lambda: ui.navigate.to('/hard')).classes('text-xl py-4 w-64')
            ui.button('Solver', on_click=lambda: ui.navigate.to('/solver')).classes('text-xl py-4 w-64')
