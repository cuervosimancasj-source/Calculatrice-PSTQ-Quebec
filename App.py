import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (LIMPIO Y FUNCIONAL) ---
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
        
        /* Header */
        header[data-testid="stHeader"] { background-color: #003399 !important; }

        /* === 1. INPUTS BLANCOS === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important;
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
        }

        /* === 2. RADIO BUTTONS (LISTAS DE SELECCIÓN) === */
        /* El contenedor de las opciones */
        div[role="radiogroup"] {
            background-color: #FFFFFF;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
        }
        /* Las etiquetas de las opciones */
        div[role="radiogroup"] label {
            color: #333333 !important;
            margin-bottom: 5px;
        }
        /* El círculo */
        div[data-baseweb="radio"] div {
            background-color: #FFFFFF !important;
            border-color: #003399 !important;
        }
        div[data-baseweb="radio"][aria-checked="true"] div div {
            background-color: #003399 !important;
        }

        /* === 3. BOTONES === */
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

        /* === 4. EXTRAS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 10px; border-radius: 5px; margin-bottom: 10px; }
        .step-box { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; }
        
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; color: white; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        
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
            text-align: center;
            flex-grow: 1;
        }
        .pro-header p { color: #e0e0e0 !important; margin: 0; text-align: center; font-size: 0.9rem; }
        .flag-icon { height: 35px; border: 1px solid white; border-radius: 4px; }
        
        /* Enlaces */
        div.stLinkButton > a {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            text-align: center;
            font-weight: bold;
            border-radius: 8px;
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. INICIALIZACIÓN ---
default_values = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary', 'sp_fr': '0',
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'job_search_term': '', 'current_loc': '', 'origin_country': '', 
    'arrival_text': '',
    'teer_sel': 'TEER 0, 1', # Valor defecto
    'edu': 'Secondary', 
    'sp_edu_val': 'Secondary'
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Resetear valores dependientes del idioma
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]
    st.session_state.teer_sel = t[st.session_state.language]['teer_opts'][0]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 4. TRADUCCIONES (AHORA SÍ COMPLETAS - SIN KEYERROR) ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Projet indépendant. Pas de conseil juridique.",
        'coffee': "☕ Café", 'courses': "📚 Cours",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER",
        'yes_no': ["Non", "Oui"],
        'step1': "Étape 1 : Profil", 'step2': "Étape 2 : Travail", 'step3': "Étape 3 : Langues", 'step4': "Étape 4 : Québec",
        'tab1_sub': "Votre profil personnel.",
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_label': "Ville de destination",
        'city_opts': ["Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Autre"],
        'age': "Âge", 'spouse': "Conjoint ?", 'kids12': "Enfants -12", 'kids13': "Enfants +12",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge conjoint", 'sp_edu': "Éducation conjoint",
        'sp_edu_opts': ["PhD", "Maîtrise", "Baccalauréat", "Technique", "Secondaire"],
        'job_title': "Emploi actuel", 'job_place': "Ex: Ingénieur (Entrée)",
        'teer_label': "Catégorie TEER",
        'teer_opts': [
            "TEER 0,1: Gestion/Univ", "TEER 2: Collégial/Tech", 
            "TEER 3: Métiers/Admin", "TEER 4,5: Manœuvre/Service"
        ],
        'edu_label': "Niveau d'études",
        'edu_opts': ["PhD", "Maîtrise", "Baccalauréat", "Collégial", "Diplôme Pro", "Secondaire"],
        'teer_manual_help': "Ou sélectionnez dans la liste :",
        'exp_title': "Expérience (5 ans)",
        'exp_qc_label': "Mois Québec", 'exp_ca_label': "Mois Canada", 'exp_for_label': "Mois Étranger",
        'lang_info': "Niv 7 (B2) Principal | Niv 4 (A2) Conjoint",
        'fr_oral': "Français Oral", 'fr_write': "Français Écrit", 'en': "Anglais",
        'sp_fr_title': "Français Conjoint",
        'oev_info': "ℹ️ **OEV:** Offre validée par MIFI.",
        'vjo_label': "Offre Validée ?", 'vjo_opts': ["Non", "Oui (Montréal)", "Oui (Région)"],
        'dip_qc_label': "Diplôme Québec ?", 'dip_qc_help': "AEC, DEC, Bac...",
        'fam_qc_label': "Famille Québec ?", 'fam_qc_help': "Résident/Citoyen.",
        'res_title': "Résultat", 'advice_good': "Excellent !", 'advice_low': "Améliorez votre profil.",
        'details': "Détails", 'sp_points': "Pts Conjoint",
        'noc_link_text': "🔎 Chercher CNP",
        # ESTAS FALTABAN Y CAUSABAN EL ERROR:
        'guide_title': "Votre Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence."
    },
    'es': {
        'btn_lang': "🌐 Cambiar Idioma", 'brand': "Calculadora PSTQ",
        'subtitle': "Análisis Residencia Permanente.",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "Independiente. NO abogados.",
        'coffee': "☕ Café", 'courses': "📚 Cursos",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "CALCULAR",
        'yes_no': ["No", "Sí"],
        'step1': "Paso 1: Perfil", 'step2': "Paso 2: Trabajo", 'step3': "Paso 3: Idiomas", 'step4': "Paso 4: Quebec",
        'tab1_sub': "Tu perfil personal.",
        'loc_label': "¿Dónde estás?", 'loc_opts': ["En Quebec", "Canadá (Otro)", "Extranjero"],
        'country_label': "País residencia", 'arrival_label': "Fecha llegada",
        'city_label': "Ciudad destino", 'city_opts': ["Montreal", "Quebec", "Laval", "Otra"],
        'age': "Edad", 'spouse': "¿Pareja?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_header': "Datos Pareja", 'sp_age': "Edad pareja", 'sp_edu': "Educación pareja",
        'sp_edu_opts': ["PhD", "Maestría", "Bachelor", "Técnico", "Secundaria"],
        'job_title': "Trabajo actual", 'job_place': "Ej: Ingeniero (Enter)",
        'teer_label': "Categoría TEER",
        'teer_opts': [
            "TEER 0,1: Uni/Gerencia", "TEER 2: Tec/College", 
            "TEER 3: Oficios", "TEER 4,5: Manual/Secund"
        ],
        'edu_label': "Nivel Estudios",
        'edu_opts': ["PhD", "Maestría", "Bachelor", "College", "Diploma", "Secundaria"],
        'teer_manual_help': "O selecciona abajo:",
        'exp_title': "Experiencia (5 años)",
        'exp_qc_label': "Meses Quebec", 'exp_ca_label': "Meses Canadá", 'exp_for_label': "Meses Extranjero",
        'lang_info': "Reqs: Niv 7 (B2) | Pareja Niv 4",
        'fr_oral': "Francés Oral", 'fr_write': "Francés Escrito", 'en': "Inglés",
        'sp_fr_title': "Francés Pareja",
        'oev_info': "ℹ️ **VJO:** Oferta Validada.",
        'vjo_label': "¿Oferta Validada?", 'vjo_opts': ["No", "Sí (Montreal)", "Sí (Región)"],
        'dip_qc_label': "¿Diploma Quebec?", 'dip_qc_help': "AEC, DEC...",
        'fam_qc_label': "¿Familia Quebec?", 'fam_qc_help': "Residente/Ciudadano.",
        'res_title': "Resultado", 'advice_good': "¡Excelente!", 'advice_low': "Mejora el francés.",
        'details': "Detalles", 'sp_points': "Pts Pareja",
        'noc_link_text': "🔎 Buscar NOC",
        # ESTAS FALTABAN:
        'guide_title': "Tu Hoja de Ruta",
        'g_step1': "1. Evaluar", 'g_desc1': "Fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2.",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia."
    },
    'en': {
        'btn_lang': "🌐 Change Lang", 'brand': "PSTQ Calculator",
        'subtitle': "Residency Analysis Tool.",
        'disclaimer_title': "⚠️ DISCLAIMER", 'disclaimer_text': "Independent. Not lawyers.",
        'coffee': "☕ Support", 'courses': "📚 Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "CALCULATE",
        'yes_no': ["No", "Yes"],
        'step1': "Step 1: Profile", 'step2': "Step 2: Work", 'step3': "Step 3: Languages", 'step4': "Step 4: Quebec",
        'tab1_sub': "Personal profile.",
        'loc_label': "Location?", 'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country_label': "Country", 'arrival_label': "Arrival Date",
        'city_label': "Dest. City", 'city_opts': ["Montreal", "Quebec", "Laval", "Other"],
        'age': "Age", 'spouse': "Spouse?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_header': "Spouse Data", 'sp_age': "Spouse Age", 'sp_edu': "Spouse Edu",
        'sp_edu_opts': ["PhD", "Master", "Bachelor", "Technical", "Secondary"],
        'job_title': "Current Job", 'job_place': "Ex: Welder (Enter)",
        'teer_label': "TEER Category",
        'teer_opts': ["TEER 0,1", "TEER 2", "TEER 3", "TEER 4,5"],
        'edu_label': "Education",
        'edu_opts': ["PhD", "Master", "Bachelor", "College", "Diploma", "Secondary"],
        'teer_manual_help': "Select below:",
        'exp_title': "Experience (5 years)",
        'exp_qc_label': "Months Quebec", 'exp_ca_label': "Months Canada", 'exp_for_label': "Months Abroad",
        'lang_info': "Reqs: Lvl 7 | Spouse Lvl 4",
        'fr_oral': "French Oral", 'fr_write': "French Written", 'en': "English",
        'sp_fr_title': "Spouse French",
        'oev_info': "ℹ️ **VJO:** Validated Offer.",
        'vjo_label': "Validated Offer?", 'vjo_opts': ["No", "Yes (Montreal)", "Yes (Region)"],
        'dip_qc_label': "Quebec Diploma?", 'dip_qc_help': "AEC, DEC...",
        'fam_qc_label': "Family in Quebec?", 'fam_qc_help': "PR or Citizen.",
        'res_title': "Result", 'advice_good': "Excellent!", 'advice_low': "Improve French.",
        'details': "Details", 'sp_points': "Spouse Pts",
        'noc_link_text': "🔎 Search NOC",
        # ESTAS FALTABAN:
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
with c_b: st.button(l['btn_lang'], on_click=cycle_language, type="secondary", use_container_width=True)
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
        
        st.markdown(f"**{l['loc_label']}**")
        idx_loc = 0
        if st.session_state.current_loc in l['loc_opts']: idx_loc = l['loc_opts'].index(st.session_state.current_loc)
        st.session_state.current_loc = st.radio("Loc", l['loc_opts'], index=idx_loc, label_visibility="collapsed")

        if "bec" not in st.session_state.current_loc:
            st.text_input(l['country_label'], placeholder="Ex: Belgique, France...")
            st.divider()
            st.markdown(f"**{l['city_label']}**")
            st.radio("City", l['city_opts'], index=0, label_visibility="collapsed")
            st.divider()
            st.markdown(f"**{l['arrival_label']}**")
            st.text_input("Date", placeholder="YYYY-MM-DD", label_visibility="collapsed")
        
        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.session_state.age = st.number_input(l['age'], 18, 65, 30)
        with c2: st.session_state.spouse = st.checkbox(l['spouse'], value=st.session_state.spouse)
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(l['kids12'], 0, 5, 0)
        with c4: st.session_state.k2 = st.number_input(l['kids13'], 0, 5, 0)
        
        if st.session_state.spouse:
            st.info(l['sp_header'])
            c_sa, c_se = st.columns(2)
            with c_sa: st.number_input(l['sp_age'], 18, 65, 30)
            with c_se: st.radio("SpEdu", l['sp_edu_opts'], index=2, label_visibility="collapsed")
        
        st.markdown("###")
        col_e, col_n = st.columns([3, 1])
        with col_n: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 2
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {l['step2']}")
        st.text_input(l['job_title'], placeholder=l['job_place'])
        st.divider()
        
        st.markdown(f"**{l['teer_label']}**")
        idx_t = 0
        if st.session_state.teer_sel in l['teer_opts']: idx_t = l['teer_opts'].index(st.session_state.teer_sel)
        st.session_state.teer_sel = st.radio("TEER", l['teer_opts'], index=idx_t, label_visibility="collapsed")
        
        st.divider()
        st.markdown(f"**{l['edu_label']}**")
        st.radio("Edu", l['edu_opts'], index=2, label_visibility="collapsed")
        
        st.divider()
        st.markdown(f"**{l['exp_title']}**")
        st.number_input(l['exp_qc_label'], 0, 60, 0)
        st.number_input(l['exp_ca_label'], 0, 60, 0)
        st.number_input(l['exp_for_label'], 0, 60, 36)

        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 3
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {l['step3']}")
        st.info(l['lang_info'])
        st.select_slider(l['fr_oral'], ["0","A1","A2","B1","B2","C1","C2"], value="B2")
        st.select_slider(l['fr_write'], ["0","A1","A2","B1","B2","C1","C2"], value="B1")
        st.select_slider(l['en'], ["0","Beg","Int","Adv"], value="0")
        
        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{l['sp_fr_title']}**")
            st.select_slider("Niveau", ["0","A1","A2","B1","B2","C1","C2"], value="0")
            
        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['next'], type="primary", on_click=next_step)

    # PASO 4
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {l['step4']}")
        st.info(l['oev_info'])
        idx_v = 0
        if st.session_state.vjo in l['vjo_opts']: idx_v = l['vjo_opts'].index(st.session_state.vjo)
        st.session_state.vjo = st.radio(l['vjo_label'], l['vjo_opts'], index=idx_v)
        
        st.divider()
        st.info(l['dip_qc_help'])
        st.radio(l['dip_qc_label'], l['yes_no'], horizontal=True)
        
        st.divider()
        st.info(l['fam_qc_help'])
        st.radio(l['fam_qc_label'], l['yes_no'], horizontal=True)
        
        st.markdown("###")
        cp, cn = st.columns(2)
        with cp: st.button(l['prev'], type="secondary", on_click=prev_step)
        with cn: st.button(l['calc'], type="primary", on_click=trigger_calculation)

    # RESULTADOS
    if st.session_state.show_results:
        st.markdown("---")
        score = 580 # Simulado
        st.markdown(f"<div class='result-box'><h2>{l['res']}: {score}</h2></div>", unsafe_allow_html=True)
        st.success(l['adv_g'])
        if st.button("🔄"): reset_calc(); st.rerun()
        
    # MONETIZACIÓN
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: st.link_button(l['coffee'], "https://www.buymeacoffee.com")
    with c2: st.link_button(l['courses'], "https://google.com")

# --- TAB 2: GUÍA ---
with main_tabs[1]:
    st.markdown(f"### 🗺️ {l['guide_title']}")
    st.markdown("---")
    st.markdown(f"<div class='step-box'><h4>📊 {l['g_step1']}</h4><p>{l['g_desc1']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='step-box'><h4>🗣️ {l['g_step2']}</h4><p>{l['g_desc2']}</p></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='step-box'><h4>📂 {l['g_step3']}</h4><p>{l['g_desc3']}</p></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.error(f"**{l['disclaimer_title']}**")
st.markdown(l['disclaimer_text'])
st.markdown("</div>", unsafe_allow_html=True)
