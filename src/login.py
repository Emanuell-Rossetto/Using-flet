"""
CONTEXTO PARA O GITHUB COPILOT:
Estou usando Flet versão 0.80.5.
"""

import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#121212"
    background = "#121212"
    loginBackground = "#1E1E1E"
    def on_keyboard(e: ft.KeyboardEvent):
        if e.shift and e.key == "S":           
            page.show_semantics_debugger = not page.show_semantics_debugger          
            page.update()
    page.on_keyboard_event = on_keyboard

    
    textTitulo = ft.Text("🐀 R.A.T.O", size=30, weight=ft.FontWeight.BOLD, margin=ft.Margin(0, 80, 0, 20))
    textLogin = ft.TextField(label="Login", width=200)
    textSenha = ft.TextField(label="Senha", width=200, password=True)
    btnLogin = ft.Button(content=ft.Text("Entrar"), width=200, color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE, on_click=lambda e: print("Login clicado"))
    textCadastro = ft.Text( "Não tem uma conta? Cadastre-se", size=12, margin=ft.Margin(0, 20, 0, 0))

    teste=ft.Container(
        border_radius=10,
        width=400, #LADOS
        height=550, #CIMA
        align=ft.Alignment.CENTER, #Centraliza o container INTERNO
        bgcolor=loginBackground,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, #Centraliza os itens dentro da coluna
            controls=[
            textTitulo,
            textLogin,
            textSenha,
            btnLogin,
            textCadastro
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
    page.update()
ft.run(main)
