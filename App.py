import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (DISEÑO CARRUSEL) ---
st.markdown("""
    <style>
        /* === 0. BASE === */
        :root { color-scheme: light only !important; }
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important;
            color: #000000 !important;
        }
        .stApp, p, label, h1, h2, h3, h4, h5, h6, div, span, li {
            color: #000000 !important;
        }
        header[data-testid="stHeader"] { background-color: #003399 !important; }
        h1 { color: #FFFFFF !important; }

        /* === 1. CAJAS DE VISUALIZACIÓN (CARRUSEL) === */
        .stepper-display {
            background-color: #FFFFFF;
            color: #000000;
            padding: 10px;
            border: 1px solid #003399;
            border-radius: 8px;
            text-align: center;
            font-weight: bold;
            min-height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* === 2. BOTONES DE CARRUSEL (FLECHAS) === */
        /* Botones pequeños para cambiar opciones */
        div[data-testid="column"] button {
            background-color: #e0e0e0 !important;
            color: #000000 !important;
            border: 1px solid #ccc !important;
            height: 45px;
        }
        div[data-testid="column"] button:hover {
            background-color: #d0d0d0 !important;
            border-color: #003399 !important;
        }

        /* === 3. INPUTS DE TEXTO (BUSCADOR/PAÍS) === */
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

        /* === 4. BOTONES PRINCIPALES (ANCHO COMPLETO) === */
        /* Usamos selectores específicos para no afectar las flechas del carrusel */
        div.stButton > button[kind="primary"] {
            width: 100%;
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }
        
        div.stButton > button[kind="secondary"] {
            width: 100%;
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }

        /* === 5. EXTRAS === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 1.5rem; 
            border-radius: 15px;
            border-top: 5px solid #003399;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 10px; border-radius: 5px; margin-bottom: 10px; }
        .result-box { background-color: #003399; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .deco-sub { color: #666 !important; font-style: italic; margin-bottom: 15px; display: block; font-size: 0.9em; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; }
        
        /* Header Pro */
        .pro-header {
            background-color: #003399; padding: 15px 20px; border-radius: 12px;
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        .pro-header h1 { color: #FFFFFF !important; margin: 0; text-align: center; font-size: 1.5rem; flex-grow: 1; }
        .pro-header p { color: #e0e0e0 !important; }
        .flag-icon { height: 40px; border: 1px solid white; border-radius: 4px; }
        
        /* Enlaces */
        div.stLinkButton > a {
            background-color: #003399 !important; color: #FFFFFF !important; font-weight: bold !important; text-align: center !important;
        }
        div.stLinkButton > a * { color: #FFFFFF !important; }
        
        /* Radio */
        div[role="radiogroup"] label { color: #000000 !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (STEPPER) ---
def render_carousel(label, options, key_name):
    """Crea un selector tipo carrusel con botones"""
    # Inicializar índice en session_state
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    st.markdown(f"**{label}**")
    
    c_prev, c_disp, c_next = st.columns([1, 4, 1])
    
    with c_prev:
        if st.button("◀", key=f"btn_prev_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
            
    with c_next:
        if st.button("▶", key=f"btn_next_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
    with c_disp:
        current_val = options[st.session_state[f"{key_name}_idx"]]
        st.markdown(f"<div class='stepper-display'>{current_val}</div>", unsafe_allow_html=True)
    
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
    'arrival_date': date.today(),
    # Indices para carruseles
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0
}
for key, value in default_values.items():
    if key not in st.session_state: st.session_state[key] = value

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]
    # Resetear ubicación
    st.session_state.current_loc = t[st.session_state.language]['loc_opts'][2]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
    st.session_state.job_search_term = ''

def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ",
        'subtitle': "Outil d'analyse pour la Résidence Permanente.",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants.",
        'coffee': "☕ M'offrir un café", 'courses': "📚 Cours",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "CALCULER",
        'yes_no': ["Non", "Oui"],
        'step1': "Étape 1 : Profil & Famille",
        'step2': "Étape 2 : Travail & TEER",
        'step3': "Étape 3 : Langues",
        'step4': "Étape 4 : Québec & Offre",
        'tab1_sub': "Situation personnelle et familiale.",
        'tab2_sub': "Votre métier et expérience.",
        'tab3_sub': "Le français est la clé.",
        'tab4_sub': "Facteurs Québec.",
        
        'loc_label': "Où êtes-vous actuellement ?",
        'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country_label': "Pays de résidence",
        'arrival_label': "Date d'arrivée (AAAA-MM-JJ)",
        'city_opts': ["-", "Montréal", "Québec (Ville)", "Laval", "Gatineau", "Sherbrooke", "Trois-Rivières", "Saguenay", "Autre"],
        'city_label': "Ville de destination",

        'age': "Âge du candidat",
        'spouse': "Avez-vous un conjoint ?",
        'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'sp_header': "Données du Conjoint",
        'sp_age': "Âge du conjoint", 'sp_edu': "Éducation conjoint",
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
        'edu_opts': ["PhD (Doctorat)", "Maîtrise", "Baccalauréat (Univ)", "Collégial (3 ans)", "Dipl
