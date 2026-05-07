import flet as ft


def RegisterView(page, auth_controller):

    nombre_input = ft.TextField(label="Nombre",hint_text="Ingresa tu nombre",width=350,border_radius=10)
    apellido_input = ft.TextField(label="Apellidos",hint_text="Ingresa tus apellidos",width=350,border_radius=10)
    email_input = ft.TextField(label="Correo",hint_text="Ingresa tu correo",width=350,border_radius=10)
    telefono_input = ft.TextField(label="Teléfono",width=350,border_radius=10)
    contra_input = ft.TextField(label="Contraseña",hint_text="Ingresa tu contraseña",password=True,can_reveal_password=True,width=350,border_radius=10)
    confirmar_input = ft.TextField(label="Confirmar contraseña",hint_text="Repite tu contraseña",password=True,can_reveal_password=True,width=350,border_radius=10)
    mensaje = ft.Text("", color="red")

    def register_click(e):

        if not nombre_input.value or not email_input.value or not contra_input.value or not confirmar_input.value or not apellido_input.value or not telefono_input.value:
            mensaje.value = "Complete todos los los campos"
            page.update()
            return

        if contra_input.value != confirmar_input.value:
            mensaje.value = "Las contraseñas no coinciden"
            page.update()
            return

        success, msg = auth_controller.register(nombre_input.value,apellido_input.value,telefono_input.value,email_input.value,contra_input.value)
        mensaje.value = msg
        page.update()

        if success:
            page.go("/")

    register_button = ft.ElevatedButton("Registrarse",on_click=register_click,width=350,bgcolor=ft.Colors.BLACK,color=ft.Colors.WHITE)

    return ft.View(
        route="/registro",vertical_alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Text(
                        "Crear Cuenta",
                        size=30,
                        weight=ft.FontWeight.BOLD
                    ),
                    nombre_input,
                    apellido_input,
                    telefono_input,
                    email_input,
                    contra_input,
                    confirmar_input,
                    register_button,
                    mensaje,

                    ft.TextButton(
                        "Ya tengo cuenta",
                        on_click=lambda _: page.go("/")
                    )

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )