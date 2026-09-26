# 🏷️ App Desconto: Sistema de Descontos Progressivos

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vendas](https://img.shields.io/badge/Descontos_&_Vendas-E53935?style=for-the-badge&logo=cashapp&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## 🎯 Objetivo do Projeto
O **App Descontos** é um sistema simples desenvolvido em terminal para automatizar a aplicação de descontos progressivos em uma loja online. Ele recebe o valor da compra do cliente e, baseado em regras pré-definidas, calcula automaticamente o percentual de desconto, o valor economizado e o preço final a pagar! 🛍️💰

## 💻 Linguagem Utilizada
- **Python** 🐍

## 🧮 Lógica e Fórmulas Utilizadas
O sistema aplica regras condicionais para determinar o percentual de desconto:
- **Compras abaixo de R$ 200,00:** 5% de desconto.
- **Compras entre R$ 200,00 e R$ 299,99:** 10% de desconto.
- **Compras a partir de R$ 300,00:** 15% de desconto.

O cálculo final é feito utilizando a seguinte fórmula padrão:

```python
valor_desconto = valor_compra * (desconto_percentual / 100)
valor_final = valor_compra - valor_desconto
```

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. Baixe os arquivos do projeto para uma pasta local.
3. Abra o terminal (ou prompt de comando).
4. Navegue até a pasta onde o arquivo se encontra e execute o seguinte comando:
   ```bash
   python app_descontos.py
   ```
   *(Nota: Se o seu arquivo tiver outro nome, substitua `app_descontos.py` pelo nome correto do arquivo salvo).*
5. Digite o valor da sua compra quando solicitado e veja o desconto acontecer! 🎉
