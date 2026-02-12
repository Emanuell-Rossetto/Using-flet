"""
CONTEXTO PARA O GITHUB COPILOT:
Estou usando Flet versão 0.80.5.
"""

import flet as ft

def main(page: ft.Page):

    def on_keyboard(e: ft.KeyboardEvent):
        if e.shift and e.key == "S":           
            page.show_semantics_debugger = not page.show_semantics_debugger          
            page.update()
    page.on_keyboard_event = on_keyboard

    
    textTitulo = ft.Text("Login", size=30, weight=ft.FontWeight.BOLD, align=ft.Alignment.CENTER)
    textLogin = ft.TextField(label="Login", width=200)
    textSenha = ft.TextField(label="Senha", width=200, password=True)

    # btnEntrar = ft.ElevatedButton(text="Entrar", width=200)
    teste=ft.Container(
        bgcolor=ft.Colors.BLUE,
        content=ft.Column(controls=[
            textLogin,
            textSenha,
            

        ])
    )
    
    page.add(
       ft.Container(
           expand=True,
            content= ft.Column(
                controls=[
                    textTitulo,
                    teste
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            bgcolor=ft.Colors.WHITE,
            align=ft.Alignment.CENTER,
            width=400, #LADOS
            height=600, #CIMA
        )
    )      
ft.run(main)
