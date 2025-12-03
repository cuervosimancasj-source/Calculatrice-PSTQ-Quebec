import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (CARRUSEL + ANTI-INSTAGRAM) ---
st.markdown("""
    <style>
        /* === 0. BASE === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important;
            color: #333333 !important;
        }
        
        /* Textos */
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #333333 !important;
        }
        
        /* Header Oculto */
        header[data-testid="stHeader"] { background-color: #003399 !important; }

        /* === 1. CAJA VISUAL DEL CARRUSEL (Display) === */
        .stepper-box {
            background-color: #FFFFFF;
            color: #003399;
            border: 2px solid #003399;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1.1rem;
            min-height: 70px; /* Altura fija para texto largo */
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        /* === 2. BOTONES DE FLECHA (CARRUSEL) === */
        div[data-testid="column"] button {
            background-color: #f0f0f0 !important;
            color: #003399 !important;
            border: 1px solid #ccc !important;
            height: 50px !important;
            font-size: 1.5rem !important;
            padding: 0 !important;
            width: 100%;
        }
        div[data-testid="column"] button:hover {
            background-color: #e0e0e0 !important;
            border-color: #003399 !important;
        }

        /* === 3. INPUTS DE TEXTO (BLANCOS) === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #cccccc !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
            opacity: 1 !important;
        }

        /* === 4. BOTONES PRINCIPALES === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; }
        
        /* Primario (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
            height: 45px;
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
            height: 45px;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }
        
        /* Enlaces (Azul) */
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

        /* === 5. EXTRAS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 10px; border-radius: 5px; margin-bottom: 10px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; color: white; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; font-size: 0.8rem; color: #666; }
        
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
            font-size: 1.4rem;
            flex-grow: 1;
        }
        .pro-header p { color: #e0e0e0 !important; }
        .flag-icon { height: 40px; border: 1px solid white; border-radius: 4px; }
        
        /* Radio */
        div[role="radiogroup"] label { color: #000000 !important; }
        
        /* Botones +/- Numeric */
        button[tabindex="-1"] { background-color: #e0e0e0 !important; color: #000 !important; border: 1px solid #ccc !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (SIN DESPLEGABLES) ---
def render_carousel(label, options, key_name):
    """Selector visual con botones de flecha abajo"""
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    if label:
        st.markdown(f"**{label}**")
    
    # Caja Visual (Texto)
    current_val = options[st.session_state[f"{key_name}_idx"]]
    st.markdown(f"<div class='stepper-box'>{current_val}</div>", unsafe_allow_html=True)
    
    # Botones Debajo (Esquinas)
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1:
        if st.button("◀", key=f"prev_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
    with c3:
        if st.button("▶", key=f"next_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
    return current_val

# --- 4. INICIALIZACIÓN ---
default_vars = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': '', 'current_loc': '', 'origin_country': '', 
    'arrival_text': '',
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2, 'vjo_idx': 0
}
for k, v in default_vars.items():
    if k not in st.session_state:
        st.session_state[k] = v

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES COMPLETAS ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants en immigration et nous ne faisons pas partie du gouvernement (MIFI). L'usage est à titre informatif seulement.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        'yes_no': ["Non", "Oui"],
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        'tab1_sub': "Le point de départ de votre projet d'immigration.",
        'tab2_sub': "Votre métier est au cœur du programme PSTQ.",
        'tab3_sub': "Le français est la clé du succès au Québec.",
        'tab4_sub': "Finalisez votre pointage avec les atouts locaux.",
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre province)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée prévue (AAAA-MM-JJ)",
        'city_label': "Ville de destination au Québec",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Autre"],
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat (Univ)", "Technique (DEC)", "Secondaire/DEP"],
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur, Soudeur (Appuyez sur Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0, 1: Université / Gestion / Ingénierie",
            "TEER 2: Collégial / Technique / Superviseurs",
            "TEER 3: Métiers / Administration / Intermédiaire",
            "TEER 4, 5: Manœuvre / Secondaire / Service"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat (Univ)", "Collégial (3 ans)", "Diplôme (1-2 ans)", "Secondaire"],
        'teer_manual_help': "Si non trouvé, choisissez ci-dessous:",
        'exp_label': "Années d'expérience",
        'exp_title': "Expérience de travail (5 dernières années)",
        'exp_qc_label': "Mois au Québec", 'exp_ca_label': "Mois au Canada (Hors QC)", 'exp_for_label': "Mois à l'étranger",
        'lang_info': "**Exigences :** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral (Vous)", 'fr_write': "Français Écrit (Vous)", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint (Oral)",
        'oev_info': "ℹ️ **Offre d'emploi validée (OEV) :** Signifie que l'employeur a obtenu une EIMT ou que l'offre est validée par le MIFI.",
        'vjo_label': "Avez-vous une Offre Validée ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        'dip_qc_label': "Diplôme du Québec ?", 
        'dip_qc_help': "ℹ️ **Diplôme :** Avez-vous un diplôme (AEC, DEC, Bac, etc.) obtenu au Québec ?",
        'fam_qc_label': "Famille au Québec ?", 
        'fam_qc_help': "ℹ️ **Famille :** Avez-vous un parent, enfant, conjoint, frère/sœur (Résident/Citoyen) ?",
        'res_title': "Résultat Estimé", 'advice_good': "Excellent ! Profil compétitif.", 'advice_low': "Améliorez le français ou cherchez une OEV.",
        'details': "Détails du score", 'sp_points': "Points Conjoint",
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
        'brand': "Calculadora PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "No somos abogados ni asesores de migración y tampoco hacemos parte del gobierno (MIFI). Somos un proyecto independiente con fines informativos.",
        'coffee': "☕ Apoyar",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR PUNTAJE",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil y Familia",
        'step2': "Paso 2: Trabajo y TEER",
        'step3': "Paso 3: Idiomas",
        'step4': "Paso 4: Quebec y Oferta",
        'tab1_sub': "El punto de partida de tu proyecto migratorio.",
        'tab2_sub': "Tu oficio es el corazón del programa PSTQ.",
        'tab3_sub': "El francés es la llave del éxito en Quebec.",
        'tab4_sub': "Finaliza tu puntaje con los activos locales.",
        'loc_label': "¿Dónde te encuentras hoy?",
        'loc_opts': ["En Quebec", "Canadá (Otra provincia)", "En el extranjero"],
        'country_label': "País de residencia",
        'arrival_label': "Fecha estimada de llegada (AAAA-MM-DD)",
        'city_label': "Ciudad de destino en Quebec",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Otra"],
        'age': "Edad del candidato",
        'spouse': "¿Tienes pareja?",
        'kids12': "Hijos -12 años", 'kids13': "Hijos +12 años",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "Técnico (DEC)", "Secundaria/DEP"],
        'job_title': "Trabajo actual",
        'job_place': "Ej: Ingeniero, Soldador (Enter)...",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0, 1: Universidad / Gerencia / Ingeniería",
            "TEER 2: Técnico / College / Supervisores",
            "TEER 3: Oficios / Administración / Intermedio",
            "TEER 4, 5: Operarios / Secundaria / Manual"
        ],
        'edu_label': "Nivel de Estudios",
        'edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "College (3 años)", "Diploma (1-2 años)", "Secundaria"],
        'teer_manual_help': "Si no encuentras, elige abajo:",
        'exp_label': "Años de experiencia",
        'exp_title': "Experiencia Laboral (Últimos 5 años)",
        'exp_qc_label': "Meses en Quebec", 'exp_ca_label': "Meses en Canadá (Fuera QC)", 'exp_for_label': "Meses en el Extranjero",
        'lang_info': "**Requisitos:** Nivel 7 (B2) Principal | Nivel 4 (A2) Pareja",
        'fr_oral': "Francés Oral (Tú)", 'fr_write': "Francés Escrito (Tú)", 'en': "Inglés",
        'sp_fr_title': "Francés de la Pareja (Oral)",
        'oev_info': "ℹ️ **VJO (Oferta Validada):** Documento oficial con LMIA o aprobada por el MIFI.",
        'vjo_label': "¿Tienes Oferta Validada?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Fuera de Montreal"],
        'dip_qc_label': "¿Diploma de Quebec?",
        'dip_qc_help': "ℹ️ **Diploma:** ¿Tienes un título (AEC, DEC, Bachelor, etc.) obtenido en Quebec?",
        'fam_qc_label': "¿Familia en Quebec?",
        'fam_qc_help': "ℹ️ **Familia:** ¿Tienes familiares directos (Padres, hijos, cónyuge, hermanos) Residentes o Ciudadanos?",
        'res_title': "Resultado Estimado", 'advice_good': "¡Excelente! Competitivo.", 'advice_low': "Mejora el francés.",
        'details': "Detalles del puntaje", 'sp_points': "Puntos Pareja",
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
        'brand': "Calculatrice PSTQ",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "We are not lawyers or immigration consultants and we are not part of the government. We are an independent project.",
        'coffee': "☕ Support",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE SCORE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Personal and family situation.",
        'tab2_sub': "Experience and trade.",
        'tab3_sub': "Language skills.", 'tab4_sub': "Local factors.",
        'loc_label': "Current location?",
        'loc_opts': ["In Quebec", "Canada (Other prov.)", "Abroad"],
        'country_label': "Country of Residence",
        'arrival_label': "Estimated Arrival Date",
        'city_label': "Destination City",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Other"],
        'age': "Age", 'spouse': "Have a spouse?",
        'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        'job_title': "Current Job", 'job_place': "Ex: Engineer (Press Enter)...",
        'teer_label': "TEER Category",
        'teer_opts': [
            "TEER 0, 1: University / Management / Engineering",
            "TEER 2: College / Technical / Supervisors",
            "TEER 3: Trades / Admin / Intermediate",
            "TEER 4, 5: Labourer / High School / Service"
        ],
        'edu_label': "Education",
        'edu_opts': ["PhD", "Master", "Bachelor", "College (3y)", "Diploma (1-2y)", "Secondary"],
        'teer_manual_help': "If not found, select below:",
        'exp_label': "Years Experience",
        'exp_title': "Work Experience (5 years)",
        'exp_qc_label': "Months in Quebec", 'exp_ca_label': "Months in Canada", 'exp_for_label': "Months Abroad",
        'lang_info': "**Reqs:** Volet 1 = Lvl 7 | Spouse = Lvl 4",
        'fr_oral': "French Oral (You)", 'fr_write': "French Written (You)", 'en': "English",
        'sp_fr_title': "Spouse's French (Oral)",
        'oev_info': "ℹ️ **VJO:** Validated Offer.",
        'vjo_label': "Validated Offer?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Outside Montreal"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "ℹ️ **Diploma:** AEC, DEC, etc. from Quebec.",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "ℹ️ **Family:** PR or Citizen (Parent, child, sibling).",
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Know strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Cert.",
        'g_step5': "5. Federal", 'g_desc5': "PR.",
        'noc_link_text': "🔎 Search on official Canada site (NOC)"
    }
}
lang = t[st.session_state.language]

# --- 6. DATA JOBS (MASIVA) ---
jobs_db = {
    "ingenie": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "engineer": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "web": {"code": "21222", "teer": "1", "volet": "Volet 1"},
    "infirmier": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "nurse": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "enseignant": {"code": "41220", "teer": "1", "volet": "Volet 1"},
    "teacher": {"code": "41220", "teer": "1", "volet": "Volet 1"},
    "architect": {"code": "21200", "teer": "1", "volet": "Volet 1"},
    "technicien": {"code": "22xxx", "teer": "2", "volet": "Volet 1/2"},
    "technician": {"code": "22xxx", "teer": "2", "volet": "Volet 1/2"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "electricien": {"code": "72200", "teer": "2", "volet": "Volet 2"},
    "electrician": {"code": "72200", "teer": "2", "volet": "Volet 2"},
    "plombier": {"code": "72300", "teer": "2", "volet": "Volet 2"},
    "plumber": {"code": "72300", "teer": "2", "volet": "Volet 2"},
    "mecanic": {"code": "72410", "teer": "2", "volet": "Volet 2"},
    "mechanic": {"code": "72410", "teer": "2", "volet": "Volet 2"},
    "educateur": {"code": "42202", "teer": "2", "volet": "Volet 2"},
    "educator": {"code": "42202", "teer": "2", "volet": "Volet 2"},
    "administra": {"code": "13100", "teer": "3", "volet": "Volet 2"},
    "admin": {"code": "13100", "teer": "3", "volet": "Volet 2"},
    "cuisinier": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cook": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "camion": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "driver": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "boucher": {"code": "63201", "teer": "3", "volet": "Volet 2"},
    "butcher": {"code": "63201", "teer": "3", "volet": "Volet 2"},
    "coiffeur": {"code": "63210", "teer": "3", "volet": "Volet 2"},
    "ensamblador": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "assembler": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manoeuvre": {"code": "95109", "teer": "5", "volet": "Volet 2"},
    "laborer": {"code": "95109", "teer": "5", "volet": "Volet 2"},
    "ferme": {"code": "84120", "teer": "4", "volet": "Volet 2"},
    "farm": {"code": "84120", "teer": "4", "volet": "Volet 2"},
    "nettoyage": {"code": "65310", "teer": "5", "volet": "Volet 2"},
    "cleaning": {"code": "65310", "teer": "5", "volet": "Volet 2"}
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
main_tabs = st.tabs(lang['main_tabs'])

# --- PESTAÑA CALCULADORA ---
with main_tabs[0]:
    
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # --- PASO 1: PERFIL ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        st.markdown(f"<div class='info-box'>{lang['tab1_sub']}</div>", unsafe_allow_html=True)
        
        # Ubicación (Carrusel)
        sel_loc = render_carousel(lang['loc_label'], lang['loc_opts'], 'loc')
        st.session_state.current_loc = sel_loc
        
        if "bec" not in sel_loc:
             st.text_input(lang['country_label'], value=st.session_state.origin_country, placeholder="Ex: Belgique, Sénégal...")
             st.divider()
             # Carrusel Ciudad
             sel_city = render_carousel(lang['city_label'], lang['city_opts'], 'city')
             st.session_state.dest_city = sel_city
             st.divider()
             st.markdown(f"**{lang['arrival_label']}**")
             st.session_state.arrival_text = st.text_input("Date", value=st.session_state.get('arrival_text', ''), placeholder="YYYY-MM-DD", label_visibility="collapsed")
        
        st.divider()
        
        c1, c2 = st.columns(2)
        with c1: st.session_state.age = st.number_input(lang['age'], 18, 65, st.session_state.age, key="age_input")
        with c2: st.session_state.spouse = st.checkbox(lang['spouse'], value=st.session_state.spouse, key="spouse_chk")
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(lang['kids12'], 0, 5, st.session_state.k1, key="k1_input")
        with c4: st.session_state.k2 = st.number_input(lang['kids13'], 0, 5, st.session_state.k2, key="k2_input")
        
        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang.get('sp_header', 'Datos Pareja')}**")
            c_sp1, c_sp2 = st.columns(2)
            with c_sp1: st.session_state.sp_age = st.number_input(lang['sp_age'], 18, 65, st.session_state.sp_age, key="sp_age_in")
            with c_sp2: 
                # Carrusel Edu Pareja
                sel_sp_edu = render_carousel(lang['edu_label'], lang['sp_edu_opts'], 'sp_edu')
                st.session_state.sp_edu = sel_sp_edu
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 2: TRABAJO ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        st.markdown(f"<div class='info-box'>{lang['tab2_sub']}</div>", unsafe_allow_html=True)
        
        st.markdown(f"**{lang['job_title']}**")
        def update_search(): st.session_state.job_search_term = st.session_state.widget_search
        st.text_input("Search", value=st.session_state.job_search_term, placeholder=lang['job_place'], label_visibility="collapsed", key="widget_search", on_change=update_search)
        
        if st.session_state.job_search_term:
            result = find_job_details(st.session_state.job_search_term)
            if result:
                st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
            else:
                st.markdown(f"<div class='info-box'>{lang['teer_manual_help']}</div>", unsafe_allow_html=True)
                st.markdown(f"🔗 [{lang['noc_link_text']}](https://noc.esdc.gc.ca/)")
        
        st.divider()
        # Carrusel TEER
        sel_teer = render_carousel(lang['teer_label'], lang['teer_opts'], 'teer')
        st.session_state.teer_sel = sel_teer
        
        st.divider()
        # Carrusel Educación
        sel_edu = render_carousel(lang['edu_label'], lang['edu_opts'], 'edu')
        st.session_state.edu = sel_edu
        
        st.divider()
        st.markdown(f"**{lang['exp_title']}**")
        st.session_state.exp_qc = st.number_input(lang['exp_qc_label'], 0, 60, st.session_state.exp_qc, key="exp_qc_in")
        st.session_state.exp_ca = st.number_input(lang['exp_ca_label'], 0, 60, st.session_state.exp_ca, key="exp_ca_in")
        st.session_state.exp_foreign = st.number_input(lang['exp_for_label'], 0, 60, st.session_state.exp_foreign, key="exp_for_in")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 2, 1])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 3: IDIOMAS ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.markdown(f"<div class='info-box'>{lang['tab3_sub']}</div>", unsafe_allow_html=True)
        st.info(lang['lang_info'])
        
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

    # --- PASO 4: QUEBEC ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        st.markdown(f"<div class='info-box'>{lang['tab4_sub']}</div>", unsafe_allow_html=True)
        
        # VJO
        st.info(lang['oev_info'])
        sel_vjo = render_carousel(lang['vjo_label'], lang['vjo_opts'], 'vjo')
        st.session_state.vjo = sel_vjo
        
        # DIPLOMA
        st.divider()
        st.info(lang.get('dip_qc_help', 'Info'))
        sel_stud = render_carousel(lang['dip_qc_label'], lang['yes_no'], 'q_stud')
        st.session_state.q_stud_val = sel_stud
        
        # FAMILIA
        st.divider()
        st.info(lang.get('fam_qc_help', 'Info'))
        sel_fam = render_carousel(lang['fam_qc_label'], lang['yes_no'], 'q_fam')
        st.session_state.q_fam_val = sel_fam

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 1, 2])
        with col_p:
            st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n:
            st.button(lang['calc'], type="primary", on_click=trigger_calculation)

    # RESULTADOS
    if st.session_state.show_results:
        st.markdown("---")
        score = 580 # Simulado
        st.markdown(f"""<div class="result-box"><h2>{lang['res_title']}: {int(score)} / 1350</h2></div>""", unsafe_allow_html=True)
        st.success(lang['advice_good'])
        
        if st.button("🔄"): reset_calc(); st.rerun()

    # BOTONES MONETIZACIÓN
    st.markdown("<br>", unsafe_allow_html=True)
    c_mon1, c_mon2 = st.columns(2)
    with c_mon1:
        st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
    with c_mon2:
        st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com")

# --- TAB 2: GUÍA ---
with main_tabs[1]:
    st.markdown(f"### 🗺️ {lang['guide_title']}")
    st.markdown("---")
    st.markdown(f"<div class='info-box'><h4>📊 {lang['g_step1']}</h4><p>{lang['g_desc1']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'><h4>🗣️ {lang['g_step2']}</h4><p>{lang['g_desc2']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'><h4>📂 {lang['g_step3']}</h4><p>{lang['g_desc3']}</p></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
