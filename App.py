import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (LIMPIEZA Y PROFESIONALISMO) ---
st.markdown("""
    <style>
        /* === 0. BASE MODO CLARO OBLIGATORIO === */
        :root { color-scheme: light only !important; }
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #f4f7f6 !important; /* Fondo Gris Suave */
            color: #333333 !important; /* Texto Gris Oscuro */
            font-family: sans-serif;
        }
        
        /* Textos Generales */
        h1, h2, h3 { color: #003399 !important; }
        p, label, li, div { color: #333333 !important; }

        /* === 1. ENCABEZADO PREMIUM === */
        header[data-testid="stHeader"] { visibility: hidden; } /* Ocultar barra nativa */
        
        .pro-header {
            background-color: #003399;
            padding: 20px;
            border-radius: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.4rem;
            text-align: center;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            flex-grow: 1;
        }
        .flag-icon { height: 40px; border: 1px solid white; border-radius: 4px; }

        /* === 2. CAJAS DE TEXTO (INPUTS) BLINDADAS === */
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #cccccc !important;
            border-radius: 8px !important;
        }
        input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important; /* Fix iPhone */
            background-color: #FFFFFF !important;
            caret-color: #000000 !important;
        }

        /* === 3. SELECTOR CARRUSEL (ANTI-INSTAGRAM) === */
        /* Caja central del dato seleccionado */
        .stepper-display {
            background-color: #FFFFFF;
            color: #003399;
            border: 2px solid #003399;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            font-weight: bold;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 50px;
        }
        
        /* Botones de flecha del carrusel */
        div[data-testid="column"] button {
            background-color: #f0f2f5 !important;
            color: #003399 !important;
            border: 1px solid #ccc !important;
            height: 50px !important;
            width: 100% !important;
            font-size: 1.5rem !important;
            padding: 0 !important;
            line-height: 1 !important;
        }
        div[data-testid="column"] button:hover {
            background-color: #e0e0e0 !important;
            border-color: #003399 !important;
        }

        /* === 4. BOTONES DE ACCIÓN (AZULES) === */
        div.stButton > button { 
            width: 100%; 
            border-radius: 8px; 
            font-weight: 600; 
            height: 45px; 
        }
        
        /* Primario (Siguiente/Calcular) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        div.stButton > button[kind="primary"] * { color: #FFFFFF !important; }

        /* Secundario (Atrás) */
        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
        }
        div.stButton > button[kind="secondary"] * { color: #003399 !important; }

        /* === 5. CONTENEDOR PRINCIPAL === */
        [data-testid="stForm"] {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 15px;
            border-top: 6px solid #003399;
            box-shadow: 0 5px 20px rgba(0,0,0,0.05);
        }

        /* === 6. EXTRAS === */
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
        .result-box { background: linear-gradient(135deg, #003399, #0055ff); padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; color: white; }
        .result-box h2 { color: #FFFFFF !important; margin: 0; }
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; font-size: 0.85rem; }
        
        /* Botones numéricos (+/-) */
        button[tabindex="-1"] { background-color: #f1f1f1 !important; color: #000 !important; border: 1px solid #ddd !important; }

    </style>
""", unsafe_allow_html=True)

# --- 3. FUNCIÓN CARRUSEL (Selector Manual) ---
def render_carousel(label, options, key_name):
    """Crea un selector con flechas laterales que no usa el menú nativo"""
    if f"{key_name}_idx" not in st.session_state:
        st.session_state[f"{key_name}_idx"] = 0
    
    st.markdown(f"**{label}**")
    
    # Diseño: [ < ] [ TEXTO ] [ > ]
    c_prev, c_text, c_next = st.columns([1, 5, 1])
    
    with c_prev:
        if st.button("◀", key=f"p_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] - 1) % len(options)
            st.rerun()
            
    with c_next:
        if st.button("▶", key=f"n_{key_name}"):
            st.session_state[f"{key_name}_idx"] = (st.session_state[f"{key_name}_idx"] + 1) % len(options)
            st.rerun()
            
    val = options[st.session_state[f"{key_name}_idx"]]
    with c_text:
        st.markdown(f"<div class='stepper-display'>{val}</div>", unsafe_allow_html=True)
        
    return val

# --- 4. INICIALIZACIÓN ---
default_state = {
    'language': 'fr', 'step': 1, 'show_results': False,
    'age': 30, 'spouse': False, 'k1': 0, 'k2': 0,
    'sp_age': 30, 'sp_edu': 'Secondary',
    'fr_oral': 'B2', 'fr_write': 'B1', 'en_lvl': '0',
    'vjo': '', 'q_stud_val': 'Non', 'q_fam_val': 'Non',
    'exp_qc': 0, 'exp_ca': 0, 'exp_foreign': 36,
    'job_search_term': '', 'origin_country': '', 'arrival_text': '',
    'teer_idx': 0, 'edu_idx': 2, 'city_idx': 0, 'sp_edu_idx': 2, 'loc_idx': 2
}

for k, v in default_state.items():
    if k not in st.session_state:
        st.session_state[k] = v

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1
def reset_calc(): 
    st.session_state.step = 1
    st.session_state.show_results = False
def trigger_calculation(): st.session_state.show_results = True

# --- 5. TRADUCCIONES (REVISADAS) ---
t = {
    'fr': {
        'btn_lang': "🌐 Français", 'brand': "CALCULATRICE PSTQ",
        'step1': "Profil", 'step2': "Travail", 'step3': "Langues", 'step4': "Québec",
        'next': "Suivant ➡", 'prev': "⬅ Retour", 'calc': "VOIR MON SCORE",
        'loc_label': "Où êtes-vous ?", 'loc_opts': ["Au Québec", "Canada (Autre)", "À l'étranger"],
        'country': "Pays de résidence", 'city': "Ville destination", 'date': "Date d'arrivée",
        'city_opts': ["Montréal", "Québec", "Laval", "Gatineau", "Sherbrooke", "Autre"],
        'age': "Âge", 'spouse': "Conjoint ?", 'k1': "Enfants -12", 'k2': "Enfants +12",
        'job': "Emploi actuel", 'job_ph': "Ex: Soudeur...",
        'teer': "Catégorie TEER", 
        'teer_opts': ["TEER 0,1: Gestion/Univ", "TEER 2: Tech/Collégial", "TEER 3: Métiers", "TEER 4,5: Manuel"],
        'edu': "Niveau Études", 'edu_opts': ["Doctorat", "Maîtrise", "Baccalauréat", "Collégial (DEC)", "Diplôme Pro", "Secondaire"],
        'exp_t': "Expérience (5 ans)", 'exp_qc': "Mois Québec", 'exp_ca': "Mois Canada", 'exp_ex': "Mois Étranger",
        'lang_t': "Niveaux (B2 requis)", 'fr_o': "Français Oral", 'fr_e': "Français Écrit", 'en': "Anglais",
        'sp_fr': "Français Conjoint",
        'vjo_t': "Offre Validée (VJO)", 'vjo_opts': ["Non", "Oui (Montréal)", "Oui (Région)"],
        'dip_qc': "Diplôme Québec ?", 'fam_qc': "Famille Québec ?", 'yes_no': ["Non", "Oui"],
        'res': "Résultat", 'adv_g': "Excellent !", 'adv_b': "Améliorez votre profil.",
        'legal': "Projet indépendant. Non affilié au MIFI."
    },
    'es': {
        'btn_lang': "🌐 Español", 'brand': "CALCULADORA PSTQ",
        'step1': "Perfil", 'step2': "Trabajo", 'step3': "Idiomas", 'step4': "Quebec",
        'next': "Siguiente ➡", 'prev': "⬅ Atrás", 'calc': "VER PUNTAJE",
        'loc_label': "¿Dónde estás?", 'loc_opts': ["En Quebec", "Canadá (Otro)", "Extranjero"],
        'country': "País residencia", 'city': "Ciudad destino", 'date': "Fecha llegada",
        'city_opts': ["Montreal", "Quebec", "Laval", "Gatineau", "Sherbrooke", "Otra"],
        'age': "Edad", 'spouse': "¿Pareja?", 'k1': "Hijos -12", 'k2': "Hijos +12",
        'job': "Trabajo actual", 'job_ph': "Ej: Soldador...",
        'teer': "Categoría TEER", 
        'teer_opts': ["TEER 0,1: Uni/Gerencia", "TEER 2: Tec/College", "TEER 3: Oficios", "TEER 4,5: Manual"],
        'edu': "Nivel Estudios", 'edu_opts': ["Doctorado", "Maestría", "Bachelor", "Técnico (DEC)", "Diploma Pro", "Secundaria"],
        'exp_t': "Experiencia (5 años)", 'exp_qc': "Meses Quebec", 'exp_ca': "Meses Canadá", 'exp_ex': "Meses Extranjero",
        'lang_t': "Niveles (B2 req)", 'fr_o': "Francés Oral", 'fr_e': "Francés Escrito", 'en': "Inglés",
        'sp_fr': "Francés Pareja",
        'vjo_t': "Oferta Validada", 'vjo_opts': ["No", "Sí (Montreal)", "Sí (Región)"],
        'dip_qc': "¿Diploma Quebec?", 'fam_qc': "¿Familia Quebec?", 'yes_no': ["No", "Sí"],
        'res': "Resultado", 'adv_g': "¡Excelente!", 'adv_b': "Mejora tu perfil.",
        'legal': "Proyecto independiente. No somos abogados."
    },
    'en': {
        'btn_lang': "🌐 English", 'brand': "PSTQ CALCULATOR",
        'step1': "Profile", 'step2': "Work", 'step3': "Language", 'step4': "Quebec",
        'next': "Next ➡", 'prev': "⬅ Back", 'calc': "GET SCORE",
        'loc_label': "Current Location", 'loc_opts': ["In Quebec", "Canada (Other)", "Abroad"],
        'country': "Country", 'city': "Dest. City", 'date': "Arrival Date",
        'city_opts': ["Montreal", "Quebec", "Laval", "Gatineau", "Sherbrooke", "Other"],
        'age': "Age", 'spouse': "Spouse?", 'k1': "Kids -12", 'k2': "Kids +12",
        'job': "Current Job", 'job_ph': "Ex: Welder...",
        'teer': "TEER Category", 
        'teer_opts': ["TEER 0,1: Mgmt/Uni", "TEER 2: Tech/College", "TEER 3: Trades", "TEER 4,5: Manual"],
        'edu': "Education", 'edu_opts': ["PhD", "Master", "Bachelor", "College", "Diploma", "High School"],
        'exp_t': "Experience (5 yrs)", 'exp_qc': "Months Quebec", 'exp_ca': "Months Canada", 'exp_ex': "Months Abroad",
        'lang_t': "Levels (B2 req)", 'fr_o': "French Oral", 'fr_e': "French Written", 'en': "English",
        'sp_fr': "Spouse French",
        'vjo_t': "Validated Offer", 'vjo_opts': ["No", "Yes (Montreal)", "Yes (Region)"],
        'dip_qc': "Quebec Diploma?", 'fam_qc': "Quebec Family?", 'yes_no': ["No", "Yes"],
        'res': "Result", 'adv_g': "Excellent!", 'adv_b': "Improve profile.",
        'legal': "Independent project. Not legal advice."
    }
}
lang = t[st.session_state.language]

# --- 6. DATA JOBS ---
jobs_db = {"ingenie": "213xx", "welder": "72106", "cook": "63200", "nurse": "31301", "sales": "64100"}
def find_job(k):
    if not k: return None
    for j, c in jobs_db.items(): 
        if j in k.lower(): return c
    return None

# ==========================================
# HEADER
# ==========================================
st.markdown(f"""
<div class="pro-header">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
    <h1>{lang['brand']}</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
</div>
""", unsafe_allow_html=True)

c_space, c_btn = st.columns([3, 1])
with c_btn: st.button(lang['btn_lang'], on_click=cycle_language, type="secondary")
st.markdown("###")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tabs = st.tabs([lang['step1'], lang['step2'], lang['step3'], lang['step4']])
current_tab = main_tabs[st.session_state.step - 1]

with st.container():
    # Usamos un contenedor único y renderizamos según el paso
    
    # --- PASO 1 ---
    if st.session_state.step == 1:
        st.markdown(f"### 👤 {lang['step1']}")
        
        # Carrusel Ubicación
        sel_loc = render_carousel(lang['loc_label'], lang['loc_opts'], 'loc')
        
        if "bec" not in sel_loc and "Quebec" not in sel_loc:
             st.text_input(lang['country'], placeholder="Ex: Belgique...")
             st.divider()
             render_carousel(lang['city'], lang['city_opts'], 'city')
             st.text_input(lang['date'], placeholder="YYYY-MM-DD")
        
        st.divider()
        c1, c2 = st.columns(2)
        with c1: st.session_state.age = st.number_input(lang['age'], 18, 65, st.session_state.age)
        with c2: st.session_state.spouse = st.checkbox(lang['spouse'], value=st.session_state.spouse)
        
        c3, c4 = st.columns(2)
        with c3: st.session_state.k1 = st.number_input(lang['k1'], 0, 5, st.session_state.k1)
        with c4: st.session_state.k2 = st.number_input(lang['k2'], 0, 5, st.session_state.k2)
        
        if st.session_state.spouse:
            st.info(lang['sp_header'])
            c_sa, c_se = st.columns(2)
            with c_sa: st.number_input("Age", 18, 65, 30, key="sp_age_in")
            with c_se: render_carousel("Edu", lang['edu_opts'], 'sp_edu')

        st.markdown("###")
        if st.button(lang['next'], type="primary"): next_step(); st.rerun()

    # --- PASO 2 ---
    elif st.session_state.step == 2:
        st.markdown(f"### 💼 {lang['step2']}")
        
        st.text_input(lang['job'], placeholder=lang['job_ph'])
        st.divider()
        
        # Carruseles en lugar de Selectbox
        st.session_state.teer_sel = render_carousel(lang['teer'], lang['teer_opts'], 'teer')
        st.divider()
        st.session_state.edu = render_carousel(lang['edu'], lang['edu_opts'], 'edu')
        
        st.divider()
        st.markdown(f"**{lang['exp_t']}**")
        st.number_input(lang['exp_qc'], 0, 60, st.session_state.exp_qc, key="eqc")
        st.number_input(lang['exp_ca'], 0, 60, st.session_state.exp_ca, key="eca")
        st.number_input(lang['exp_ex'], 0, 60, st.session_state.exp_foreign, key="eex")

        st.markdown("###")
        c_p, c_n = st.columns(2)
        with c_p: 
            if st.button(lang['prev'], type="secondary"): prev_step(); st.rerun()
        with c_n: 
            if st.button(lang['next'], type="primary"): next_step(); st.rerun()

    # --- PASO 3 ---
    elif st.session_state.step == 3:
        st.markdown(f"### 🗣️ {lang['step3']}")
        st.info(lang['lang_t'])
        
        st.select_slider(lang['fr_o'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        st.select_slider(lang['fr_e'], ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        st.select_slider(lang['en'], ["0", "Beg", "Int", "Adv"], value="0")
        
        if st.session_state.spouse:
            st.divider()
            st.markdown(f"**{lang['sp_fr']}**")
            st.select_slider("Niveau", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

        st.markdown("###")
        c_p, c_n = st.columns(2)
        with c_p: 
            if st.button(lang['prev'], type="secondary"): prev_step(); st.rerun()
        with c_n: 
            if st.button(lang['next'], type="primary"): next_step(); st.rerun()

    # --- PASO 4 ---
    elif st.session_state.step == 4:
        st.markdown(f"### ⚜️ {lang['step4']}")
        
        # Carrusel para VJO
        st.session_state.vjo = render_carousel(lang['vjo_t'], lang['vjo_opts'], 'vjo')
        
        st.divider()
        st.markdown(f"**{lang['dip_qc']}**")
        render_carousel("", lang['yes_no'], 'dip_qc')
        
        st.divider()
        st.markdown(f"**{lang['fam_qc']}**")
        render_carousel("", lang['yes_no'], 'fam_qc')

        st.markdown("###")
        c_p, c_n = st.columns(2)
        with c_p: 
            if st.button(lang['prev'], type="secondary"): prev_step(); st.rerun()
        with c_n: 
            if st.button(lang['calc'], type="primary"): trigger_calculation(); st.rerun()

# RESULTADOS
if st.session_state.show_results:
    st.markdown("---")
    st.markdown(f"<div class='result-box'><h2>{lang['res']}: 680 / 1350</h2></div>", unsafe_allow_html=True)
    st.success(lang['adv_g'])
    if st.button("🔄"): reset_calc(); st.rerun()

# Footer Monetización
st.markdown("---")
c1, c2 = st.columns(2)
with c1: st.link_button("☕ Coffee", "https://buymeacoffee.com")
with c2: st.link_button("📚 Français", "https://google.com")
st.markdown("###")
st.caption(lang['legal'])
