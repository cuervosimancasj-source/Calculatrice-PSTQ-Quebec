import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (CORRECCIÓN BOTONES + WIZARD) ---
st.markdown("""
    <style>
        /* === 0. INSTRUCCIÓN MAESTRA === */
        :root { color-scheme: light; }
        
        /* === 1. FONDO Y TEXTOS === */
        [data-testid="stAppViewContainer"] { background-color: #f0f2f6 !important; }
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li { color: #000000 !important; }
        header[data-testid="stHeader"] { background-color: #003399 !important; }
        h1, h2, h3 { color: #003399 !important; }

        /* === 2. INPUTS Y SELECTORES === */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
            color: #000000 !important;
        }
        input { color: #000000 !important; -webkit-text-fill-color: #000000 !important; }
        div[data-baseweb="select"] * { color: #000000 !important; }
        
        /* Menú desplegable */
        ul[data-baseweb="menu"] { background-color: #FFFFFF !important; }
        li[data-baseweb="menu-item"] { background-color: #FFFFFF !important; color: #000000 !important; }
        li[data-baseweb="menu-item"]:hover { background-color: #e6f0ff !important; color: #003399 !important; }

        /* === 3. BOTONES DE NAVEGACIÓN (CORREGIDO TEXTO BLANCO) === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; }
        
        /* Botón Siguiente/Calcular (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
            padding: 10px 20px;
        }
        div.stButton > button[kind="primary"]:hover { background-color: #002266 !important; }
        
        /* ESTA REGLA FUERZA EL TEXTO BLANCO DENTRO DEL BOTÓN AZUL */
        div.stButton > button[kind="primary"] * {
            color: #FFFFFF !important;
        }

        /* Botón Anterior/Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }

        /* === 4. TARJETA PRINCIPAL === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 2rem; 
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
            border-top: 5px solid #003399;
        }
        
        /* Cajas Informativas */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; color: #000 !important; margin-bottom: 15px;}
        .help-box { background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; border-radius: 5px; color: #000 !important; }
        .step-box { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; color: #000 !important; }
        
        /* Resultado */
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }

        /* Footer */
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        .deco-sub { font-style: italic; margin-bottom: 15px; display: block; color: #666666 !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN ---
default_values = {
    'language': 'fr',
    'step': 1,
    'show_results': False,
    'age': 30,
    'spouse': False,
    'k1': 0,
    'k2': 0,
    'sp_age': 30,
    'sp_edu': 'Secondary',
    'sp_fr': '0',
    'teer_sel': 'TEER 0, 1: Université / Gestion / Ingénierie',
    'edu': 'Secondary',
    'exp': 3,
    'fr_oral': 'B2',
    'fr_write': 'B1',
    'en_lvl': '0',
    'vjo': '',
    'q_stud_val': 'Non',
    'q_fam_val': 'Non',
    'job_search_term': ''
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

def cycle_language():
    if st.session_state.language == 'fr': st.session_state.language = 'es'
    elif st.session_state.language == 'es': st.session_state.language = 'en'
    else: st.session_state.language = 'fr'

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation():
    st.session_state.show_results = True

# --- 4. TRADUCCIONES (REVISADAS) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants. Nous ne représentons PAS le MIFI.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        'yes_no': ["Non", "Oui"], 
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation du conjoint",
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur, Soudeur (Appuyez sur Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': ["TEER 0, 1: Université / Gestion / Ingénierie", "TEER 2: Collégial / Technique / Superviseurs", "TEER 3: Métiers / Administration / Intermédiaire", "TEER 4, 5: Manœuvre / Secondaire / Service"],
        'teer_manual_help': "Si non trouvé, choisissez ci-dessous:",
        'exp_label': "Années d'expérience",
        'lang_info': "**Exigences :** Volet 1 = Niv 7 | Volet 2 = Niv 5 | Conjoint = Niv 4",
        'fr_oral': "Français Oral (Vous)", 'fr_write': "Français Écrit (Vous)", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint (Oral)",
        'oev_info': "**ℹ️ OEV (Offre d'emploi validée) :** EIMT ou validée par le MIFI.",
        'vjo_label': "Avez-vous une Offre Validée (OEV) ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Hors Montréal (Région)"],
        'dip_qc_label': "Diplôme du Québec ?",
        'dip_qc_help': "AEC, DEP, DEC, Baccalauréat, Maîtrise, Doctorat obtenu au Québec.",
        'fam_qc_label': "Famille au Québec ?",
        'fam_qc_help': "Parent, enfant, conjoint, frère/sœur, grand-parent (Citoyen ou Résident).",
        'arr_year': "Année d'arrivée",
        'city_label': "Ville de résidence",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Autre"],
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Profil compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV.",
        'details': "Détails du score",
        'sp_points': "Points Conjoint",
        'guide_title': "Votre Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente.",
        'noc_link_text': "🔎 Chercher sur le site officiel du Canada (CNP)"
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Análisis Residencia Permanente (Arrima).",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "Proyecto independiente. NO abogados. Resultados estimados.",
        'coffee': "☕ Invítame un café",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR PUNTAJE",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil y Familia",
        'step2': "Paso 2: Trabajo y TEER",
        'step3': "Paso 3: Idiomas",
        'step4': "Paso 4: Quebec y Oferta",
        'age': "Edad del candidato",
        'spouse': "¿Tienes pareja?",
        'kids12': "Hijos -12 años", 'kids13': "Hijos +12 años",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'job_title': "Trabajo actual",
        'job_place': "Ej: Ingeniero (Enter para buscar)...",
        'teer_label': "Categoría TEER",
        'teer_opts': ["TEER 0, 1: Universidad / Gerencia", "TEER 2: College / Técnico", "TEER 3: Oficios / Intermedio", "TEER 4, 5: Operarios / Manual"],
        'teer_manual_help': "Si no encuentras, elige abajo:",
        'exp_label': "Años de experiencia",
        'lang_info': "**Requisitos:** Volet 1 = Niv 7 | Volet 2 = Niv 5 | Pareja = Niv 4",
        'fr_oral': "Francés Oral (Tú)", 'fr_write': "Francés Escrito (Tú)", 'en': "Inglés",
        'sp_fr_title': "Francés de la Pareja (Oral)",
        'oev_info': "**ℹ️ VJO (Oferta Validada):** Con LMIA o aprobada por MIFI.",
        'vjo_label': "¿Tienes Oferta Validada (VJO)?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Fuera de Montreal"],
        'dip_qc_label': "¿Diploma de Quebec?", 'dip_qc_help': "AEC, DEC, Bachelor, etc.",
        'fam_qc_label': "¿Familia en Quebec?", 'fam_qc_help': "Residente o Ciudadano.",
        'arr_year': "Año llegada", 'city_label': "Ciudad", 'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Otra"],
        'res_title': "Resultado", 'advice_good': "¡Excelente! Competitivo.", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Puntos Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado Selección.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia Permanente.",
        'noc_link_text': "🔎 Buscar en sitio oficial Canadá (NOC)"
    },
    'en': {
        'btn_lang': "🌐 Change Language",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "Independent. NOT lawyers. Estimated results.",
        'coffee': "☕ Support",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE SCORE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile & Family",
        'step2': "Step 2: Work & TEER",
        'step3': "Step 3: Languages",
        'step4': "Step 4: Quebec & Offer",
        'age': "Age",
        'spouse': "Have a spouse?",
        'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data",
        'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'job_title': "Current Job",
        'job_place': "Ex: Engineer (Press Enter)...",
        'teer_label': "TEER Category",
        'teer_opts': ["TEER 0,1 (Uni)", "TEER 2 (Tech)", "TEER 3 (Trades)", "TEER 4,5 (Manual)"],
        'teer_manual_help': "If not found, select below:",
        'exp_label': "Years Experience",
        'lang_info': "**Reqs:** Volet 1 = Lvl 7 | Volet 2 = Lvl 5 | Spouse = Lvl 4",
        'fr_oral': "French Oral (You)", 'fr_write': "French Written (You)", 'en': "English",
        'sp_fr_title': "Spouse's French (Oral)",
        'oev_info': "**ℹ️ VJO:** Validated Offer (LMIA/MIFI).",
        'vjo_label': "Validated Job Offer?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Outside Montreal"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "AEC, DEC, etc.",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "PR or Citizen.",
        'arr_year': "Arrival Year", 'city_label': "City", 'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Other"],
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Know strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Selection Cert.",
        'g_step5': "5. Federal", 'g_desc5': "Residency.",
        'noc_link_text': "🔎 Search on official Canada site (NOC)"
    }
}
lang = t[st.session_state.language]

# --- 5. DATA JOBS ---
jobs_db = {
    "ingenie": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "engineer": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "web": {"code": "21222", "teer": "1", "volet": "Volet 1"},
    "infirmier": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "nurse": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "architect": {"code": "21200", "teer": "1", "volet": "Volet 1"},
    "administra": {"code": "13100", "teer": "3", "volet": "Volet 2"},
    "technicien": {"code": "22300", "teer": "2", "volet": "Volet 1/2"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "cuisinier": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cook": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "camion": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "mecanic": {"code": "72410", "teer": "2", "volet": "Volet 2"},
    "ensamblador": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "assembler": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manguera": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hose": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hidraulica": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manoeuvre": {"code": "95109", "teer": "5", "volet": "Volet 2"},
}

def find_job_details(keyword):
    if not keyword: return None
    keyword = keyword.lower().strip()
    for key, data in jobs_db.items():
        if key in keyword: return data
    return None

# ==========================================
# HEADER
# ==========================================
col_brand, col_lang = st.columns([3, 1])
with col_brand:
    st.markdown(f"## {lang['brand']}")
    st.caption(lang['subtitle'])
with col_lang:
    st.markdown("###") 
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary", key="top_lang_btn")

# ==========================================
# APP PRINCIPAL (WIZARD SIN FORMULARIOS)
# ==========================================
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

with main_tab_calc:
    
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # --- PASO 1: PERFIL ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        
        c1, c2 = st.columns(2)
        with c1: 
            st.session_state.age = st.number_input(lang['age'], 18, 65, st.session_state.age, key="age_input")
        with c2: 
            st.session_state.spouse = st.checkbox(lang['spouse'], value=st.session_state.spouse, key="spouse_chk")
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(lang['kids12'], 0, 5, st.session_state.k1, key="k1_input")
        with c4: st.session_state.k2 = st.number_input(lang['kids13'], 0, 5, st.session_state.k2, key="k2_input")
        
        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang['sp_header']}**")
            c_sp1, c_sp2 = st.columns(2)
            with c_sp1: st.session_state.sp_age = st.number_input(lang['sp_age'], 18, 65, st.session_state.sp_age, key="sp_age_in")
            with c_sp2: st.session_state.sp_edu = st.selectbox(lang['sp_edu'], ["PhD", "Master", "Bachelor", "Technical", "Secondary"], index=2, key="sp_edu_in")
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n:
            st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 2: TRABAJO ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        
        st.markdown(f"**{lang['job_title']}**")
        
        def update_search():
            st.session_state.job_search_term = st.session_state.widget_search
            
        st.text_input(
            "Search", 
            value=st.session_state.job_search_term, 
            placeholder=lang['job_place'], 
            label_visibility="collapsed",
            key="widget_search",
            on_change=update_search
        )

        if st.session_state.job_search_term:
            result = find_job_details(st.session_state.job_search_term)
            if result:
                st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
            else:
                st.markdown(f"<div class='help-box'>{lang['teer_manual_help']}</div>", unsafe_allow_html=True)
                st.markdown(f"🔗 [{lang['noc_link_text']}](https://noc.esdc.gc.ca/)")

        st.divider()
        
        current_idx = 0
        if st.session_state.teer_sel in lang['teer_opts']:
            current_idx = lang['teer_opts'].index(st.session_state.teer_sel)
            
        st.session_state.teer_sel = st.selectbox(lang['teer_label'], lang['teer_opts'], index=current_idx, key="teer_input")
        st.session_state.edu = st.selectbox("Education", ["PhD", "Master", "Bachelor", "College (3y)", "Diploma (1-2y)", "Secondary"], index=2, key="edu_input")
        st.session_state.exp = st.slider(lang['exp_label'], 0, 10, st.session_state.exp, key="exp_input")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p:
            st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n:
            st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 3: IDIOMAS ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1: st.session_state.fr_oral = st.select_slider(lang['fr_oral'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_oral, key="fro_input")
        with c2: st.session_state.fr_write = st.select_slider(lang['fr_write'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_write, key="frw_input")
        st.session_state.en_lvl = st.select_slider(lang['en'], ["0", "Beginner", "Intermediate", "Advanced"], value=st.session_state.en_lvl, key="en_input")

        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang['sp_fr_title']}**")
            st.session_state.sp_fr = st.select_slider("Niveau", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.sp_fr, key="spfr_input")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p:
            st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n:
            st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 4: QUEBEC (FINAL) ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        
        st.info(lang['oev_info'])
        
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']:
            vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx, key="vjo_input")
        
        st.divider()
        
        st.markdown(f"**{lang['dip_qc_label']}**")
        st.caption(lang['dip_qc_help'])
        
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio("DipQC", lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True, label_visibility="collapsed", key="q_stud_in")
        
        st.markdown("---")
        st.markdown(f"**{lang['fam_qc_label']}**")
        st.caption(lang['fam_qc_help'])
        
        curr_fam = st.session_state.q_fam_val
        if curr_fam not in lang['yes_no']: curr_fam = lang['yes_no'][0]
        st.session_state.q_fam_val = st.radio("FamQC", lang['yes_no'], index=lang['yes_no'].index(curr_fam), horizontal=True, label_visibility="collapsed", key="q_fam_in")
        
        st.divider()
        
        c_city, c_year = st.columns(2)
        with c_city:
            st.selectbox(lang['city_label'], lang['city_opts'], key="city_input")
        with c_year:
            st.selectbox(lang['arr_year'], range(2025, 1990, -1), key="year_input")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 1, 2])
        with col_p:
            st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n:
            st.button(lang['calc'], type="primary", on_click=trigger_calculation)

    # LÓGICA & RESULTADOS
    if st.session_state.show_results:
        age = st.session_state.age
        edu = st.session_state.edu
        teer = st.session_state.teer_sel
        exp = st.session_state.exp
        fr_o = st.session_state.fr_oral
        fr_w = st.session_state.fr_write
        en = st.session_state.en_lvl
        vjo_val = st.session_state.vjo
        
        q_stud_str = st.session_state.q_stud_val
        q_fam_str = st.session_state.q_fam_val
        is_yes_stud = q_stud_str in ["Oui", "Sí", "Yes"]
        is_yes_fam = q_fam_str in ["Oui", "Sí", "Yes"]
        
        score = 0
        score_sp = 0 
        
        if 18 <= age <= 30: score += 130
        elif age <= 45: score += (130 - (age-30)*5)
        
        if "PhD" in edu: score += 90
        elif "Master" in edu: score += 75
        elif "Bachelor" in edu: score += 60
        elif "College" in edu: score += 50
        else: score += 30
        
        if "TEER 0, 1" in teer or "TEER 0,1" in teer: score += 60 
        elif "TEER 2" in teer: score += 40
        elif "TEER 3" in teer: score += 20
        
        score += min(80, int(exp * 10))
        
        pts_map = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
        score += pts_map.get(fr_o,0) * 1.2 + pts_map.get(fr_w,0) * 0.8
        
        if en == "Advanced": score += 25
        elif en == "Intermediate": score += 15
        
        if "Hors" in vjo_val or "Outside" in vjo_val or "Fuera" in vjo_val: score += 380
        elif "Grand" in vjo_val or "Greater" in vjo_val or "Gran" in vjo_val: score += 180
        
        if is_yes_stud: score += 50
        if is_yes_fam: score += 30
        
        if st.session_state.spouse:
            sp_a = st.session_state.sp_age
            sp_e = st.session_state.sp_edu
            sp_f = st.session_state.sp_fr
            
            if 18 <= sp_a <= 40: score_sp += 10
            if "Bachelor" in sp_e or "Master" in sp_e or "PhD" in sp_e: score_sp += 10
            elif "College" in sp_e: score_sp += 5
            
            if sp_f in ["C1", "C2"]: score_sp += 30
            elif sp_f == "B2": score_sp += 20
            elif sp_f in ["A2", "B1"]: score_sp += 10
            score += score_sp
            
        score += (st.session_state.k1*4) + (st.session_state.k2*2)

        st.markdown(f"""
        <div class="result-box">
            <h2>{lang['res_title']}: {int(score)} / 1350</h2>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander(lang['details']):
            st.write(f"**Principal:** {int(score - score_sp - (st.session_state.k1*4 + st.session_state.k2*2))} pts")
            if st.session_state.spouse:
                st.write(f"**{lang['sp_points']}:** {score_sp} pts")
            st.write(f"**Enfants:** {(st.session_state.k1*4 + st.session_state.k2*2)} pts")
        
        if score > 580:
            st.success(lang['advice_good'])
            st.balloons()
        else:
            st.warning(lang['advice_low'])
            
        if st.button("🔄 Recalculer / Reiniciar"):
            reset_calc()
            st.rerun()

# PESTAÑA 2: GUÍA
with main_tab_guide:
    st.markdown(f"### 🗺️ {lang['guide_title']}")
    st.markdown("---")
    st.markdown(f"""
    <div class='step-box'><h4>📊 {lang['g_step1']}</h4><p>{lang['g_desc1']}</p></div>
    <div class='step-box'><h4>🗣️ {lang['g_step2']}</h4><p>{lang['g_desc2']}</p></div>
    <div class='step-box'><h4>📂 {lang['g_step3']}</h4><p>{lang['g_desc3']}</p></div>
    <div class='step-box'><h4>📩 {lang['g_step4']}</h4><p>{lang['g_desc4']}</p></div>
    <div class='step-box'><h4>🍁 {lang['g_step5']}</h4><p>{lang['g_desc5']}</p></div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)

fc1, fc2 = st.columns(2)
with fc1:
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
with fc2:
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com") 

st.markdown("###")
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])

st.markdown("</div>", unsafe_allow_html=True)
