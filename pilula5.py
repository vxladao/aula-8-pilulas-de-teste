def processar_consultas(regristros):
    tempos = {}
    cont = {}
    status = {}
    
    for reg in regristros:
        p = reg['paciente']
        if p not in tempos:
            tempos[p] = 0
            cont[p] = 0
        tempos[p] += reg['tempo']
        cont[p] += 1
        
    for p in tempos:
        t = tempos[p]
        if t < 2:
            status[p] = 'Leve'
        elif t <= 5:
            status[p] = 'Moderado'
        else:
            status[p] = 'Crítico'
            
    for p in tempos:
        print(f'{p} | Tempo: {tempos[p]} | Qtd de consultas: {cont[p]} | Status clínico: {status[p]}')
            
        

def main():
    registros = [
        {'paciente': 'Ana', 'tempo' : 1},
        {'paciente': 'Ana', 'tempo' : 4},
        {'paciente': 'Carlos', 'tempo' : 2},
        {'paciente': 'Carlos', 'tempo' : 2},
        {'paciente': 'Maria', 'tempo' : 2},
        {'paciente': 'Maria', 'tempo' : 5}
    ]
    
    processar_consultas(registros)
    
main()

main()