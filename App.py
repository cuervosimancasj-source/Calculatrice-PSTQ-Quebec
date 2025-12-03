import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (LIMPIO, BLANCO Y SIN ERRORES) ---
st.markdown("""
    <style>
        /* === 0. BASE MODO CLARO === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important;
            color: #333333 !important;
        }
        
        /* Textos */
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #333333 !important;
        }
        /* Título Header Blanco */
        h1 { color: #FFFFFF !important; }
        
        /* Header Azul */
        header[data-testid="stHeader"] { background-color: #003399 !important; }

        /* === 1. CAJA VISUAL DEL CARRUSEL === */
        .stepper-box {
            background-color: #FFFFFF;
            color: #003399;
            border: 2px solid #003399;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1rem;
            min-height: 60px; /* Altura fija */
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        /* === 2. INPUTS DE TEXTO (BLINDADOS) === */
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

        /* === 3. BOTONES DE ACCIÓN === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; height: 45px; }
        
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
        
        /* Botones Pequeños del Carrusel */
        div[data-testid="column"] button {
            background-color: #f0f0f0 !important;
            color: #003399 !important;
            border: 1px solid #ccc !important;
            height: 40px !important;
        }

        /* === 4. EXTRAS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; color: white;}
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; font-size: 0.8rem; }
        .deco-sub { font-style: italic; margin-bottom: 15px; display: block; color: #666666 !important; font-size: 0.9em; }

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
            font-size: 1.4rem;
            font-weight: 800;
            text-align: center;
            flex-grow: 1;
        }
        .flag-icon { height: 35px; border: 1px solid white; border-radius: 4px; }
        
        /* Radio / Checkbox labels */
        div[role="radiogroup"] label { color: #000000 !important; }
        
        /* Botones +/- */
        button[tabindex="-1"] { background-color: #e0e0e0 !important; color: #000 !important; border: 1px solid #ccc !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (BOTONES ABAJO EN ESQUINAS) ---
def render_carousel(label, options, key_name):
    """Muestra el valor y botones de navegación debajo"""
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    st.markdown(f"**{label}**")
    
    # Caja Visual
    current_val = options[st.session_state[f"{key_name}_idx"]]
    st.markdown(f"<div class='stepper-box'>{current_val}</div>", unsafe_allow_html=True)
    
    # Botones Debajo (Separados)
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
    # Índices para carruseles
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2, 'vjo_idx': 0, 'q_stud_idx': 0, 'q_fam_idx': 0
}
for k, v in default_vars.items():
    if k not in st.session_state:
        st.session_state[k] = v

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Resetear ubicación default
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES (REVISADAS - SIN KEYERROR) ---
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
        'tab1_sub': "Le point de départ de votre projet.",
        'tab2_sub': "Votre métier est au cœur du programme.",
        'tab3_sub': "Le français est la clé du succès.",
        'tab4_sub': "Finalisez votre pointage.",
        
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_label': "Ville de destination",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Autre"],

        'age': "Âge du candidat",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat", "Technique (DEC)", "Secondaire"],

        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur (Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0, 1: Université / Gestion",
            "TEER 2: Collégial / Technique",
            "TEER 3: Métiers / Administration",
            "TEER 4, 5: Manœuvre / Service"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat", "Collégial (3 ans)", "Diplôme (1-2 ans)", "Secondaire"],
        'teer_manual_help': "Si non trouvé, utilisez le sélecteur :",
        'exp_label': "Années d'expérience",
        'exp_title': "Expérience (5 dernières années)",
        'exp_qc_label': "Mois au Québec", 'exp_ca_label': "Mois au Canada", 'exp_for_label': "Mois à l'étranger",

        'lang_info': "**Exigences :** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint",
        
        'oev_info': "ℹ️ **OEV (Offre Validée) :** Une offre formelle approuvée par le MIFI (EIMT).",
        'vjo_label': "Avez-vous une Offre Validée ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        
        'dip_qc_label': "Diplôme du Québec ?", 
        'dip_qc_help': "ℹ️ **Diplôme :** Avez-vous un diplôme (AEC, DEC, Bac...) obtenu au Québec ?",
        
        'fam_qc_label': "Famille au Québec ?", 
        'fam_qc_help': "ℹ️ **Famille :** Parent, enfant, conjoint, frère/sœur (Résident/Citoyen).",

        'res_title': "Résultat Estimé", 'advice_good': "Excellent !", 'advice_low': "Améliorez le français.",
        'details': "Détails du score", 'sp_points': "Pts Conjoint",
        'noc_link_text': "🔎 Chercher CNP",
        
        'guide_title': "Votre Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence."
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma",
        'brand': "Calculadora PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "No somos abogados ni asesores de migración. Somos un proyecto independiente informativo.",
        'coffee': "☕ Apoyar",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR",
        'yes_no': ["No", "Sí"],
        
        'step1': "Paso 1: Perfil", 'step2': "Paso 2: Trabajo", 'step3': "Paso 3: Idiomas", 'step4': "Paso 4: Quebec",
        'tab1_sub': "Tu perfil personal.",
        'tab2_sub': "Experiencia y oficio.",
        'tab3_sub': "El francés es la clave.",
        'tab4_sub': "Factores locales.",
        
        'loc_label': "¿Dónde estás hoy?",
        'loc_opts': ["En Quebec", "Canadá (Otro)", "Extranjero"],
        'country_label': "País de residencia",
        'arrival_label': "Fecha llegada (AAAA-MM-DD)",
        'city_label': "Ciudad destino",
        'city_opts': ["Montréal", "Québec", "Laval", "Gatineau", "Otra"],
        
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
        'edu_label': "Nivel Estudios",
        'edu_opts': ["PhD", "Maestría", "Bachelor", "College", "Diploma", "Secundaria"],
        'teer_manual_help': "Si no encuentras, elige:",
        'exp_label': "Años de experiencia",
        'exp_title': "Experiencia (5 años)",
        'exp_qc_label': "Meses Quebec", 'exp_ca_label': "Meses Canadá", 'exp_for_label': "Meses Extranjero",
        
        'lang_info': "Requisitos: Niv 7 (B2) | Pareja Niv 4",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja",
        
        'oev_info': "ℹ️ **VJO:** Oferta Validada por MIFI.",
        'vjo_label': "¿Oferta Validada?", 'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Región"],
        'dip_qc_label': "¿Diploma de Quebec?", 'dip_qc_help': "ℹ️ **Diploma:** ¿Título (AEC, DEC...) de Quebec?",
        'fam_qc_label': "¿Familia en Quebec?", 'fam_qc_help': "ℹ️ **Familia:** ¿Padres/Hijos/Hermanos Residentes?",
        
        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Pts Pareja",
        'noc_link_text': "🔎 Buscar NOC",
        
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Evaluar", 'g_desc1': "Fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia."
    },
    'en': {
        'btn_lang': "🌐 Change Lang",
        'brand': "PSTQ Calculator",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "Independent project. Not legal advice.",
        'coffee': "☕ Support",
        'courses': "📚 Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE",
        'yes_no': ["No", "Yes"],
        
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Personal profile.",
        'tab2_sub': "Experience and trade.",
        'tab3_sub': "Language skills.",
        'tab4_sub': "Local factors.",
        
        'loc_label': "Location?", 'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country", 'arrival_label': "Arrival Date",
        'city_label': "Dest. City", 'city_opts': ["Montréal", "Québec", "Laval", "Other"],
        'age': "Age", 'spouse': "Spouse?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        
        'job_title': "Current Job", 'job_place': "Ex: Welder (Enter)",
        'teer_label': "TEER Category",
        'teer_opts': ["TEER 0,1", "TEER 2", "TEER 3", "TEER 4,5"],
        'edu_label': "Education",
        'edu_opts': ["PhD", "Master", "Bachelor", "College", "Diploma", "Secondary"],
        'teer_manual_help': "If not found, select:",
        'exp_label': "Years Experience",
        'exp_title': "Experience (5 years)",
        'exp_qc_label': "Months Quebec", 'exp_ca_label': "Months Canada", 'exp_for_label': "Months Abroad",
        
        'lang_info': "Reqs: Lvl 7 (B2) | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French",
        
        'oev_info': "ℹ️ **VJO:** Validated Offer.",
        'vjo_label': "Validated Offer?", 'vjo_opts': ["No", "Yes, Montreal", "Yes, Region"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "ℹ️ **Diploma:** AEC, DEC from QC?",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "ℹ️ **Family:** PR or Citizen?",
        
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'noc_link_text': "🔎 Search NOC",
        
        'guide_title': "Roadmap",
        'g_step1': "1. Assess", 'g_desc1': "Strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Cert.",
        'g_step5': "5. Federal", 'g_desc5': "PR."
    }
}
l = t[st.session_state.language]

# --- 6. DATA JOBS ---
jobs_db = {"ingenie": {"code":"213xx","teer":"1"}, "soud": {"code":"72106","teer":"2"}}
def find_job_details(k):
    if not k: return None
    for j, d in jobs_db.items(): 
        if j in k.lower(): return d
    return None

# ==========================================
# HEADER
# ==========================================
st.markdown(f"""
<div class="pro-header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
    <div><h1>{l['brand']}</h1><p style="color:#e0e0e0; margin:0;">{l['subtitle']}</p></div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
</div>
""", unsafe_allow_html=True)

c_s, c_b = st.columns([3, 1])
with c_b: st.button(l['btn_lang'], on_click=cycle_language, type="secondary", key="top_lang_btn")
st.markdown("###")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tabs = st.tabs(l['main_tabs'])

# --- TAB 1: CALCULADORA ---
with main_tabs[0]:
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # PASO 1
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {l['step1']}")
        st.markdown(f"<div class='info-box'>{l['tab1_sub']}</div>", unsafe_allow_html=True)
        
        # Ubicación
        sel_loc = render_carousel(l['loc_label'], l['loc_opts'], 'loc', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.current_loc = sel_loc
        
        if "bec" not in sel_loc:
             st.text_input(l['country_label'], value=st.session_state.origin_country, placeholder="Ex: Belgique...")
             st.divider()
             sel_city = render_carousel(l['city_label'], l['city_opts'], 'city', l['btn_prev_c'], l['btn_next_c'])
             st.session_state.dest_city = sel_city
             st.divider()
             st.markdown(f"**{l['arrival_label']}**")
             st.session_state.arrival_text = st.text_input("Date", value=st.session_state.get('arrival_text', ''), placeholder="YYYY-MM-DD", label_visibility="collapsed")
        
        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.session_state.age = st.number_input(l['age'], 18, 65, st.session_state.age)
        with c2: st.session_state.spouse = st.checkbox(l['spouse'], value=st.session_state.spouse)
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(l['kids12'], 0, 5, st.session_state.k1)
        with c4: st.session_state.k2 = st.number_input(l['kids13'], 0, 5, st.session_state.k2)
        
        if st.session_state.spouse:
            st.divider()
            st.info(l['sp_header'])
            c_sa, c_se = st.columns(2)
            with c_sa: st.number_input(l['age'], 18, 65, 30, key="sp_age_in")
            with c_se: render_carousel(l['edu_label'], l['sp_edu_opts'], 'sp_edu', l['btn_prev_c'], l['btn_next_c'])
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 2
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {l['step2']}")
        st.markdown(f"<div class='info-box'>{l['tab2_sub']}</div>", unsafe_allow_html=True)
        
        st.text_input(l['job_title'], placeholder=l['job_place'])
        st.divider()
        
        sel_teer = render_carousel(l['teer_label'], l['teer_opts'], 'teer', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.teer_sel = sel_teer
        
        st.divider()
        sel_edu = render_carousel(l['edu_label'], l['edu_opts'], 'edu', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.edu = sel_edu
        
        st.divider()
        st.markdown(f"**{l['exp_title']}**")
        st.number_input(l['exp_qc_label'], 0, 60, st.session_state.exp_qc, key="eqc")
        st.number_input(l['exp_ca_label'], 0, 60, st.session_state.exp_ca, key="eca")
        st.number_input(l['exp_for_label'], 0, 60, st.session_state.exp_foreign, key="eex")

        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 3
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {l['step3']}")
        st.info(l['lang_info'])
        
        st.select_slider(l['fr_oral'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        st.select_slider(l['fr_write'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        st.select_slider(l['en'], ["0", "Beg", "Int", "Adv"], value="0")

        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{l['sp_fr_title']}**")
            st.select_slider("Niveau", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 4
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {l['step4']}")
        
        st.info(l['oev_info'])
        sel_vjo = render_carousel(l['vjo_label'], l['vjo_opts'], 'vjo', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.vjo = sel_vjo
        
        st.divider()
        st.info(l['dip_qc_help'])
        sel_stud = render_carousel(l['dip_qc_label'], l['yes_no'], 'q_stud', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.q_stud_val = sel_stud
        
        st.divider()
        st.info(l['fam_qc_help'])
        sel_fam = render_carousel(l['fam_qc_label'], l['yes_no'], 'q_fam', l['btn_prev_c'], l['btn_next_c'])
        st.session_state.q_fam_val = sel_fam

        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['calc'], type="primary", on_click=trigger_calculation)

    # RESULTADOS
    if st.session_state.show_results:
        st.markdown("---")
        score = 580
        st.markdown(f"""<div class="result-box"><h2>{l['res_title']}: {score} / 1350</h2></div>""", unsafe_allow_html=True)
        st.success(l['advice_good'])
        
        with st.expander(l['details']):
            st.write(f"**Principal:** {int(score)} pts")
            
        if st.button("🔄"): reset_calc(); st.rerun()

    # MONETIZACIÓN
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.link_button(l['coffee'], "https://buymeacoffee.com")
    with c2: st.link_button(l['courses'], "https://google.com")

# --- TAB 2: GUÍA ---
with main_tabs[1]:
    st.markdown(f"### 🗺️ {l['guide_title']}")
    st.markdown("---")
    st.markdown(f"<div class='info-box'><h4>📊 {l['g_step1']}</h4><p>{l['g_desc1']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'><h4>🗣️ {l['g_step2']}</h4><p>{l['g_desc2']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='info-box'><h4>📂 {l['g_step3']}</h4><p>{l['g_desc3']}</p></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.error(f"**{l['disclaimer_title']}**")
st.markdown(l['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
