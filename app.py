import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="DevOps & Python",
    page_icon="🔧",
    layout="wide"
)


# Menu lateral
st.sidebar.title("🚀 Menu de Navegação")
pagina = st.sidebar.selectbox(
    "Escolha uma página:",
    ["🏗️ História do DevOps", "⚙️ Como Compilar Python", "🔄 Símbolo DevOps", "🚀 DevOps vs SRE"]
)

st.sidebar.markdown("---")
st.sidebar.info("Projeto feito com ❤️ usando Streamlit.")

# Página 1 - História do DevOps
if pagina == "🏗️ História do DevOps":
    st.title("📜 História do DevOps")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("👉 Onde tudo começou...")
        st.write("""
        O movimento **DevOps** surgiu oficialmente em 2009, buscando aproximar os times de desenvolvimento (**Dev**) e operações (**Ops**).
        
        Antes, os times trabalhavam de forma isolada, o que gerava:
        - Entregas demoradas
        - Muitos erros em produção
        - Dificuldade na comunicação

        O **DevOps** promove:
        - 🚀 Entregas contínuas
        - 🤝 Colaboração entre equipes
        - 🔄 Automação de processos
        - 📈 Feedback rápido e melhoria contínua
        """)

    
# Página 2 - Como Compilar Python
elif pagina == "⚙️ Como Compilar Python":
    st.title("⚙️ Como funciona a compilação no Python")
    st.subheader("🧠 Python é compilado ou interpretado?")
    st.markdown("""
    🔹 **Python é uma linguagem interpretada, mas passa por uma etapa de compilação para bytecode.**

    O processo acontece assim:

    1. ✅ O código fonte é lido e convertido em uma **árvore sintática**.
    2. ✅ Ele é então **compilado em bytecode** (`.pyc`).
    3. ✅ O bytecode é executado pela **Python Virtual Machine (PVM)**.

    💡 Você pode criar executáveis usando ferramentas como:
    - 👉 **PyInstaller**
    - 👉 **Cython**
    - 👉 **Nuitka**
    """)

# Página 3 - Símbolo DevOps
elif pagina == "🔄 Símbolo DevOps":
    st.title("🔄 O Símbolo do DevOps")
    st.subheader("♾️ O ciclo infinito da melhoria contínua")
    st.write("""
    O símbolo do **DevOps** é um infinito ♾️, que representa um ciclo contínuo de:

    - Planejamento
    - Desenvolvimento
    - Construção
    - Teste
    - Entrega
    - Operação
    - Monitoramento
    - Feedback

    🔁 Este ciclo nunca para, garantindo agilidade, qualidade e evolução constante dos sistemas.
    """)

   #img = Image.open("devops_symbol.png")
   # st.image(img, use_column_width=True, caption="Símbolo clássico do DevOps")

# Página 4 - DevOps vs SRE
elif pagina == "🚀 DevOps vs SRE":
    st.title("🚀 DevOps vs SRE")
    st.subheader("👨‍💻 Duas abordagens que se complementam")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔸 **DevOps**")
        st.markdown("""
        - 🎯 Cultura, filosofia e práticas.
        - 🔧 Foco na **automação**, **colaboração** e **entregas contínuas**.
        - 📦 Menos definição formal, mais um **mindset**.
        - 🏗️ Cria as bases para ciclos de desenvolvimento ágeis.
        """)

    with col2:
        st.markdown("### 🔹 **SRE (Site Reliability Engineering)**")
        st.markdown("""
        - 🔥 Criado pelo Google.
        - 🏗️ Aplicação de **engenharia de software nas operações**.
        - 🎯 Foco na **confiabilidade, estabilidade e escalabilidade**.
        - 📊 Usa métricas como:
          - **SLI** (Indicadores)
          - **SLO** (Objetivos)
          - **Error Budget** (Orçamento de erros)
        """)

    st.markdown("---")
    st.markdown("""
    ### 🚀 **Resumo prático:**  
    - DevOps é **cultura**.  
    - SRE é uma **implementação técnica dessa cultura**, com foco em confiabilidade.
    """)

st.markdown("---")
st.caption("🧠 CANEPA - UTC | © 2025")
