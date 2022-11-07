import PySimpleGUI as sg
from layouts import login, create_account, main_menu, bg_left, bg_right
from debug import Log
import database.database as db
# from database.database import add_to_db


sg.theme("Reddit")
# Debug(sg.theme("DarkGrey2")) # Exemplo de Debug()

global_size = (400, 150)

layout = [[
    sg.Column(bg_left, key='col-bg_left', pad=(0, 0)),
    sg.Column(login, s=global_size, key='col-login'),
    sg.Column(create_account, s=global_size, key='col-logup', visible=False),
    sg.Column(main_menu, s=global_size, key='col-main', visible=False),
    sg.Column(bg_right, key='col-bg_right', pad=(0, 0)),
]]

window = sg.Window("Programa Foda", layout, finalize=True, margins=(0, 0))
# window.maximize()

while True:
    event, values = window.read()

    Log(event, values) # Exemplo de Log()

    if event == sg.WIN_CLOSED or event == "Cancelar": break

    if event == "proceed_login":
        window['col-login'].update(visible=False)

        window['col-bg_right'].update(visible=False)
        window['col-main'].update(visible=True)
        window['col-bg_right'].update(visible=True)

    if event == "create_account":
        window['col-login'].update(visible=False)
        window['col-bg_right'].update(visible=False)
        window['col-logup'].update(visible=True)
        window['col-bg_right'].update(visible=True)

        event, values = window.read()

        db.add_to_db("database/test.db", "usuario", {
          "name": values['create_user'],
          "email": values['create_email'],
          "password": values['create_password']
        })

        Log("Teste: ",values['create_user'], values['create_email'], values['create_password'])

    if "back_to_login" in event:
        window['col-main'].update(visible=False)

        window['col-bg_right'].update(visible=False)
        window['col-login'].update(visible=True)
        window['col-logup'].update(visible=False)
        window['col-bg_right'].update(visible=True)

    if event == "Criar conta":
        sg.popup("Conta Criada")

        window['col-login'].update(visible=True)
        window['col-bg_right'].update(visible=False)
        window['col-logup'].update(visible=False)
        window['col-bg_right'].update(visible=True)

window.close()
