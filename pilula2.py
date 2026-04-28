def especialidadeTop(consultas):
    cont= {}
    for c in consultas:
        esp = c['especialidade']
        if esp not in cont:
            cont[esp] = 0 
        cont[esp] += 1
    maior_esp = ''
    max_valor = -1
    for esp in cont:
        if cont[esp] > max_valor:
            maior_esp = esp
    return maior_esp

def main():
    consultar = [
        {'paciente': 'Ana', 'especialidade': 'Cardiologia'},
        {'paciente': 'Gabriel', 'especialidade': 'Cardiologia'},
        {'paciente': 'Cauã', 'especialidade': 'Cardiologia'},
        {'paciente': 'Vitor', 'especialidade': 'Cardiologia'},
    ]
    print(especialidadeTop(consultar))
    
main()
