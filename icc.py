# -*- coding: utf-8 -*-

"""
CALCULADORA - ÍNDICE DE COMORBIDADE DE CHARLSON (ICC)
@author: isabelle carvalho
@date: 2021-06
"""

#python -m pip install PySimpleGUI
#conda install -c conda-forge pysimplegui

import PySimpleGUI as sg

#vetores de comorbidades/pesos
p1 = ["I21", "I22", "I252", "I50", "I71", "I790", "I739","R02", "Z958", "Z959", "I60", "I61", "I62", "I63", "I65", "I66","G450", "G451", "G452", "G458", "G459", "G46", "I64", "G454","I670", "I671", "I672", "I674", "I675", "I676", "I677", "I678","I679", "I681", "I682", "I688", "I69", "F00", "F01", "F02", "F051","J40", "J41", "J42", "J44", "J43", "J45", "J46", "J47", "J67","J44", "J60", "J61", "J62", "J63", "J66", "J64", "J65", "M32","M34", "M332", "M053", "M058", "M059", "M060", "M063", "M069","M050", "M052", "M051", "M353", "K25", "K26", "K27", "K28", "K702","K703", "K73", "K717", "K740", "K742", "K746", "K743", "K744","K745", "E109", "E119", "E139", "E149", "E101", "E111", "E131","E141", "E105", "E115", "E135", "E145"]
p2 = ["E102", "E112", "E132", "E142", "E103", "E113","E133", "E143", "E104", "E114", "E134", "E144", "G81", "G041","G820", "G821", "G822", "N03", "N052", "N053", "N054", "N055","N056", "N072", "N073", "N074", "N01", "N18", "N19", "N25", "C0","C1", "C2", "C3", "C40", "C41", "C43", "C45", "C46", "C47", "C48","C49", "C5", "C6", "C70", "C71", "C72", "C73", "C74", "C75", "C76","C80", "C81", "C82", "C83", "C84", "C85", "C883", "C887", "C889","C900", "C901", "C91", "C92", "C93", "C940", "C941", "C942","C943", "C9451", "C947", "C95", "C96"]
p3 = ["C77", "C78", "C79", "C80", "K729", "K766", "K767","K721"]
p6 = ["B20", "B21", "B22", "B23", "B24"]

#calcular ICC
def calcICC(paciente):
    v_icc=0
    #tratar string
    paciente = paciente.replace(" ", "")
    paciente = paciente.replace(".", "")
    paciente = paciente.swapcase()
    comorb = paciente.split(',')
    #calcular peso-comorbidades
    for cid in comorb:
        if cid in p1:
            v_icc=v_icc+1
        if cid in p2:
            v_icc=v_icc+2
        if cid in p3:
            v_icc=v_icc+3
        if cid in p6:
            v_icc=v_icc+6
    return v_icc
    
#GUI
layout = [[sg.Text("Digite os códigos CID-10, separados por vírgulas, das comorbidades do paciente")],
          [sg.Text("Ex.: E101,C78", font=("Arial",8, "italic"))],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(60,1), key='-OUTPUT-')],
          [sg.Button('Consultar'), sg.Button('Sair')]]

window = sg.Window('Calculadora ICC', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    # Consulta ICC
    if(values['-INPUT-']==''):
        window['-OUTPUT-'].update("Não é possível realizar a consulta. Preencha os valores.")
    else:
        icc = calcICC(values['-INPUT-'])
        if(icc==0):
            window['-OUTPUT-'].update("Valor ICC: "+str(icc)+". As comorbidades do paciente não agravam as chances de óbito.")
        else:    
            window['-OUTPUT-'].update("Valor ICC: "+str(icc)+". O paciente tem "+str(icc)+" vez(es) mais chance(s) de ir a óbito.")

window.close()


    