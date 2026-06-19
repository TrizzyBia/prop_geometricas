import streamlit as st

st.title("Propriedades Geométricas")

st.write("Área da Seção Tranversal e Momentos de Inércia")
# ÁREA DA SEÇÃO TRANSVERSAL

# usei as siglas padrão
# cuidado quando for colocar número decimal, só aceita ponto e não vírgula


h = st.number_input('Altura interna da alma (mm)', min_value=1.0)
tw = st.number_input('Espessura da alma (mm)', min_value=1.0)
bfi = st.number_input('Largura da aba inferior (mm)', min_value=1.0)
tfi = st.number_input('Espessura da aba inferior (mm)', min_value=1.0)
bfs = st.number_input('Largura da aba superior (mm)', min_value=1.0)
tfs = st.number_input('Espessura da aba superior (mm)', min_value=1.0)


def area_aba_inf(tfi, bfi):
    return tfi * bfi

def area_aba_sup(tfs, bfs):
    return tfs * bfs

def area_alma(h, tw):
    return h * tw

def area_total(h, tw, bfi, tfi, bfs, tfs):
    total = area_alma(h, tw) + area_aba_inf(tfi, bfi) + area_aba_sup(tfs, bfs)
    return total


#CENTROIDE
#Adotando o eixo y no eixo de simetria do perfil, temos que calcular yc
#Adotando o eixo x coincidindo com a parte inferior do perfil, temos que xc=0

#Calculando o yc:
def y_c(h, tw, bfi, tfi, bfs, tfs):
    yc=(area_aba_inf(tfi, bfi)*tfi/2+area_alma(h, tw)*(tfi+h/2)+area_aba_sup(tfs, bfs)*(tfi+h+tfs/2))/area_total(h, tw, bfi, tfi, bfs, tfs)
    return(yc)


# MOMENTO DE INÉRCIA

# eixo y vertical no centro de massa da viga e eixo x horizontal no centro de massa da viga

def mi_eixoy(h, tw, bfi, tfi, bfs, tfs):
    Iabay_inf = tfi * bfi**3 / 12
    Ialmay = h * tw**3 / 12
    Iabay_sup = tfs * bfs**3 / 12
    Itotaly = Iabay_inf+Ialmay+Iabay_sup
    return Itotaly

def mi_eixox(h, tw, bfi, tfi, bfs, tfs, yc):
    d_abax_inf = yc - tfi/2
    d_almax = yc - (tfi + h/2)
    d_abax_sup = yc - (tfi + h + tfs/2)
    
    Iabax_inf = bfi * tfi**3 / 12 + area_aba_inf(tfi, bfi) * d_abax_inf**2
    Ialmax = tw * h**3 / 12 + area_alma(h, tw) * d_almax**2
    Iabax_sup = bfs * tfs**3 / 12 + area_aba_sup(tfs, bfs) * d_abax_sup**2

    Itotalx = Iabax_inf + Ialmax + Iabax_sup
   
    
    return Itotalx

if st.button('Calcular Propriedades'):
    area = area_total(h, tw, bfi, tfi, bfs, tfs)
    yc = y_c(h, tw, bfi, tfi, bfs, tfs)
    mix = mi_eixox(h, tw, bfi, tfi, bfs, tfs, yc)
    miy = mi_eixoy(h, tw, bfi, tfi, bfs, tfs)

    st.header('Resultados')
    st.write(f'Área da Seção Transversal = {area:.3f} mm²')
    st.write(f'Coordenada y do centróide = {yc:.3f} mm')
    st.write(f'Ix = {mix:.3f} mm⁴')
    st.write(f'Iy = {miy:.3f} mm⁴')
