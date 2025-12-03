import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (DISEÑO PREMIUM + ANTI-INSTAGRAM) ---
st.markdown("""
    <style>
        /* === 0. BASE === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important; /* Fondo Gris Elegante */
            color: #333333 !important;
        }
        
        /* Textos */
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #333333 !important;
        }
        
        /* Header Oculto */
        header[data-testid="stHeader"] { background-color: #003399 !important; }

        /* === 1. CARRUSEL (SELECTOR VISUAL) === */
        .carousel-container {
            background-color: #ffffff;
            border: 2px solid #003399;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            color: #003399 !important;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 10px;
        }
        
        /* === 2. INPUTS (TEXTO/FECHA) - BLINDADOS === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important; /* Fix iPhone */
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
            opacity: 1 !important;
        }

        /* === 3. BOTONES === */
        div.stButton > button { 
            width: 100%; 
            border-radius: 8px; 
            font-weight: bold; 
            transition: 0.2s;
        }
        
        /* Botón Primario (Azul) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
            height: 45px;
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Botón Secundario (Blanco) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
            height: 45px;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }
        
        /* Botones Flecha del Carrusel (Pequeños) */
        div[data-testid="column"] button {
            height: 50px !important;
            background-color: #f0f0f0 !important;
            color: #003399 !important;
            border: 1px solid #ccc !important;
            font-size: 1.2rem !important;
            padding: 0 !important;
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
            padding: 10px;
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }

        /* === 4. TARJETA PRINCIPAL === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 2rem; 
            border-radius: 15px;
            border-top: 5px solid #003399;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        
        /* === 5. EXTRAS === */
        /* Header Pro */
        .pro-header {
            background-color: #003399;
            padding: 20px;
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
            font-weight: 800;
            flex-grow: 1;
        }
        .pro-header p { color: #e0e0e0 !important; }
        .flag-icon { height: 45px; border: 2px solid white; border-radius: 5px; }

        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .result-box { 
            background: linear-gradient(135deg, #003399 0%, #0055ff 100%);
            padding: 25px; 
            border-radius: 12px; 
            text-align: center; 
            margin-top: 20px; 
            color: white !important;
        }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; color: #666; }
        .deco-sub { color: #666 !important; font-style: italic; margin-bottom: 20px; display: block; }
        
        /* Radio / Checkbox */
        div[role="radiogroup"] label { color: #333 !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (SELECTOR APP) ---
def render_carousel(label, options, key_name):
    """Muestra un selector visual tipo app"""
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    st.markdown(f"**{label}**")
    
    # Columnas: Flecha (1) - Texto (6) - Flecha (1)
    c1, c2, c3 = st.columns([1, 6, 1])
    
    with c1:
        if st.button("◀", key=f"prev_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
            
    with c3:
        if st.button("▶", key=f"next_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
    # Caja central
    current_val = options[st.session_state[f"{key_name}_idx"]]
    with c2:
        st.markdown(f"<div class='carousel-container'>{current_val}</div>", unsafe_allow_html=True)
        
    return current_val

# --- 4. INICIALIZACIÓN ---
default_values = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'teer_sel': '', 'edu': 'Secondary', 
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': '',
    'current_loc': '', 'origin_country': '', 'dest_city': '-', 'arrival_text': '',
    # Índices
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Resetear índices al cambiar idioma para actualizar texto
    st.session_state.teer_idx = 0
    st.session_state.city_idx = 0

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''
    st.session_state.teer_idx = 0

def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES (DICCIONARIO COMPLETO) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Projet indépendant. Résultats estimés.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        'yes_no': ["Non", "Oui"],
        
        # Pasos
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        
        # Subtítulos
        'tab1_sub': "Le point de départ de votre projet d'immigration.",
        'tab2_sub': "Votre métier est au cœur du programme.",
        'tab3_sub': "Le français est la clé du succès.",
        'tab4_sub': "Finalisez votre pointage avec les atouts locaux.",
        
        # P1
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_label': "Ville de destination",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Autre"],
        'age': "Âge du candidat",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat", "Technique (DEC)", "Secondaire"],

        # P2
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur (Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0, 1: Univ / Gestion",
            "TEER 2: Collégial / Tech",
            "TEER 3: Métiers / Admin",
            "TEER 4, 5: Manœuvre / Service"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat", "Collégial (3 ans)", "Diplôme (1-2 ans)", "Secondaire"],
        'teer_manual_help': "Si non trouvé, utilisez le sélecteur :",
        'exp_title': "Expérience (5 dernières années)",
        'exp_qc_label': "Mois au Québec",
        'exp_ca_label': "Mois au Canada",
        'exp_for_label': "Mois à l'étranger",

        # P3
        'lang_info': "**Exigences:** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint", 'sp_fr_label': "Niveau Oral",

        # P4
        'oev_info': "ℹ️ **Offre d'emploi validée (OEV) :** Une offre formelle approuvée par le MIFI (EIMT). Une simple lettre d'embauche ne suffit pas.",
        'vjo_label': "Avez-vous une OEV ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        
        'dip_qc_label': "Diplôme du Québec ?",
        'dip_qc_help': "Avez-vous un diplôme (AEC, DEC, Bac, etc.) obtenu au Québec ?",
        
        'fam_qc_label': "Famille au Québec ?",
        'fam_qc_help': "Parent, enfant, conjoint, frère/sœur (Résident ou Citoyen).",

        'res_title': "Résultat Estimé", 'advice_good': "Excellent !", 'advice_low': "Améliorez le français.",
        'details': "Détails", 'sp_points': "Pts Conjoint",
        'guide_title': "Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente.",
        'noc_link_text': "🔎 Chercher CNP"
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculadora PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "Independiente. NO abogados.",
        'coffee': "☕ Apoyar",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil y Familia",
        'step2': "Paso 2: Trabajo y TEER",
        'step3': "Paso 3: Idiomas",
        'step4': "Paso 4: Quebec y Oferta",
        'tab1_sub': "Situación personal y familiar.",
        'tab2_sub': "Experiencia y oficio.",
        'tab3_sub': "El francés es la clave.",
        'tab4_sub': "Factores locales.",
        
        'loc_label': "¿Dónde te encuentras hoy?",
        'loc_opts': ["En Quebec", "Canadá (Otra)", "En el extranjero"],
        'country_label': "País de residencia",
        'arrival_label': "Fecha llegada (AAAA-MM-DD)",
        'city_label': "Ciudad destino",
        'city_opts': ["-", "Montréal", "Québec", "Laval", "Gatineau", "Otra"],

        'age': "Edad", 'spouse': "¿Pareja?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_header': "Datos de la Pareja",
        'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD", "Maestría", "Bachelor", "Técnico", "Secundaria"],

        'job_title': "Trabajo actual", 'job_place': "Ej: Ingeniero (Enter)",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0,1: Uni / Gerencia",
            "TEER 2: Tec / College",
            "TEER 3: Oficios / Intermedio",
            "TEER 4,5: Manual / Secund"
        ],
        'edu_label': "Nivel de Estudios",
        'edu_opts': ["PhD", "Maestría", "Bachelor", "College (3 años)", "Diploma (1-2 años)", "Secundaria"],
        'teer_manual_help': "Si no encuentras, usa el selector:",
        'exp_title': "Experiencia (5 años)",
        'exp_qc_label': "Meses en Quebec",
        'exp_ca_label': "Meses en Canadá",
        'exp_for_label': "Meses Extranjero",

        'lang_info': "Requisitos: Niv 7 (B2) | Pareja Niv 4 (A2)",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja", 'sp_fr_label': "Nivel Oral",
        
        'oev_info': "ℹ️ **Oferta Validada (VJO):** Documento oficial del MIFI. Una carta de trabajo simple NO sirve.",
        'vjo_label': "¿Oferta Validada?",
        'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Región"],
        
        'dip_qc_label': "¿Diploma de Quebec?",
        'dip_qc_help': "¿Tienes un título (AEC, DEC, Bachelor) obtenido en Quebec?",
        
        'fam_qc_label': "¿Familia en Quebec?",
        'fam_qc_help': "Padres, hijos, hermanos (Residentes/Ciudadanos).",

        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Pts Pareja", 'guide_title': "Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia.",
        'noc_link_text': "🔎 Buscar NOC"
    },
    'en': {
        'btn_lang': "🌐 Change Lang",
        'brand': "PSTQ Calculator",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "Independent. Estimated results.",
        'coffee': "☕ Support",
        'courses': "📚 Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Personal and family situation.",
        'tab2_sub': "Experience and trade.",
        'tab3_sub': "Language skills.", 'tab4_sub': "Local factors.",
        
        'loc_label': "Current location?",
        'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country",
        'arrival_label': "Arrival Date (YYYY-MM-DD)",
        'city_label': "Destination City",
        'city_opts': ["-", "Montréal", "Québec", "Other"],

        'age': "Age", 'spouse': "Spouse?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        
        'job_title': "Current Job", 'job_place': "Ex: Welder (Enter)",
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
        'exp_title': "Work Experience (5 years)",
        'exp_qc_label': "Months in Quebec", 'exp_ca_label': "Months in Canada", 'exp_for_label': "Months Abroad",

        'lang_info': "Reqs: Lvl 7 (B2) | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French", 'sp_fr_label': "Oral Level",
        
        'oev_info': "ℹ️ **VJO:** Validated Offer (LMIA/MIFI).",
        'vjo_label': "Validated Offer?",
        'vjo_opts': ["No", "Yes, Greater Montreal", "Yes, Region"],
        
        'dip_qc_label': "Quebec Diploma?",
        'dip_qc_help': "AEC, DEC, Bachelor from Quebec.",
        
        'fam_qc_label': "Family in Quebec?",
        'fam_qc_help': "PR or Citizen (Parent, child, sibling).",
        
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts", 'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Cert.",
        'g_step5': "5. Federal", 'g_desc5': "PR.",
        'noc_link_text': "🔎 Search NOC"
    }
}
lang = t[st.session_state.language]

# --- 6. DATA JOBS ---
jobs_db = {
    "ingenie": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "engineer": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
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
             st.session_state.origin_country = st.text_input(lang['country_label'], value=st.session_state.origin_country, placeholder="Ex: Belgique, Sénégal...")
             
             # CARRUSEL CIUDAD
             st.divider()
             sel_city = render_carousel(lang['city_label'], lang['city_opts'], 'city')
             st.session_state.dest_city = sel_city
             
             # FECHA TEXTO
             st.divider()
             st.markdown(f"**{lang['arrival_label']}**")
             st.session_state.arrival_text = st.text_input("Date", value=st.session_state.arrival_text, placeholder="YYYY-MM-DD", label_visibility="collapsed")
        
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
        
        st.info(lang['oev_info'])
        
        vjo_idx = 0
        if st.session_state.vjo in lang['vjo_opts']: vjo_idx = lang['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(lang['vjo_label'], lang['vjo_opts'], index=vjo_idx, key="vjo_input")
        
        st.divider()
        st.info(lang['dip_qc_help'])
        curr_stud = st.session_state.q_stud_val
        if curr_stud not in lang['yes_no']: curr_stud = lang['yes_no'][0]
        st.session_state.q_stud_val = st.radio(lang['dip_qc_label'], lang['yes_no'], index=lang['yes_no'].index(curr_stud), horizontal=True, key="q_stud_in")
        
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
        # Lógica de cálculo igual...
        score = 0
        # (Aquí iría la lógica completa, simplificada para el ejemplo)
        
        st.markdown(f"""<div class="result-box"><h2>{lang['res_title']}: {int(score)}</h2></div>""", unsafe_allow_html=True)
        st.success(lang['advice_good'])
        if st.button("🔄"): reset_calc(); st.rerun()

# COLUMNAS DE BOTONES (AL FINAL DE TODO)
c1, c2 = st.columns(2)
with c1: st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
with c2: st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com")

with main_tab_guide:
    st.markdown(f"### 🗺️ {lang['guide_title']}")
    st.markdown("---")
    st.markdown(f"<div class='step-box'><h4>📊 {lang['g_step1']}</h4><p>{lang['g_desc1']}</p></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
