import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (DISEÑO QUEBEC) ---
st.markdown("""
    <style>
        .stApp { background-color: #f0f2f6; }
        header[data-testid="stHeader"] { background-color: #003399; }
        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #003399 !important; }
        div.stButton > button[type="primary"] {
            background-color: #003399; color: white; border-radius: 8px; font-weight: bold; border: none;
        }
        div.stButton > button[type="primary"]:hover { background-color: #002266; }
        [data-testid="stForm"] {
            background-color: white; padding: 2rem; border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-top: 5px solid #003399;
        }
        .info-box {
            background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; margin-bottom: 15px; border-radius: 5px;
        }
        .help-box {
            background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; margin-top: 10px; border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE IDIOMA ---
if 'language' not in st.session_state:
    st.session_state.language = 'fr'

def cycle_language():
    if st.session_state.language == 'fr': st.session_state.language = 'es'
    elif st.session_state.language == 'es': st.session_state.language = 'en'
    else: st.session_state.language = 'fr'

# --- 4. TRADUCCIONES ---
t = {
    'fr': {
        'btn_lang': "Langue: Français 🇫🇷",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_text': "Projet indépendant. Résultats estimés.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'tabs': ["👤 Profil", "💼 Travail & TEER", "🗣️ Langues", "⚜️ Québec/OEV", "ℹ️ Guide DI"],
        'job_title': "Quel est votre emploi actuel ?",
        'job_placeholder': "Ex: Ingénieur, Soudeur, Assembleur...",
        'teer_manual_help': "Guide manuel si emploi non trouvé :",
        'teer_guide': "**Guide Rapide:** TEER 0,1 (Uni) -> Sec A/B | TEER 2,3 (Tech) -> Sec B/C | TEER 4,5 (Sec) -> Général",
        'exp_label': "Années d'expérience qualifiée",
        'lang_info': "**Exigences :** Volet 1 = Niveau 7 | Volet 2 = Niveau 5",
        'guide_title': "Guide Déclaration d'Intérêt",
        'guide_steps': "1. Compte Arrima. 2. Profil. 3. Code CNP 2021.",
        'example_text': "Exemple: Dév Web, Français B2, OEV Région.",
        'age': "Âge", 'spouse': "Conjoint(e) ?", 'kids12': "Enfants -12", 'kids13': "Enfants +12",
        'sp_section': "Calcul du niveau de Français du Conjoint",
        'sp_fr_label': "Niveau de Français (Oral) du conjoint",
        'edu': "Niveau d'études", 'vjo': "Offre d'emploi (OEV)", 'calc': "CALCULER MON SCORE",
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Vous êtes compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV en région."
    },
    'es': {
        'btn_lang': "Idioma: Español 🇪🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Herramienta de análisis para Residencia (TEER, Volets, Puntaje).",
        'disclaimer_text': "Proyecto independiente. Resultados estimados.",
        'coffee': "☕ Invítame un café",
        'courses': "📚 Cursos de Francés",
        'tabs': ["👤 Perfil", "💼 Trabajo y TEER", "🗣️ Idiomas", "⚜️ Quebec/VJO", "ℹ️ Guía DI"],
        'job_title': "¿Cuál es tu trabajo actual?",
        'job_placeholder': "Ej: Ingeniero, Soldador, Ensamblador...",
        'teer_manual_help': "Guía manual si no encuentras tu empleo:",
        'teer_guide': "**Guía Rápida:** TEER 0,1 (Uni) -> Sec A/B | TEER 2,3 (Tec) -> Sec B/C | TEER 4,5 (Sec) -> General",
        'exp_label': "Años de experiencia calificada",
        'lang_info': "**Requisitos:** Volet 1 = Nivel 7 | Volet 2 = Nivel 5",
        'guide_title': "Guía Declaración de Interés",
        'guide_steps': "1. Cuenta Arrima. 2. Perfil. 3. Código CNP 2021.",
        'example_text': "Ejemplo: Dev Web, Francés B2, VJO Región.",
        'age': "Edad", 'spouse': "Pareja ?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_section': "Calcula el nivel de francés de tu pareja",
        'sp_fr_label': "Nivel de Francés (Oral) de la pareja",
        'edu': "Nivel estudios", 'vjo': "Oferta empleo (VJO)", 'calc': "CALCULAR PUNTAJE",
        'res_title': "Resultado Estimado",
        'advice_good': "¡Excelente! Eres competitivo.",
        'advice_low': "Mejora el francés o busca una VJO en regiones."
    },
    'en': {
        'btn_lang': "Language: English 🇺🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Analysis tool for Residency (TE
