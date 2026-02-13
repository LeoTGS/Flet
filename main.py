import flet as ft


def main(page: ft.Page):
    page.title = 'Login'
    page.bgcolor = ft.Colors.BLUE_GREY_700
    page.window_with = 400
    page.window_height = 600

    page.vertical_alignment  = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    card = ft.Container(
        width = 300,
        padding = 20,
        bgcolor = ft.Colors.WHITE,
        border_radius = 10,
        content=ft.Column(
            [],
            spacing = 10
        )
    )

    tf_usuario = ft.TextField(
        label = 'Usuário',
        hint_text = 'Digite seu Usuário',
        autofocus= True
    )

    tf_senha = ft.TextField(
        label= 'Senha',
        hint_text = 'Digite sua senha',
        autofocus = True,
        can_reveal_password = True
    )

    def fazer_login(e):
        usuario = tf_usuario.value
        senha = tf_senha.value

        page.add(ft.Text(f"Usuario: {usuario}, Senha: {senha}", color=ft.Colors.RED))
        page.update()

    card.content.controls.extend([
        ft.Text('Login', size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
        tf_usuario,
        tf_senha,
        ft.ElevatedButton("Entrar", on_click=fazer_login)
    ])

    page.add(card)


if __name__ == '__main__':
    ft.app(target = main)