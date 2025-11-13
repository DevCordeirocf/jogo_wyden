import random

# Variável global para o saldo, mantida para simplificar a integração com o Gradio
saldo = 1000.0

def _validar_aposta(valor_aposta):
    """Valida se a aposta é positiva e se o saldo é suficiente."""
    global saldo
    if valor_aposta <= 0 or valor_aposta > saldo:
        # Retorna False para vitória, mensagem de erro e saldo
        return False, f"❌ Aposta inválida! Seu saldo é R$ {saldo:.2f}", f"💰 Saldo: R$ {saldo:.2f}"
    return True, None, None

def _atualizar_saldo(resultado, valor_aposta, ganho):
    """Atualiza o saldo e retorna a mensagem de resultado, o novo saldo formatado e o status de vitória."""
    global saldo
    
    vitoria = False
    if ganho > 0:
        vitoria = True
        saldo += ganho
        resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
    else:
        saldo -= valor_aposta
        resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
        
    resultado += f"\n\n💰 Saldo atual: **R$ {saldo:.2f}**"
    # Retorna o resultado, o saldo formatado e o status de vitória
    return resultado, f"💰 Saldo: R$ {saldo:.2f}", vitoria

# --- JOGO: ROLETA ---
def jogar_roleta(valor_aposta, escolha_cor):
    """Lógica do jogo de Roleta."""
    valido, msg_erro, saldo_erro = _validar_aposta(valor_aposta)
    if not valido:
        # Retorna False para vitória em caso de erro
        return msg_erro, saldo_erro, False
    
    numero = random.randint(0, 36)
    vermelhos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    
    if numero == 0:
        cor_sorteada = "Verde"
    elif numero in vermelhos:
        cor_sorteada = "Vermelho"
    else:
        cor_sorteada = "Preto"
    
    resultado = f"🎰 **ROLETA**\n\n"
    resultado += f"🎲 Número sorteado: **{numero}**\n"
    resultado += f"🎨 Cor: **{cor_sorteada}**\n\n"
    resultado += f"Você apostou em: **{escolha_cor}**\n\n"
    
    ganho = 0
    if escolha_cor == cor_sorteada and numero != 0:
        ganho = valor_aposta * 2
        
    return _atualizar_saldo(resultado, valor_aposta, ganho)

# --- JOGO: CAÇA-NÍQUEL ---
def jogar_caca_niquel(valor_aposta):
    """Lógica do jogo de Caça-Níquel."""
    valido, msg_erro, saldo_erro = _validar_aposta(valor_aposta)
    if not valido:
        # Retorna False para vitória em caso de erro
        return msg_erro, saldo_erro, False
    
    simbolos = ['🍒', '🍋', '🍊', '🍇', '💎', '7️⃣']
    slot1, slot2, slot3 = random.choices(simbolos, k=3)
    
    resultado = f"🎰 **CAÇA-NÍQUEL**\n\n"
    resultado += f"╔═══════════╗\n"
    resultado += f"║  {slot1}  {slot2}  {slot3}  ║\n"
    resultado += f"╚═══════════╝\n\n"
    
    ganho = 0
    if slot1 == slot2 == slot3:
        if slot1 == '💎':
            ganho = valor_aposta * 50
            resultado += f"💎 **MEGA JACKPOT!** "
        elif slot1 == '7️⃣':
            ganho = valor_aposta * 25
            resultado += f"7️⃣ **SUPER JACKPOT!** "
        else:
            ganho = valor_aposta * 10
            resultado += f"🎉 **JACKPOT!** "
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        ganho = valor_aposta * 2
        resultado += f"🎊 **Dois iguais!** "
        
    return _atualizar_saldo(resultado, valor_aposta, ganho)

# --- JOGO: DADOS ---
def jogar_dados(valor_aposta, escolha_numero):
    """Lógica do jogo de Dados."""
    valido, msg_erro, saldo_erro = _validar_aposta(valor_aposta)
    if not valido:
        # Retorna False para vitória em caso de erro
        return msg_erro, saldo_erro, False
    
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    
    resultado = f"🎲 **JOGO DE DADOS**\n\n"
    resultado += f"Primeiro dado: **{dado1}**\n"
    resultado += f"Segundo dado: **{dado2}**\n"
    resultado += f"Soma dos dados: **{soma}**\n\n"
    resultado += f"Você apostou em: **{escolha_numero}**\n\n"
    
    ganho = 0
    
    if escolha_numero == "7 ou 11":
        if soma == 7 or soma == 11:
            ganho = valor_aposta * 3
    elif escolha_numero == "Par":
        if soma % 2 == 0:
            ganho = valor_aposta * 2
    elif escolha_numero == "Ímpar":
        if soma % 2 != 0:
            ganho = valor_aposta * 2
    
    return _atualizar_saldo(resultado, valor_aposta, ganho)

# --- JOGO: CARA OU COROA ---
def jogar_cara_coroa(valor_aposta, escolha_lado):
    """Lógica do jogo Cara ou Coroa."""
    valido, msg_erro, saldo_erro = _validar_aposta(valor_aposta)
    if not valido:
        # Retorna False para vitória em caso de erro
        return msg_erro, saldo_erro, False
    
    lados = ["Cara", "Coroa"]
    lado_sorteado = random.choice(lados)
    
    resultado = f"🪙 **CARA OU COROA**\n\n"
    resultado += f"Lado sorteado: **{lado_sorteado}**\n\n"
    resultado += f"Você apostou em: **{escolha_lado}**\n\n"
    
    ganho = 0
    if escolha_lado == lado_sorteado:
        ganho = valor_aposta * 2
        
    return _atualizar_saldo(resultado, valor_aposta, ganho)

# --- FUNÇÕES DE SALDO ---
def adicionar_saldo(valor):
    """Adiciona valor ao saldo."""
    global saldo
    if valor > 0:
        saldo += valor
        # Retorna False para vitória, pois não é um jogo
        return f"✅ R$ {valor:.2f} adicionados!", f"💰 Saldo: R$ {saldo:.2f}", False
    # Retorna False para vitória em caso de erro
    return "❌ Valor inválido!", f"💰 Saldo: R$ {saldo:.2f}", False

def resetar():
    """Reseta o saldo para o valor inicial."""
    global saldo
    saldo = 1000.0
    # Retorna False para vitória, pois não é um jogo
    return "✅ Saldo resetado para R$ 1000.00!", f"💰 Saldo: R$ {saldo:.2f}", False

def get_saldo_inicial():
    """Retorna o saldo inicial formatado."""
    return f"💰 Saldo: R$ {saldo:.2f}"
