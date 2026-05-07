import flet as ft

def DashboardView(page, tarea_controller):
    user = page.user
    if not user:
        page.go("/")
        return

    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)

    
    prioridad_input = ft.Dropdown(
        options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Media"),
            ft.dropdown.Option("Baja")
        ],value="Media",width=120)

    

    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user["idUs"]):
            prioridad = t["prioridad"]
            color = (
                ft.Colors.RED_400 if prioridad == "Alta"
                else ft.Colors.ORANGE_300 if prioridad == "Media"
                else ft.Colors.GREEN_400
            )
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t["titulo"], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']} | Prioridad: {t['prioridad']}"),
                            trailing=ft.Container(
                                content=ft.Text(t["estado"]),
                                padding=5,
                                bgcolor=color,
                                border_radius=10
                            ),),)))
        page.update()

    def add_task(e):

        success, msg = tarea_controller.guardar_nueva(
            user['idUs'],
            txt_titulo.value,
            "",
            prioridad_input.value,   
            "trabajo"
        )

        print(msg)

        if success:
            txt_titulo.value = ""
            refresh()
        else:
            print("ERROR AL GUARDAR:", msg)

    view = ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre']}"),
                actions=[ft.IconButton(
                        ft.Icons.EXIT_TO_APP,
                        on_click=lambda _: page.go("/"))]
            ),
            ft.Column(
                [
                    ft.Row([
                            txt_titulo,
                            prioridad_input,   
                            ft.FloatingActionButton(icon=ft.Icons.ADD,on_click=add_task
                            )]),
                    ft.Divider(),
                    ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
                    lista_tareas
                ],expand=True)])

    refresh()
    return view