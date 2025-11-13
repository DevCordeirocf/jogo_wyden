# 🎰 Cassino Wyden

Este projeto é uma simulação simples de cassino desenvolvida em Python utilizando a biblioteca **Gradio** para a interface web. Foi criado como parte de um trabalho acadêmico.

## 🎲 Jogos Disponíveis

O cassino atualmente oferece os seguintes jogos:

1.  **Roleta:** Aposte na cor (Vermelho ou Preto).
2.  **Caça-Níquel:** Gire os slots e tente a sorte com combinações de símbolos.
3.  **Dados:** Aposte na soma dos dados, se o resultado será Par/Ímpar ou se será 7/11.
4.  **Cara ou Coroa:** Aposta simples para dobrar o valor.

Todos os jogos compartilham um saldo inicial de R$ 1000,00, que pode ser adicionado ou resetado a qualquer momento.

## 🛠️ Como Executar

Para rodar o Cassino Wyden localmente, siga os passos abaixo:

### Pré-requisitos

Você precisa ter o **Python 3** instalado em seu sistema.

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/DevCordeirocf/jogo_wyden
    cd jogo_wyden
    ```

2.  **Instale as dependências:**
    ```bash
    pip install gradio
    ```

### Execução

Execute o script principal:

```bash
python cassino.py
```

O Gradio irá iniciar o servidor e fornecer um link local e um link público temporário para acessar a interface do cassino no seu navegador.
