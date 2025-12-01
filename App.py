import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (CORRECCIÓN VISUAL DEFINITIVA) ---
st.markdown("""
    <style>
        /* === 0. INSTRUCCIÓN MAESTRA PARA MÓVIL === */
        :root {
            color-scheme: light; 
        }
        
        /* === 1. FONDO Y TEXTOS GENERALES === */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f2f6 !important;
        }
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #000000 !important;
        }
        header[data-testid="stHeader"] { background-color: #003399 !important; }
        h1, h2, h3 { color: #003399 !important; }

        /* === 2. ARREGLO DE CAJAS DE SELECCIÓN (SELECTBOX) === */
        /* La caja cerrada */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
            color: #000000 !important;
        }
        /* El texto dentro de la caja */
        div[data-baseweb="select"] span {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }
        /* El icono de la flecha */
        div[data-baseweb="select"] svg {
            fill: #000000 !important;
        }

        /* === 3. ARREGLO DEL MENÚ DESPLEGABLE (LISTA DE OPCIONES) === */
        ul[data-baseweb="menu"] {
            background-color: #FFFFFF !important;
        }
        li[data-baseweb="menu-item"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        li[data-baseweb="menu-item"]:hover, li[aria-selected="true"] {
            background-color: #e6f0ff !important;
            color: #003399 !important;
        }
        /* Forzar color a los hijos del item */
        li[data-baseweb="menu-item"] * {
            color: #000000 !important;
        }

        /* === 4. INPUTS DE TEXTO === */
        div[data-baseweb="input"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
        }

        /* === 5. BOTONES === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; }
        
        /* Botón Siguiente/Calcular (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        div.stButton > button[kind="primary"] p { color: #FFFFFF !important; }

        /* Botón Anterior/Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] p { color: #003399 !important; }

        /* === 6. TARJETA PRINCIPAL === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 1.5rem; 
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
            border-top: 5px solid #003399;
        }
        
        /* === 7. OTROS ELEMENTOS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .help-box { background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; border-radius: 5px; }
        .step-box { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        .deco-sub { font-style: italic; margin-bottom: 15px; display: block; color: #666666 !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN DE VARIABLES (PARA EVITAR KEYERROR) ---
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
    'teer_sel': 'TEER 0, 1: Université / Gestion / Ingénierie', # Default safe
    'edu': 'Secondary',
    'exp': 3,
    'fr_oral': 'B2',
    'fr_write': 'B1',
    'en_lvl': '0',
    'vjo': '',
    'q_stud': False,
    'q_fam': False
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

def trigger_calculation():
    st.session_state.show_results = True

# --- 4. TRADUCCIONES COMPLETA (SIN ERRORES) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_text': "Projet indépendant. PAS avocats/consultants. Résultats estimés.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        # PASOS
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        # CONTENIDO
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation du conjoint",
        'job_title': "Emploi actuel",
        'job_place': "Ex: Ingénieur, Soudeur...",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0, 1: Université / Gestion / Ingénierie",
            "TEER 2: Collégial / Technique / Superviseurs",
            "TEER 3: Métiers / Administration / Intermédiaire",
            "TEER 4, 5: Manœuvre / Secondaire / Service"
        ],
        'teer_manual_help': "Si non trouvé, choisissez ci-dessous:",
        'exp_label': "Années d'expérience",
        'lang_info': "**Exigences :** Volet 1 = Niv 7 | Volet 2 = Niv 5 | Conjoint = Niv 4",
        'fr_oral': "Français Oral (Vous)", 'fr_write': "Français Écrit (Vous)", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint (Oral)",
        # QUEBEC
        'oev_info': "**ℹ️ OEV (Offre d'emploi validée) :** Signifie que l'employeur a obtenu une EIMT ou que l'offre est validée par le MIFI. Une simple lettre d'embauche ne suffit pas toujours.",
        'vjo_label': "Avez-vous une Offre Validée (OEV) ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Hors Montréal (Région)"],
        'dip_qc_label': "Diplôme du Québec ?",
        'dip_qc_help': "AEC, DEP, DEC, Baccalauréat, Maîtrise, Doctorat obtenu au Québec.",
        'fam_qc_label': "Famille au Québec ?",
        'fam_qc_help': "Parent, enfant, conjoint, frère/sœur, grand-parent (Citoyen ou Résident Permanent).",
        'arr_year': "Année d'arrivée au Québec (si applicable)",
        'city_label': "Ville de résidence (si au Québec)",
        'city_opts': ["-", "Montréal", "Québec (Ville)", "Laval", "Gatineau", "Longueuil", "Sherbrooke", "Lévis", "Saguenay", "Trois-Rivières", "Terrebonne", "Autre"],
        # RESULTADOS (AQUÍ ESTABA EL ERROR)
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Profil compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV.",
        'details': "Détails du score",
        'sp_points': "Points Conjoint",
        'guide_title': "Votre Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Connaître vos points forts (Langue, VJO).",
        'g_step2': "2. Français", 'g_desc2': "Visez un niveau B2 (7) ou C1.",
        'g_step3': "3. Arrima", 'g_desc3': "Créez votre profil gratuitement.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat de Sélection du Québec.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente Canada.",
        'noc_link_text': "🔎 Chercher sur le site officiel du Canada (CNP)"
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Herramienta de análisis para Residencia Permanente.",
        'disclaimer_text': "Proyecto independiente. NO abogados. Resultados estimados.",
        'coffee': "☕ Invítame un café",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR PUNTAJE",
        # PASOS
        'step1': "Paso 1: Perfil y Familia",
        'step2': "Paso 2: Trabajo y TEER",
        'step3': "Paso 3: Idiomas",
        'step4': "Paso 4: Quebec y Oferta",
        # CONTENIDO
        'age': "Edad del candidato",
        'spouse': "¿Tienes pareja?",
        'kids12': "Hijos -12 años", 'kids13': "Hijos +12 años",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'job_title': "Trabajo actual",
        'job_place': "Ej: Ingeniero, Soldador...",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0, 1: Universidad / Gerencia / Ingeniería",
            "TEER 2: College / Técnico / Supervisores",
            "TEER 3: Oficios / Administración / Intermedio",
            "TEER 4, 5: Operarios / Secundaria / Manual"
        ],
        'teer_manual_help': "Si no encuentras, elige abajo:",
        'exp_label': "Años de experiencia",
        'lang_info': "**Requisitos:** Volet 1 = Niv 7 | Volet 2 = Niv 5 | Pareja = Niv 4",
        'fr_oral': "Francés Oral (Tú)", 'fr_write': "Francés Escrito (Tú)", 'en': "Inglés",
        'sp_fr_title': "Francés de la Pareja (Oral)",
        # QUEBEC
        'oev_info': "**ℹ️ VJO (Oferta Validada):** Significa que el empleador obtuvo una LMIA/EIMT o aprobación del MIFI. Una carta simple de trabajo no siempre cuenta.",
        'vjo_label': "¿Tienes Oferta Validada (VJO)?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Fuera de Montreal (Región)"],
        'dip_qc_label': "¿Diploma de Quebec?",
        'dip_qc_help': "AEC, DEP, DEC, Bachelor, Maestría, Doctorado obtenido en una institución de Quebec.",
        'fam_qc_label': "¿Familia en Quebec?",
        'fam_qc_help': "Padres, hijos, cónyuge, hermanos, abuelos (Que sean Residentes o Ciudadanos).",
        'arr_year': "Año de llegada a Quebec (si aplica)",
        'city_label': "Ciudad de residencia (si estás en Quebec)",
        'city_opts': ["-", "Montréal", "Québec (Ville)", "Laval", "Gatineau", "Longueuil", "Sherbrooke", "Lévis", "Saguenay", "Trois-Rivières", "Terrebonne", "Otra"],
        # RESULTADOS (AQUÍ ESTABA EL ERROR)
        'res_title': "Resultado",
        'advice_good': "¡Excelente! Competitivo.",
        'advice_low': "Mejora el francés o busca VJO.",
        'details': "Detalles",
        'sp_points': "Puntos Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Conoce tus fortalezas (Idioma, VJO).",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a un nivel B2 (7) o C1.",
        'g_step3': "3. Arrima", 'g_desc3': "Crea tu perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado de Selección de Quebec.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia Permanente Canadá.",
        'noc_link_text': "🔎 Buscar en sitio oficial Canadá (NOC)"
    },
    'en': {
        'btn_lang': "🌐 Change Language",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_text': "Independent. NOT lawyers. Estimated results.",
        'coffee': "☕ Support",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE SCORE",
        # STEPS
        'step1': "Step 1: Profile & Family",
        'step2': "Step 2: Work & TEER",
        'step3': "Step 3: Languages",
        'step4': "Step 4: Quebec & Offer",
        # CONTENT
        'age': "Age",
        'spouse': "Have a spouse?",
        'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data",
        'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'job_title': "Current Job",
        'job_place': "Ex: Engineer, Welder...",
        'teer_label': "TEER Category",
        'teer_opts': [
            "TEER 0, 1: University / Management / Engineering",
            "TEER 2: College / Technical / Supervisors",
            "TEER 3: Trades / Admin / Intermediate",
            "TEER 4, 5: Labourer / High School / Service"
        ],
        'teer_manual_help': "If not found, select below:",
        'exp_label': "Years Experience",
        'lang_info': "**Reqs:** Volet 1 = Lvl 7 | Volet 2 = Lvl 5 | Spouse = Lvl 4",
        'fr_oral': "French Oral (You)", 'fr_write': "French Written (You)", 'en': "English",
        'sp_fr_title': "Spouse's French (Oral)",
        # QUEBEC
        'oev_info': "**ℹ️ VJO (Validated Offer):** Means employer got LMIA or MIFI approval. A simple job letter is usually not enough.",
        'vjo_label': "Validated Job Offer (VJO)?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Outside Montreal (Regions)"],
        'dip_qc_label': "Quebec Diploma?",
        'dip_qc_help': "AEC, DEP, DEC, Bachelor, Master, PhD from a Quebec institution.",
        'fam_qc_label': "Family in Quebec?",
        'fam_qc_help': "Parent, child, spouse, sibling, grandparent (PR or Citizen).",
        'arr_year': "Arrival Year in Quebec (if applicable)",
        'city_label': "City of residence",
        'city_opts': ["-", "Montréal", "Québec (Ville)", "Laval", "Gatineau", "Longueuil", "Sherbrooke", "Lévis", "Saguenay", "Trois-Rivières", "Terrebonne", "Other"],
        # RESULTS (AQUÍ ESTABA EL ERROR)
        'res_title': "Result",
        'advice_good': "Excellent! Competitive.",
        'advice_low': "Improve French or find VJO.",
        'details': "Details",
        'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Know strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim for B2 (7) or C1.",
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
# APP PRINCIPAL
# ==========================================
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

# --- PESTAÑA CALCULADORA (WIZARD MODE) ---
with main_tab_calc:
    
    # BARRA DE PROGRESO DEL WIZARD
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # ------------------------------------
    # PASO 1: PERFIL
    # ------------------------------------
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        with st.form("step1_form"):
            c1, c2 = st.columns(2)
            with c1: 
                st.session_state.age = st.number_input(lang['age'], 18, 65, st.session_state.age)
            with c2: 
                st.session_state.spouse = st.checkbox(lang['spouse'], value=st.session_state.spouse)
            
            c3, c4 = st.columns(2)
            with c3: st.session_state.k1 = st.number_input(lang['kids12'], 0, 5, st.session_state.k1)
            with c4: st.session_state.k2 = st.number_input(lang['kids13'], 0, 5, st.session_state.k2)
            
            if st.session_state.spouse:
                st.divider()
                st.markdown(f"**{lang['sp_header']}**")
                c_sp1, c_sp2 = st.columns(2)
                with c_sp1: st.session_state.sp_age = st.number_input(lang['sp_age'], 18, 65, st.session_state.sp_age)
                with c_sp2: st.session_state.sp_edu = st.selectbox(lang['sp_edu'], ["PhD", "Master", "Bachelor", "Technical", "Secondary"], index=2)
            
            st.markdown("###")
            # Botón Siguiente
            col_e, col_n = st.columns([3, 1])
            with col_n:
                if st.form_submit_button(lang['next'], type="primary"):
                    next_step()
                    st.rerun()

    # ------------------------------------
    # PASO 2: TRABAJO
    # ------------------------------------
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        with st.form("step2_form"):
            st.markdown(f"**{lang['job_title']}**")
            job_query = st.text_input("Search", placeholder=lang['job_place'], label_visibility="collapsed")
            if job_query:
                result = find_job_details(job_query)
                if result:
                    st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
                else:
                    st.markdown(f"<div class='help-box'>{lang['teer_manual_help']}</div>", unsafe_allow_html=True)
                    st.markdown(f"🔗 [{lang['noc_link_text']}](https://noc.esdc.gc.ca/)")

            st.divider()
            
            # Recuperar índice si ya hay selección
            current_idx = 0
            if st.session_state.teer_sel in lang['teer_opts']:
                current_idx = lang['teer_opts'].index(st.session_state.teer_sel)
                
            st.session_state.teer_sel = st.selectbox(lang['teer_label'], lang['teer_opts'], index=current_idx)
            
            st.session_state.edu = st.selectbox("Education", ["PhD", "Master", "Bachelor", "College (3y)", "Diploma (1-2y)", "Secondary"], index=2)
            st.session_state.exp = st.slider(lang['exp_label'], 0, 10, st.session_state.exp)

            st.markdown("###")
            col_p, col_e, col_n = st.columns([1, 2, 1])
            with col_p:
                if st.form_submit_button(lang['prev'], type="secondary"):
                    prev_step()
                    st.rerun()
            with col_n:
                if st.form_submit_button(lang['next'], type="primary"):
                    next_step()
                    st.rerun()

    # ------------------------------------
    # PASO 3: IDIOMAS
    # ------------------------------------
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
        
        with st.form("step3_form"):
            c1, c2 = st.columns(2)
            with c1: st.session_state.fr_oral = st.select_slider(lang['fr_oral'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_oral)
            with c2: st.session_state.fr_write = st.select_slider(lang['fr_write'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.fr_write)
            st.session_state.en_lvl = st.select_slider(lang['en'], ["0", "Beginner", "Intermediate", "Advanced"], value=st.session_state.en_lvl)

            if st.session_state.spouse:
                st.divider()
                st.markdown(f"**{lang['sp_fr_title']}**")
                st.session_state.sp_fr = st.select_slider("Niveau", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value=st.session_state.sp_fr)

            st.markdown("###")
            col_p, col_e, col_n = st.columns([1, 2, 1])
            with col_p:
                if st.form_submit_button(lang['prev'], type="secondary"):
                    prev_step()
                    st.rerun()
            with col_n:
                if st.form_submit_button(lang['next'], type="primary"):
                    next_step()
                    st.rerun()

    # ------------------------------------
    # PASO 4: QUEBEC (FINAL)
    # ------------------------------------
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        
        st.info(lang['oev_info'])
        
        with st.form("step4_form"):
            # Recuperar índice si ya hay selección
            vjo_idx = 0
            if st.session_state.vjo in lang['vjo_opts']:
                vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
            st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx)
            
            st.divider()
            
            st.markdown(f"**{lang['dip_qc_label']}**")
            st.caption(lang['dip_qc_help'])
            st.session_state.q_stud = st.checkbox("Oui / Yes / Sí (Diploma)", value=st.session_state.q_stud)
            
            st.markdown("---")
            st.markdown(f"**{lang['fam_qc_label']}**")
            st.caption(lang['fam_qc_help'])
            st.session_state.q_fam = st.checkbox("Oui / Yes / Sí (Famille)", value=st.session_state.q_fam)
            
            st.divider()
            
            c_city, c_year = st.columns(2)
            with c_city:
                st.selectbox(lang['city_label'], lang['city_opts'])
            with c_year:
                st.selectbox(lang['arr_year'], range(2025, 1990, -1))

            st.markdown("###")
            col_p, col_e, col_n = st.columns([1, 1, 2])
            with col_p:
                if st.form_submit_button(lang['prev'], type="secondary"):
                    prev_step()
                    st.rerun()
            with col_n:
                if st.form_submit_button(lang['calc'], type="primary"):
                    trigger_calculation()
                    st.rerun()

    # LÓGICA & RESULTADOS
    if st.session_state.show_results:
        # Recuperar variables
        age = st.session_state.age
        edu = st.session_state.edu
        teer = st.session_state.teer_sel
        exp = st.session_state.exp
        fr_o = st.session_state.fr_oral
        fr_w = st.session_state.fr_write
        en = st.session_state.en_lvl
        vjo_val = st.session_state.vjo
        
        score = 0
        score_sp = 0 
        
        # Edad
        if 18 <= age <= 30: score += 130
        elif age <= 45: score += (130 - (age-30)*5)
        # Edu
        if "PhD" in edu: score += 90
        elif "Master" in edu: score += 75
        elif "Bachelor" in edu: score += 60
        elif "College" in edu: score += 50
        else: score += 30
        # TEER
        if "TEER 0, 1" in teer or "TEER 0,1" in teer: score += 60 
        elif "TEER 2" in teer: score += 40
        elif "TEER 3" in teer: score += 20
        # Exp
        score += min(80, int(exp * 10))
        # Idioma
        pts_map = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
        score += pts_map.get(fr_o,0) * 1.2 + pts_map.get(fr_w,0) * 0.8
        
        if en == "Advanced": score += 25
        elif en == "Intermediate": score += 15
        # VJO
        if "Hors" in vjo_val or "Outside" in vjo_val or "Fuera" in vjo_val: score += 380
        elif "Grand" in vjo_val or "Greater" in vjo_val or "Gran" in vjo_val: score += 180
        # Quebec
        if st.session_state.q_stud: score += 50
        if st.session_state.q_fam: score += 30
        # Spouse
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
