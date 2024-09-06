import flet as ft


def main(page: ft.Page):
    page.tittle = "¿Regresamos?"
    page.bgcolor="566ce6"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿Regresamos?"
                style=ft.TextStyle(size=40,weight="bold"))
    img1=ft.Image(src="triste.png",width=200,height=200)
    
    btnSi=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50
                            )
    
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            width=100,
                            height=50
                            )
    page.add(
        ft.Colum(
            [
                lbl1,
                img1,
                ft.Row(
                    [btnSi,btnNo]
                )
            ]
        )
    )

ft.app(main)
