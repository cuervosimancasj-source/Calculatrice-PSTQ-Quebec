import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA / CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Calculadora Completa PSTQ Québec", page_icon="⚜️", layout="wide")

st.title("⚜️ Calculadora Avanzada de Puntos Québec (PSTQ)")
st.markdown("""
**Esta herramienta simula la 'Grille de sélection' oficial.**
Calcula el puntaje para el solicitante principal y, si aplica, para su cónyuge.
*Cet outil simule la Grille de sélection officielle.*
""")

# --- BARRA LATERAL: ESTADO CIVIL / BARRE LATÉRALE : ÉTAT CIVIL ---
with st.sidebar:
    st.header("Perfil del Solicitante / Profil")
    estado_civil = st.radio(
        "¿Cuál es tu estado civil? / Quel est votre état civil ?",
        ("Soltero(a) / Seul", "Casado(a) o Pareja de hecho / En couple")
    )
    
    es_casado = "Casado" in estado_civil
    
    st.info("ℹ️ El puntaje de corte cambia si estás solo o en pareja.")
    
    # Monetización simulada
    st.divider()
    st.write("☕ **Apoya el proyecto:**")
    st.markdown("[Donar un café](https://www.buymeacoffee.com)", unsafe_allow_html=True)

# --- VARIABLES DE PUNTAJE ---
pts_total = 0
pts_corte_empleabilidad = 43 if not es_casado else 52
pts_corte_seleccion = 50 if not es_casado else 59

# ==========================================
# SECCIÓN 1: FORMACIÓN (FORMATION)
# ==========================================
st.header("1. Formación / Formation")
col1, col2 = st.columns(2)

with col1:
    nivel_estudios = st.selectbox(
        "Nivel de escolaridad / Niveau de scolarité",
        options=[
            ("Doctorado", 14),
            ("Maestría / Maîtrise", 12),
            ("Licenciatura (3+ años) / 1er cycle 3+ ans", 10),
            ("Licenciatura (2 años) / 1er cycle 2 ans", 6),
            ("Técnico (DEC) / Collégial technique 3 ans", 8),
            ("Técnico (AEC) / Collégial technique 2 ans", 6),
            ("Secundaria profesional (DEP) / Secondaire pro", 6),
            ("Secundaria general / Secondaire général", 2)
        ],
        format_func=lambda x: x[0]
    )
    pts_formacion = nivel_estudios[1]

with col2:
    st.markdown("**Área de Formación (Domaine de formation)**")
    st.markdown("""
    *Nota: Esto depende de tu carrera y demanda (Sección A, B, C...).*
    *Note : Cela dépend de votre domaine et de la demande.*
    """)
    area_formacion = st.selectbox(
        "Puntos por Área de Formación",
        options=[("Sección A (Prioritario)", 12), ("Sección B", 9), ("Sección C", 6), ("Sección D", 2), ("Sección E/F/G", 0)],
        format_func=lambda x: x[0]
    )
    pts_area = area_formacion[1]

st.success(f"Puntos Formación: **{pts_formacion + pts_area}**")
pts_total += pts_formacion + pts_area

# ==========================================
# SECCIÓN 2: EXPERIENCIA (EXPÉRIENCE)
# ==========================================
st.header("2. Experiencia Laboral / Expérience")
st.caption("Experiencia calificada en los últimos 5 años (TEER 0, 1, 2, 3).")
meses_exp = st.slider("Meses de experiencia / Mois d'expérience", 0, 60, 24)

if meses_exp >= 48: pts_exp = 8
elif meses_exp >= 24: pts_exp = 6
elif meses_exp >= 12: pts_exp = 4
else: pts_exp = 0

st.success(f"Puntos Experiencia: **{pts_exp}**")
pts_total += pts_exp

# ==========================================
# SECCIÓN 3: EDAD (ÂGE)
# ==========================================
st.header("3. Edad / Âge")
edad = st.number_input("Edad actual / Âge actuel", 18, 60, 29)

if 18 <= edad <= 35: pts_edad = 16
elif edad == 36: pts_edad = 14
elif edad == 37: pts_edad = 12
elif edad == 38: pts_edad = 10
elif edad == 39: pts_edad = 8
elif edad == 40: pts_edad = 6
elif edad == 41: pts_edad = 4
elif edad == 42: pts_edad = 2
else: pts_edad = 0

st.success(f"Puntos Edad: **{pts_edad}**")
pts_total += pts_edad

# ==========================================
# SECCIÓN 4: IDIOMAS (LANGUES)
# ==========================================
st.header("4. Idiomas / Langues")
st.caption("Francés (Máx 16) + Inglés (Máx 6)")

# Francés
col_f1, col_f2 = st.columns(2)
with col_f1:
    fr_oral = st.selectbox("Francés: Comprensión y Expresión Oral", ["Principiante", "B1", "B2 (Intermedio Alto)", "C1/C2 (Avanzado)"])
    pts_fr_oral = 0
    if "C1" in fr_oral: pts_fr_oral = 14
    elif "B2" in fr_oral: pts_fr_oral = 10
    elif "B1" in fr_oral: pts_fr_oral = 4
    
with col_f2:
    fr_escrito = st.selectbox("Francés: Comprensión y Expresión Escrita", ["Principiante", "B1", "B2", "C1/C2"])
    pts_fr_escrito = 0
    if "C1" in fr_escrito: pts_fr_escrito = 2
    elif "B2" in fr_escrito: pts_fr_escrito = 1

pts_fr_total = pts_fr_oral + pts_fr_escrito

# Inglés
ing_oral = st.checkbox("¿Tienes inglés avanzado (IELTS 5.0+ / CLB 5+)?")
pts_ing = 6 if ing_oral else 0

st.success(f"Puntos Idiomas: **{pts_fr_total + pts_ing}**")
pts_total += pts_fr_total + pts_ing

# ==========================================
# SECCIÓN 5: ESTANCIA Y FAMILIA (SÉJOUR ET FAMILLE)
# ==========================================
st.header("5. Estancia y Familia en Quebec / Séjour et Famille")
col_fam1, col_fam2 = st.columns(2)

with col_fam1:
    estancia = st.selectbox(
        "Estancias en Quebec / Séjours au Québec",
        options=[
            ("Sin estancia / Aucune", 0),
            ("Estudios o Trabajo (6+ meses)", 5),
            ("Estudios o Trabajo (3-6 meses)", 5), # Simplificado, a veces varía
            ("Visita turística (>2 semanas)", 1)
        ],
        format_func=lambda x: x[0]
    )
    pts_estancia = estancia[1]

with col_fam2:
    familia = st.selectbox(
        "Familia en Quebec (Residente/Ciudadano)",
        options=[("No", 0), ("Cónyuge, padre, hijo, hermano/a, abuelo/a", 3)],
        format_func=lambda x: x[0]
    )
    pts_familia = familia[1]

pts_total += pts_estancia + pts_familia

# ==========================================
# SECCIÓN 6: CÓNYUGE (CONJOINT) - SOLO SI APLICA
# ==========================================
if es_casado:
    st.header("6. Factores del Cónyuge / Facteurs du Conjoint")
    st.info("Al declarar pareja, el puntaje necesario para aprobar sube.")
    
    col_c1, col_c2, col_c3 = st.columns(3)
    
    with col_c1:
        # Edad cónyuge
        edad_c = st.number_input("Edad Cónyuge", 18, 65, 30)
        if 18 <= edad_c <= 35: pts_edad_c = 3
        elif edad_c == 36: pts_edad_c = 2
        elif edad_c == 37: pts_edad_c = 1
        else: pts_edad_c = 0
        st.write(f"Pts Edad: {pts_edad_c}")

    with col_c2:
        # Educación cónyuge
        edu_c = st.selectbox("Educación Cónyuge", ["Universitario (3+ años)", "Técnico/Otros", "Secundaria"], index=1)
        if "Universitario" in edu_c: pts_edu_c = 3 # Simplificado
        elif "Técnico" in edu_c: pts_edu_c = 2
        else: pts_edu_c = 1
        st.write(f"Pts Edu: {pts_edu_c}")
        
        # Área formación cónyuge
        area_c = st.selectbox("Área Formación Cónyuge", ["Sección A (Prioritaria)", "Sección B", "Otras"], index=2)
        pts_area_c = 4 if "A" in area_c else (3 if "B" in area_c else 0)
        st.write(f"Pts Área: {pts_area_c}")

    with col_c3:
        # Francés cónyuge
        fr_c = st.selectbox("Francés Oral Cónyuge", ["Avanzado (B2+)", "Intermedio", "Básico"])
        if "Avanzado" in fr_c: pts_fr_c = 3 # Máximo suele ser 3 o 6 según versión
        else: pts_fr_c = 0
        st.write(f"Pts Francés: {pts_fr_c}")

    pts_conyuge_total = pts_edad_c + pts_edu_c + pts_area_c + pts_fr_c
    st.success(f"Puntos aportados por Cónyuge: **{pts_conyuge_total}**")
    pts_total += pts_conyuge_total

# ==========================================
# SECCIÓN 7: OFERTA DE EMPLEO (OFFRE D'EMPLOI)
# ==========================================
st.header("7. Oferta de Empleo Validada (VJO)")
oferta = st.selectbox(
    "¿Tienes una oferta de empleo validada?",
    options=[("No", 0), ("Sí, en Montreal", 8), ("Sí, fuera de Montreal", 14)], # Valores aprox
    format_func=lambda x: x[0]
)
pts_oferta = oferta[1]
st.success(f"Puntos Oferta: **{pts_oferta}**")
pts_total += pts_oferta

# ==========================================
# SECCIÓN 8: HIJOS (ENFANTS)
# ==========================================
st.header("8. Hijos / Enfants")
tiene_hijos = st.checkbox("¿Tienes hijos?")
pts_hijos = 0

if tiene_hijos:
    st.write("Ingresa la edad de cada hijo:")
    num_hijos = st.number_input("Número de hijos", 1, 10, 1)
    
    for i in range(num_hijos):
        edad_hijo = st.number_input(f"Edad hijo {i+1}", 0, 22, 5, key=f"hijo_{i}")
        if edad_hijo <= 12:
            pts_hijos += 4
        elif 13 <= edad_hijo <= 21:
            pts_hijos += 2
            
st.success(f"Puntos por Hijos: **{pts_hijos}**")
pts_total += pts_hijos

# ==========================================
# SECCIÓN 9: AUTONOMÍA FINANCIERA
# ==========================================
st.header("9. Autonomía Financiera")
finanzas = st.checkbox("¿Firmarás el contrato de autonomía financiera? (1 pto)")
pts_finanzas = 1 if finanzas else 0
pts_total += pts_finanzas

# ==========================================
# RESULTADOS FINALES
# ==========================================
st.divider()
st.subheader("📊 RESULTADO FINAL (RÉSULTAT FINAL)")

col_res1, col_res2 = st.columns(2)

with col_res1:
    st.metric(label="Tu Puntaje Total", value=f"{pts_total} pts")

with col_res2:
    st.write("#### Análisis:")
    
    # Corte de Empleabilidad (Sin hijos, sin oferta, factores básicos)
    # Corte de Selección (Total)
    
    umbral = 59 if es_casado else 50
    st.write(f"Umbral de aprobación (CSQ): **{umbral} puntos** (aprox)")
    
    if pts_total >= umbral:
        st.success("✅ **ELIGIBLE:** Superas el umbral de selección preliminar.")
        st.balloons()
    else:
        st.error(f"❌ **NO ELIGIBLE AÚN:** Te faltan {umbral - pts_total} puntos.")
        st.markdown("**Consejo:** Mejora tu nivel de francés o consigue una oferta de trabajo.")

# Disclaimer final
st.caption("""
---
**Nota Legal:** Esta aplicación es una simulación basada en la 'Grille de sélection' del MIFI. 
Las leyes de inmigración cambian. No utilizar para procesos legales oficiales.
*Avertissement : Cette application est une simulation.*
""")
