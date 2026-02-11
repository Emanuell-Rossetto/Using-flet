import flet as ft

def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        if e.shift and e.key == "S":           
            page.show_semantics_debugger = not page.show_semantics_debugger          
            page.update()
    page.on_keyboard_event = on_keyboard

    page.add(
       ft.Stack(
        expand=True,
        controls=[
            ft.Container(
                width=200,
                height=100,
                bgcolor=ft.Colors.RED,
                content=ft.Text("Topo direita", text_align=ft.TextAlign.CENTER),
                top=20,
                right=30,
            )
        ],
    )
        
    )

  
ft.run(main)
