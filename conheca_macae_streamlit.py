import streamlit as st
from IBGE_figs import *

def kpi_card(title, info, width=250):
    st.markdown(
        f"""
        <style>
            .kpi-card {{
                background-color: #3498db;
                color: #fff;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                width: {width}px;
                margin-right: 50px
            }}
            .kpi-title {{
                font-size: 18px;
                font-weight: bold;
                
            }}
            .kpi-info {{
                font-size: 24px;
            }}
        </style>
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-info">{info}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
def main():
    st.markdown("<h1 style='text-align: center;'>Conheça Macaé - Informações Sociais</h1><hr>", unsafe_allow_html=True)
    
    st.write("""Bem-vindo à encantadora cidade de Macaé, localizada no interior do Rio de Janeiro. 
        Conhecida por sua rica história e deslumbrante paisagem litorânea, Macaé destaca-se como 
        um importante polo econômico na região. Suas praias deslumbrantes, como a Praia dos 
        Cavaleiros, atraem visitantes em busca de tranquilidade e lazer. Além disso, a cidade é 
        notável por seu papel significativo na indústria petrolífera, sendo um centro estratégico 
        para o desenvolvimento e análise de recursos energéticos. Neste projeto, exploraremos 
        diversos gráficos e dados que oferecerão insights valiosos sobre a dinâmica e o potencial 
        da Princesinha do Atlântico."""
    )
    
    col_cor_graph1, col_cor_graph2 = st.columns(2)
    col_cor_graph1.plotly_chart(macae_cor_fig, use_container_width=True)
    col_cor_graph2.plotly_chart(brasil_cor_fig, use_container_width=True)
    
    st.write("""Macaé possui uma população residente ligeiramente menor de amarelos e indigenas se comparados
                com o panorama brasileiro. A distribuição de negros e brancos também varia em mais de cinco pontos percentuais,
                com a população negra sendo 7.2% mais populosa, e a população branca sendo 6.1% menos populosa
                na Capital Nacional da Energia.
                """)
    st.write("""A população vem estado em constante crescimento, quase dobrando em quantidade nos ultimos vinte anos,
                seu crescimento está diretamente ligado ao mercado petrolifero que atrai cada vez mais trabalhadores das 
                mais diversas regiões do Brasil em busca de oportunidades que a industria multibilionaria proporciona.
                """)
    
    st.plotly_chart(macae_pop_fig)
    
    
    col_txt_etaria, col_graph_etaria = st.columns(2)
    with col_txt_etaria:
        st.markdown("<br><br>",unsafe_allow_html=True)
        st.write("""A distribuição entre a população macaense que se identifica como homens ou mulheres é uniforme para todas
                                as idades, com a população feminina ultrapassando por pouco a masculina na maioria dos casos.
                                """)
        st.write("""Existe uma concentração maior de residentes entre os 30 e 45 anos, mostrando o envelhecimento gradual
                                da Capital da Energia. Entretanto, seu Indice de Envelhecimento ainda se encontra em 40.58, ou seja, para 
                                cada 100 pessoas de 15 anos ou menos, há cerca de 40 de 60 anos ou mais.
                                """)
        
    with col_graph_etaria:
        st.plotly_chart(piramide_etaria_fig)
    
    col_card_1, _col_card_2,col_card_3, _col_card_4,col_card_5 = st.columns(5)
    with col_card_1:
        kpi_card("Indice de Envelhecimento","40.58")
    
    with col_card_3:
        kpi_card("IDH","0.76")
    
    with col_card_5:
        kpi_card("Índice de GINI","0.56")
    
    
    
    st.plotly_chart(sun_pop_fig)
    
    

if __name__ == "__main__":
    main()