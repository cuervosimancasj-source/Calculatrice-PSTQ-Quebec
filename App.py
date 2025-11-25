import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA / CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Calculadora PSTQ (Arrima Score)", page_icon="⚜️", layout="wide")

st.title("⚜️ Calculadora de Puntaje de CLASIFICACIÓN Arrima (PSTQ)")
st.markdown("""
**Esta herramienta simula el Score de Classement de Arrima.**
El puntaje final (máx. ~1350) se usa para el ranking de invitaciones. El corte de invitación es variable y alto (ej: 600+).
*Cet outil simule le Score de Classement Arrima (PSTQ). Le seuil d'invitation est variable.*
""")

# --- VARIABLES DE PUNTAJE Y CORTE (Máx. Total ~1350 pts) ---
pts_total = 0

# Establecemos un puntaje de referencia alto para la comparación
PUNTAJE_REFERENCIA_ALTO = 600

# --- BARRA LATERAL: ESTADO CIVIL Y MONETIZACIÓN ---
with st.sidebar:
    st.header("Perfil del Solicitante / Profil")
    estado_civil = st.radio(
        "¿Cuál es tu estado civil? / Quel est votre état civil ?",
        ("Soltero(a) / Seul", "Casado(a) o Pareja de hecho / En couple")
    )
    
    es_casado = "Casado" in estado_civil
    
    st.info(f"ℹ️ El puntaje de invitación **VARÍA** (generalmente **>{PUNTAJE_REFERENCIA_ALTO}**)")
    
    # --- MONETIZACIÓN (CORREGIDA) ---
    st.divider()
    st.write("☕ **Apoya el proyecto / Soutenir ce projet:**")
    st.write("Si esta herramienta te ayudó, ¡invítame a un café!")
    
    # ENLACE CORREGIDO CON TU USUARIO Y COMILLAS CORRECTAS
    st.markdown("[**☕ Invítame un café (Donar)**](https://www.buymeacoffee.com/CalculatricePSTQQuebec)", unsafe_allow_html=True)
    
    st.write("---")
    st.write("¿Necesitas mejorar tu francés?")
    st.markdown("[📚 Curso de Francés Recomendado](https://www.google.com)", unsafe_allow_html=True)


# ==========================================
# SECCIÓN A: CAPITAL HUMANO (Máx. 590 pts)
# ==========================================
st.header("A. Capital Humano (Máx. 590 pts)")

# --- 1. IDIOMAS - FRANCÉS (Máx. 380 pts) ---
st.subheader("1. Francés / Français (Máx. 380 pts)")
st.caption("Los puntos se basan en exámenes oficiales (TEF/TCF).")
col_f1, col_f2 = st.columns(2)

with col_f1:
    fr_oral = st.selectbox("Expresión Oral (Máx. 100 pts)", ["Sin examen", "B2 (80 pts)", "C1 (90 pts)", "C2 (100 pts)"], key='fr_oral')
    pts_oral = 0
    if "C2" in fr_oral: pts_oral = 100
    elif "C1" in fr_oral: pts_oral = 90
    elif "B2" in fr_oral: pts_oral = 80
    
    fr_escucha = st.selectbox("Comprensión Auditiva (Máx. 100 pts)", ["Sin examen", "B2 (80 pts)", "C1 (90 pts)", "C2 (100 pts)"], key='fr_escucha')
    pts_escucha = 0
    if "C2" in fr_escucha: pts_escucha = 100
    elif "C1" in fr_escucha: pts_escucha = 90
    elif "B2" in fr_escucha: pts_escucha = 80

with col_f2:
    fr_escrito = st.selectbox("Expresión Escrita (Máx. 90 pts)", ["Sin examen", "B2 (70 pts)", "C1 (80 pts)", "C2 (90 pts)"], key='fr_escrito')
    pts_escrito = 0
    if "C2" in fr_escrito: pts_escrito = 90
    elif "C1" in fr_escrito: pts_escrito = 80
    elif "B2" in fr_escrito: pts_escrito = 70

    fr_lectura = st.selectbox("Comprensión Lectora (Máx. 90 pts)", ["Sin examen", "B2 (70 pts)", "C1 (80 pts)", "C2 (90 pts)"], key='fr_lectura')
    pts_lectura = 0
    if "C2" in fr_lectura: pts_lectura = 90
    elif "C1" in fr_lectura: pts_lectura = 80
    elif "B2" in fr_lectura: pts_lectura = 70

pts_fr_total = pts_oral + pts_escucha + pts_escrito + pts_lectura
st.success(f"Puntos Francés Total: **{pts_fr_total}**")
pts_total += pts_fr_total

# --- 2. IDIOMAS - INGLÉS (Máx. 40 pts) ---
st.subheader("2. Inglés / English (Máx. 40 pts)")
ing_oral = st.slider("Nivel de Inglés (CLB/IELTS equivalente)", 0, 40, 0, step=10, key='ing_oral')
pts_ing = ing_oral
st.success(f"Puntos Inglés: **{pts_ing}**")
pts_total += pts_ing

# --- 3. EDAD (Máx. 110 pts) ---
st.subheader("3. Edad / Âge (Máx. 110 pts)")
edad = st.number_input("Edad actual", 18, 60, 29, key='edad_arrima')

if 25 <= edad <= 35: pts_edad = 110
elif 20 <= edad <= 24: pts_edad = 90
elif 36 <= edad <= 40: pts_edad = 70
elif 41 <= edad <= 45: pts_edad = 40
else: pts_edad = 0

st.success(f"Puntos Edad: **{pts_edad}**")
pts_total += pts_edad

# --- 4. EXPERIENCIA (Máx. 80 pts) ---
st.subheader("4. Experiencia Laboral (Máx. 80 pts)")
st.caption("Experiencia a tiempo completo en los últimos 5 años (TEER 0, 1, 2, 3).")
meses_exp = st.slider("Meses de experiencia", 0, 60, 24, key='exp_arrima')

if meses_exp >= 48: pts_exp = 80
elif meses_exp >= 24: pts_exp = 60
elif meses_exp >= 12: pts_exp = 30
else: pts_exp = 0

st.success(f"Puntos Experiencia: **{pts_exp}**")
pts_total += pts_exp

# ==========================================
# SECCIÓN B: NECESIDADES DE QUEBEC (Máx. 760 pts)
# ==========================================
st.header("B. Necesidades de Quebec (Máx. 760 pts)")

# --- 5. ÁREA DE FORMACIÓN (Máx. 140 pts) ---
st.subheader("5. Área de Formación (Domaine de formation) (Máx. 140 pts)")
st.caption("Los puntos se asignan según la demanda de tu profesión en la lista del MIFI.")
area_formacion = st.selectbox(
    "Selecciona el Nivel de Prioridad de tu Área de Formación",
    options=[("Sección A (Prioritaria, ej: TI/Salud)", 140), ("Sección B", 100), ("Sección C", 60), ("Sección D/Otros", 20)],
    format_func=lambda x: x[0]
)
pts_area = area_formacion[1]
st.success(f"Puntos Área de Formación: **{pts_area}**")
pts_total += pts_area

# --- 6. OFERTA DE EMPLEO (Máx. 180 pts) ---
st.subheader("6. Oferta de Empleo Validada (VJO) (Máx. 180 pts)")
oferta = st.selectbox(
    "¿Tienes una oferta de empleo validada por el MIFI?",
    options=[("No", 0), ("Sí, en Montreal (140 pts)", 140), ("Sí, fuera de Montreal (180 pts)", 180)], 
    format_func=lambda x: x[0]
)
pts_oferta = oferta[1]
st.success(f"Puntos Oferta de Empleo: **{pts_oferta}**")
pts_total += pts_oferta

# --- 7. HIJOS (ENFANTS) (Máx. 80 pts) ---
st.subheader("7. Hijos / Enfants (Máx. 80 pts)")
st.caption("40 puntos por cada hijo dependiente menor de 22 años.")
num_hijos = st.number_input("Número de hijos menores de 22 años", 0, 5, 0, key='num_hijos_arrima')
pts_hijos = num_hijos * 40 # 40 pts por hijo
if pts_hijos > 80: pts_hijos = 80 # Máximo 80 pts (dos hijos)
st.success(f"Puntos por Hijos: **{pts_hijos}**")
pts_total += pts_hijos


# ==========================================
# SECCIÓN C: CÓNYUGE (CONJOINT) - SOLO SI APLICA
# ==========================================
if es_casado:
    st.header("C. Factores del Cónyuge / Facteurs du Conjoint (Máx. 180 pts)")
    st.info("La pareja aporta puntos, principalmente por el francés.")
    
    # Francés Cónyuge (Máx 180 pts)
    fr_c_oral = st.slider("Francés Oral Cónyuge (Máx. 100 pts)", 0, 100, 0, step=20, key='fr_c_oral')
    fr_c_escrito = st.slider("Francés Escrito Cónyuge (Máx. 80 pts)", 0, 80, 0, step=20, key='fr_c_escrito')
    
    pts_fr_c_total = fr_c_oral + fr_c_escrito
    
    # Otros factores (Edad, Formación, etc., son menos en el Arrima Score)
    pts_conyuge_total = pts_fr_c_total
    
    st.success(f"Puntos aportados por Cónyuge: **{pts_conyuge_total}**")
    pts_total += pts_conyuge_total

# --- FACTOR ADICIONAL: EXPERIENCIA EN QUEBEC (Máx. 180 pts) ---
st.header("D. Experiencia en Quebec (Máx. 180 pts)")
exp_qc = st.selectbox(
    "Experiencia o Estudios en Québec",
    options=[("Ninguna", 0), ("Trabajo (12+ meses, TEER 0/1/2/3)", 180), ("Estudios (18+ meses)", 180), ("Trabajo o Estudios (6-11 meses)", 50)],
    format_func=lambda x: x[0]
)
pts_exp_qc = exp_qc[1]
st.success(f"Puntos Experiencia/Estudios QC: **{pts_exp_qc}**")
pts_total += pts_exp_qc


# ==========================================
# RESULTADOS FINALES
# ==========================================
st.divider()
st.subheader("📊 RESULTADO FINAL (RÉSULTAT FINAL)")

col_res1, col_res2 = st.columns(2)

with col_res1:
    st.metric(label="Tu Puntaje de CLASIFICACIÓN Total", value=f"{pts_total} pts")
    st.metric(label="Puntaje Máximo Posible", value=f"~1350 pts")

with col_res2:
    st.write("#### Análisis de Ranking:")
    
    st.markdown(f"**Puntaje de Referencia para Invitación (Ejemplo): {PUNTAJE_REFERENCIA_ALTO} pts**")
    
    if pts_total >= PUNTAJE_REFERENCIA_ALTO:
        st.success("✅ **PERFIL MUY COMPETITIVO:** Tu puntaje es alto y tienes buenas probabilidades.")
        st.balloons()
    else:
        st.error(f"⚠️ **PERFIL NO GARANTIZADO:** Tu puntaje (Arrima) necesita mejorar para ser invitado.")
        st.markdown(f"**Mejora:** Necesitas enfocarte en el **Francés (Máx. 380 pts)** o conseguir una **Oferta de Empleo (Máx. 180 pts)**.")

# Disclaimer final
st.caption("""
---
**Nota Legal:** Esta es una SIMULACIÓN del puntaje de CLASIFICACIÓN Arrima (PSTQ). El puntaje real de corte para las invitaciones es variable y fijado por el MIFI.
*Avertissement : Ceci est une simulation du score de classement Arrima (PSTQ). Le seuil d'invitation est variable.*
""")
