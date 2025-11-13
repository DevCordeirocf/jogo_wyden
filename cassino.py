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
    gr.Markdown("### Jogue Roleta e Slot Machine")
    
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
    
    btn_add.click(fn=adicionar_saldo, inputs=[valor_add], outputs=[resultado_roleta, saldo_display])
    btn_reset.click(fn=resetar, outputs=[resultado_roleta, saldo_display])

if __name__ == "__main__":
    app.launch(share=True)
