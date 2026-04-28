def atualizar_hist(hist,paciente):
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist

def main():
    hist = ['Ana', 'Cauã', 'Gabriel']
    novo = "Vitor"
    print(f'Hist atual {hist}')
    hist= atualizar_hist(hist,novo)
    print(f'Hist atualizado: {hist}')