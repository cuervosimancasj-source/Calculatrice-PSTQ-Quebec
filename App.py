import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Calculadora PSTQ - Escala 1350", page_icon="⚜️", layout="centered")

# --- ESTADO DEL IDIOMA ---
if 'language' not in st.session_state:
    st.session_state.language = 'es'

def toggle_language():
    st.session_state.language = 'fr' if st.session_state.language == 'es' else 'es'

# --- TEXTOS (DICCIONARIO BILINGÜE) ---
t = {
    'es': {
        'title': "Calculadora PSTQ (Quebec) - Nueva Escala",
        'toggle': "Passer au Français 🇫🇷",
        'disclaimer': """
            **⚠️ AVISO LEGAL IMPORTANTE:** Esta herramienta es un proyecto independiente para fines informativos. 
            **NO** somos abogados, **NO** somos consultores de inmigración y **NO** representamos al MIFI ni al Gobierno de Canadá.
            Los puntajes son estimaciones basadas en la escala actual (aprox. 1350 puntos máx). Para un diagnóstico oficial, usa Arrima.
        """,
        'support': "Apoya este proyecto",
        'coffee': "☕ Invítame a un café (Buy Me a Coffee)",
        'courses': "📚 Mejora tu Francés Aquí",
        # Secciones
        'h_human': "1. Capital Humano (Candidato Principal)",
        'h_french': "2. Idiomas (Factor Decisivo)",
        'h_quebec': "3. Experiencia y Oferta en Quebec",
        'h_spouse': "4. Factores de Pareja/Cónyuge",
        # Etiquetas
        'age': "Edad actual",
        'edu': "Nivel educativo más alto",
        'area': "Área de Formación (Demanda en el mercado)",
        'exp': "Meses de experiencia laboral (últimos 5 años)",
        'fr_oral': "Francés Oral (Escuchar + Hablar)",
        'fr_write': "Francés Escrito (Leer + Escribir)",
        'en_level': "Nivel de Inglés",
        'q_study': "¿Tienes un Diploma de Quebec (o >900 horas)?",
        'q_exp': "Meses de experiencia laboral DENTRO de Quebec",
        'vjo': "¿Tienes una Oferta de Empleo Validada (VJO)?",
        'family': "¿Tienes familia directa en Quebec?",
        'spouse_check': "¿Te acompaña tu pareja?",
        'sp_age': "Edad de la pareja",
        'sp_edu': "Nivel educativo de la pareja",
        'sp_fr': "Francés de la pareja",
        # Opciones
        'opt_no': "No / Ninguna",
        'opt_vjo_mtl': "Sí, en la CMM (Montreal)",
        'opt_vjo_ext': "Sí, FUERA de la CMM (Regiones)",
        'opt_area_a': "Sección A (Prioritaria/Alta)",
        'opt_area_b': "Sección B (Media)",
        'opt_area_c': "Sección C (Baja)",
        'opt_area_d': "General",
        'calc': "CALCULAR PUNTAJE",
        'res_label': "Puntaje Total Estimado"
    },
    'fr': {
        'title': "Calculateur PSTQ (Québec) - Nouvelle Échelle",
        'toggle': "Cambiar a Español 🇪🇸",
        'disclaimer': """
            **⚠️ AVIS DE NON-RESPONSABILITÉ :** Cet outil est un projet indépendant à titre informatif. 
            Nous ne sommes **PAS** avocats, nous ne sommes **PAS** consultants et nous ne représentons **PAS** le MIFI.
            Les scores sont des estimations basées sur l'échelle actuelle (env. 1350 points max). Pour un diagnostic officiel, utilisez Arrima.
        """,
        'support': "Soutenez ce projet",
        'coffee': "☕ Offrez-moi un café (Buy Me a Coffee)",
        'courses': "📚 Améliorez votre Français Ici",
        # Sections
        'h_human': "1. Capital Humain (Candidat Principal)",
        'h_french': "2. Langues (Facteur Décisif)",
        'h_quebec': "3. Expérience et Offre au Québec",
        'h_spouse': "4. Facteurs du Conjoint",
        # Labels
        'age': "Âge actuel",
        'edu': "Niveau de scolarité le plus élevé",
        'area': "Domaine de Formation (Demande)",
        'exp': "Mois d'expérience (5 dernières années)",
        'fr_oral': "Français Oral (Écouter + Parler)",
        'fr_write': "Français Écrit (Lire + Écrire)",
        'en_level': "Niveau d'Anglais",
        'q_study': "Avez-vous un diplôme du Québec (ou >900h) ?",
        'q_exp': "Mois d'expérience À L'INTÉRIEUR du Québec",
        'vjo': "Avez-vous une Offre d'Emploi Validée (OEV) ?",
        'family': "Avez-vous de la famille directe au Québec ?",
        'spouse_check': "Votre conjoint(e) vous accompagne ?",
        'sp_age': "Âge du conjoint",
        'sp_edu': "Éducation du conjoint",
        'sp_fr': "Français du conjoint",
        # Options
        'opt_no': "Non / Aucune",
        'opt_vjo_mtl': "Oui, dans la CMM (Montréal)",
        'opt_vjo_ext': "Oui, HORS CMM (Régions)",
        'opt_area_a': "Section A (Prioritaire)",
        'opt_area_b': "Section B (Moyenne)",
        'opt_area_c': "Section C (Faible)",
        'opt_area_d': "Général",
        'calc': "CALCULER LE SCORE",
        'res_label': "Score Total Estimé"
    }
}

lang = t[st.session_state.language]

# --- BARRA LATERAL ---
with st.sidebar:
    st.button(lang['toggle'], on_click=toggle_language)
    st.info(lang['disclaimer'])
    st.divider()
    st.header(lang['support'])
    # Reemplaza con tu usuario real
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/TU_USUARIO") 
    st.link_button(lang['courses'], "https://www.tus_cursos.com")

# --- APP PRINCIPAL ---
st.title(lang['title'])

with st.form("new_score_form"):
    
    # 1. CAPITAL HUMANO
    st.subheader(lang['h_human'])
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(lang['age'], 18, 65, 30)
        education = st.selectbox(lang['edu'], ["PhD", "Master", "Bachelor (3+)", "College/Technical", "Secondary"])
    with col2:
        # Áreas de formación (Points varian según demanda)
        area = st.selectbox(lang['area'], [lang['opt_area_a'], lang['opt_area_b'], lang['opt_area_c'], lang['opt_area_d']])
        experience = st.slider(lang['exp'], 0, 60, 36)

    # 2. IDIOMAS
    st.subheader(lang['h_french'])
    c_fr1, c_fr2, c_en = st.columns(3)
    with c_fr1:
        fr_oral_lvl = st.selectbox(lang['fr_oral'], ["C2 (Avancé+)", "C1 (Avancé)", "B2 (Interm.)", "B1", "A1-A2", "0"])
    with c_fr2:
        fr_write_lvl = st.selectbox(lang['fr_write'], ["C2 (Avancé+)", "C1 (Avancé)", "B2 (Interm.)", "B1", "A1-A2", "0"])
    with c_en:
        en_lvl = st.selectbox(lang['en_level'], ["Advanced (C1-C2)", "Intermediate (B1-B2)", "Beginner", "0"])

    # 3. QUEBEC & VJO
    st.subheader(lang['h_quebec'])
    vjo_status = st.radio(lang['vjo'], [lang['opt_no'], lang['opt_vjo_mtl'], lang['opt_vjo_ext']])
    
    cq1, cq2 = st.columns(2)
    with cq1:
        quebec_studies = st.checkbox(lang['q_study'])
        family_quebec = st.checkbox(lang['family'])
    with cq2:
        quebec_exp_months = st.slider(lang['q_exp'], 0, 60, 0)

    # 4. CÓNYUGE
    st.subheader(lang['h_spouse'])
    has_spouse = st.checkbox(lang['spouse_check'])
    
    sp_age, sp_edu, sp_fr = 30, "Secondary", "0" # Defaults
    if has_spouse:
        sc1, sc2, sc3 = st.columns(3)
        with sc1: sp_age = st.number_input(lang['sp_age'], 18, 65, 30)
        with sc2: sp_edu = st.selectbox(lang['sp_edu'], ["PhD", "Master", "Bachelor", "College/Technical", "Secondary"])
        with sc3: sp_fr = st.selectbox(lang['sp_fr'], ["C1-C2", "B2", "A1-B1", "0"])

    submitted = st.form_submit_button(lang['calc'])

# --- LÓGICA MATEMÁTICA 1350 PUNTOS ---
# Esta lógica simula la "Grille de pondération" actual de Arrima
def calculate_1350_score():
    score = 0
    
    # --- A. CAPITAL HUMANO (BASE) ---
    
    # 1. Edad (Max 130)
    if 18 <= age <= 30: score += 130
    elif age <= 45: score += max(0, 130 - (age - 30) * 5)
    
    # 2. Educación (Max 90)
    # Nota: PhD=90, Master=75, Bach=60...
    edu_map = {"PhD": 90, "Master": 75, "Bachelor (3+)": 60, "College/Technical": 45, "Secondary": 20}
    score += edu_map.get(education, 0)
    
    # 3. Área de Formación (Max 60)
    if area == lang['opt_area_a']: score += 60
    elif area == lang['opt_area_b']: score += 40
    elif area == lang['opt_area_c']: score += 20
    
    # 4. Experiencia Laboral General (Max 80)
    # Aprox 1.4 pts por mes hasta tope
    score += min(80, int(experience * 1.4))
    
    # --- B. IDIOMAS (MUY PESADO EN NUEVO SISTEMA) ---
    
    # Francés (Max ~180-200 para Principal)
    # Oral vale más que escrito
    fr_oral_map = {"C2 (Avancé+)": 110, "C1 (Avancé)": 90, "B2 (Interm.)": 60, "B1": 20, "A1-A2": 0, "0": 0}
    fr_write_map = {"C2 (Avancé+)": 70, "C1 (Avancé)": 50, "B2 (Interm.)": 30, "B1": 10, "A1-A2": 0, "0": 0}
    score += fr_oral_map.get(fr_oral_lvl, 0)
    score += fr_write_map.get(fr_write_lvl, 0)
    
    # Inglés (Max ~50)
    en_map = {"Advanced (C1-C2)": 50, "Intermediate (B1-B2)": 25, "Beginner": 0, "0": 0}
    score += en_map.get(en_lvl, 0)
    
    # --- C. FACTORES QUEBEC & OFERTA ---
    
    # 1. Oferta Validada (VJO) - EL FACTOR MÁS ALTO
    # Fuera de MTL = 380 pts, En MTL = 180 pts
    if vjo_status == lang['opt_vjo_ext']: score += 380
    elif vjo_status == lang['opt_vjo_mtl']: score += 180
    
    # 2. Experiencia en Quebec (Max 100)
    score += min(100, int(quebec_exp_months * 3)) # Sube rápido
    
    # 3. Estudios en Quebec (Max 50)
    if quebec_studies: score += 50
    
    # 4. Familia en Quebec (Aprox 20-30)
    if family_quebec: score += 30

    # --- D. CÓNYUGE (Max ~160) ---
    if has_spouse:
        spouse_pts = 0
        # Edad
        if 18 <= sp_age <= 40: spouse_pts += 20
        # Educación
        spouse_pts += edu_map.get(sp_edu, 0) * 0.4 # Peso reducido
        # Francés (Muy importante para pareja ahora)
        sp_fr_map = {"C1-C2": 50, "B2": 30, "A1-B1": 0, "0": 0}
        spouse_pts += sp_fr_map.get(sp_fr, 0)
        
        score += spouse_pts

    # TOPE TEÓRICO
    # Aunque sume más, el sistema suele topar ciertas secciones. 
    # Pero dejaremos la suma libre hasta 1350 para ver el potencial.
    return min(1350, score)

# --- RESULTADOS ---
if submitted:
    final_score = calculate_1350_score()
    
    st.divider()
    
    # Diseño visual del resultado
    col_res1, col_res2 = st.columns([1, 2])
    
    with col_res1:
        st.metric(label=lang['res_label'], value=f"{final_score} / 1350")
    
    with col_res2:
        if final_score >= 580 and vjo_status == lang['opt_no']:
             st.warning("Buen puntaje base, pero sin oferta validada (VJO) es difícil ser invitado.")
        elif final_score >= 1000:
             st.balloons()
             st.success("¡Puntaje Excelente! Con una VJO fuera de Montreal tienes prioridad.")
        elif vjo_status != lang['opt_no']:
             st.success("Tener una Oferta Validada (VJO) es tu mayor fortaleza.")
        else:
             st.info("Consejo: La clave actual es subir el Francés al máximo o conseguir una VJO.")
