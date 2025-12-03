import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (CORRECCIÓN DE BOTONES Y DISEÑO) ---
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

        /* === 1. INPUTS DE TEXTO (BLINDAJE) === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
            opacity: 1 !important;
        }

        /* === 2. SOLUCIÓN BOTONES +/- (NUMÉRICOS) === */
        /* Forzamos un gris visible para los botones de sumar/restar */
        button[tabindex="-1"] {
            background-color: #e0e0e0 !important; 
            border: 1px solid #999 !important;
            color: #000000 !important;
        }
        /* El icono + o - dentro del botón */
        button[tabindex="-1"] span, button[tabindex="-1"] svg {
            color: #000000 !important;
            fill: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
        }

        /* === 3. CARRUSEL (DISPLAY) === */
        .stepper-box {
            background-color: #FFFFFF;
            color: #003399;
            padding: 10px;
            border: 2px solid #003399;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            font-size: 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 55px;
            margin-bottom: 8px;
        }

        /* === 4. BOTONES DE ACCIÓN === */
        div.stButton > button { 
            width: 100%; 
            border-radius: 8px; 
            font-weight: 600; 
        }
        
        /* Primario (Siguiente) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Secundario (Atrás) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        
        /* Botones Pequeños del Carrusel (Flechas) */
        div[data-testid="column"] button {
            background-color: #f1f3f4 !important;
            color: #003399 !important;
            border: 1px solid #ccc !important;
            height: 40px !important; /* Más pequeños */
            padding: 0 !important;
        }

        /* === 5. EXTRAS === */
        /* Header Pro */
        .pro-header {
            background-color: #003399;
            padding: 15px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.4rem;
            text-align: center;
            flex-grow: 1;
        }
        .pro-header p { color: #e0e0e0 !important; margin: 0; text-align: center; font-size: 0.8rem; }
        .flag-icon { height: 35px; border: 1px solid white; border-radius: 4px; }
        
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 10px; border-radius: 5px; margin-bottom: 10px; }
        .result-box { background: linear-gradient(135deg, #003399, #0056b3); padding: 20px; border-radius: 10px; text-align: center; color: white; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; font-size: 0.8rem; color: #666; }
        .deco-sub { color: #666; font-style: italic; margin-bottom: 15px; display: block; font-size: 0.9rem; }
        
        /* Radio */
        div[role="radiogroup"] label { color: #333 !important; }
        
        /* Enlaces Monetización (Estilo botón azul) */
        div.stLinkButton > a {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            font-weight: bold;
            text-align: center;
            border-radius: 8px;
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (BOTONES ABAJO) ---
def render_carousel(label, options, key_name):
    """Selector con botones debajo para móvil"""
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    # Etiqueta
    st.markdown(f"**{label}**")
    
    # Caja de visualización (Texto)
    current_val = options[st.session_state[f"{key_name}_idx"]]
    st.markdown(f"<div class='stepper-box'>{current_val}</div>", unsafe_allow_html=True)
    
    # Botones debajo (Pequeños y en esquinas)
    c1, c2, c3 = st.columns([1, 2, 1]) # Espacio en el medio
    
    with c1:
        if st.button("⬅️", key=f"prev_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
    
    with c3:
        if st.button("➡️", key=f"next_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
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
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2, 'loc_idx': 2
}

for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Resetear ubicacion por defecto
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES (REVISADAS A FONDO) ---
t = {
    'fr': {
        'btn_lang': "🌐 Français", 'brand': "CALCULATRICE PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants. Nous ne représentons PAS le MIFI.",
        'coffee': "☕ M'offrir un café", 'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER MON SCORE",
        'yes_no': ["Non", "Oui"],
        'step1': "Étape 1 : Profil", 'step2': "Étape 2 : Travail", 'step3': "Étape 3 : Langues", 'step4': "Étape 4 : Québec",
        'tab1_sub': "Situation personnelle et familiale.",
        'tab2_sub': "Expérience et métier.",
        'tab3_sub': "Le français est la clé.",
        'tab4_sub': "Facteurs locaux.",
        
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_label': "Ville de destination",
        'city_opts': ["Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Autre"],

        'age': "Âge du candidat", 'spouse': "Conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD", "Maîtrise", "Baccalauréat", "Technique", "Secondaire"],
        
        'job_title': "Quel est votre emploi actuel ?",
        'job_place': "Ex: Ingénieur (Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0,1: Gestion / Univ",
            "TEER 2: Collégial / Tech",
            "TEER 3: Métiers / Admin",
            "TEER 4,5: Manœuvre / Sec"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD", "Maîtrise", "Baccalauréat", "Collégial (3 ans)", "Diplôme (1-2 ans)", "Secondaire"],
        'teer_manual_help': "Si non trouvé, utilisez le sélecteur :",
        'exp_title': "Expérience (5 dernières années)",
        'exp_qc_label': "Mois au Québec",
        'exp_ca_label': "Mois au Canada",
        'exp_for_label': "Mois à l'étranger",

        'lang_info': "**Exigences:** Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français du Conjoint",
        
        'oev_info': "**ℹ️ OEV:** Offre validée par le MIFI.",
        'vjo_label': "Offre Validée (OEV) ?",
        'vjo_opts': ["Non", "Oui, Grand Montréal", "Oui, Région"],
        'dip_qc_label': "Diplôme du Québec ?", 'dip_qc_help': "AEC, DEC, Bac...",
        'fam_qc_label': "Famille au Québec ?", 'fam_qc_help': "Résident ou Citoyen.",
        
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
        'btn_lang': "🌐 Español", 'brand': "CALCULADORA PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "No somos abogados ni asesores de migración y tampoco hacemos parte del gobierno. Somos un proyecto independiente.",
        'coffee': "☕ Apoyar", 'courses': "📚 Cursos",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil", 'step2': "Paso 2: Trabajo", 'step3': "Paso 3: Idiomas", 'step4': "Paso 4: Quebec",
        'tab1_sub': "Situación personal y familiar.",
        'tab2_sub': "Experiencia y oficio.",
        'tab3_sub': "El francés es la clave.", 'tab4_sub': "Factores locales.",
        'loc_label': "¿Dónde estás hoy?", 'loc_opts': ["En Quebec", "Canadá (Otro)", "Extranjero"],
        'country_label': "País de residencia", 'city_label': "Ciudad destino", 'arrival_label': "Fecha llegada",
        'city_opts': ["Montreal", "Quebec", "Laval", "Gatineau", "Otra"],
        
        'age': "Edad", 'spouse': "¿Pareja?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_header': "Datos Pareja", 'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD", "Maestría", "Bachelor", "Técnico", "Secundaria"],
        
        'job_title': "Trabajo actual", 'job_place': "Ej: Ingeniero (Enter)",
        'teer_label': "Categoría TEER",
        'teer_opts': ["TEER 0,1: Uni/Gerencia", "TEER 2: Tec/College", "TEER 3: Oficios", "TEER 4,5: Manual"],
        'edu_label': "Nivel Estudios",
        'edu_opts': ["PhD", "Maestría", "Bachelor", "College (3 años)", "Diploma (1-2 años)", "Secundaria"],
        'teer_manual_help': "Si no encuentras, usa el selector:",
        'exp_title': "Experiencia (5 años)",
        'exp_qc_label': "Meses en Quebec", 'exp_ca_label': "Meses en Canadá", 'exp_for_label': "Meses Extranjero",
        
        'lang_info': "Requisitos: Niv 7 (B2) | Pareja Niv 4 (A2)",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja",
        
        'oev_info': "**ℹ️ VJO:** Oferta Validada.",
        'vjo_label': "¿Oferta Validada?", 'vjo_opts': ["No", "Sí, Gran Montreal", "Sí, Región"],
        'dip_qc_label': "¿Diploma Quebec?", 'dip_qc_help': "AEC, DEC, Bachelor...",
        'fam_qc_label': "¿Familia Quebec?", 'fam_qc_help': "Residente/Ciudadano.",
        
        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Pts Pareja",
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia.",
        'noc_link_text': "🔎 Buscar NOC"
    },
    'en': {
        'btn_lang': "🌐 English", 'brand': "PSTQ CALCULATOR",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "We are not lawyers or immigration consultants and we are not part of the government. We are an independent project.",
        'coffee': "☕ Support", 'courses': "📚 Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Personal and family situation.",
        'tab2_sub': "Experience and trade.",
        'tab3_sub': "Language skills.", 'tab4_sub': "Local factors.",
        'loc_label': "Current location?", 'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country", 'arrival_label': "Arrival Date", 'city_label': "Dest. City",
        'city_opts': ["Montreal", "Quebec", "Laval", "Other"],
        'age': "Age", 'spouse': "Spouse?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        'job_title': "Current Job", 'job_place': "Ex: Welder (Enter)",
        'teer_label': "TEER Category", 
        'teer_opts': ["TEER 0,1: Mgmt", "TEER 2: Tech", "TEER 3: Trades", "TEER 4,5: Manual"],
        'edu_label': "Education",
        'edu_opts': ["PhD", "Master", "Bachelor", "College", "Diploma", "Secondary"],
        'teer_manual_help': "If not found, select:",
        'exp_title': "Experience (5 years)",
        'exp_qc_label': "Months Quebec", 'exp_ca_label': "Months Canada", 'exp_for_label': "Months Abroad",
        'lang_info': "Reqs: Lvl 7 (B2) | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French",
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
        'noc_link_text': "🔎 Search NOC"
    }
}
l = t[st.session_state.language]

# --- 6. DATA JOBS ---
jobs_db = {"ingenie": {"code":"21300","teer":"1"}, "soud": {"code":"72106","teer":"2"}, "weld": {"code":"72106","teer":"2"}}
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
    <div><h1>{l['brand']}</h1><p>{l['subtitle']}</p></div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
</div>
""", unsafe_allow_html=True)

c_s, c_b = st.columns([3, 1])
with c_b: st.button(l['btn_lang'], on_click=cycle_language, type="secondary", use_container_width=True)
st.markdown("###")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tabs = st.tabs(l['main_tabs'])

with main_tabs[0]: # CALCULADORA
    progress = (st.session_state.step / 4)
    st.progress(progress)

    # --- PASO 1 ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {l['step1']}")
        st.markdown(f"<span class='deco-sub'>{l['tab1_sub']}</span>", unsafe_allow_html=True)
        
        # Ubicación (Carrusel)
        sel_loc = render_carousel(l['loc_label'], l['loc_opts'], 'loc')
        st.session_state.current_loc = sel_loc
        
        if "bec" not in sel_loc and "Quebec" not in sel_loc:
            st.text_input(l['country_label'], placeholder="Ex: Belgique...")
            st.divider()
            sel_city = render_carousel(l['city_label'], l['city_opts'], 'city')
            st.text_input(l['arrival_label'], placeholder="YYYY-MM-DD")
        
        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.number_input(l['age'], 18, 65, 30, key="age_in")
        with c2: 
            spouse = st.checkbox(l['spouse'])
            st.session_state.spouse = spouse
        
        c3, c4 = st.columns(2)
        with c3: st.number_input(l['kids12'], 0, 5, 0, key="k1_in")
        with c4: st.number_input(l['kids13'], 0, 5, 0, key="k2_in")
        
        if spouse:
            st.info(l['sp_header'])
            c_sa, c_se = st.columns(2)
            with c_sa: st.number_input(l['sp_age'], 18, 65, 30, key="sp_age_in")
            with c_se: render_carousel(l['sp_edu'], l['sp_edu_opts'], 'sp_edu')

        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(l['next'], type="primary", on_click=next_step)

    # --- PASO 2 ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {l['step2']}")
        st.markdown(f"<span class='deco-sub'>{l['tab2_sub']}</span>", unsafe_allow_html=True)
        
        st.text_input(l['job_title'], placeholder=l['job_place'])
        st.divider()
        
        # Carruseles
        render_carousel(l['teer_label'], l['teer_opts'], 'teer')
        st.divider()
        render_carousel(l['edu_label'], l['edu_opts'], 'edu')
        
        st.divider()
        st.markdown(f"**{l['exp_title']}**")
        st.number_input(l['exp_qc_label'], 0, 60, 0, key="eqc")
        st.number_input(l['exp_ca_label'], 0, 60, 0, key="eca")
        st.number_input(l['exp_for_label'], 0, 60, 36, key="eex")

        st.markdown("###")
        cp, cn = st.columns([1, 1])
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['next'], type="primary", on_click=next_step)

    # --- PASO 3 ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {l['step3']}")
        st.markdown(f"<span class='deco-sub'>{l['tab3_sub']}</span>", unsafe_allow_html=True)
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

    # --- PASO 4 ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {l['step4']}")
        st.markdown(f"<span class='deco-sub'>{l['tab4_sub']}</span>", unsafe_allow_html=True)
        
        st.info(l['oev_info'])
        render_carousel(l['vjo_label'], l['vjo_opts'], 'vjo')
        
        st.divider()
        st.info(l['dip_qc_help'])
        render_carousel(l['dip_qc_label'], l['yes_no'], 'dip_qc')
        
        st.divider()
        st.info(l['fam_qc_help'])
        render_carousel(l['fam_qc_label'], l['yes_no'], 'fam_qc')

        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['calc'], type="primary", on_click=trigger_calculation)

    # RESULTADOS
    if st.session_state.show_results:
        st.markdown("---")
        # Lógica simplificada para demo visual
        score = 580
        st.markdown(f"""
        <div class="result-box">
            <h2>{l['res']}: {score} / 1350</h2>
        </div>
        """, unsafe_allow_html=True)
        st.success(l['adv_g'])
        
        with st.expander(l['details']):
            st.write("Détails...")
            
        if st.button("🔄"): reset_calc(); st.rerun()

    # BOTONES MONETIZACIÓN
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.link_button(l['coffee'], "https://buymeacoffee.com")
    with c2: st.link_button(l['courses'], "https://google.com")

# --- TAB 2: GUÍA ---
with main_tabs[1]:
    st.markdown(f"### 🗺️ {l['guide_title']}")
    st.markdown("---")
    st.markdown(f"<div class='step-box'><h4>📊 {l['g_step1']}</h4><p>{l['g_desc1']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='step-box'><h4>🗣️ {l['g_step2']}</h4><p>{l['g_desc2']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='step-box'><h4>📂 {l['g_step3']}</h4><p>{l['g_desc3']}</p></div>", unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.error(f"**{l['disclaimer_title']}**")
st.markdown(l['disclaimer_text'])
st.caption(l['legal'])
