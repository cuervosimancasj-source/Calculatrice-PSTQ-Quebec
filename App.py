import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="PSTQ Calculator | Calculadora | Calculateur",
    page_icon="🍁",
    layout="centered"
)

# --- 2. GESTIÓN DE IDIOMA (ES -> FR -> EN) ---
if 'language' not in st.session_state:
    st.session_state.language = 'es'

def cycle_language():
    if st.session_state.language == 'es':
        st.session_state.language = 'fr'
    elif st.session_state.language == 'fr':
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'es'

# --- 3. DICCIONARIO DE TRADUCCIÓN (3 IDIOMAS) ---
t = {
    'es': {
        'btn_lang': "Idioma / Language: Español 🇪🇸",
        'title': "Calculadora de Puntos Quebec (Arrima / PSTQ)",
        'subtitle': "Estima tu puntaje para la Residencia Permanente bajo el sistema actual.",
        'disclaimer_title': "⚠️ AVISO LEGAL (LEER ANTES DE USAR)",
        'disclaimer_text': """
            Esta herramienta es un proyecto independiente con fines informativos.
            **NO** somos abogados ni consultores de inmigración. **NO** representamos al gobierno de Quebec (MIFI).
            Los resultados son estimaciones basadas en el sistema de ~1350 puntos. Para asesoría oficial, consulta un experto.
        """,
        'sidebar_opt': "Apoya & Aprende",
        'coffee': "☕ Invítame un Café (Buy Me a Coffee)",
        'courses': "📚 Cursos de Francés e Inglés",
        # Pestañas
        'tab1': "👤 Perfil y Familia",
        'tab2': "🎓 Educación y Trabajo",
        'tab3': "🗣️ Idiomas",
        'tab4': "⚜️ Oferta y Quebec",
        # Inputs Tab 1
        'age': "Edad del candidato principal",
        'spouse': "¿Tienes pareja/cónyuge que te acompaña?",
        'children_12': "Número de hijos (0 a 12 años)",
        'children_13': "Número de hijos (13 a 21 años)",
        'sp_age': "Edad de la pareja",
        'sp_edu': "Nivel de estudios de la pareja",
        'sp_fr': "Nivel de Francés de la pareja (Oral)",
        # Inputs Tab 2
        'edu_level': "Nivel de escolaridad más alto",
        'area': "Área de Formación (Demanda en el mercado)",
        'exp': "Experiencia laboral calificada (últimos 5 años)",
        'exp_help': "Cuenta solo experiencia en empleos calificados (TEER 0, 1, 2, 3).",
        # Inputs Tab 3
        'fr_oral': "Francés: Comprensión y Expresión Oral",
        'fr_write': "Francés: Comprensión y Expresión Escrita",
        'en_global': "Inglés: Nivel Global",
        'lang_help': "El francés tiene un peso decisivo en el nuevo sistema.",
        # Inputs Tab 4
        'vjo': "¿Tienes una Oferta de Empleo Validada (VJO)?",
        'opt_vjo_no': "No tengo oferta",
        'opt_vjo_mtl': "Sí, en Montreal (CMM)",
        'opt_vjo_out': "Sí, FUERA de Montreal (Regiones)",
        'q_studies': "¿Diploma obtenido en Quebec?",
        'q_exp': "Experiencia laboral DENTRO de Quebec",
        'family_q': "¿Familiares directos en Quebec?",
        # Botones y Res
        'calc_btn': "Calcular Puntaje",
        'result_title': "Tu Puntaje Estimado",
        'details': "Detalles del puntaje",
        'advice_good': "¡Excelente perfil! Tienes altas probabilidades.",
        'advice_avg': "Perfil sólido. Mejora el francés o busca una VJO para asegurar.",
        'advice_low': "Necesitas subir el francés o conseguir una oferta fuera de Montreal."
    },
    'fr': {
        'btn_lang': "Langue / Language: Français 🇫🇷",
        'title': "Calculateur de Points Québec (Arrima / PSTQ)",
        'subtitle': "Estimez votre score pour la Résidence Permanente selon le système actuel.",
        'disclaimer_title': "⚠️ AVIS DE NON-RESPONSABILITÉ",
        'disclaimer_text': """
            Cet outil est un projet indépendant à titre informatif.
            Nous ne sommes **PAS** avocats ni consultants. Nous ne représentons **PAS** le MIFI.
            Les résultats sont des estimations basées sur le système de ~1350 points.
        """,
        'sidebar_opt': "Soutien & Apprentissage",
        'coffee': "☕ Offrez-moi un café (Buy Me a Coffee)",
        'courses': "📚 Cours de Français et Anglais",
        # Tabs
        'tab1': "👤 Profil et Famille",
        'tab2': "🎓 Éducation et Travail",
        'tab3': "🗣️ Langues",
        'tab4': "⚜️ Offre et Québec",
        # Inputs Tab 1
        'age': "Âge du candidat principal",
        'spouse': "Avez-vous un conjoint qui vous accompagne ?",
        'children_12': "Nombre d'enfants (0 à 12 ans)",
        'children_13': "Nombre d'enfants (13 à 21 ans)",
        'sp_age': "Âge du conjoint",
        'sp_edu': "Niveau de scolarité du conjoint",
        'sp_fr': "Niveau de Français du conjoint (Oral)",
        # Inputs Tab 2
        'edu_level': "Niveau de scolarité le plus élevé",
        'area': "Domaine de Formation (Demande)",
        'exp': "Expérience de travail qualifiée (5 dernières années)",
        'exp_help': "Comptez uniquement l'expérience qualifiée (TEER 0, 1, 2, 3).",
        # Inputs Tab 3
        'fr_oral': "Français : Compréhension et Expression Orale",
        'fr_write': "Français : Compréhension et Expression Écrite",
        'en_global': "Anglais : Niveau Global",
        'lang_help': "Le français a un poids décisif dans le nouveau système.",
        # Inputs Tab 4
        'vjo': "Avez-vous une Offre d'Emploi Validée (OEV) ?",
        'opt_vjo_no': "Non, aucune offre",
        'opt_vjo_mtl': "Oui, à Montréal (CMM)",
        'opt_vjo_out': "Oui, HORS Montréal (Régions)",
        'q_studies': "Diplôme obtenu au Québec ?",
        'q_exp': "Expérience de travail AU Québec",
        'family_q': "Famille directe au Québec ?",
        # Results
        'calc_btn': "Calculer le Score",
        'result_title': "Votre Score Estimé",
        'details': "Détails du score",
        'advice_good': "Excellent profil ! Vous avez de fortes chances.",
        'advice_avg': "Profil solide. Améliorez le français ou cherchez une OEV.",
        'advice_low': "Vous devez améliorer le français ou obtenir une offre hors Montréal."
    },
    'en': {
        'btn_lang': "Language: English 🇺🇸",
        'title': "Quebec Points Calculator (Arrima / PSTQ)",
        'subtitle': "Estimate your score for Permanent Residency under the current system
