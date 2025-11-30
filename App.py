import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS PERSONALIZADOS (BRANDING QUEBEC) ---
# Esto inyecta código CSS para forzar los colores de Quebec y el estilo "tarjeta"
st.markdown("""
    <style>
        /* Color de fondo general más gris para contraste */
        .stApp {
            background-color: #f0f2f6;
        }
        
        /* Encabezado superior (donde va el menú hamburguesa) en Azul Quebec */
        header[data-testid="stHeader"] {
            background-color: #003399;
        }

        /* Títulos principales en Azul Quebec */
        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #003399 !important;
        }

        /* Estilo para los botones principales (Primary) */
        div.stButton > button[type="primary"] {
            background-color: #003399;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }
        div.stButton > button[type="primary"]:hover {
            background-color: #002266; /* Un azul más oscuro al pasar el mouse */
            border: none;
            color: white;
        }
        
        /* Estilo para los botones secundarios (como Buy me a Coffee en el sidebar) */
        div.stButton > button[type="secondary"] {
             border: 2px solid #003399;
             color: #003399;
             border-radius: 8px;
             font-weight: 600;
        }

        /* Hacer que el formulario parezca una "tarjeta" blanca */
        [data-testid="stForm"] {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            border-top: 5px solid #003399; /* Línea azul arriba */
        }

        /* Pestañas (Tabs) activas */
        button[data-baseweb="tab"][aria-selected="true"] {
            background-color: #003399 !important;
            color: white !important;
        }
        
        /* Sidebar un poco más limpia */
        [data-testid="stSidebar"] {
             background-color: #ffffff;
             border-right: 1px solid #e0e0e0;
        }

    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE IDIOMA (ES -> FR -> EN) ---
if 'language' not in st.session_state:
    st.session_state.language = 'fr' # Empezamos en Francés por defecto

def cycle_language():
    if st.session_state.language == 'es':
        st.session_state.language = 'fr'
    elif st.session_state.language == 'fr':
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'es'

# --- 4. DICCIONARIO DE TRADUCCIÓN (3 IDIOMAS) ---
t = {
    'es': {
        'btn_lang': "Idioma / Language: Español 🇪🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Herramienta de estimación para la Residencia Permanente (Sistema Arrima Actual).",
        'disclaimer_title': "⚠️ AVISO LEGAL IMPORTANTE",
        'disclaimer_text': """
            Esta herramienta es un proyecto independiente. NO somos abogados ni consultores. 
            NO representamos al MIFI. Los resultados son estimaciones (~1350 puntos).
        """,
        'sidebar_opt': "Apoya & Aprende",
        'coffee': "☕ Invítame un Café (Apoyar)",
        'courses': "📚 Ver Cursos de Francés",
        'tab1': "👤 Perfil",
        'tab2': "🎓 Educación/Trabajo",
        'tab3': "🗣️ Idiomas",
        'tab4': "⚜️ Quebec/VJO",
        'age': "Edad del candidato principal",
        'spouse': "¿Te acompaña tu pareja/cónyuge?",
        'children_12': "Hijos (0-12 años)",
        'children_13': "Hijos (13-21 años)",
        'sp_age': "Edad de la pareja",
        'sp_edu': "Nivel estudios pareja",
        'sp_fr': "Francés pareja (Oral)",
        'edu_level': "Nivel escolaridad más alto",
        'area': "Área de Formación (Demanda)",
        'exp': "Experiencia calificada (últimos 5 años)",
        'fr_oral': "Francés: Oral (Escuchar/Hablar)",
        'fr_write': "Francés: Escrito (Leer/Escribir)",
        'en_global': "Inglés: Nivel Global",
        'lang_help': "El francés es el factor más importante en el nuevo sistema.",
        'vjo': "Oferta de Empleo Validada (VJO)",
        'opt_vjo_no': "Sin oferta",
        'opt_vjo_mtl': "Sí, Montreal (CMM)",
        'opt_vjo_out': "Sí, FUERA Montreal (Regiones)",
        'q_studies': "¿Diploma de Quebec?",
        'q_exp': "Experiencia DENTRO de Quebec",
        'family_q': "¿Familia directa en Quebec?",
        'calc_btn': "CALCULAR MI PUNTAJE AHORA",
        'result_title': "Puntaje Total Estimado",
        'advice_good': "¡Excelente perfil! Tus probabilidades son altas.",
        'advice_avg': "Perfil sólido. Enfócate en subir el francés o conseguir VJO.",
        'advice_low': "Necesitas subir el francés al máximo o conseguir una oferta fuera de Montreal."
    },
    'fr': {
        'btn_lang': "Langue / Language: Français 🇫🇷",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'estimation pour la Résidence Permanente (Système Arrima Actuel).",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': """
            Cet outil est un projet indépendant. Nous ne sommes PAS avocats ni consultants.
            Nous ne représentons PAS le MIFI. Les résultats sont des estimations (~1350 points).
        """,
        'sidebar_opt': "Soutien & Apprentissage",
        'coffee': "☕ M'offrir un café (Soutenir)",
        'courses': "📚 Voir les Cours de Français",
        'tab1': "👤 Profil",
        'tab2': "🎓 Éducation/Travail",
        'tab3': "🗣️ Langues",
        'tab4': "⚜️ Québec/OEV",
        'age': "Âge du candidat principal",
        'spouse': "Votre conjoint(e) vous accompagne ?",
        'children_12': "Enfants (0-12 ans)",
        'children_13': "Enfants (13-21 ans)",
        'sp_age': "Âge du conjoint",
        'sp_edu': "Niveau scolaire conjoint",
        'sp_fr': "Français conjoint (Oral)",
        'edu_level': "Niveau de scolarité le plus élevé",
        'area': "Domaine de Formation (Demande)",
        'exp': "Expérience qualifiée (5 dernières années)",
        'fr_oral': "Français : Oral (Compréhension/Expression)",
        'fr_write': "Français : Écrit (Compréhension/Expression)",
        'en_global': "Anglais : Niveau Global",
        'lang_help': "Le français est le facteur le plus important dans le nouveau système.",
        'vjo': "Offre d'Emploi Validée (OEV)",
        'opt_vjo_no': "Sans offre",
        'opt_vjo_mtl': "Oui, Montréal (CMM)",
        'opt_vjo_out': "Oui, HORS Montréal (Régions)",
        'q_studies': "Diplôme du Québec ?",
        'q_exp': "Expérience AU Québec",
        'family_q': "Famille directe au Québec ?",
        'calc_btn': "CALCULER MON SCORE MAINTENANT",
        'result_title': "Score Total Estimé",
        'advice_good': "Excellent profil ! Vos chances sont élevées.",
        'advice_avg': "Profil solide. Concentrez-vous sur le français ou une OEV.",
        'advice_low': "Vous devez maximiser le français ou obtenir une offre hors Montréal."
    },
    'en': {
        'btn_lang': "Language: English 🇺🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Estimation tool for Permanent Residency (Current Arrima System).",
        'disclaimer_title': "⚠️ IMPORTANT DISCLAIMER",
        'disclaimer_text': """
            This tool is an independent project. We are NOT lawyers or consultants.
            We do NOT represent the MIFI. Results are estimates (~1350 points).
        """,
        'sidebar_opt': "Support & Learn",
        'coffee': "☕ Buy Me a Coffee (Support)",
        'courses': "📚 See French Courses",
        'tab1': "👤 Profile",
        'tab2': "🎓 Education/Work",
        'tab3': "🗣️ Languages",
        'tab4': "⚜️ Quebec/VJO",
        'age': "Age of principal applicant",
        'spouse': "Is your spouse accompanying you?",
        'children_12': "Children (0-12 years)",
        'children_13': "Children (13-21 years)",
        'sp_age': "Spouse's Age",
        'sp_edu': "Spouse's Education Level",
        'sp_fr': "Spouse's French Level (Oral)",
        'edu_level': "Highest Level of Education",
        'area': "Area of Training (Demand)",
        'exp': "Qualified Experience (Last 5 years)",
        'fr_oral': "French: Oral (Listen/Speak)",
        'fr_write': "French: Written (Read/Write)",
        'en_global': "English: Global Level",
        'lang_help': "French is the most important factor in the new system.",
        'vjo': "Validated Job Offer (VJO)",
        'opt_vjo_no': "No offer",
        'opt_vjo_mtl': "Yes, Montreal (CMM)",
        'opt_vjo_out': "Yes, OUTSIDE Montreal (Regions)",
        'q_studies': "Quebec Diploma?",
        'q_exp': "Experience INSIDE Quebec",
        'family_q': "Direct family in Quebec?",
        'calc_btn': "CALCULATE MY SCORE NOW",
        'result_title': "Total Estimated Score",
        'advice_good': "Excellent profile! Your chances are high.",
        'advice_avg': "Solid profile. Focus on improving French or getting a VJO.",
        'advice_low': "You need to maximize French or get an offer outside Montreal."
    }
}

lang = t[st.session_state.language]

# --- 5. SIDEBAR ---
with st.sidebar:
    # Botón de idioma secundario
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary")
    st.markdown("---")
    st.header(lang['sidebar_opt'])
    
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec") 
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com") 
    
    st.markdown("---")
    st.warning(f"**{lang['disclaimer_title']}**\n\n{lang['disclaimer_text']}")

# --- 6. INTERFAZ PRINCIPAL (TABS) ---
# Título grande estilo marca
st.markdown(f"# {lang['brand']}")
st.write(lang['subtitle'])

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
        
        st.divider()
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
        
        st.divider()
        experience = st.slider(lang['exp'], 0, 60, 36)

    # --- TAB 3: IDIOMAS ---
    with tab3:
        st.caption(lang['lang_help'])
        c_fr1, c_fr2 = st.columns(2)
        with c_fr1:
            fr_oral_lvl = st.select_slider(lang['fr_oral'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        with c_fr2:
            fr_write_lvl = st.select_slider(lang['fr_write'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        
        st.divider()
        en_lvl = st.select_slider(lang['en_global'], options=["0", "Beginner", "Intermediate", "Advanced"], value="0")

    # --- TAB 4: QUEBEC Y OFERTA ---
    with tab4:
        vjo_status = st.radio(lang['vjo'], [lang['opt_vjo_no'], lang['opt_vjo_mtl'], lang['opt_vjo_out']])
        
        st.divider()
        cq1, cq2, cq3 = st.columns(3)
        with cq1: q_studies = st.checkbox(lang['q_studies'])
        with cq2: family_qc = st.checkbox(lang['family_q'])
        with cq3: q_exp_months = st.number_input(lang['q_exp'], 0, 60, 0)

    st.markdown("###")
    # Botón principal (Primary) con estilo azul
    submitted = st.form_submit_button(lang['calc_btn'], type="primary", use_container_width=True)

# --- 7. LÓGICA DE CÁLCULO ---
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

# --- 8. RESULTADOS ---
if submitted:
    final_score = calculate_score()
    
    st.markdown("---")
    # Uso HTML para dar estilo azul al resultado final también
    st.markdown(f"<h2 style='text-align: center; color: #003399;'>{lang['result_title']}: {final_score} / 1350</h2>", unsafe_allow_html=True)
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
        st.metric("VJO (Offre d'emploi)", 'Oui' if vjo_status != lang['opt_vjo_no'] else 'Non')
        st.metric("Niveau Français (Oral)", fr_oral_lvl)
