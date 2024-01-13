import streamlit as st
from IBGE_figs import *

def main():
    st.markdown("<h1 style='text-align: center;'>Conheça Macaé - Informações Sociais</h1><hr>", unsafe_allow_html=True)
    
    st.markdown("""Bem-vindo à encantadora cidade de Macaé, localizada no interior do Rio de Janeiro. 
        Conhecida por sua rica história e deslumbrante paisagem litorânea, Macaé destaca-se como 
        um importante polo econômico na região. Suas praias deslumbrantes, como a Praia dos 
        Cavaleiros, atraem visitantes em busca de tranquilidade e lazer. Além disso, a cidade é 
        notável por seu papel significativo na indústria petrolífera, sendo um centro estratégico 
        para o desenvolvimento e análise de recursos energéticos. Neste projeto, exploraremos 
        diversos gráficos e dados que oferecerão insights valiosos sobre a dinâmica e o potencial 
        da Princesinha do Atlântico."""
    )
    
    col1, col2 = st.columns(2)
    col1.plotly_chart(macae_cor_fig, use_container_width=True)
    col2.plotly_chart(brasil_cor_fig, use_container_width=True)
    
    st.markdown("""Macaé possui uma população residente ligeiramente menor de amarelos e indigenas se comparados
                com o panorama brasileiro. A distribuição de negros e brancos também varia em mais de cinco pontos percentuais,
                com a população negra sendo 7.2% mais populosa, e a população branca sendo 6.1% menos populosa
                na Capital Nacional da Energia.
                """)
    
    
    
    
    #st.dataframe(macae_population_df)
    #st.dataframe(df_dist_idade_sexo)
    #st.dataframe(macae_cor_fig)
    st.plotly_chart(macae_pop_fig)
    st.plotly_chart(sun_pop_fig)
    
    

if __name__ == "__main__":
    main()