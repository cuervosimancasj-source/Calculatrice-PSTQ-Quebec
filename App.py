import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (DISEÑO PREMIUM + ANTI-DARK MODE) ---
st.markdown("""
    <style>
        /* === 0. FORZADO GLOBAL MODO CLARO === */
        :root { color-scheme: light !important; }
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important; /* Gris muy suave profesional */
            color: #000000 !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Ocultar header default de Streamlit para poner el nuestro */
        header[data-testid="stHeader"] { visibility: hidden; }
        
        /* === 1. ENCABEZADO DE LUJO (NUEVO) === */
        .pro-header {
            background-color: #003399; /* Azul Quebec */
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .pro-header img {
            height: 50px;
            border: 2px solid white;
            border-radius: 4px;
        }
        .pro-header h1 {
            color: white !important;
            margin: 0;
            font-size: 1.8rem;
            font-weight: 700;
        }
        .pro-header p {
            color: #e0e0e0 !important;
            margin: 0;
            font-size: 0.9rem;
        }

        /* === 2. TEXTOS Y ETIQUETAS === */
        p, label, h2, h3, h4, li, div, span { color: #000000 !important; }
        h2, h3 { color: #003399 !important; font-weight: 700; }

        /* === 3. INPUTS Y SELECTORES (BLINDADOS) === */
        div[data-baseweb="select"] > div, 
        div[data-baseweb="input"] > div,
        div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ced4da !important;
            border-radius: 6px !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
        }
        /* Texto selector cerrado */
        div[data-baseweb="select"] span {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

        /* === 4. MENÚ DESPLEGABLE === */
        ul[data-baseweb="menu"] { background-color: #FFFFFF !important; }
        li[data-baseweb="menu-item"] { background-color: #FFFFFF !important; color: #000000 !important; }
        li[data-baseweb="menu-item"] * { color: #000000 !important; }
        li[data-baseweb="menu-item"]:hover, li[aria-selected="true"] { background-color: #e6f0ff !important; }

        /* === 5. BOTONES MODERNOS === */
        div.stButton > button { width: 100%; border-radius: 6px; font-weight: bold; transition: 0.3s; }
        
        /* Primario (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            border: none !important;
            color: #FFFFFF !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }
        div.stButton > button[kind="primary"]:hover { background-color: #002266 !important; box-shadow: 0 4px 8px rgba(0,0,0,0.3); }

        /* Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }

        /* === 6. TARJETA FORMULARIO === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 2rem; 
            border-radius: 15px;
            border-top: 6px solid #003399;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        }
        
        /* Cajas Informativas */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; font-size: 0.95rem;}
        .help-box { background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .result-box { 
            background: linear-gradient(135deg, #003399 0%, #0044cc 100%); 
            padding: 25px; 
            border-radius: 12px; 
            text-align: center; 
            margin-top: 20px; 
            color: white !important;
            box-shadow: 0 5px 15px rgba(0,51,153,0.3);
        }
        .result-box h2 { color: #FFFFFF !important; margin: 0; font-size: 2.2rem; }
        
        /* Footer */
        .footer { margin-top: 60px; padding: 30px; border-top: 1px solid #e0e0e0; text-align: center; color: #666; }
        
        /* Botones +/- */
        button[tabindex="-1"] { background-color: #f1f3f4 !important; color: #000 !important; border: 1px solid #ccc !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN ---
default_values = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'teer_sel': '', 'edu': 'Secondary', 'exp': 3,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': ''
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]

def trigger_calculation(): st.session_state.show_results = True

# --- 4. TRADUCCIONES ---
t = {
    'fr': {
        'btn_lang': "🌐 Français",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Simulation de pointage pour l'immigration au Québec",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce site est un outil informatif indépendant. Nous ne sommes PAS affiliés au gouvernement du Québec (MIFI) ni consultants en immigration.",
        'coffee': "☕ Soutenir le projet",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "VOIR MON SCORE",
        'yes_no': ["Non", "Oui"],
        'step1': "Profil Personnel",
        'step2': "Expérience & Métier",
        'step3': "Compétences Linguistiques",
        'step4': "Facteurs Québec",
        'tab1_sub': "Commençons par votre situation personnelle et familiale.",
        'tab2_sub': "Votre Classification Nationale des Professions (CNP) est cruciale.",
        'tab3_sub': "Le français est le facteur le plus important de la grille.",
        'tab4_sub': "Avez-vous des liens ou une offre au Québec ?",
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint(e) qui vous accompagne ?",
        'kids12': "Enfants (-12 ans)", 'kids13': "Enfants (13-21 ans)",
        'sp_header': "Informations du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Niveau d'études du conjoint",
        'job_title': "Quel est votre métier principal ?",
        'job_place': "Ex: Soudeur, Infirmier (Appuyez sur Entrée)",
        'teer_label': "Niveau de compétence (TEER)",
        'teer_opts': [
            "TEER 0, 1: Gestion / Université / Ingénieurs",
            "TEER 2: Technique / Collégial / Superviseurs",
            "TEER 3: Métiers / Administration / Intermédiaire",
            "TEER 4, 5: Manœuvre / Secondaire / Service"
        ],
        'teer_manual_help': "Si le métier n'apparait pas, sélectionnez manuellement :",
        'exp_label': "Années d'expérience dans ce métier",
        'lang_info': "💡 **Niveaux requis :** Principal = Niv 7 (B2) | Conjoint = Niv 4 (A2)",
        'fr_oral': "Français Oral (Principal)", 'fr_write': "Français Écrit (Principal)", 'en': "Anglais",
        'sp_fr_title': "Niveau de Français du Conjoint",
        'sp_fr_label': "Compréhension et Expression Orale",
        'oev_info': "**ℹ️ Offre d'emploi validée (OEV) :** Une offre formelle approuvée par le MIFI. Une simple lettre d'embauche n'est pas une OEV.",
        'vjo_label': "Détenez-vous une Offre d'Emploi Validée ?",
        'vjo_opts': ["Non", "Oui, dans le Grand Montréal", "Oui, Hors Montréal (Région)"],
        'dip_qc_label': "Diplôme du Québec",
        'dip_qc_help': "Avez-vous obtenu un diplôme (AEC, DEC, Bac, etc.) d'un établissement au Québec ?",
        'fam_qc_label': "Famille au Québec",
        'fam_qc_help': "Avez-vous de la famille proche (Résident ou Citoyen) habitant au Québec ?",
        'arr_year': "Année d'arrivée prévue",
        'city_label': "Ville de destination",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Autre"],
        'res_title': "Score Total Estimé",
        'advice_good': "Félicitations ! Votre profil est très compétitif.",
        'advice_low': "Conseil : Améliorez le français ou visez une OEV en région.",
        'details': "Voir le détail des points",
        'sp_points': "Points Conjoint",
        'guide_title': "Étapes vers la Résidence",
        'g_step1': "1. Calcul du Score", 'g_desc1': "Vérifiez votre admissibilité.",
        'g_step2': "2. Test de Français", 'g_desc2': "TEFAQ ou TCF-Q obligatoire.",
        'g_step3': "3. Arrima", 'g_desc3': "Déclaration d'intérêt en ligne.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat de Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Vérification médicale et sécurité.",
        'noc_link_text': "🔎 Trouver mon code CNP (Site Officiel)"
    },
    'es': {
        'btn_lang': "🌐 Español",
        'brand': "Calculadora PSTQ",
        'subtitle': "Simulación de puntaje para Residencia Permanente Quebec",
        'disclaimer_title': "⚠️ AVISO LEGAL IMPORTANTE",
        'disclaimer_text': "Este sitio es una herramienta informativa independiente. NO somos parte del gobierno (MIFI) ni abogados de inmigración.",
        'coffee': "☕ Apoyar proyecto",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "VER MI PUNTAJE",
        'yes_no': ["No", "Sí"],
        'step1': "Perfil y Familia",
        'step2': "Trabajo y TEER",
        'step3': "Idiomas",
        'step4': "Quebec y Oferta",
        'tab1_sub': "El punto de partida de tu proyecto migratorio.",
        'tab2_sub': "Tu oficio define tu categoría en el PSTQ.",
        'tab3_sub': "El francés es el factor más importante.",
        'tab4_sub': "Finaliza tu puntaje con los factores locales.",
        'age': "Edad del candidato",
        'spouse': "¿Te acompaña tu pareja?",
        'kids12': "Hijos (-12 años)", 'kids13': "Hijos (13-21 años)",
        'sp_header': "Información de la Pareja",
        'sp_age': "Edad de la pareja", 'sp_edu': "Nivel estudios pareja",
        'job_title': "¿Cuál es tu profesión actual?",
        'job_place': "Ej: Ingeniero, Soldador (Presiona Enter)",
        'teer_label': "Nivel de competencia (TEER)",
        'teer_opts': [
            "TEER 0, 1: Universidad / Gerencia / Ingeniería",
            "TEER 2: Técnico / College / Supervisores",
            "TEER 3: Oficios / Administración / Intermedio",
            "TEER 4, 5: Operarios / Secundaria / Manual"
        ],
        'teer_manual_help': "Si no aparece, selecciona manualmente:",
        'exp_label': "Años de experiencia",
        'lang_info': "💡 **Requisitos:** Principal = Niv 7 (B2) | Pareja = Niv 4 (A2)",
        'fr_oral': "Francés Oral (Tú)", 'fr_write': "Francés Escrito (Tú)", 'en': "Inglés",
        'sp_fr_title': "Nivel de Francés de la Pareja",
        'sp_fr_label': "Comprensión y Expresión Oral",
        'oev_info': "**ℹ️ Oferta Validada (VJO):** Documento oficial aprobado por el MIFI. Una carta de trabajo simple no cuenta como VJO.",
        'vjo_label': "¿Tienes una Oferta de Empleo Validada?",
        'vjo_opts': ["No", "Sí, en Gran Montreal", "Sí, Fuera de Montreal (Región)"],
        'dip_qc_label': "Diploma de Quebec",
        'dip_qc_help': "¿Tienes un título (AEC, DEC, Bachelor, etc.) obtenido en una institución de Quebec?",
        'fam_qc_label': "Familia en Quebec",
        'fam_qc_help': "¿Tienes familiares directos (Residentes o Ciudadanos) viviendo en Quebec?",
        'arr_year': "Año estimado de llegada",
        'city_label': "Ciudad de destino",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Otra"],
        'res_title': "Puntaje Total Estimado",
        'advice_good': "¡Felicidades! Tienes un perfil competitivo.",
        'advice_low': "Consejo: Mejora el francés o busca una oferta en región.",
        'details': "Ver desglose de puntos",
        'sp_points': "Puntos Pareja",
        'guide_title': "Tu Camino a la Residencia",
        'g_step1': "1. Cálculo", 'g_desc1': "Evalúa tus posibilidades.",
        'g_step2': "2. Examen Francés", 'g_desc2': "TEFAQ o TCF-Q son vitales.",
        'g_step3': "3. Arrima", 'g_desc3': "Declaración de interés.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado de Selección.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia Permanente.",
        'noc_link_text': "🔎 Buscar mi código NOC (Sitio Oficial)"
    },
    'en': {
        'btn_lang': "🌐 English",
        'brand': "PSTQ Calculator",
        'subtitle': "Score Analysis for Quebec Permanent Residency.",
        'disclaimer_title': "⚠️ IMPORTANT NOTICE",
        'disclaimer_text': "This is an independent project. We are NOT lawyers or consultants. We do NOT represent the MIFI.",
        'coffee': "☕ Buy me a coffee",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CHECK MY SCORE",
        'yes_no': ["No", "Yes"],
        'step1': "Profile & Family",
        'step2': "Work & TEER",
        'step3': "Language Skills",
        'step4': "Quebec Factors",
        'tab1_sub': "The starting point of your immigration journey.",
        'tab2_sub': "Your trade is the core of the PSTQ program.",
        'tab3_sub': "French is the key to success in Quebec.",
        'tab4_sub': "Finalize your score with local assets.",
        'age': "Main Applicant Age",
        'spouse': "Do you have a spouse?",
        'kids12': "Children (-12 years)", 'kids13': "Children (13-21 years)",
        'sp_header': "Spouse Information",
        'sp_age': "Spouse Age", 'sp_edu': "Spouse Education",
        'job_title': "Current Occupation",
        'job_place': "Ex: Engineer, Welder (Press Enter)",
        'teer_label': "TEER Category",
        'teer_opts': [
            "TEER 0, 1: University / Management / Engineering",
            "TEER 2: College / Technical / Supervisors",
            "TEER 3: Trades / Admin / Intermediate",
            "TEER 4, 5: Labourer / High School / Service"
        ],
        'teer_manual_help': "If not found, select manually below:",
        'exp_label': "Years of Experience",
        'lang_info': "💡 **Reqs:** Main = Lvl 7 (B2) | Spouse = Lvl 4 (A2)",
        'fr_oral': "French Oral (You)", 'fr_write': "French Written (You)", 'en': "English",
        'sp_fr_title': "Spouse's French Level",
        'sp_fr_label': "Oral Proficiency",
        'oev_info': "**ℹ️ Validated Job Offer (VJO):** Formal offer approved by MIFI. A simple job letter is not a VJO.",
        'vjo_label': "Do you have a Validated Job Offer?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Outside Montreal"],
        'dip_qc_label': "Quebec Diploma",
        'dip_qc_help': "Did you obtain a degree (AEC, DEC, Bachelor, etc.) in Quebec?",
        'fam_qc_label': "Family in Quebec",
        'fam_qc_help': "Do you have immediate family (PR or Citizen) living in Quebec?",
        'arr_year': "Estimated Arrival",
        'city_label': "Destination City",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Other"],
        'res_title': "Estimated Score",
        'advice_good': "Congratulations! Strong profile.",
        'advice_low': "Tip: Improve French or find a VJO.",
        'details': "Score Details",
        'sp_points': "Spouse Points",
        'guide_title': "Your Roadmap",
        'g_step1': "1. Score Check", 'g_desc1': "Assess eligibility.",
        'g_step2': "2. French Test", 'g_desc2': "Aim for B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Expression of Interest.",
        'g_step4': "4. CSQ", 'g_desc4': "Selection Certificate.",
        'g_step5': "5. Federal", 'g_desc5': "Permanent Residency.",
        'noc_link_text': "🔎 Find NOC Code (Official Site)"
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
# HEADER PREMIUM CON BANDERA (URL EXTERNA FIABLE)
st.markdown(f"""
<div class="pro-header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" alt="Quebec Flag">
    <div>
        <h1>{lang['brand']}</h1>
        <p>{lang['subtitle']}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# BOTÓN DE IDIOMA FLOTANTE
c_lang_spacer, c_lang_btn = st.columns([3, 1])
with c_lang_btn:
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary", key="top_lang_btn")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

# --- PESTAÑA CALCULADORA ---
with main_tab_calc:
    
    # BARRA DE PROGRESO
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # --- PASO 1: PERFIL ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab1_sub']}</span>", unsafe_allow_html=True)
        
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
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 2: TRABAJO ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab2_sub']}</span>", unsafe_allow_html=True)
        
        st.markdown(f"**{lang['job_title']}**")
        
        def update_search():
            st.session_state.job_search_term = st.session_state.widget_search
            
        st.text_input("Search", value=st.session_state.job_search_term, placeholder=lang['job_place'], label_visibility="collapsed", key="widget_search", on_change=update_search)

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
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 3: IDIOMAS ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab3_sub']}</span>", unsafe_allow_html=True)
        st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1: st.session_state.fr_oral = st.select_slider(lang['fr_oral'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_oral, key="fro_input")
        with c2: st.session_state.fr_write = st.select_slider(lang['fr_write'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_write, key="frw_input")
        st.session_state.en_lvl = st.select_slider(lang['en'], ["0", "Beginner", "Intermediate", "Advanced"], value=st.session_state.en_lvl, key="en_input")

        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang['sp_fr_title']}**")
            st.session_state.sp_fr = st.select_slider(lang['sp_fr_label'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.sp_fr, key="spfr_input")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 4: QUEBEC (FINAL) ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab4_sub']}</span>", unsafe_allow_html=True)
        
        st.info(lang['oev_info'])
        
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']:
            vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx, key="vjo_input")
        
        st.divider()
        
        # DIPLOMA
        st.markdown(f"**{lang['dip_qc_label']}**")
        st.caption(lang['dip_qc_help'])
        
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio("DipQC", lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True, label_visibility="collapsed", key="q_stud_in")
        
        st.divider()
        
        # FAMILIA
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
