import flet as ft


def main(pagina:ft.Page):
    pagina.title = "Calculadora"
    pagina.bgcolor = "#806D58"
    pagina.horizontal_alignment = "center"

   

    titulo = ft.Text(value="Calculadora",
                     size = 40,
                     font_family = "Broadway",
                     color= "#462E01")


    campo_valor1 = ft.TextField(label = "Digite o Valor:",
                               bgcolor = "#c2b3a5",
                               border_radius = 50,
                               border_color= "#6d5433",
                               border_width= 3)

    campo_valor2 = ft.TextField(label = "Digite o Valor:",
                               bgcolor = "#c2b3a5",
                               border_radius = 50,
                               border_color= "#6d5433",
                               border_width= 3)

    linha_valores = ft.Row(controls = [campo_valor1,
                                      campo_valor2],
                                      alignment = "center")

    botao_soma = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.ADD,
                                                color="#FFFFFF"),
                                                bgcolor="#837562",
                                                foreground_color="#584A41",
                                                hover_color="#806D4E",)

    botao_subtracao = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.REMOVE,
                                                    color="#FFFFFF"),
                                                    bgcolor="#837562",
                                                    foreground_color="#584A41",
                                                    hover_color="#806D4E",)

    botao_multiplicacao = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.CLOSE,
                                                    color="#FFFFFF"),
                                                    bgcolor="#837562",
                                                    foreground_color="#584A41",
                                                    hover_color="#806D4E",)

    botao_divisao = ft.FloatingActionButton(content=ft.Text("÷",
                                            color="#FFFFFF",
                                            size=22,),
                                            bgcolor="#837562",
                                            foreground_color="#584A41",
                                            hover_color="#806D4E",)

    linha_botoes = ft.Row(controls = [botao_soma,
                                      botao_subtracao,
                                      botao_multiplicacao,
                                      botao_divisao],
                                      alignment = "center")
    



    pagina.controls = [titulo,
                       linha_valores,
                       linha_botoes       
                       ]

    pagina.update()
ft.run(main)