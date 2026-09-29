import flet as ft


def main(pagina:ft.Page):
    pagina.title = "Calculadora"
    pagina.bgcolor = "#806D58"
    pagina.horizontal_alignment = "center"
    pagina.window.height = 800 #altura da janela
    pagina.window.width = 1000 # largura da janela

   

    titulo = ft.Text(value="Calculadora",
                     size = 40,
                     font_family = "Broadway",
                     color= "#462E01")

    historico = ft.Text(value="histórico",
                         size = 30,
                         font_family = "Elephant",
                         color= "#83714F",
                         
                        )


    campo_valor1 = ft.TextField(label = "Digite o Valor:",
                               bgcolor = "#c2b3a5",
                               border_radius = 50,
                               border_color= "#6d5433",
                               border_width= 3,
                               value = "")

    campo_valor2 = ft.TextField(label = "Digite o Valor:",
                               bgcolor = "#c2b3a5",
                               border_radius = 50,
                               border_color= "#6d5433",
                               border_width= 3,
                               value = "")

    linha_valores = ft.Row(controls = [campo_valor1,
                                      campo_valor2],
                                      alignment = "center")

    def soma():
        campo1 = int(campo_valor1.value)
        campo2 = int(campo_valor2.value)
        resultado = campo1 + campo2
        print(f"{campo1} + {campo2} = {resultado}")

    def sub():
        campo1 = int(campo_valor1.value)
        campo2 = int(campo_valor2.value)
        resultado = campo1 - campo2
        print(f"{campo1} - {campo2} = {resultado}")

    def mult():
            campo1 = int(campo_valor1.value)
            campo2 = int(campo_valor2.value)
            resultado = campo1 * campo2
            print(f"{campo1} x {campo2} = {resultado}")
    
    def div():
            campo1 = int(campo_valor1.value)
            campo2 = int(campo_valor2.value)
            resultado = campo1 / campo2
            print(f"{campo1} ÷ {campo2} = {resultado}")

    botao_soma = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.ADD,
                                                color="#FFFFFF"),
                                                bgcolor="#837562",
                                                foreground_color="#584A41",
                                                hover_color="#806D4E",
                                                on_click= soma)

    botao_subtracao = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.REMOVE,
                                                    color="#FFFFFF"),
                                                    bgcolor="#837562",
                                                    foreground_color="#584A41",
                                                    hover_color="#806D4E",
                                                    on_click= sub)

    botao_multiplicacao = ft.FloatingActionButton(icon = ft.Icon(icon=ft.Icons.CLOSE,
                                                    color="#FFFFFF"),
                                                    bgcolor="#837562",
                                                    foreground_color="#584A41",
                                                    hover_color="#806D4E",
                                                    on_click=mult)

    botao_divisao = ft.FloatingActionButton(content=ft.Text("÷",
                                            color="#FFFFFF",
                                            size=22,),
                                            bgcolor="#837562",
                                            foreground_color="#584A41",
                                            hover_color="#806D4E",
                                            on_click=div)

    linha_botoes = ft.Row(controls = [botao_soma,
                                      botao_subtracao,
                                      botao_multiplicacao,
                                      botao_divisao],
                                      alignment = "center")

    container1 = ft.Container(content=ft.Column(controls=[linha_valores,
                                                            linha_botoes,]),
                                       bgcolor= "#442913",
                                       padding=30,
                                       border=ft.Border.all(1),
                                       border_radius = 30)

    container2 = ft.Container(content=ft.Column(controls=[historico],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                                           bgcolor= "#442913",
                                           padding=30,
                                           border=ft.Border.all(1),
                                           border_radius = 30,
                                           width=1000,
                                           height=450)
    



    pagina.controls = [titulo,
                       container1,
                       container2,
                       

                       ]

    pagina.update()
ft.run(main)