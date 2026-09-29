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

    historico = ft.Text(value="histórico de calculos",
                         size = 30,
                         font_family = "Elephant",
                         color= "#462E01",
                         
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

    lista_contas = []

    def soma():

        try:
            campo1 = int(campo_valor1.value)
            campo2 = int(campo_valor2.value)

        except:
            pagina.show_dialog(ft.SnackBar("Digite um número"))
            return
             
        resultado = campo1 + campo2
        if resultado != 67:
            lista_contas.append(ft.TextField(value=f"{campo1} + {campo2} = {resultado}",
                                         width=300,
                                         bgcolor="#b4a290",
                                         color="#462E01",
                                         border_radius=20,
                                         border_color= "#b4a290"))

        elif resultado == 67:
             pagina.show_dialog(ft.AlertDialog(title=ft.Text("ALERTA DE AURA!"),
                                               content=ft.Text("67 67 67 67 67 "),
                                               open=True,))

    def sub():

        try:
            campo1 = int(campo_valor1.value)
            campo2 = int(campo_valor2.value)

        except:
            pagina.show_dialog(ft.SnackBar("Digite um número"))
            return

        resultado = campo1 - campo2
        lista_contas.append(ft.TextField(value=f"{campo1} - {campo2} = {resultado}",
                                                width=300,
                                                bgcolor="#b4a290",
                                                color="#462E01",
                                                border_radius=20,
                                                border_color= "#b4a290"))

    def mult():

            try:
                campo1 = int(campo_valor1.value)
                campo2 = int(campo_valor2.value)

            except:
                pagina.show_dialog(ft.SnackBar("Digite um número"))
                return
            
            resultado = campo1 * campo2
            lista_contas.append(ft.TextField(value=f"{campo1} x {campo2} = {resultado}",
                                                     width=300,
                                                     bgcolor="#b4a290",
                                                    color="#462E01",
                                                    border_radius=20,
                                                    border_color= "#b4a290"))
    
    def div():

        try:
            campo1 = int(campo_valor1.value)
            campo2 = int(campo_valor2.value)

        except:
            pagina.show_dialog(ft.SnackBar("Digite um número"))
            return
        
        resultado = campo1 / campo2
        lista_contas.append(ft.TextField(value=f"{campo1} ÷ {campo2} = {resultado}",
                                                     width=300,
                                                     bgcolor="#b4a290",
                                                    color="#462E01",
                                                    border_radius=20,
                                                    border_color= "#b4a290"))

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
                                       bgcolor= "#533B27",
                                       padding=30,
                                       #border=ft.Border.all(1),
                                       border_radius = 30)

    container2 = ft.Container(content=ft.Column(controls=[historico,
                                                          ft.Column(controls=lista_contas,),],
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                                           bgcolor= "#6E5641",
                                           padding=30,
                                           #border=ft.Border.all(1),
                                           border_radius = 30,
                                           width=1000,
                                           height=450)
    



    pagina.controls = [titulo,
                       container1,
                       container2,
                       ]

    pagina.update()
ft.run(main)