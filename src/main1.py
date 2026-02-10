import flet as ft

def main(page: ft.Page):
    page.title = "App Flet 0.80.5"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT  # Forçar tema pode evitar glitchs visuais na nova versão

    # Criando referências para os controles (Boa prática em versões novas para evitar perda de referência)
    txt_numero_ref = ft.Ref[ft.TextField]()

    def somar(e):
        # Acessamos o controle através da referência 'current'
        if txt_numero_ref.current:
            valor_atual = int(txt_numero_ref.current.value or 0)
            txt_numero_ref.current.value = str(valor_atual + 1)
            txt_numero_ref.current.update() # Atualiza apenas o componente, mais eficiente que page.update()

    def subtrair(e):
        if txt_numero_ref.current:
            valor_atual = int(txt_numero_ref.current.value or 0)
            txt_numero_ref.current.value = str(valor_atual - 1)
            txt_numero_ref.current.update()

    # Layout
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=subtrair),
                # Associamos a Ref ao controle aqui
                ft.TextField(ref=txt_numero_ref, value="0", text_align=ft.TextAlign.CENTER, width=100),
                ft.IconButton(ft.Icons.ADD, on_click=somar),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

# Execução padrão
ft.app(target=main)