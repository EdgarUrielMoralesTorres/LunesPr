import flet as ft
from controller.UserController import AuthController
from controller.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        
        if page.route == "/":
            page.add(ft.Text("1"))
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route== "/dashboard":
            page.views.append(DashboardView(page,task_ctrl))
            
            
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada")])
            )
    
        page.update()
    
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    main()