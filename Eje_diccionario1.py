registro_diccionario = {}
list_pendiente = []

import os
sw = True




def fnt_añadir(diccionario, codigo, nombres, contacto, correo, edad, estrato, sexo, direccion):
    if not all([codigo, nombres, contacto, correo, edad, estrato, sexo, direccion]):
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[codigo] = {'Nombre': nombres, 'Contacto': contacto, 'Correo': correo, 'Edad': edad, 'Estrato': estrato, 'Sexo': sexo, 'Direccion': direccion}
        enter = input(f'\nLa persona {nombres} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        codigo = input('Ingrese su codigo:')
        nombres = input('Nombres completos:  ')
        contacto = input('Número de contacto:   ')
        correo = input('Ingrese su correo:  ')
        direccion = input('Ingrese su dirección: ')
        sexo = input('Sexo (M/F):  ')
        edad = int(input('ingrese su Edad: ->  '))
        estrato = int(input('Ingrese su estrato: -> '))
        
        if (sexo == 'M' and 15 <= edad <= 25 and estrato in (1, 2)) or (sexo == 'F' and 20 <= edad <= 35 and estrato in (1, 2, 3, 4)):
            fnt_añadir(registro_diccionario, codigo, nombres, contacto, correo, edad, estrato, sexo, direccion)
        else:
            print('No cumple con la edad para los requisitos de registro, pero agregaremos su contacto a la "lista Pendiente".')
            list_pendiente.append(contacto)
        enter = input('\nPresione <ENTER> para continuar por favor...\n')
def fnt_mostrar_pendiente():
    os.system('cls')
    print('\nLista de contactos pendientes:\n')
    for contacto in list_pendiente:
        print(f'- {contacto}')
    enter = input('\nPresione <ENTER> para continuar por favor')

while sw == True:
    os.system('cls')
    opcion = input('1. REGISTRAR\n2. MOSTRAR\n3. LISTA DE PENDIENTES\n4. SALIR\n- >  ')
    if opcion == "1":
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(registro_diccionario),'\n')
        for clave, valor in registro_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\nPresione <ENTER> para continuar')
    elif opcion == '3':
        fnt_mostrar_pendiente()
    elif opcion == '4':
        sw = False