import streamlit as st

st.title('Calculadora de Custos de Produção')

# Seção 1: Informações da Peça Bruta
st.header('1. Informações da Peça Bruta')
valor_bruto = st.number_input('Valor da peça bruta (R$)', min_value=0.0, step=0.01)
largura_bruta = st.number_input('Largura da peça bruta (cm)', min_value=0.0, step=0.1)
comprimento_bruto = st.number_input('Comprimento da peça bruta (cm)', min_value=0.0, step=0.1)

# Cálculo da área bruta
area_bruta = largura_bruta * comprimento_bruto
st.write(f'Área total da peça bruta: {area_bruta:.2f} cm²')
custo_por_cm2 = valor_bruto / area_bruta if area_bruta > 0 else 0
st.write(f'Custo por cm²: R$ {custo_por_cm2:.4f}')

# Seção 2: Custos de Processamento
st.header('2. Custos de Processamento')
custo_minuto = st.number_input('Custo da máquina por minuto (R$)', min_value=0.0, step=0.01)
quantidade_pecas = st.number_input('Quantidade de peças', min_value=1, step=1)
tempo_producao = st.number_input('Tempo de produção por lote (minutos)', min_value=0.0, step=0.1)

# Cálculo do custo de processamento
custo_processamento = custo_minuto * tempo_producao
custo_processamento_por_peca = custo_processamento / quantidade_pecas
st.write(f'Custo de processamento por peça: R$ {custo_processamento_por_peca:.2f}')

# Seção 3: Dimensões Finais
st.header('3. Dimensões da Peça Final')
largura_final = st.number_input('Largura final da peça (cm)', min_value=0.0, step=0.1)
comprimento_final = st.number_input('Comprimento final da peça (cm)', min_value=0.0, step=0.1)

# Cálculo da área final e custo do material
area_final = largura_final * comprimento_final
custo_material_final = area_final * custo_por_cm2
st.write(f'Área final da peça: {area_final:.2f} cm²')
st.write(f'Custo do material final: R$ {custo_material_final:.2f}')

# Seção 4: Custo Total e Preço de Venda
st.header('4. Custo Total e Preço de Venda')
custo_total = custo_material_final + custo_processamento_por_peca
st.write(f'Custo total por peça: R$ {custo_total:.2f}')

margem_lucro = st.slider('Margem de lucro desejada (%)', min_value=0, max_value=500, value=30)
preco_venda = custo_total * (1 + margem_lucro/100)

st.success(f'Preço de venda sugerido por peça: R$ {preco_venda:.2f}')

# Resumo final
st.header('Resumo do Cálculo')
col1, col2 = st.columns(2)

with col1:
    st.write('**Custos:**')
    st.write(f'- Material: R$ {custo_material_final:.2f}')
    st.write(f'- Processamento: R$ {custo_processamento_por_peca:.2f}')
    st.write(f'- Total: R$ {custo_total:.2f}')

with col2:
    st.write('**Venda:**')
    st.write(f'- Margem: {margem_lucro}%')
    st.write(f'- Lucro por peça: R$ {(preco_venda - custo_total):.2f}')
    st.write(f'- Preço final: R$ {preco_venda:.2f}')
