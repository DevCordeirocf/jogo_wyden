import gradio as gr 
import random

saldo = 1000.0

def jogar_roleta(valor_aposta, escolha_cor):
    global saldo
    
    if valor_aposta <= 0 or valor_aposta > saldo:
        return f"❌ Aposta inválida! Seu saldo é R$ {saldo:.2f}", f"💰 Saldo: R$ {saldo:.2f}"
    
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
    
    if escolha_cor == cor_sorteada and numero != 0:
        ganho = valor_aposta * 2
        saldo += ganho
        resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
    else:
        saldo -= valor_aposta
        resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
    
    resultado += f"\n\n💰 Saldo atual: **R$ {saldo:.2f}**"
    
    return resultado, f"💰 Saldo: R$ {saldo:.2f}"

def jogar_caca_niquel(valor_aposta):
    global saldo
    
    if valor_aposta <= 0 or valor_aposta > saldo:
        return f"❌ Aposta inválida! Seu saldo é R$ {saldo:.2f}", f"💰 Saldo: R$ {saldo:.2f}"
    
    simbolos = ['🍒', '🍋', '🍊', '🍇', '💎', '7️⃣']
    
    slot1 = random.choice(simbolos)
    slot2 = random.choice(simbolos)
    slot3 = random.choice(simbolos)
    
    resultado = f"🎰 **CAÇA-NÍQUEL**\n\n"
    resultado += f"╔═══════════╗\n"
    resultado += f"║  {slot1}  {slot2}  {slot3}  ║\n"
    resultado += f"╚═══════════╝\n\n"
    
    if slot1 == slot2 == slot3:
        if slot1 == '💎':
            ganho = valor_aposta * 50
            resultado += f"💎 **MEGA JACKPOT! Ganhou R$ {ganho:.2f}!**"
        elif slot1 == '7️⃣':
            ganho = valor_aposta * 25
            resultado += f"7️⃣ **SUPER JACKPOT! Ganhou R$ {ganho:.2f}!**"
        else:
            ganho = valor_aposta * 10
            resultado += f"🎉 **JACKPOT! Ganhou R$ {ganho:.2f}!**"
        saldo += ganho
    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        ganho = valor_aposta * 2
        saldo += ganho
        resultado += f"🎊 **Dois iguais! Ganhou R$ {ganho:.2f}!**"
    else:
        saldo -= valor_aposta
        resultado += f"😢 **Não foi dessa vez! Perdeu R$ {valor_aposta:.2f}**"
    
    resultado += f"\n\n💰 Saldo atual: **R$ {saldo:.2f}**"
    
    return resultado, f"💰 Saldo: R$ {saldo:.2f}"

# --- NOVO JOGO 1: DADOS ---
def jogar_dados(valor_aposta, escolha_numero):
    global saldo
    
    if valor_aposta <= 0 or valor_aposta > saldo:
        return f"❌ Aposta inválida! Seu saldo é R$ {saldo:.2f}", f"💰 Saldo: R$ {saldo:.2f}"
    
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
            saldo += ganho
            resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
        else:
            saldo -= valor_aposta
            resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
    elif escolha_numero == "Par":
        if soma % 2 == 0:
            ganho = valor_aposta * 2
            saldo += ganho
            resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
        else:
            saldo -= valor_aposta
            resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
    elif escolha_numero == "Ímpar":
        if soma % 2 != 0:
            ganho = valor_aposta * 2
            saldo += ganho
            resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
        else:
            saldo -= valor_aposta
            resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
    else:
        # Aposta em um número específico (2 a 12)
        try:
            aposta_num = int(escolha_numero)
            if soma == aposta_num:
                ganho = valor_aposta * 5
                saldo += ganho
                resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
            else:
                saldo -= valor_aposta
                resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
        except ValueError:
            # Isso não deve acontecer com o gr.Radio, mas é uma segurança
            resultado = f"❌ Erro na escolha do número."
            
    resultado += f"\n\n💰 Saldo atual: **R$ {saldo:.2f}**"
    
    return resultado, f"💰 Saldo: R$ {saldo:.2f}"

# --- NOVO JOGO 2: CARA OU COROA ---
def jogar_cara_coroa(valor_aposta, escolha_lado):
    global saldo
    
    if valor_aposta <= 0 or valor_aposta > saldo:
        return f"❌ Aposta inválida! Seu saldo é R$ {saldo:.2f}", f"💰 Saldo: R$ {saldo:.2f}"
    
    lados = ["Cara", "Coroa"]
    lado_sorteado = random.choice(lados)
    
    resultado = f"🪙 **CARA OU COROA**\n\n"
    resultado += f"Lado sorteado: **{lado_sorteado}**\n\n"
    resultado += f"Você apostou em: **{escolha_lado}**\n\n"
    
    if escolha_lado == lado_sorteado:
        ganho = valor_aposta * 2
        saldo += ganho
        resultado += f"🎉 **VOCÊ GANHOU R$ {ganho:.2f}!**"
    else:
        saldo -= valor_aposta
        resultado += f"😢 **Você perdeu R$ {valor_aposta:.2f}**"
        
    resultado += f"\n\n💰 Saldo atual: **R$ {saldo:.2f}**"
    
    return resultado, f"💰 Saldo: R$ {saldo:.2f}"

def adicionar_saldo(valor):
    global saldo
    if valor > 0:
        saldo += valor
        return f"✅ R$ {valor:.2f} adicionados!", f"💰 Saldo: R$ {saldo:.2f}"
    return "❌ Valor inválido!", f"💰 Saldo: R$ {saldo:.2f}"

def resetar():
    global saldo
    saldo = 1000.0
    return "✅ Saldo resetado para R$ 1000.00!", f"💰 Saldo: R$ {saldo:.2f}"

with gr.Blocks(title="🎰 Cassino Wyden") as app:
    
    gr.Markdown("# 🎰 CASSINO WYDEN")
    gr.Markdown("### Jogue Roleta, Caça-Níquel, Dados e Cara ou Coroa")
    
    with gr.Row():
        saldo_display = gr.Textbox(label="", value=f"💰 Saldo: R$ {saldo:.2f}", interactive=False)
    
    with gr.Row():
        valor_add = gr.Number(label="Adicionar Saldo (R$)", value=100)
        btn_add = gr.Button("💵 Adicionar")
        btn_reset = gr.Button("🔄 Resetar")
    
    gr.Markdown("---")
    
    with gr.Tabs():
        
        with gr.Tab("🎰 Roleta"):
            gr.Markdown("**Escolha uma cor e torça para o número cair nela!**")
            aposta_roleta = gr.Number(label="Valor da Aposta (R$)", value=10)
            cor_roleta = gr.Radio(choices=["Vermelho", "Preto"], label="Escolha a Cor", value="Vermelho")
            btn_roleta = gr.Button("🎲 Girar Roleta!", variant="primary", size="lg")
            resultado_roleta = gr.Markdown()
            
            btn_roleta.click(
                fn=jogar_roleta,
                inputs=[aposta_roleta, cor_roleta],
                outputs=[resultado_roleta, saldo_display]
            )
        
        with gr.Tab("🎰 Caça-Níquel"):
            gr.Markdown("**Três símbolos iguais = JACKPOT!**")
            aposta_caca = gr.Number(label="Valor da Aposta (R$)", value=10)
            btn_caca = gr.Button("🎰 Girar!", variant="primary", size="lg")
            resultado_caca = gr.Markdown()
            
            btn_caca.click(
                fn=jogar_caca_niquel,
                inputs=[aposta_caca],
                outputs=[resultado_caca, saldo_display]
            )
            
        with gr.Tab("🎲 Dados"):
            gr.Markdown("**Aposte na soma dos dados, Par/Ímpar ou 7/11!**")
            aposta_dados = gr.Number(label="Valor da Aposta (R$)", value=10)
            escolha_dados = gr.Radio(choices=["7 ou 11", "Par", "Ímpar"], label="Escolha a Aposta", value="7 ou 11")
            btn_dados = gr.Button("🎲 Rolar Dados!", variant="primary", size="lg")
            resultado_dados = gr.Markdown()
            
            btn_dados.click(
                fn=jogar_dados,
                inputs=[aposta_dados, escolha_dados],
                outputs=[resultado_dados, saldo_display]
            )
            
        with gr.Tab("🪙 Cara ou Coroa"):
            gr.Markdown("**Simples e rápido: dobre sua aposta!**")
            aposta_cc = gr.Number(label="Valor da Aposta (R$)", value=10)
            escolha_cc = gr.Radio(choices=["Cara", "Coroa"], label="Escolha o Lado", value="Cara")
            btn_cc = gr.Button("🪙 Jogar Moeda!", variant="primary", size="lg")
            resultado_cc = gr.Markdown()
            
            btn_cc.click(
                fn=jogar_cara_coroa,
                inputs=[aposta_cc, escolha_cc],
                outputs=[resultado_cc, saldo_display]
            )
    
    # Atualiza os botões de saldo para afetar todos os resultados
    btn_add.click(fn=adicionar_saldo, inputs=[valor_add], outputs=[resultado_roleta, saldo_display])
    btn_reset.click(fn=resetar, outputs=[resultado_roleta, saldo_display])

if __name__ == "__main__":
    app.launch(share=True)
