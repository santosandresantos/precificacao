# Calculadora de Custos de Produção

Uma aplicação Streamlit para calcular custos de produção e preço de venda de peças, considerando:
- Custo do material bruto
- Dimensões iniciais e finais
- Custo de processamento
- Margem de lucro desejada

## Como usar

1. Insira o valor e dimensões da peça bruta
2. Forneça o custo da máquina por minuto
3. Especifique a quantidade de peças e tempo de produção
4. Insira as dimensões finais da peça
5. Ajuste a margem de lucro desejada
6. O programa calculará automaticamente o preço de venda sugerido

## Executando localmente

```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
streamlit run calculo_custo.py
```
