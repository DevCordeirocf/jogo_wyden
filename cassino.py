import gradio as gr 
from game_logic import (
    jogar_roleta, 
    jogar_caca_niquel, 
    jogar_dados, 
    jogar_cara_coroa, 
    adicionar_saldo, 
    resetar,
    get_saldo_inicial
)

with gr.Blocks(title="🎰 Cassino Wyden") as app:
    
    gr.Markdown("# 🎰 CASSINO WYDEN")
    gr.Markdown("### Jogue Roleta, Caça-Níquel, Dados e Cara ou Coroa")
    
    # Display do Saldo
    with gr.Row():
        saldo_display = gr.Textbox(label="", value=get_saldo_inicial(), interactive=False)
    
    # Controles de Saldo
    with gr.Row():
        valor_add = gr.Number(label="Adicionar Saldo (R$)", value=100)
        btn_add = gr.Button("💵 Adicionar")
        btn_reset = gr.Button("🔄 Resetar")
    
    gr.Markdown("---")
    
    # Abas dos Jogos
    with gr.Tabs():
        
        # --- Roleta ---
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
        
        # --- Caça-Níquel ---
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
            
        # --- Dados ---
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
            
        # --- Cara ou Coroa ---
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
    
    # Conexão dos botões de saldo com as saídas de resultado de todos os jogos
    # Para garantir que a mensagem de sucesso/erro apareça em algum lugar
    btn_add.click(fn=adicionar_saldo, inputs=[valor_add], outputs=[resultado_roleta, saldo_display])
    btn_reset.click(fn=resetar, outputs=[resultado_roleta, saldo_display])

if __name__ == "__main__":
    app.launch(share=True)
