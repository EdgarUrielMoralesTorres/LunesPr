import flet as ft

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="Correo electronico",width=350,border_radius=10)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True,width=350,border_radius=10)
    
    def login_click(e):
        user, msg=auth_controller.login(email_input.value,pass_input.value)
        if user:
            page.session.set("user",user)
            page.go("/dashboard")
    
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open= True
            page.update()
            
    return ft.View("/",(
        ft.AppBar(title=ft.Text("SIGE-LOGIN"),bgcolor=ft.Colors.BLUE_GREY_900,color="white"),
        ft.Column([
            ft.Text("Acceso al Sistema",size=24,weight="hola"),
            email_input,
            pass_input,
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _:page.go("/registro"))  
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.Center)
    ))       