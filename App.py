import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (SOLUCIÓN DE EMERGENCIA: SIMPLE Y FUNCIONAL) ---
st.markdown("""
    <style>
        /* Forzar modo claro */
        :root { color-scheme: light !important; }
        
        [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important;
            color: #000000 !important;
        }
        
        /* Textos */
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #000000 !important;
        }
        header[data-testid="stHeader"] { background-color: #003399 !important; }
        h1 { color: #FFFFFF !important; }

        /* Inputs Blancos con Texto Negro (Anti-Instagram) */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #cccccc !important;
            color: #000000 !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
            opacity: 1 !important;
            caret-color: #000000 !important;
        }
        div[data-baseweb="select"] span {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

        /* Menús Desplegables Blancos */
        ul[data-baseweb="menu"] { background-color: #FFFFFF !important; }
        li[data-baseweb="menu-item"] { background-color: #FFFFFF !important; color: #000000 !important; }
        li[data-baseweb="menu-item"] * { color: #000000 !important; }
        li[data-baseweb="menu-item"]:hover { background-color: #e6f0ff !important; }

        /* Botones */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; }
        
        /* Primario (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }
        
        /* Enlaces (Azules) */
        div.stLinkButton > a {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
            text-align: center !important;
            font-weight: bold !important;
            text-decoration: none !important;
            display: block !important;
            border-radius: 8px !important;
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }

        /* Header Pro */
        .pro-header {
            background-color: #003399;
            padding: 15px 20px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            text-align: center;
            font-size: 1.5rem;
            flex-grow: 1;
        }
        .flag-icon { height: 40px; border: 1px solid white; border-radius: 4px; }
        
        /* Extras */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .step-box { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        
        /* Botones +/- */
        button[tabindex="-1"] { background-color: #e0e0e0 !important; color: #000 !important; border: 1px solid #ccc !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN ---
default_values = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'teer_sel': '', 'edu': 'Secondary', 
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': '',
    'current_loc': '', 'origin_country': '', 'dest_city': '-', 'arrival_date': date.today()
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]

def trigger_calculation(): st.session_state.show_results = True

# --- 4. TRADUCCIONES (COMPLETAS Y SIN ERRORES) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        'yes_no': ["Non", "Oui"],
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        'tab1_sub': "Le point de départ de votre projet.",
        'tab2_sub': "Votre métier est au cœur du programme.",
        'tab3_sub': "Le français est la clé du succès.",
        'tab4_sub': "Finalisez votre pointage.",
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'dest_city_label': "Ville de destination",
        'arrival_label': "Date d'arrivée prévue",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Autre"],
        'age': "Âge du candidat",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation conjoint",
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur (Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0, 1: Université / Gestion",
            "TEER 2: Collégial / Technique",
            "TEER 3: Métiers / Administration",
            "TEER 4, 5: Manœuvre / Service"
        ],
        'teer_manual_help': "Si non trouvé, choisissez ci-dessous:",
        'exp_label': "Années d'expérience",
        'lang_info': "**Exigences :** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint", 'sp_fr_label': "Niveau Oral",
        'oev_info': "**ℹ️ OEV :** Offre validée par le MIFI.",
        'vjo_label': "Avez-vous une Offre Validée ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        'dip_qc_label': "Diplôme du Québec ?", 'dip_qc_help': "AEC, DEC, Bac...",
        'fam_qc_label': "Famille au Québec ?", 'fam_qc_help': "Résident ou Citoyen.",
        'arr_year': "Année d'arrivée",
        'res_title': "Résultat Estimé", 'advice_good': "Excellent !", 'advice_low': "Améliorez le français.",
        'details': "Détails du score", 'sp_points': "Pts Conjoint",
        'guide_title': "Votre Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente.",
        'noc_link_text': "🔎 Chercher CNP",
        'exp_title': "Expérience (5 dernières années)",
        'exp_qc_label': "Mois au Québec", 'exp_ca_label': "Mois au Canada", 'exp_for_label': "Mois à l'étranger"
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculadora PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "Independiente. NO abogados.",
        'coffee': "☕ Apoyar", 'courses': "📚 Cursos",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil", 'step2': "Paso 2: Trabajo", 'step3': "Paso 3: Idiomas", 'step4': "Paso 4: Quebec",
        'tab1_sub': "Punto de partida.", 'tab2_sub': "Tu oficio es clave.",
        'tab3_sub': "El francés es vital.", 'tab4_sub': "Factores locales.",
        'loc_label': "¿Dónde te encuentras?",
        'loc_opts': ["En Quebec", "Canadá (Otra)", "En el extranjero"],
        'country_label': "País de residencia",
        'dest_city_label': "Ciudad de destino",
        'arrival_label': "Fecha estimada llegada",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Otra"],
        'age': "Edad", 'spouse': "¿Pareja?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'job_title': "Trabajo actual", 'job_place': "Ej: Ingeniero (Enter)",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0,1: Uni / Gerencia",
            "TEER 2: Técnico / College",
            "TEER 3: Oficios / Intermedio",
            "TEER 4,5: Manual / Secund"
        ],
        'teer_manual_help': "Si no encuentras, elige:",
        'exp_label': "Años de experiencia",
        'lang_info': "Requisitos: Niv 7 (B2) | Pareja Niv 4 (A2)",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja", 'sp_fr_label': "Nivel Oral",
        'oev_info': "**ℹ️ VJO:** Oferta Validada.",
        'vjo_label': "¿Oferta Validada?", 'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Región"],
        'dip_qc_label': "¿Diploma de Quebec?", 'dip_qc_help': "AEC, DEC, etc.",
        'fam_qc_label': "¿Familia en Quebec?", 'fam_qc_help': "Residente o Ciudadano.",
        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Pts Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia.",
        'noc_link_text': "🔎 Buscar NOC",
        'exp_title': "Experiencia (5 años)",
        'exp_qc_label': "Meses en Quebec", 'exp_ca_label': "Meses en Canadá", 'exp_for_label': "Meses Extranjero"
    },
    'en': {
        'btn_lang': "🌐 Change Lang", 'brand': "PSTQ Calculator",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "Independent. Estimated results.",
        'coffee': "☕ Support", 'courses': "📚 Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Starting point.", 'tab2_sub': "Experience and trade.",
        'tab3_sub': "French is key.", 'tab4_sub': "Local assets.",
        'loc_label': "Current location?",
        'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country", 'dest_city_label': "Dest. City",
        'arrival_label': "Arrival Date", 'city_opts': ["-", "Montréal", "Québec", "Other"],
        'age': "Age", 'spouse': "Spouse?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'job_title': "Current Job", 'job_place': "Ex: Welder (Enter)",
        'teer_label': "TEER Category",
        'teer_opts': [
            "TEER 0,1: Mgmt/Uni",
            "TEER 2: Tech/College",
            "TEER 3: Trades/Admin",
            "TEER 4,5: Manual/Sec"
        ],
        'teer_manual_help': "If not found, select:",
        'exp_label': "Years Experience",
        'lang_info': "Reqs: Lvl 7 (B2) | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French", 'sp_fr_label': "Oral Level",
        'oev_info': "**ℹ️ VJO:** Validated Offer.",
        'vjo_label': "Validated Offer?", 'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Region"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "AEC, DEC, etc.",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "PR or Citizen.",
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Cert.",
        'g_step5': "5. Federal", 'g_desc5': "PR.",
        'noc_link_text': "🔎 Search NOC",
        'exp_title': "Work Experience (5 years)",
        'exp_qc_label': "Months in Quebec", 'exp_ca_label': "Months in Canada", 'exp_for_label': "Months Abroad"
    }
}
lang = t[st.session_state.language]

# --- 5. DATA JOBS ---
jobs_db = {
    "ingenie": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"}
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
st.markdown(f"""
<div class="pro-header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
    <div>
        <h1>{lang['brand']}</h1>
        <p style="color:#e0e0e0; margin:0; font-size:0.9rem;">{lang['subtitle']}</p>
    </div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
</div>
""", unsafe_allow_html=True)

c_sp, c_btn = st.columns([3, 1])
with c_btn: st.button(lang['btn_lang'], on_click=cycle_language, type="secondary", key="top_lang_btn", use_container_width=True)
st.markdown("###")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

# --- PESTAÑA CALCULADORA ---
with main_tab_calc:
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # --- PASO 1: PERFIL ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab1_sub']}</span>", unsafe_allow_html=True)
        
        st.markdown(f"**{lang['loc_label']}**")
        curr_loc = st.session_state.current_loc
        if curr_loc not in lang['loc_opts']: curr_loc = lang['loc_opts'][2]
        st.session_state.current_loc = st.radio("Loc", lang['loc_opts'], index=lang['loc_opts'].index(curr_loc), label_visibility="collapsed")
        
        if "bec" not in st.session_state.current_loc:
             st.session_state.origin_country = st.text_input(lang['country_label'], value=st.session_state.origin_country, placeholder="Ex: Belgique...")
             c_dest, c_date = st.columns(2)
             with c_dest:
                 st.selectbox(lang['dest_city_label'], lang['city_opts'])
             with c_date:
                 st.date_input(lang['arrival_label'], value=st.session_state.arrival_date)
        
        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.session_state.age = st.number_input(lang['age'], 18, 65, st.session_state.age)
        with c2: st.session_state.spouse = st.checkbox(lang['spouse'], value=st.session_state.spouse)
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(lang['kids12'], 0, 5, st.session_state.k1)
        with c4: st.session_state.k2 = st.number_input(lang['kids13'], 0, 5, st.session_state.k2)
        
        if st.session_state.spouse:
            st.divider()
            st.info(lang.get('sp_header', 'Data'))
            c_sp1, c_sp2 = st.columns(2)
            with c_sp1: st.session_state.sp_age = st.number_input(lang['sp_age'], 18, 65, st.session_state.sp_age)
            with c_sp2: st.selectbox(lang['sp_edu'], ["PhD", "Master", "Bac", "Tech", "Sec"])
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 2: TRABAJO ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab2_sub']}</span>", unsafe_allow_html=True)
        
        st.text_input(lang['job_title'], placeholder=lang['job_place'])
        st.divider()
        
        current_idx = 0
        if st.session_state.teer_sel in lang['teer_opts']:
            current_idx = lang['teer_opts'].index(st.session_state.teer_sel)
        st.session_state.teer_sel = st.selectbox(lang['teer_label'], lang['teer_opts'], index=current_idx)
        st.session_state.edu = st.selectbox("Education", ["PhD", "Master", "Bachelor", "College (3y)", "Diploma (1-2y)", "Secondary"], index=2)
        
        st.divider()
        st.markdown(f"**{lang['exp_title']}**")
        st.number_input(lang['exp_qc_label'], 0, 60, st.session_state.exp_qc, key="eqc")
        st.number_input(lang['exp_ca_label'], 0, 60, st.session_state.exp_ca, key="eca")
        st.number_input(lang['exp_for_label'], 0, 60, st.session_state.exp_foreign, key="efor")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 3: IDIOMAS ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.info(lang['lang_info'])
        st.select_slider(lang['fr_oral'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        st.select_slider(lang['fr_write'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        st.select_slider(lang['en'], ["0", "Beg", "Int", "Adv"], value="0")

        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang['sp_fr_title']}**")
            st.select_slider("Niveau", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 4: QUEBEC ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab4_sub']}</span>", unsafe_allow_html=True)
        
        st.info(lang['oev_info'])
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']: vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx)
        
        st.divider()
        st.info(lang['dip_qc_help'])
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio(lang['dip_qc_label'], lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True)
        
        st.divider()
        st.info(lang['fam_qc_help'])
        curr_fam = st.session_state.q_fam_val
        if curr_fam not in lang['yes_no']: curr_fam = lang['yes_no'][0]
        st.session_state.q_fam_val = st.radio(lang['fam_qc_label'], lang['yes_no'], index=lang['yes_no'].index(curr_fam), horizontal=True)

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 1, 2])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['calc'], type="primary", on_click=trigger_calculation)

    # RESULTADOS
    if st.session_state.show_results:
        score = 580 # Simulado para seguridad
        st.markdown(f"""<div class="result-box"><h2>{lang['res_title']}: {score} / 1350</h2></div>""", unsafe_allow_html=True)
        st.success(lang['advice_good'])
        if st.button("🔄"): reset_calc(); st.rerun()

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

# FOOTER
st.markdown("---")
c1, c2 = st.columns(2)
with c1: st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
with c2: st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com") 
st.markdown("###")
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
