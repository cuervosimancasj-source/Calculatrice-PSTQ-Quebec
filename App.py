import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (MODO ALTO CONTRASTE - INFALIBLE) ---
st.markdown("""
    <style>
        /* === 0. BASE DE LA PÁGINA === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #FFFFFF !important; /* Fondo Blanco Puro para evitar confusiones */
            color: #000000 !important;
        }
        
        /* Textos siempre negros */
        .stApp, p, label, h2, h3, h4, h5, h6, div, span, li {
            color: #000000 !important;
        }
        
        /* Título Header Blanco */
        h1 { color: #FFFFFF !important; }
        
        /* Header Azul */
        header[data-testid="stHeader"] { background-color: #003399 !important; }

        /* === 1. ENCABEZADO PERSONALIZADO === */
        .pro-header {
            background-color: #003399;
            padding: 20px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.4rem;
            font-weight: 800;
            text-align: center;
            flex-grow: 1;
            -webkit-text-fill-color: #FFFFFF !important; /* Fix iPhone */
        }
        .pro-header p {
            color: #e0e0e0 !important;
            -webkit-text-fill-color: #e0e0e0 !important;
            margin: 0;
            text-align: center;
            font-size: 0.9rem;
        }
        .flag-icon { height: 35px; border: 1px solid white; border-radius: 3px; }

        /* === 2. INPUTS DE TEXTO (CAJAS SIMPLES) === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #f8f9fa !important; /* Gris muy claro */
            border: 1px solid #999 !important;
            color: #000000 !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: transparent !important;
            caret-color: #000000 !important;
            opacity: 1 !important;
        }

        /* === 3. RADIO BUTTONS (EL SUSTITUTO DEL MENÚ) === */
        /* Convertimos los radios en una lista limpia */
        div[role="radiogroup"] {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #eee;
        }
        div[role="radiogroup"] label {
            color: #000000 !important;
            margin-bottom: 8px;
            padding: 5px;
            border-radius: 4px;
        }
        /* El círculo del radio */
        div[data-baseweb="radio"] div {
            background-color: #FFFFFF !important;
            border-color: #003399 !important;
        }
        /* El punto seleccionado */
        div[data-baseweb="radio"][aria-checked="true"] div div {
            background-color: #003399 !important;
        }

        /* === 4. BOTONES === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; height: 45px; }
        
        /* Primario (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        div.stButton > button[kind="primary"] * { 
            color: #FFFFFF !important; 
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { 
            color: #003399 !important;
            -webkit-text-fill-color: #003399 !important;
        }
        
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
        div.stLinkButton > a * { 
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }

        /* === 5. EXTRAS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; -webkit-text-fill-color: #FFFFFF !important; }
        
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        .deco-sub { font-style: italic; margin-bottom: 15px; display: block; color: #666666 !important; font-size: 0.9em; }
        
        /* Botones +/- de edad (Gris claro para contraste) */
        button[tabindex="-1"] { 
            background-color: #e0e0e0 !important; 
            color: #000000 !important; 
            border: 1px solid #ccc !important; 
        }
        button[tabindex="-1"] span {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

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
    'current_loc': '', 'origin_country': '', 'dest_city': '-', 'arrival_text': ''
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Asegurar valores por defecto al cambiar idioma
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]
    st.session_state.dest_city = t[st.session_state.language]['city_opts'][0]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 4. TRADUCCIONES COMPLETAS ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Nous ne sommes pas avocats ni consultants en immigration et nous ne faisons pas partie du gouvernement. Nous sommes un projet indépendant.",
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
        'dest_city_label': "Ville de destination au Québec",
        'arrival_label': "Date d'arrivée prévue (Format: AAAA-MM-JJ)",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Autre"],
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation du conjoint",
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
        'lang_info': "**Exigences :** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral (Vous)", 'fr_write': "Français Écrit (Vous)", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint (Oral)",
        'sp_fr_label': "Niveau Oral",
        'oev_info': "**ℹ️ OEV (Offre d'emploi validée) :** Signifie que l'employeur a obtenu une EIMT ou que l'offre est validée par le MIFI.",
        'vjo_label': "Avez-vous une Offre Validée (OEV) ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Hors Montréal (Région)"],
        'dip_qc_label': "Diplôme du Québec ?",
        'dip_qc_help': "Avez-vous obtenu un diplôme (AEC, DEC, Bac, etc.) d'un établissement au Québec ?",
        'fam_qc_label': "Famille au Québec ?",
        'fam_qc_help': "Avez-vous de la famille proche (Parent, enfant, conjoint, frère/sœur) Résident ou Citoyen ?",
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
        'noc_link_text': "🔎 Chercher sur le site officiel du Canada (CNP)",
        'exp_title': "Expérience de travail (5 dernières années)",
        'exp_qc_label': "Mois au Québec",
        'exp_ca_label': "Mois au Canada (Hors QC)",
        'exp_for_label': "Mois à l'étranger"
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculadora PSTQ",
        'subtitle': "Simulación de puntaje para Residencia Permanente Quebec",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "No somos abogados ni asesores de migración y tampoco hacemos parte del gobierno. Somos un proyecto independiente.",
        'coffee': "☕ Apoyar proyecto",
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
        'dest_city_label': "Ciudad de destino en Quebec",
        'arrival_label': "Fecha estimada de llegada (Formato: AAAA-MM-DD)",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Otra"],
        'age': "Edad del candidato",
        'spouse': "¿Tienes pareja?",
        'kids12': "Hijos -12 años", 'kids13': "Hijos +12 años",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "Técnico (DEC)", "Secundaria/DEP"],
        'job_title': "Trabajo actual",
        'job_place': "Ej: Ingeniero (Enter para buscar)...",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0, 1: Universidad / Gerencia / Ingeniería",
            "TEER 2: Técnico / College / Supervisores",
            "TEER 3: Oficios / Administración / Intermedio",
            "TEER 4, 5: Operarios / Secundaria / Manual"
        ],
        'edu_label': "Nivel de Estudios",
        'edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "College (3 años)", "Diploma (1-2 años)", "Secundaria"],
        'teer_manual_help': "Si no encuentras, usa la lista de abajo:",
        'exp_label': "Años de experiencia",
        'lang_info': "**Requisitos:** Niv 7 (B2) | Pareja Niv 4 (A2)",
        'fr_oral': "Francés Oral (Tú)", 'fr_write': "Francés Escrito (Tú)", 'en': "Inglés",
        'sp_fr_title': "Francés de la Pareja (Oral)",
        'sp_fr_label': "Nivel Oral",
        'oev_info': "**ℹ️ VJO (Oferta Validada):** Con LMIA o aprobada por MIFI. Una carta de trabajo simple no es VJO.",
        'vjo_label': "¿Tienes Oferta Validada (VJO)?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Fuera de Montreal"],
        'dip_qc_label': "¿Diploma de Quebec?",
        'dip_qc_help': "¿Tienes un título (AEC, DEC, Bachelor, etc.) obtenido en Quebec?",
        'fam_qc_label': "¿Familia en Quebec?",
        'fam_qc_help': "¿Tienes familiares directos (Residentes o Ciudadanos) viviendo en Quebec?",
        'res_title': "Resultado", 'advice_good': "¡Excelente! Competitivo.", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Puntos Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado Selección.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia Permanente.",
        'noc_link_text': "🔎 Buscar en sitio oficial Canadá (NOC)",
        'exp_title': "Experiencia Laboral (Últimos 5 años)",
        'exp_qc_label': "Meses en Quebec",
        'exp_ca_label': "Meses en Canadá (Fuera QC)",
        'exp_for_label': "Meses en el Extranjero"
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
        'step1': "Step 1: Profile & Family",
        'step2': "Step 2: Work & TEER",
        'step3': "Step 3: Languages",
        'step4': "Step 4: Quebec & Offer",
        'tab1_sub': "The starting point of your immigration journey.",
        'tab2_sub': "Your trade is the core of the PSTQ program.",
        'tab3_sub': "French is the key to success in Quebec.",
        'tab4_sub': "Finalize your score with local assets.",
        'loc_label': "Where are you today?",
        'loc_opts': ["In Quebec", "Canada (Other prov.)", "Abroad"],
        'country_label': "Country of Residence",
        'dest_city_label': "Destination City",
        'arrival_label': "Estimated Arrival Date (Format: YYYY-MM-DD)",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Other"],
        'age': "Age",
        'spouse': "Have a spouse?",
        'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data",
        'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        'job_title': "Current Job",
        'job_place': "Ex: Engineer (Press Enter)...",
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
        'lang_info': "**Reqs:** Volet 1 = Lvl 7 | Volet 2 = Lvl 5 | Spouse = Lvl 4",
        'fr_oral': "French Oral (You)", 'fr_write': "French Written (You)", 'en': "English",
        'sp_fr_title': "Spouse's French (Oral)",
        'sp_fr_label': "Oral Level",
        'oev_info': "**ℹ️ VJO:** Validated Offer (LMIA/MIFI).",
        'vjo_label': "Validated Job Offer?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Outside Montreal"],
        'dip_qc_label': "Quebec Diploma?",
        'dip_qc_help': "Did you obtain a degree (AEC, DEC, Bachelor, etc.) in Quebec?",
        'fam_qc_label': "Family in Quebec?",
        'fam_qc_help': "Do you have immediate family (PR or Citizen) living in Quebec?",
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Know strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Selection Cert.",
        'g_step5': "5. Federal", 'g_desc5': "PR Canada.",
        'noc_link_text': "🔎 Search on official Canada site (NOC)",
        'exp_title': "Work Experience (5 years)",
        'exp_qc_label': "Months in Quebec",
        'exp_ca_label': "Months in Canada",
        'exp_for_label': "Months Abroad"
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
        
        # Ubicación
        st.markdown(f"**{lang['loc_label']}**")
        curr_loc = st.session_state.current_loc
        if curr_loc not in lang['loc_opts']: curr_loc = lang['loc_opts'][2]
        st.session_state.current_loc = st.radio("Loc", lang['loc_opts'], index=lang['loc_opts'].index(curr_loc), label_visibility="collapsed")
        
        if "bec" not in st.session_state.current_loc:
             st.session_state.origin_country = st.text_input(lang['country_label'], value=st.session_state.origin_country, placeholder="Ex: Belgique, Sénégal...")
             
             st.divider()
             # CIUDAD (RADIO BUTTONS PARA EVITAR MENU NEGRO)
             st.markdown(f"**{lang['dest_city_label']}**")
             curr_city = st.session_state.dest_city
             if curr_city not in lang['city_opts']: curr_city = lang['city_opts'][0]
             st.session_state.dest_city = st.radio("City", lang['city_opts'], index=lang['city_opts'].index(curr_city), label_visibility="collapsed")
             
             st.divider()
             # FECHA COMO TEXTO
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
                st.markdown(f"**{lang['edu_label']}**")
                st.session_state.sp_edu = st.radio("SpEdu", lang['sp_edu_opts'], index=2, label_visibility="collapsed")
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(lang['next'], type="primary", on_click=next_step)

    # --- PASO 2: TRABAJO ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab2_sub']}</span>", unsafe_allow_html=True)
        
        st.markdown(f"**{lang['job_title']}**")
        def update_search(): st.session_state.job_search_term = st.session_state.widget_search
        st.text_input("Search", value=st.session_state.job_search_term, placeholder=lang['job_place'], label_visibility="collapsed", key="widget_search", on_change=update_search)
        
        if st.session_state.job_search_term:
            result = find_job_details(st.session_state.job_search_term)
            if result:
                st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
            else:
                st.markdown(f"<div class='help-box'>{lang['teer_manual_help']}</div>", unsafe_allow_html=True)
                st.markdown(f"🔗 [{lang['noc_link_text']}](https://noc.esdc.gc.ca/)")
        st.divider()
        
        # TEER CON RADIO BUTTONS (NO SE PONE NEGRO)
        st.markdown(f"**{lang['teer_label']}**")
        teer_index = 0
        if st.session_state.teer_sel in lang['teer_opts']:
            teer_index = lang['teer_opts'].index(st.session_state.teer_sel)
        st.session_state.teer_sel = st.radio("Teer", lang['teer_opts'], index=teer_index, label_visibility="collapsed")
        
        st.divider()
        
        # EDUCACION CON RADIO BUTTONS
        st.markdown(f"**{lang['edu_label']}**")
        st.session_state.edu = st.radio("Edu", lang['edu_opts'], index=2, label_visibility="collapsed")
        
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
        
        # VJO
        st.info(lang['oev_info'])
        st.markdown(f"**{lang['vjo_label']}**")
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']:
            vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio("VJO", lang['vjo_opts'], index=vjo_idx, label_visibility="collapsed", key="vjo_input")
        
        st.divider()
        
        # DIPLOMA
        st.info(lang['dip_qc_help'])
        st.markdown(f"**{lang['dip_qc_label']}**")
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio("DipQC", lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True, label_visibility="collapsed", key="q_stud_in")
        
        st.divider()
        
        # FAMILIA
        st.info(lang['fam_qc_help'])
        st.markdown(f"**{lang['fam_qc_label']}**")
        curr_fam = st.session_state.q_fam_val
        if curr_fam not in lang['yes_no']: curr_fam = lang['yes_no'][0]
        st.session_state.q_fam_val = st.radio("FamQC", lang['yes_no'], index=lang['yes_no'].index(curr_fam), horizontal=True, label_visibility="collapsed", key="q_fam_in")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 1, 2])
        with col_p:
            st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n:
            st.button(lang['calc'], type="primary", on_click=trigger_calculation)

    # LÓGICA Y RESULTADOS
    if st.session_state.show_results:
        age = st.session_state.age
        edu = st.session_state.edu
        teer = st.session_state.teer_sel
        # CÁLCULO EXPERIENCIA TOTAL
        exp_months = st.session_state.exp_qc + st.session_state.exp_ca + st.session_state.exp_foreign
        exp_calc = min(60, exp_months) # Tope 5 años
        
        fr_o, fr_w, en, vjo_val = st.session_state.fr_oral, st.session_state.fr_write, st.session_state.en_lvl, st.session_state.vjo
        
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
        
        score += int(exp_calc * 1.33)
        
        pts_map = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
        score += pts_map.get(fr_o,0) * 1.2 + pts_map.get(fr_w,0) * 0.8
        
        if en == "Advanced": score += 25
        elif en == "Intermediate": score += 15
        
        if "Hors" in vjo_val or "Outside" in vjo_val or "Fuera" in vjo_val: score += 380
        elif "Grand" in vjo_val or "Greater" in vjo_val or "Gran" in vjo_val: score += 180
        
        if is_yes_stud: score += 50
        if is_yes_fam: score += 30
        
        # Bonus estancia Quebec
        if st.session_state.exp_qc >= 6: score += 30
        
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
            
        if st.button("🔄 Recalculer"): reset_calc(); st.rerun()

# COLUMNAS PARA LOS BOTONES DE MONETIZACIÓN (JUSTO DEBAJO)
c_mon1, c_mon2 = st.columns(2)
with c_mon1:
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
with c_mon2:
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com")

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

st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
