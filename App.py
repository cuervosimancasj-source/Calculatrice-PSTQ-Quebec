import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (DISEÑO FINAL PULIDO) ---
st.markdown("""
    <style>
        /* === 0. BASE === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f8f9fa !important; /* Gris muy muy suave */
            color: #333333 !important;
        }
        
        /* Textos */
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #333333 !important;
        }
        
        /* Header Oculto */
        header[data-testid="stHeader"] { background-color: #4A90E2 !important; } /* Azul Tenue */

        /* === 1. CARRUSEL (SELECTOR VISUAL SIMÉTRICO) === */
        .stepper-box {
            background-color: #FFFFFF;
            color: #000000;
            border: 2px solid #4A90E2; /* Azul Tenue */
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 50px !important; /* Altura fija para simetría */
            margin-bottom: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        /* Botones Flecha del Carrusel */
        div[data-testid="column"] button {
            height: 50px !important; /* Misma altura que la caja */
            background-color: #FFFFFF !important;
            color: #4A90E2 !important;
            border: 2px solid #4A90E2 !important;
            border-radius: 10px !important;
            font-size: 1.2rem !important;
            padding: 0 !important;
            line-height: 0 !important;
        }
        div[data-testid="column"] button:hover {
            background-color: #eef6ff !important;
        }

        /* === 2. INPUTS DE TEXTO (BLANCOS) Y PLACEHOLDER GRIS === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
            border-radius: 8px !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
        }
        
        /* AQUÍ ESTÁ EL GRIS SUAVE PARA EL EJEMPLO (PAÍS) */
        ::placeholder {
            color: #999999 !important;
            -webkit-text-fill-color: #999999 !important;
            opacity: 1 !important;
        }

        /* === 3. BOTONES PRINCIPALES (AZUL TENUE) === */
        div.stButton > button { 
            width: 100%; 
            border-radius: 8px; 
            font-weight: 600; 
            height: 50px; 
            transition: all 0.2s;
        }
        
        /* Primario (Siguiente/Calcular) */
        div.stButton > button[kind="primary"] {
            background-color: #4A90E2 !important; /* Azul Tenue */
            color: #FFFFFF !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(74, 144, 226, 0.3);
        }
        div.stButton > button[kind="primary"]:hover {
            background-color: #357ABD !important;
            box-shadow: 0 6px 8px rgba(74, 144, 226, 0.4);
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Secundario (Atrás) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #4A90E2 !important;
            border: 2px solid #4A90E2 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #4A90E2 !important; }

        /* Enlaces (Coffee/Cursos) */
        div.stLinkButton > a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #4A90E2 !important;
            color: #FFFFFF !important;
            padding: 12px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            width: 100%;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }
        div.stLinkButton > a:hover {
            background-color: #357ABD !important;
        }

        /* === 4. TARJETA PRINCIPAL === */
        [data-testid="stForm"] {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 15px;
            border-top: 6px solid #4A90E2; /* Azul Tenue */
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        }

        /* === 5. EXTRAS === */
        .info-box { background-color: #f0f7ff; border-left: 5px solid #4A90E2; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        
        .result-box { 
            background: linear-gradient(135deg, #4A90E2, #357ABD); 
            padding: 25px; 
            border-radius: 15px; 
            text-align: center; 
            color: white; 
            margin-top: 20px; 
            box-shadow: 0 5px 15px rgba(74, 144, 226, 0.3);
        }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        
        .footer { margin-top: 60px; padding: 20px; border-top: 1px solid #ddd; text-align: center; color: #666; font-size: 0.85rem;}
        .deco-sub { color: #666; font-style: italic; margin-bottom: 20px; display: block; }

        /* Header Pro */
        .pro-header {
            background-color: #4A90E2; /* Azul Tenue */
            padding: 20px;
            border-radius: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 12px rgba(74, 144, 226, 0.25);
            margin-bottom: 20px;
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.5rem;
            font-weight: 800;
            text-align: center;
            flex-grow: 1;
        }
        .pro-header p { color: #f0f0f0 !important; }
        .flag-icon { height: 40px; border: 2px solid white; border-radius: 5px; }

        /* Radio */
        div[role="radiogroup"] label { color: #333 !important; }
        
        /* Botones +/- */
        button[tabindex="-1"] { background-color: #f8f9fa !important; border: 1px solid #ddd !important; }
        button[tabindex="-1"] span { color: #333 !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (SIMÉTRICA) ---
def render_carousel(label, options, key_name):
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    st.markdown(f"**{label}**")
    
    # Columnas Simétricas: 1 (Botón) - 5 (Texto) - 1 (Botón)
    c1, c2, c3 = st.columns([1, 5, 1])
    
    with c1:
        if st.button("◀", key=f"prev_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
            
    with c3:
        if st.button("▶", key=f"next_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
    current_val = options[st.session_state[f"{key_name}_idx"]]
    with c2:
        st.markdown(f"<div class='stepper-box'>{current_val}</div>", unsafe_allow_html=True)
        
    return current_val

# --- 4. INICIALIZACIÓN ---
default_values = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': '', 'current_loc': '', 'origin_country': '', 
    'arrival_text': '',
    # Índices (City empieza en 1 si "Montréal" es el segundo elemento de la lista global, ajustamos abajo)
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

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

# --- 5. TRADUCCIONES (CORREGIDAS Y COMPLETAS) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Simulation de pointage pour l'immigration au Québec",
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
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Autre"],
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants (-12 ans)", 'kids13': "Enfants (13-21 ans)",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat", "Technique (DEC)", "Secondaire/DEP"],
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur (Appuyez sur Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0,1: Université / Gestion",
            "TEER 2: Collégial / Technique",
            "TEER 3: Métiers / Administration",
            "TEER 4,5: Manœuvre / Service"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat (Univ)", "Collégial (3 ans)", "Diplôme (1-2 ans)", "Secondaire"],
        'teer_manual_help': "Si non trouvé, utilisez le sélecteur :",
        'exp_label': "Années d'expérience (Total)",
        'lang_info': "**Exigences :** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint", 'sp_fr_label': "Niveau Oral",
        'oev_info': "**ℹ️ OEV :** Offre validée par MIFI. Une simple lettre d'embauche ne suffit pas.",
        'vjo_label': "Avez-vous une Offre Validée (OEV) ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        'dip_qc_label': "Diplôme du Québec ?", 'dip_qc_help': "AEC, DEC, Bac, Maîtrise, Doctorat obtenu au Québec.",
        'fam_qc_label': "Famille au Québec ?", 'fam_qc_help': "Parent, enfant, conjoint, frère/sœur (Résident/Citoyen).",
        'res_title': "Résultat Estimé", 'advice_good': "Excellent ! Profil compétitif.", 'advice_low': "Améliorez le français.",
        'details': "Détails", 'sp_points': "Pts Conjoint", 'guide_title': "Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente.",
        'noc_link_text': "🔎 Chercher CNP (Site Officiel)",
        'exp_title': "Expérience (5 dernières années)",
        'exp_qc_label': "Mois au Québec", 'exp_ca_label': "Mois au Canada", 'exp_for_label': "Mois à l'étranger"
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
        'tab2_sub': "Tu oficio define tu categoría en el PSTQ.",
        'tab3_sub': "El francés es la llave del éxito en Quebec.",
        'tab4_sub': "Finaliza tu puntaje con los factores locales.",
        'loc_label': "¿Dónde te encuentras hoy?",
        'loc_opts': ["En Quebec", "Canadá (Otra provincia)", "En el extranjero"],
        'country_label': "País de residencia",
        'dest_city_label': "Ciudad de destino en Quebec",
        'arrival_label': "Fecha estimada de llegada",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Otra"],
        'age': "Edad del candidato",
        'spouse': "¿Tienes pareja?",
        'kids12': "Hijos (-12 años)", 'kids13': "Hijos (13-21 años)",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "Técnico (DEC)", "Secundaria/DEP"],
        'job_title': "Trabajo actual",
        'job_place': "Ej: Ingeniero (Enter)",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0,1: Uni / Gerencia",
            "TEER 2: Técnico / College",
            "TEER 3: Oficios / Intermedio",
            "TEER 4,5: Manual / Secund"
        ],
        'edu_label': "Nivel de Estudios",
        'edu_opts': ["PhD (Doctorado)", "Maestría", "Bachelor (Univ)", "College (3 años)", "Diploma (1-2 años)", "Secundaria"],
        'teer_manual_help': "Si no encuentras, usa el selector:",
        'exp_label': "Años de experiencia (Total)",
        'lang_info': "Requisitos: Niv 7 (B2) | Pareja Niv 4 (A2)",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja", 'sp_fr_label': "Nivel Oral",
        'oev_info': "**ℹ️ VJO:** Oferta Validada por MIFI. Una carta simple no sirve.",
        'vjo_label': "¿Tienes Oferta Validada (VJO)?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Fuera de Montreal"],
        'dip_qc_label': "¿Diploma de Quebec?",
        'dip_qc_help': "¿Tienes un título (AEC, DEC, Bachelor, etc.) obtenido en Quebec?",
        'fam_qc_label': "¿Familia en Quebec?",
        'fam_qc_help': "Padres, hijos, cónyuge, hermanos (Residentes o Ciudadanos).",
        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Puntos Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia.",
        'noc_link_text': "🔎 Buscar NOC",
        'exp_title': "Experiencia Laboral (5 años)",
        'exp_qc_label': "Meses en Quebec", 'exp_ca_label': "Meses en Canadá", 'exp_for_label': "Meses Extranjero"
    },
    'en': {
        'btn_lang': "🌐 Change Lang",
        'brand': "PSTQ Calculator",
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
        'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country",
        'dest_city_label': "Destination City",
        'arrival_label': "Estimated Arrival Date",
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
            "TEER 0,1: Mgmt/Uni",
            "TEER 2: Tech/College",
            "TEER 3: Trades/Admin",
            "TEER 4,5: Manual/Sec"
        ],
        'edu_label': "Education",
        'edu_opts': ["PhD", "Master", "Bachelor", "College (3y)", "Diploma (1-2y)", "Secondary"],
        'teer_manual_help': "If not found, use selector:",
        'exp_label': "Years Experience",
        'lang_info': "Reqs: Lvl 7 (B2) | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French", 'sp_fr_label': "Oral Level",
        'oev_info': "**ℹ️ VJO:** Validated Offer (LMIA/MIFI).",
        'vjo_label': "Validated Offer?", 'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Region"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "AEC, DEC, etc. from Quebec.",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "PR or Citizen (Parent, child, spouse).",
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts", 'guide_title': "Roadmap",
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
             # CARRUSEL CIUDAD (NO DESPLEGABLE)
             sel_city = render_carousel(lang['dest_city_label'], lang['city_opts'], 'city')
             st.session_state.dest_city = sel_city
             
             # FECHA TEXTO
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
            st.markdown(f"**{lang['sp_header']}**")
            c_sp1, c_sp2 = st.columns(2)
            with c_sp1: st.session_state.sp_age = st.number_input(lang['sp_age'], 18, 65, st.session_state.sp_age, key="sp_age_in")
            with c_sp2: 
                # CARRUSEL EDUCACION PAREJA
                sel_sp_edu = render_carousel(lang['sp_edu'], lang['sp_edu_opts'], 'sp_edu')
                st.session_state.sp_edu = sel_sp_edu
        
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
        
        # CARRUSEL TEER
        sel_teer = render_carousel(lang['teer_label'], lang['teer_opts'], 'teer')
        st.session_state.teer_sel = sel_teer
        
        st.divider()
        
        # CARRUSEL EDUCACION
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
        
        # INFO OEV
        st.info(lang['oev_info'])
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']: vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx, key="vjo_input")
        
        # DIPLOMA
        st.divider()
        st.info(lang['dip_qc_help'])
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio(lang['dip_qc_label'], lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True, key="q_stud_in")
        
        # FAMILIA
        st.divider()
        st.info(lang['fam_qc_help'])
        curr_fam = st.session_state.q_fam_val
        if curr_fam not in lang['yes_no']: curr_fam = lang['yes_no'][0]
        st.session_state.q_fam_val = st.radio(lang['fam_qc_label'], lang['yes_no'], index=lang['yes_no'].index(curr_fam), horizontal=True, key="q_fam_in")

        st.markdown("###")
        col_p, col_e, col_n = st.columns([1, 1, 2])
        with col_p: st.button(lang['prev'], type="secondary", on_click=prev_step)
        with col_n: st.button(lang['calc'], type="primary", on_click=trigger_calculation)

    # LÓGICA
    if st.session_state.show_results:
        age, edu, teer = st.session_state.age, st.session_state.edu, st.session_state.teer_sel
        exp_months = st.session_state.exp_qc + st.session_state.exp_ca + st.session_state.exp_foreign
        exp_calc = min(60, exp_months)
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
        
        if "0, 1" in teer or "0,1" in teer: score += 60 
        elif "2" in teer: score += 40
        elif "3" in teer: score += 20
        
        score += int(exp_calc * 1.33)
        pts_map = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
        score += pts_map.get(fr_o,0) * 1.2 + pts_map.get(fr_w,0) * 0.8
        if en == "Advanced": score += 25
        elif en == "Intermediate": score += 15
        if "Hors" in vjo_val or "Outside" in vjo_val or "Fuera" in vjo_val: score += 380
        elif "Grand" in vjo_val or "Greater" in vjo_val or "Gran" in vjo_val: score += 180
        if is_yes_stud: score += 50
        if is_yes_fam: score += 30
        if st.session_state.exp_qc >= 6: score += 30
        
        if st.session_state.spouse:
            sp_a, sp_e, sp_f = st.session_state.sp_age, st.session_state.sp_edu, st.session_state.sp_fr
            if 18 <= sp_a <= 40: score_sp += 10
            if "Bachelor" in sp_e or "Master" in sp_e or "PhD" in sp_e: score_sp += 10
            elif "College" in sp_e: score_sp += 5
            if sp_f in ["C1", "C2"]: score_sp += 30
            elif sp_f == "B2": score_sp += 20
            elif sp_f in ["A2", "B1"]: score_sp += 10
            score += score_sp
        score += (st.session_state.k1*4) + (st.session_state.k2*2)

        st.markdown(f"""<div class="result-box"><h2>{lang['res_title']}: {int(score)} / 1350</h2></div>""", unsafe_allow_html=True)
        with st.expander(lang['details']):
            st.write(f"**Principal:** {int(score - score_sp - (st.session_state.k1*4 + st.session_state.k2*2))} pts")
            if st.session_state.spouse: st.write(f"**{lang['sp_points']}:** {score_sp} pts")
            st.write(f"**Enfants:** {(st.session_state.k1*4 + st.session_state.k2*2)} pts")
        
        if score > 580: st.success(lang['advice_good']); st.balloons()
        else: st.warning(lang['advice_low'])
        if st.button("🔄 Recalculer"): reset_calc(); st.rerun()

    # BOTONES DE MONETIZACIÓN (SEPARADOS Y ABAJO)
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
    with c2: st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com")

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
