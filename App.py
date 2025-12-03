import streamlit as st
from datetime import date

# --- 1. CONFIGURACIÓN BÁSICA ---
st.set_page_config(page_title="Calculatrice PSTQ Québec", page_icon="⚜️", layout="centered")

# --- 2. ESTILOS CSS (LIMPIEZA TOTAL - SOLO LO NECESARIO) ---
st.markdown("""
    <style>
        /* Forzar modo claro */
        :root { color-scheme: light; }
        [data-testid="stAppViewContainer"] { background-color: #f4f7f6; color: #000000; }
        
        /* Encabezado personalizado */
        .pro-header {
            background-color: #003399;
            padding: 15px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .pro-header h1 {
            color: #FFFFFF !important;
            margin: 0;
            font-size: 1.4rem;
            font-weight: 800;
            text-align: center;
            flex-grow: 1;
        }
        .pro-header p { color: #e0e0e0 !important; margin: 0; text-align: center; font-size: 0.8rem; }
        .flag-icon { height: 35px; border: 1px solid white; border-radius: 3px; }

        /* Inputs y Radios (Fondo Blanco, Texto Negro) */
        .stApp p, .stApp label, .stApp div { color: #000000 !important; }
        div[data-baseweb="input"] > div, div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        input { color: #000000 !important; -webkit-text-fill-color: #000000 !important; caret-color: #000 !important; }
        
        /* Botones */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important; color: white !important; border: none; width: 100%;
        }
        div.stButton > button[kind="secondary"] {
            background-color: #fff !important; color: #003399 !important; border: 1px solid #003399; width: 100%;
        }
        
        /* Enlaces Monetización */
        div.stLinkButton > a {
            background-color: #003399 !important; color: white !important; border-radius: 8px; text-align: center; font-weight: bold;
        }
        
        /* Cajas de Ayuda */
        .info-box { background-color: #e8f4fd; border-left: 4px solid #003399; padding: 10px; border-radius: 4px; margin-bottom: 10px; font-size: 0.9rem; }
        
        /* Ocultar header nativo */
        header[data-testid="stHeader"] { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE ESTADO (MEMORIA) ---
if 'language' not in st.session_state: st.session_state.language = 'fr'
if 'show_results' not in st.session_state: st.session_state.show_results = False

def cycle_language():
    lang_map = {'fr': 'es', 'es': 'en', 'en': 'fr'}
    st.session_state.language = lang_map[st.session_state.language]

# --- 4. TEXTOS (DICCIONARIO COMPLETO) ---
t = {
    'fr': {
        'btn': "🌐 Changer la langue", 'title': "Calculatrice PSTQ", 'sub': "Analyse Résidence Permanente",
        'tabs': ["👤 Profil", "💼 Travail", "🗣️ Langues", "⚜️ Québec"],
        'loc_q': "Où habitez-vous ?", 'loc_opt': ["Québec", "Canada (Autre)", "Étranger"],
        'ctry_q': "Pays de résidence", 'city_q': "Ville au Québec", 'arr_q': "Date d'arrivée (AAAA-MM-JJ)",
        'age_q': "Âge", 'sp_q': "Conjoint ?", 'k1': "Enfants -12", 'k2': "Enfants +12",
        'sp_h': "Infos Conjoint", 'sp_a': "Âge", 'sp_e': "Études",
        'job_q': "Emploi actuel (Ex: Soudeur)", 'teer_q': "Catégorie TEER",
        'edu_q': "Niveau d'études", 'exp_q': "Expérience (Mois)",
        'lang_t': "Français (Niv 7 requis)", 'oral': "Oral", 'write': "Écrit", 'en': "Anglais",
        'oev_h': "ℹ️ **OEV:** Offre validée par le MIFI (EIMT/LMIA).",
        'vjo_q': "Avez-vous une Offre Validée ?", 'vjo_o': ["Non", "Oui (Montréal)", "Oui (Région)"],
        'dip_h': "ℹ️ **Diplôme QC:** AEC, DEC, Bac, Maîtrise, etc.",
        'dip_q': "Diplôme du Québec ?", 'fam_q': "Famille au Québec ?", 'yn': ["Non", "Oui"],
        'calc': "CALCULER", 'res': "Résultat", 'adv_g': "Excellent !", 'adv_b': "Améliorez votre profil.",
        'legal': "Projet indépendant. Non affilié au gouvernement. Pas de conseil juridique.",
        'coffee': "☕ Café", 'course': "📚 Cours"
    },
    'es': {
        'btn': "🌐 Cambiar Idioma", 'title': "Calculadora PSTQ", 'sub': "Análisis Residencia Permanente",
        'tabs': ["👤 Perfil", "💼 Trabajo", "🗣️ Idiomas", "⚜️ Quebec"],
        'loc_q': "¿Dónde vives?", 'loc_opt': ["Quebec", "Canadá (Otro)", "Extranjero"],
        'ctry_q': "País de residencia", 'city_q': "Ciudad destino", 'arr_q': "Fecha llegada (AAAA-MM-DD)",
        'age_q': "Edad", 'sp_q': "¿Pareja?", 'k1': "Hijos -12", 'k2': "Hijos +12",
        'sp_h': "Datos Pareja", 'sp_a': "Edad", 'sp_e': "Estudios",
        'job_q': "Trabajo actual (Ej: Ingeniero)", 'teer_q': "Categoría TEER",
        'edu_q': "Nivel Estudios", 'exp_q': "Experiencia (Meses)",
        'lang_t': "Francés (Nivel 7 req)", 'oral': "Oral", 'write': "Escrito", 'en': "Inglés",
        'oev_h': "ℹ️ **VJO:** Oferta Validada por MIFI (LMIA).",
        'vjo_q': "¿Oferta Validada?", 'vjo_o': ["No", "Sí (Montreal)", "Sí (Región)"],
        'dip_h': "ℹ️ **Diploma QC:** AEC, DEC, Bachelor, etc.",
        'dip_q': "¿Diploma Quebec?", 'fam_q': "¿Familia Quebec?", 'yn': ["No", "Sí"],
        'calc': "CALCULAR", 'res': "Resultado", 'adv_g': "¡Excelente!", 'adv_b': "Mejora tu perfil.",
        'legal': "Proyecto independiente. No somos gobierno ni abogados.",
        'coffee': "☕ Café", 'course': "📚 Cursos"
    },
    'en': {
        'btn': "🌐 Change Lang", 'title': "PSTQ Calculator", 'sub': "Residency Analysis Tool",
        'tabs': ["👤 Profile", "💼 Work", "🗣️ Lang", "⚜️ Quebec"],
        'loc_q': "Current Location?", 'loc_opt': ["Quebec", "Canada (Other)", "Abroad"],
        'ctry_q': "Country", 'city_q': "Dest. City", 'arr_q': "Arrival Date (YYYY-MM-DD)",
        'age_q': "Age", 'sp_q': "Spouse?", 'k1': "Kids -12", 'k2': "Kids +12",
        'sp_h': "Spouse Info", 'sp_a': "Age", 'sp_e': "Education",
        'job_q': "Current Job (Ex: Welder)", 'teer_q': "TEER Category",
        'edu_q': "Education", 'exp_q': "Experience (Months)",
        'lang_t': "French (Lvl 7 req)", 'oral': "Oral", 'write': "Written", 'en': "English",
        'oev_h': "ℹ️ **VJO:** Validated Offer (MIFI/LMIA).",
        'vjo_q': "Validated Offer?", 'vjo_o': ["No", "Yes (Montreal)", "Yes (Region)"],
        'dip_h': "ℹ️ **QC Diploma:** AEC, DEC, Bachelor, etc.",
        'dip_q': "Quebec Diploma?", 'fam_q': "Quebec Family?", 'yn': ["No", "Yes"],
        'calc': "CALCULATE", 'res': "Result", 'adv_g': "Excellent!", 'adv_b': "Improve profile.",
        'legal': "Independent project. Not government affiliated.",
        'coffee': "☕ Coffee", 'course': "📚 Courses"
    }
}
l = t[st.session_state.language]

# --- 5. LÓGICA DE DATOS ---
jobs_db = {"ingenie": {"c":"21300","t":"1"}, "soud": {"c":"72106","t":"2"}, "welder": {"c":"72106","t":"2"}}
def search_job(k): 
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
    <div><h1>{l['title']}</h1><p>{l['sub']}</p></div>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Flag_of_Quebec.svg/128px-Flag_of_Quebec.svg.png" class="flag-icon">
</div>
""", unsafe_allow_html=True)
c1, c2 = st.columns([3,1])
with c2: st.button(l['btn'], on_click=cycle_language, type="secondary")

# ==========================================
# TABS (NAVEGACIÓN SEGURA)
# ==========================================
t1, t2, t3, t4 = st.tabs(l['tabs'])

# --- TAB 1: PERFIL ---
with t1:
    st.markdown(f"### {l['tabs'][0]}")
    loc = st.radio(l['loc_q'], l['loc_opt'])
