import streamlit as st

# Configurações da página - DEVE ser a primeira chamada Streamlit
st.set_page_config(
    page_title="Calculadora de Custos",
    page_icon="",
    layout="wide"
)

st.title('Calculadora de Custos de Produção')

# Função para validar entrada numérica
def validar_numero(valor, min_valor=0.0):
    try:
        numero = float(valor)
        if numero < min_valor:
            return False
        return True
    except (ValueError, TypeError):
        return False

# Adicionar CSS personalizado
st.markdown("""
    <style>
    .error-msg {
        color: red;
        font-size: 0.8em;
    }
    .success-msg {
        color: green;
        font-size: 1.2em;
        font-weight: bold;
    }
    .stColumn {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem;
    }
    @media (max-width: 768px) {
        .stColumn {
            margin: 0.5rem 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

try:
    # Criar três colunas para as seções principais
    col1, col2, col3 = st.columns(3)

    # Seção 1: Informações da Peça Bruta
    with col1:
        st.markdown('<div class="stColumn">', unsafe_allow_html=True)
        st.header('1. Peça Bruta')
        
        valor_bruto = st.number_input('Valor da peça (R$)', 
                                    min_value=0.0, 
                                    step=0.01,
                                    help="Insira o valor pago pela peça bruta")
        
        largura_bruta = st.number_input('Largura (cm)', 
                                       min_value=0.1,
                                       step=0.1,
                                       help="Insira a largura da peça bruta em centímetros")
        
        comprimento_bruto = st.number_input('Comprimento (cm)', 
                                          min_value=0.1,
                                          step=0.1,
                                          help="Insira o comprimento da peça bruta em centímetros")

        # Cálculo da área bruta com validação
        if largura_bruta > 0 and comprimento_bruto > 0:
            area_bruta = largura_bruta * comprimento_bruto
            st.write(f'Área total: {area_bruta:.2f} cm²')
            
            if valor_bruto > 0:
                custo_por_cm2 = valor_bruto / area_bruta
                st.write(f'Custo/cm²: R$ {custo_por_cm2:.4f}')
            else:
                st.warning('Insira um valor válido')
        else:
            st.warning('Insira dimensões válidas')
        st.markdown('</div>', unsafe_allow_html=True)

    # Seção 2: Custos de Processamento
    with col2:
        st.markdown('<div class="stColumn">', unsafe_allow_html=True)
        st.header('2. Processamento')
        
        custo_minuto = st.number_input('Custo/minuto (R$)', 
                                      min_value=0.0,
                                      step=0.01,
                                      help="Insira o custo por minuto da máquina")
        
        quantidade_pecas = st.number_input('Qtd. peças', 
                                         min_value=1,
                                         step=1,
                                         help="Insira a quantidade de peças a serem produzidas")
        
        tempo_producao = st.number_input('Tempo total (min)', 
                                       min_value=0.1,
                                       step=0.1,
                                       help="Insira o tempo total de produção em minutos")

        # Cálculo do custo de processamento com validação
        if tempo_producao > 0 and quantidade_pecas > 0:
            custo_processamento = custo_minuto * tempo_producao
            custo_processamento_por_peca = custo_processamento / quantidade_pecas
            st.write(f'Custo/peça: R$ {custo_processamento_por_peca:.2f}')
        else:
            st.warning('Insira valores válidos')
        st.markdown('</div>', unsafe_allow_html=True)

    # Seção 3: Dimensões Finais
    with col3:
        st.markdown('<div class="stColumn">', unsafe_allow_html=True)
        st.header('3. Peça Final')
        
        largura_final = st.number_input('Largura final (cm)', 
                                      min_value=0.1,
                                      step=0.1,
                                      help="Insira a largura final da peça em centímetros")
        
        comprimento_final = st.number_input('Comprimento final (cm)', 
                                         min_value=0.1,
                                         step=0.1,
                                         help="Insira o comprimento final da peça em centímetros")

        # Validação das dimensões finais
        if largura_final > largura_bruta or comprimento_final > comprimento_bruto:
            st.error('Dimensões finais não podem ser maiores que as brutas!')
        else:
            area_final = largura_final * comprimento_final
            st.write(f'Área final: {area_final:.2f} cm²')
            
            if valor_bruto > 0:
                custo_material_final = area_final * custo_por_cm2
                st.write(f'Custo material: R$ {custo_material_final:.2f}')
        st.markdown('</div>', unsafe_allow_html=True)

    # Seção 4: Custo Total e Preço de Venda
    st.header('4. Custo Total e Preço de Venda')
    
    # Calcular custo total apenas se todos os valores necessários estiverem válidos
    if (valor_bruto > 0 and area_final > 0 and 
        tempo_producao > 0 and quantidade_pecas > 0):
        
        custo_total = custo_material_final + custo_processamento_por_peca
        st.write(f'Custo total por peça: R$ {custo_total:.2f}')

        margem_lucro = st.slider('Margem de lucro desejada (%)', 
                                min_value=0,
                                max_value=500,
                                value=30,
                                help="Defina a margem de lucro desejada")
        
        preco_venda = custo_total * (1 + margem_lucro/100)
        
        st.markdown(f'<p class="success-msg">Preço de venda sugerido por peça: R$ {preco_venda:.2f}</p>', 
                   unsafe_allow_html=True)

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
            
        # Adicionar informações sobre o lote
        st.header('Informações do Lote')
        st.write(f'- Valor total do lote: R$ {(preco_venda * quantidade_pecas):.2f}')
        st.write(f'- Lucro total do lote: R$ {((preco_venda - custo_total) * quantidade_pecas):.2f}')
        
except Exception as e:
    st.error(f'Ocorreu um erro inesperado. Por favor, verifique os valores inseridos.')
    
# Adicionar footer com informações
st.markdown('---')
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
        Desenvolvido com ❤️ | Versão 1.0.0
    </div>
""", unsafe_allow_html=True)
