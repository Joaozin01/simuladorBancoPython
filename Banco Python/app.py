import tkinter as tk

class ContaBancaria:
    def __init__(self):
        self.banco = {}

    def criar_conta(self, nome):
        if nome:
            self.banco[nome] = {'saldo': 0, 'transacoes': []}
            return f'Conta para {nome} criada com sucesso.'
        else:
            return 'Por favor, insira um nome válido.'

    def depositar(self, nome, valor):
        if nome in self.banco:
            if valor > 0:
                self.banco[nome]['saldo'] += valor
                self.banco[nome]['transacoes'].append(f'Depósito de R${valor:.2f}')
                return f'Depósito de R${valor:.2f} realizado com sucesso.'
            else:
                return 'O valor do depósito deve ser maior que zero.'
        else:
            return 'Conta não encontrada.'

    def sacar(self, nome, valor):
        if nome in self.banco:
            if 0 < valor <= self.banco[nome]['saldo']:
                self.banco[nome]['saldo'] -= valor
                self.banco[nome]['transacoes'].append(f'Saque de R${valor:.2f}')
                return f'Saque de R${valor:.2f} realizado com sucesso.'
            else:
                return 'Saldo insuficiente para realizar o saque ou valor inválido.'
        else:
            return 'Conta não encontrada.'

    def visualizar_saldo(self, nome):
        if nome in self.banco:
            return f'Saldo atual: R${self.banco[nome]["saldo"]:.2f}'
        else:
            return 'Conta não encontrada.'

    def gerar_extrato(self, nome):
        if nome in self.banco:
            extrato = f'Extrato da conta de {nome}:\n'
            for transacao in self.banco[nome]['transacoes']:
                extrato += transacao + '\n'
            extrato += f'Saldo atual: R${self.banco[nome]["saldo"]:.2f}'
            return extrato
        else:
            return 'Conta não encontrada.'

    def transferir(self, conta_origem, conta_destino, valor):
        if conta_origem in self.banco and conta_destino in self.banco:
            if valor > 0 and self.banco[conta_origem]['saldo'] >= valor:
                self.banco[conta_origem]['saldo'] -= valor
                self.banco[conta_destino]['saldo'] += valor
                self.banco[conta_origem]['transacoes'].append(f'Transferência para {conta_destino} no valor de R${valor:.2f}')
                self.banco[conta_destino]['transacoes'].append(f'Transferência recebida de {conta_origem} no valor de R${valor:.2f}')
                return f'Transferência de R${valor:.2f} de {conta_origem} para {conta_destino} realizada com sucesso.'
            else:
                return 'Valor inválido ou saldo insuficiente na conta de origem.'
        else:
            return 'Conta de origem ou conta de destino não encontrada.'

contas = ContaBancaria()

def criar_conta(event=None):
    nome = entry_nome.get()
    mensagem = contas.criar_conta(nome)
    label_status['text'] = mensagem

def depositar(event=None):
    nome = entry_nome.get()
    valor = float(entry_valor.get())
    mensagem = contas.depositar(nome, valor)
    label_status['text'] = mensagem

def sacar(event=None):
    nome = entry_nome.get()
    valor = float(entry_valor.get())
    mensagem = contas.sacar(nome, valor)
    label_status['text'] = mensagem

def visualizar_saldo(event=None):
    nome = entry_nome.get()
    saldo = contas.visualizar_saldo(nome)
    label_status['text'] = saldo

def gerar_extrato(event=None):
    nome = entry_nome.get()
    extrato = contas.gerar_extrato(nome)
    label_status['text'] = extrato

def transferir(event=None):
    conta_origem = entry_origem.get()
    conta_destino = entry_destino.get()
    valor = float(entry_valor_transferencia.get())
    mensagem = contas.transferir(conta_origem, conta_destino, valor)
    label_status['text'] = mensagem

def exibir_contas_criadas(event=None):
    if contas.banco:
        contas_criadas = "Contas criadas:\n"
        for conta in contas.banco:
            contas_criadas += conta + '\n'
        label_status['text'] = contas_criadas
    else:
        label_status['text'] = 'Nenhuma conta foi criada ainda.'

def remover_usuario(event=None):
    nome = entry_nome.get()
    if nome in contas.banco:
        del contas.banco[nome]
        label_status['text'] = f'Usuário {nome} removido com sucesso.'
    else:
        label_status['text'] = "Usuário não encontrado."

def enter_pressed(event):
    focused_widget = root.focus_get()
    if focused_widget == entry_nome:
        criar_conta()
    elif focused_widget == entry_valor:
        depositar()
    elif focused_widget == entry_origem:
        transferir()
    elif focused_widget == entry_destino:
        transferir()
    elif focused_widget == entry_valor_transferencia:
        transferir()
    else:
        pass

root = tk.Tk()
root.title("Conta Bancária")

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)
label_nome.bind("<Return>", enter_pressed)

label_valor = tk.Label(root, text="Valor:")
label_valor.grid(row=1, column=0)
entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1)
label_valor.bind("<Return>", enter_pressed)

button_criar_conta = tk.Button(root, text="Criar Conta", command=criar_conta)
button_criar_conta.grid(row=2, column=0, columnspan=2, sticky="WE")

button_depositar = tk.Button(root, text="Depositar", command=depositar)
button_depositar.grid(row=3, column=0, columnspan=2, sticky="WE")

button_sacar = tk.Button(root, text="Sacar", command=sacar)
button_sacar.grid(row=4, column=0, columnspan=2, sticky="WE")

button_visualizar_saldo = tk.Button(root, text="Visualizar Saldo", command=visualizar_saldo)
button_visualizar_saldo.grid(row=5, column=0, columnspan=2, sticky="WE")

button_gerar_extrato = tk.Button(root, text="Gerar Extrato", command=gerar_extrato)
button_gerar_extrato.grid(row=6, column=0, columnspan=2, sticky="WE")

label_origem = tk.Label(root, text="Conta de Origem:")
label_origem.grid(row=7, column=0)
entry_origem = tk.Entry(root)
entry_origem.grid(row=7, column=1)
label_origem.bind("<Return>", enter_pressed)

label_destino = tk.Label(root, text="Conta de Destino:")
label_destino.grid(row=8, column=0)
entry_destino = tk.Entry(root)
entry_destino.grid(row=8, column=1)
label_destino.bind("<Return>", enter_pressed)

label_valor_transferencia = tk.Label(root, text="Valor da Transferência:")
label_valor_transferencia.grid(row=9, column=0)
entry_valor_transferencia = tk.Entry(root)
entry_valor_transferencia.grid(row=9, column=1)
label_valor_transferencia.bind("<Return>", enter_pressed)

button_transferir = tk.Button(root, text="Transferir", command=transferir)
button_transferir.grid(row=10, column=0, columnspan=2, sticky="WE")

button_exibir_contas = tk.Button(root, text="Exibir Contas Criadas", command=exibir_contas_criadas)
button_exibir_contas.grid(row=11, column=0, columnspan=2, sticky="WE")

button_remover_usuario = tk.Button(root, text="Remover Usuário", command=remover_usuario)
button_remover_usuario.grid(row=12, column=0, columnspan=2, sticky="WE")

label_status = tk.Label(root, text="")
label_status.grid(row=13, column=0, columnspan=2)

root.bind("<Return>", enter_pressed)

root.mainloop()
