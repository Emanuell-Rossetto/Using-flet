import flet as ft

def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        if e.shift and e.key == "S":           
            page.show_semantics_debugger = not page.show_semantics_debugger          
            page.update()
    page.on_keyboard_event = on_keyboard

    page.add(
    ft.Text("Bem-vindo ao Flet!", size=30, color=ft.Colors.BLUE, )
    
    )

  
ft.run(main)
