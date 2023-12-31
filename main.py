import sqlite3
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineListItem
from datetime import datetime, timedelta

class Contatos(MDBoxLayout):
    def Criar_dados(self):
        try:
            c = sqlite3.connect('agenda.db')
            r = c.cursor()
            r.execute('''
            create table if not exists client(
            id integer not null primary key autoincrement,
            dia_s date not null,
            nome text not null,
            hora time not null,
            final_h time not null)
            '''
                      )
            c.commit()
            r.close()
        except ValueError as e:
            print('O error é: "'+e+'"')
        self.inserir_dados()

    def inserir_dados(self):
        try:
            d = self.ids.day_s.text
            n = self.ids.name_s.text
            t = self.ids.inicio_s.text
            y = self.ids.final.text
            hora_inicio_str = t
            periodo_horas = int(y)

            hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M")
            hora_resultante = hora_inicio + timedelta(hours=periodo_horas)

            resultado_text = f"{hora_resultante.strftime('%H:%M')}"
            c = sqlite3.connect('agenda.db')
            r = c.cursor()
            r.execute('INSERT INTO client(dia_s, nome, hora, final_h)VALUES("'+d+'","'+n+'","'+t+'","'+resultado_text+'")')
            c.commit()
            r.close()
        except ValueError as e:
            print('Error de tentativa de inserir dados: "'+e+'"')


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            c = sqlite3.connect('agenda.db')
            r = c.cursor()
            r.execute('select dia_s, nome, final_h from client;')
            b = self.ids.t_texto
            for i in r:
                formatos = f"Dia: {i[0]}, Name: {i[1]}, Periódo total: {i[2]}"
                m = TwoLineListItem(text=formatos)
                b.add_widget(m)

            r.fetchall()
            c.close()
        except ValueError as e:
            print('Deu error na lista de dados para ver: "'+e+'"')



    def calcula_horas(self):
        try:
            hora_inicio_str = self.ids.inicio_s.text
            periodo_horas = int(self.ids.final.text)

            hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M")
            hora_resultante = hora_inicio + timedelta(hours=periodo_horas)

            resultado_text = f"Horário Resultante: {hora_resultante.strftime('%H:%M')}"
            print(f'O resultado espera é este: {resultado_text}')
        except ValueError as e:
            print(f'Valor do erro é: {e}')


class MainApp(MDApp):
    def build(self):
        return Contatos()


if __name__ == '__main__':
    MainApp().run()
