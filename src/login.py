"""
CONTEXTO PARA O GITHUB COPILOT:
Estou usando Flet versão 0.80.5.
"""

import flet as ft

def main(page: ft.Page):
    background = "#121212"
    loginBackground = "#1E1E1E"
    def on_keyboard(e: ft.KeyboardEvent):
        if e.shift and e.key == "S":           
            page.show_semantics_debugger = not page.show_semantics_debugger          
            page.update()
    page.on_keyboard_event = on_keyboard

    
    textTitulo = ft.Text("🐀 R.A.T.O", size=30, weight=ft.FontWeight.BOLD, margin=ft.Margin(0, 0, 0, 20))
    textLogin = ft.TextField(label="Login", width=200)
    textSenha = ft.TextField(label="Senha", width=200, password=True)

    # btnEntrar = ft.ElevatedButton(text="Entrar", width=200)
    teste=ft.Container(
        
        align=ft.Alignment.CENTER, #Centraliza o container INTERNO
        bgcolor=loginBackground,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, #Centraliza os itens dentro da coluna
            controls=[
            textTitulo,
            textLogin,
            textSenha,
        ])
    )
    
    page.add(
       ft.Container(
           expand=True,
            content= ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    teste
                ],
                spacing=20,
            ),
            bgcolor=background,
            align=ft.Alignment.CENTER, #Centraliza o container CENTRAL
            width=400, #LADOS
            height=600, #CIMA
        )
    )      
ft.run(main)
