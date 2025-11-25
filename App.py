import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="PSTQ Calculator | Calculadora",
    page_icon="🍁",
    layout="centered"
)

# --- 2. GESTIÓN DE IDIOMA (ES -> FR -> EN) ---
if 'language' not in st.session_state:
    st.session_state.language = 'es'

def cycle_language():
    if st.session_state.language == 'es':
        st.session_state.language = 'fr'
    elif st.session_state.language == 'fr':
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'es'

# --- 3. DICCIONARIO DE TRADUCCIÓN (3 IDIOMAS) ---
t = {
    'es': {
        'btn_lang': "Idioma / Language: Español 🇪🇸",
        'title': "Calculadora de Puntos Quebec (Arrima / PSTQ)",
        'subtitle': "Estima tu puntaje para la Residencia Permanente bajo el sistema actual.",
        'disclaimer_title': "⚠️ AVISO LEGAL (LEER ANTES DE USAR)",
        'disclaimer_text': """
            Esta herramienta es un proyecto independiente con fines informativos.
            NO somos abogados ni consultores. NO representamos al gobierno de Quebec (MIFI).
            Los resultados son estimaciones basadas en el sistema de ~1350 puntos.
        """,
        'sidebar_opt': "Apoya & Aprende",
        'coffee': "☕ Invítame un Café (Buy Me a Coffee)",
        'courses': "📚 Cursos de Francés e Inglés",
        'tab1': "👤 Perfil y Familia",
        'tab2': "🎓 Educación y Trabajo",
        'tab3': "🗣️ Idiomas",
        'tab4': "⚜️ Oferta y Quebec",
        'age': "Edad del candidato principal",
        'spouse': "¿Tienes pareja/cónyuge que te acompaña?",
        'children_12': "Número de hijos (0 a 12 años)",
        'children_13': "Número de hijos (13 a 21 años)",
        'sp_age': "Edad de la pareja",
        'sp_edu': "Nivel de estudios de la pareja",
        'sp_fr': "Nivel de Francés de la pareja (Oral)",
        'edu_level': "Nivel de escolaridad más alto",
        'area': "Área de Formación (Demanda en el mercado)",
        'exp': "Experiencia laboral calificada (últimos 5 años)",
        'exp_help': "Cuenta solo experiencia en empleos calificados (TEER 0, 1, 2, 3).",
        'fr_oral': "Francés: Comprensión y Expresión Oral",
        'fr_write': "Francés: Comprensión y Expresión Escrita",
        'en_global': "Inglés: Nivel Global",
        'lang_help': "El francés tiene un peso decisivo en el nuevo sistema.",
        'vjo': "¿Tienes una Oferta de Empleo Validada (VJO)?",
        'opt_vjo_no': "No tengo oferta",
        'opt_vjo_mtl': "Sí, en Montreal (CMM)",
        'opt_vjo_out': "Sí, FUERA de Montreal (Regiones)",
        'q_studies': "¿Diploma obtenido en Quebec?",
        'q_exp': "Experiencia laboral DENTRO de Quebec",
        'family_q': "¿Familiares directos en Quebec?",
        'calc_btn': "Calcular Puntaje",
        'result_title': "Tu Puntaje Estimado",
        'advice_good': "¡Excelente perfil! Tienes altas probabilidades.",
        'advice_avg': "Perfil sólido. Mejora el francés o busca una VJO.",
        'advice_low': "Necesitas subir el francés o conseguir una oferta fuera de Montreal."
    },
    'fr': {
        'btn_lang': "Langue / Language: Français 🇫🇷",
        'title': "Calculateur de Points Québec (Arrima / PSTQ)",
        'subtitle': "Estimez votre score pour la Résidence Permanente selon le système actuel.",
        'disclaimer_title': "⚠️ AVIS DE NON-RESPONSABILITÉ",
        'disclaimer_text': """
            Cet outil est un projet indépendant à titre informatif.
            Nous ne sommes PAS avocats ni consultants. Nous ne représentons PAS le MIFI.
            Les résultats sont des estimations basées sur le système de ~1350 points.
        """,
        'sidebar_opt': "Soutien & Apprentissage",
        'coffee': "☕ Offrez-moi un café (Buy Me a Coffee)",
        'courses': "📚 Cours de Français et Anglais",
        'tab1': "👤 Profil et Famille",
        'tab2': "🎓 Éducation et Travail",
        'tab3': "🗣️ Langues",
        'tab4': "⚜️ Offre et Québec",
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint qui vous accompagne ?",
        'children_12': "Nombre d'enfants (0 à 12 ans)",
        'children_13': "Nombre d'enfants (13 à 21 ans)",
        'sp_age': "Âge du conjoint",
        'sp_edu': "Niveau de scolarité du conjoint",
        'sp_fr': "Niveau de Français du conjoint (Oral)",
        'edu_level': "Niveau de scolarité le plus élevé",
        'area': "Domaine de Formation (Demande)",
        'exp': "Expérience de travail qualifiée (5 dernières années)",
        'exp_help': "Comptez uniquement l'expérience qualifiée (TEER 0, 1, 2, 3).",
        'fr_oral': "Français : Compréhension et Expression Orale",
        'fr_write': "Français : Compréhension et Expression Écrite",
        'en_global': "Anglais : Niveau Global",
        'lang_help': "Le français a un poids décisif dans le nouveau système.",
        'vjo': "Avez-vous une Offre d'Emploi Validée (OEV) ?",
        'opt_vjo_no': "Non, aucune offre",
        'opt_vjo_mtl': "Oui, à Montréal (CMM)",
        'opt_vjo_out': "Oui, HORS Montréal (Régions)",
        'q_studies': "Diplôme obtenu au Québec ?",
        'q_exp': "Expérience de travail AU Québec",
        'family_q': "Famille directe au Québec ?",
        'calc_btn': "Calculer le Score",
        'result_title': "Votre Score Estimé",
        'advice_good': "Excellent profil ! Vous avez de fortes chances.",
        'advice_avg': "Profil solide. Améliorez le français ou cherchez une OEV.",
        'advice_low': "Vous devez améliorer le français ou obtenir une offre hors Montréal."
    },
    'en': {
        'btn_lang': "Language: English 🇺🇸",
        'title': "Quebec Points Calculator (Arrima / PSTQ)",
        'subtitle': "Estimate your score for Permanent Residency under the current system.",
        'disclaimer_title': "⚠️ LEGAL DISCLAIMER",
        'disclaimer_text': """
            This tool is an independent project for informational purposes.
            We are NOT lawyers or immigration consultants. We do NOT represent the MIFI.
            Results are estimates based on the ~1350 point system.
        """,
        'sidebar_opt': "Support & Learn",
        'coffee': "☕ Buy Me a Coffee",
        'courses': "📚 French & English Courses",
        'tab1': "👤 Profile & Family",
        'tab2': "🎓 Education & Work",
        'tab3': "🗣️ Languages",
        'tab4': "⚜️ Offer & Quebec",
        'age': "Age of principal applicant",
        'spouse': "Is your spouse/partner accompanying you?",
        'children_12': "Number of children (0 to 12 years)",
        'children_13': "Number of children (13 to 21 years)",
        'sp_age': "Spouse's Age",
        'sp_edu': "Spouse's Education Level",
        'sp_fr': "Spouse's French Level (Oral)",
        'edu_level': "Highest Level of Education",
        'area': "Area of Training (Market Demand)",
        'exp': "Qualified Work Experience (Last 5 years)",
        'exp_help': "Only count qualified experience (TEER 0, 1, 2, 3).",
        'fr_oral': "French: Oral Comprehension & Expression",
        'fr_write': "French: Written Comprehension & Expression",
        'en_global': "English: Global Level",
        'lang_help': "French has a decisive weight in the new system.",
        'vjo': "Do you have a Validated Job Offer (VJO)?",
        'opt_vjo_no': "No offer",
        'opt_vjo_mtl': "Yes, inside Montreal (CMM)",
        'opt_vjo_out': "Yes, OUTSIDE Montreal (Regions)",
        'q_studies': "Diploma obtained in Quebec?",
        'q_exp': "Work experience INSIDE Quebec",
        'family_q': "Direct family in Quebec?",
        'calc_btn': "Calculate Score",
        'result_title': "Your Estimated Score",
        'advice_good': "Excellent profile! You have high chances.",
        'advice_avg': "Solid profile. Improve French or get a VJO.",
        'advice_low': "You need to improve French or get an offer outside Montreal."
    }
}

lang = t[st.session_state.language]

# --- 4. SIDEBAR ---
with st.sidebar:
    st.button(lang['btn_lang'], on_click=cycle_language, type="primary")
    st.markdown("---")
    st.header(lang['sidebar_opt'])
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/TU_USUARIO")
    st.link_button(lang['courses'], "https://tupaginaweb.com/cursos")
    st.markdown("---")
    st.warning(f"**{lang['disclaimer_title']}**\n\n{lang['disclaimer_text']}")

# --- 5. INTERFAZ PRINCIPAL (TABS) ---
st.title(lang['title'])
st.caption(lang['subtitle'])

with st.form("main_form"):
    
    # Pestañas
    tab1, tab2, tab3, tab4 = st.tabs([lang['tab1'], lang['tab2'], lang['tab3'], lang['tab4']])

    # --- TAB 1: PERFIL Y FAMILIA ---
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input(lang['age'], 18, 65, 30)
        with col2:
            spouse = st.checkbox(lang['spouse'])
        
        st.markdown("---")
        c_kids1, c_kids2 = st.columns(2)
        with c_kids1:
            kids_under_12 = st.number_input(lang['children_12'], 0, 10, 0)
        with c_kids2:
            kids_over_12 = st.number_input(lang['children_13'], 0, 10, 0)

        # Variables de cónyuge (defaults)
        sp_age_val, sp_edu_val, sp_fr_val = 30, "Secondary", "0"
        
        if spouse:
            st.info("Datos de la Pareja / Partner Details")
            c_sp1, c_sp2, c_sp3 = st.columns(3)
            with c_sp1: sp_age_val = st.number_input(lang['sp_age'], 18, 65, 30)
            with c_sp2: sp_edu_val = st.selectbox(lang['sp_edu'], ["PhD", "Master", "Bachelor", "College", "Secondary"])
            with c_sp3: sp_fr_val = st.selectbox(lang['sp_fr'], ["C1-C2", "B2", "A1-B1", "0"])

    # --- TAB 2: EDUCACIÓN Y TRABAJO ---
    with tab2:
        col_edu, col_area = st.columns(2)
        with col_edu:
            education = st.selectbox(lang['edu_level'], ["PhD", "Master", "Bachelor (3+)", "College (3y)", "Diploma (1-2y)", "Secondary"])
        with col_area:
            area_training = st.selectbox(lang['area'], ["Section A (Top)", "Section B", "Section C", "General"])
        
        st.markdown("---")
        experience = st.slider(lang['exp'], 0, 60, 36)
        st.caption(lang['exp_help'])

    # --- TAB 3: IDIOMAS ---
    with tab3:
        st.info(lang['lang_help'])
        c_fr1, c_fr2 = st.columns(2)
        with c_fr1:
            fr_oral_lvl = st.select_slider(lang['fr_oral'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        with c_fr2:
            fr_write_lvl = st.select_slider(lang['fr_write'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        
        st.markdown("---")
        en_lvl = st.select_slider(lang['en_global'], options=["0", "Beginner", "Intermediate", "Advanced"], value="0")

    # --- TAB 4: QUEBEC Y OFERTA ---
    with tab4:
        vjo_status = st.radio(lang['vjo'], [lang['opt_vjo_no'], lang['opt_vjo_mtl'], lang['opt_vjo_out']])
        
        st.markdown("---")
        cq1, cq2, cq3 = st.columns(3)
        with cq1: q_studies = st.checkbox(lang['q_studies'])
        with cq2: family_qc = st.checkbox(lang['family_q'])
        with cq3: q_exp_months = st.number_input(lang['q_exp'], 0, 60, 0)

    st.markdown("###")
    submitted = st.form_submit_button(lang['calc_btn'], type="primary", use_container_width=True)

# --- 6. LÓGICA DE CÁLCULO ---
def calculate_score():
    score = 0
    
    # A. Capital Humano (Principal)
    if 18 <= age <= 30: score += 130
    elif age <= 45: score += max(0, 130 - (age - 30) * 5)
    
    edu_pts = {"PhD": 90, "Master": 75, "Bachelor (3+)": 60, "College (3y)": 50, "Diploma (1-2y)": 40, "Secondary": 20}
    score += edu_pts.get(education, 0)
    
    area_pts = {"Section A (Top)": 60, "Section B": 40, "Section C": 20, "General": 0}
    score += area_pts.get(area_training, 0)
    
    score += min(80, int(experience * 1.4))
    
    # Idiomas
    fr_map = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80} 
    score += fr_map[fr_oral_lvl] * 1.2 
    score += fr_map[fr_write_lvl] * 0.8
    
    en_map = {"Advanced": 25, "Intermediate": 15, "Beginner": 5, "0": 0}
    score += en_map[en_lvl]
    
    # B. Quebec & Oferta
    if vjo_status == lang['opt_vjo_out']: score += 380
    elif vjo_status == lang['opt_vjo_mtl']: score += 180
    
    if q_studies: score += 50
    if family_qc: score += 30
    score += min(100, int(q_exp_months * 2.5))
    
    # C. Familia
    if spouse:
        if 18 <= sp_age_val <= 40: score += 20
        score += edu_pts.get(sp_edu_val, 0) * 0.3
        sp_fr_pts = {"C1-C2": 50, "B2": 30, "A1-B1": 0, "0": 0}
        score += sp_fr_pts.get(sp_fr_val, 0)
    
    score += (kids_under_12 * 4) + (kids_over_12 * 2)

    return int(score)

# --- 7. RESULTADOS ---
if submitted:
    final_score = calculate_score()
    
    st.divider()
    st.markdown(f"<h2 style='text-align: center;'>{lang['result_title']}: {final_score} / 1350</h2>", unsafe_allow_html=True)
    st.progress(min(final_score / 1350, 1.0))
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        if final_score > 600:
            st.success(lang['advice_good'])
            st.balloons()
        elif final_score > 500:
            st.warning(lang['advice_avg'])
        else:
            st.error(lang['advice_low'])
    
    with col_res2:
        st.text(f"Hijos/Enfants: {kids_under_12 + kids_over_12}")
        st.text(f"VJO: {'No' if vjo_status == lang['opt_vjo_no'] else 'Yes/Oui'}")
