
import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA / CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Calculadora PSTQ Quebec",
    page_icon="⚜️",
    layout="centered"
)

# --- GESTIÓN DEL IDIOMA / GESTION DE LA LANGUE ---
if 'language' not in st.session_state:
    st.session_state.language = 'es'

def toggle_language():
    if st.session_state.language == 'es':
        st.session_state.language = 'fr'
    else:
        st.session_state.language = 'es'

# --- TEXTOS Y TRADUCCIONES / TEXTES ET TRADUCTIONS ---
translations = {
    'es': {
        'title': "Calculadora de Puntos PSTQ (Quebec)",
        'lang_btn': "Passer au Français 🇫🇷",
        'disclaimer_title': "⚠️ AVISO LEGAL IMPORTANTE",
        'disclaimer_text': """
            No somos abogados, consultores de inmigración ni asesores. 
            Esta herramienta no pertenece al gobierno de Quebec (MIFI) ni al gobierno federal de Canadá.
            El propósito de esta calculadora es meramente informativo y educativo para estimar un puntaje.
            Para asesoría legal, contacte a un consultor regulado o visite el sitio oficial de Arrima.
        """,
        'sidebar_title': "Opciones y Apoyo",
        'coffee_text': "¿Te sirvió esta herramienta? ¡Invítame a un café!",
        'coffee_btn': "☕ Buy Me a Coffee",
        'course_text': "¿Necesitas mejorar tu puntaje de idioma?",
        'course_btn': "📚 Ver Cursos de Francés",
        # Secciones del formulario
        'sec_human_cap': "Capital Humano",
        'label_age': "¿Cuál es tu edad?",
        'label_edu': "Nivel de escolaridad más alto",
        'opt_phd': "Doctorado",
        'opt_master': "Maestría",
        'opt_bachelor': "Licenciatura / Grado (3+ años)",
        'opt_diploma': "Diploma Técnico / College",
        'opt_hs': "Secundaria",
        'label_area': "Área de formación (Campo de estudio)",
        'opt_area_a': "Sección A (Alta demanda)",
        'opt_area_b': "Sección B",
        'opt_area_c': "Sección C",
        'opt_area_d': "Sección D / General",
        'label_exp': "Meses de experiencia laboral (últimos 5 años)",
        'label_fr': "Nivel de Francés (Comprensión y Expresión)",
        'label_en': "Nivel de Inglés",
        'sec_quebec': "Oferta y Mercado de Quebec",
        'label_vjo': "¿Tienes una Oferta de Empleo Validada (VJO)?",
        'opt_no_vjo': "No",
        'opt_vjo_mtl': "Sí, dentro de Montreal",
        'opt_vjo_out': "Sí, fuera de Montreal",
        'label_quebec_deg': "¿Tienes un diploma obtenido en Quebec?",
        'label_spose': "¿Vienes con pareja?",
        'btn_calc': "Calcular Puntaje",
        'result_title': "Tu Puntaje Estimado",
        'result_msg': "puntos de un máximo posible de 1350."
    },
    'fr': {
        'title': "Calculateur de Points PSTQ (Québec)",
        'lang_btn': "Cambiar a Español 🇪🇸",
        'disclaimer_title': "⚠️ AVIS DE NON-RESPONSABILITÉ",
        'disclaimer_text': """
            Nous ne sommes pas avocats, consultants en immigration ou conseillers.
            Cet outil n'appartient ni au gouvernement du Québec (MIFI) ni au gouvernement fédéral du Canada.
            Le but de ce calculateur est purement informatif et éducatif pour estimer un score.
            Pour un avis juridique, contactez un consultant réglementé ou visitez le site officiel d'Arrima.
        """,
        'sidebar_title': "Options et Soutien",
        'coffee_text': "Cet outil vous a aidé ? Offrez-moi un café !",
        'coffee_btn': "☕ Buy Me a Coffee",
        'course_text': "Besoin d'améliorer votre score linguistique ?",
        'course_btn': "📚 Voir les Cours de Français",
        # Sections du formulaire
        'sec_human_cap': "Capital Humain",
        'label_age': "Quel est votre âge ?",
        'label_edu': "Niveau de scolarité le plus élevé",
        'opt_phd': "Doctorat",
        'opt_master': "Maîtrise",
        'opt_bachelor': "Baccalauréat / Licence (3+ ans)",
        'opt_diploma': "Diplôme Technique / Collégial",
        'opt_hs': "Secondaire",
        'label_area': "Domaine de formation",
        'opt_area_a': "Section A (Forte demande)",
        'opt_area_b': "Section B",
        'opt_area_c': "Section C",
        'opt_area_d': "Section D / Général",
        'label_exp': "Mois d'expérience de travail (5 dernières années)",
        'label_fr': "Niveau de Français (Compréhension et Expression)",
        'label_en': "Niveau d'Anglais",
        'sec_quebec': "Offre et Marché du Québec",
        'label_vjo': "Avez-vous une Offre d'Emploi Validée (OEV) ?",
        'opt_no_vjo': "Non",
        'opt_vjo_mtl': "Oui, à l'intérieur de Montréal",
        'opt_vjo_out': "Oui, à l'extérieur de Montréal",
        'label_quebec_deg': "Avez-vous un diplôme obtenu au Québec ?",
        'label_spose': "Venez-vous avec un conjoint ?",
        'btn_calc': "Calculer le Score",
        'result_title': "Votre Score Estimé",
        'result_msg': "points sur un maximum possible de 1350."
    }
}

# Seleccionar idioma actual / Sélectionner la langue actuelle
t = translations[st.session_state.language]

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Botón de idioma / Bouton de langue
    st.button(t['lang_btn'], on_click=toggle_language)
    
    st.markdown("---")
    st.header(t['sidebar_title'])
    
    # Disclaimer en la barra lateral o principal
    st.warning(f"**{t['disclaimer_title']}**\n{t['disclaimer_text']}")
    
    st.markdown("---")
    
    # Monetización / Monétisation
    st.write(t['coffee_text'])
    # REEMPLAZA 'tu_link_aqui' con tu enlace real de Buy Me a Coffee
    st.link_button(t['coffee_btn'], "https://www.buymeacoffee.com/tu_usuario")
    
    st.write(t['course_text'])
    # REEMPLAZA con tu enlace de afiliados o curso
    st.link_button(t['course_btn'], "https://www.ejemplo-cursos-frances.com")

# --- INTERFAZ PRINCIPAL / INTERFACE PRINCIPALE ---

st.title(f"⚜️ {t['title']}")

# Formulario / Formulaire
with st.form("calculator_form"):
    
    st.subheader(t['sec_human_cap'])
    
    # Edad / Âge
    age = st.number_input(t['label_age'], min_value=18, max_value=65, value=30)
    
    # Educación / Éducation
    education = st.selectbox(t['label_edu'], [
        t['opt_phd'], t['opt_master'], t['opt_bachelor'], t['opt_diploma'], t['opt_hs']
    ])
    
    # Área de formación / Domaine de formation
    area_training = st.selectbox(t['label_area'], [
        t['opt_area_a'], t['opt_area_b'], t['opt_area_c'], t['opt_area_d']
    ])
    
    # Experiencia / Expérience
    experience_months = st.slider(t['label_exp'], 0, 60, 24)
    
    # Idiomas / Langues
    col1, col2 = st.columns(2)
    with col1:
        french_level = st.select_slider(t['label_fr'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
    with col2:
        english_level = st.select_slider(t['label_en'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

    st.subheader(t['sec_quebec'])
    
    # Oferta Validada / Offre Validée
    vjo = st.radio(t['label_vjo'], [t['opt_no_vjo'], t['opt_vjo_mtl'], t['opt_vjo_out']])
    
    # Otros factores / Autres facteurs
    quebec_degree = st.checkbox(t['label_quebec_deg'])
    spouse = st.checkbox(t['label_spose'])

    submitted = st.form_submit_button(t['btn_calc'])

# --- LÓGICA DE CÁLCULO / LOGIQUE DE CALCUL ---
# NOTA: Estos valores son APROXIMADOS para llegar a la base de 1350.
# Debes verificar la "Grille de sélection" oficial más reciente para ajustar los números exactos.

def calculate_score():
    score = 0
    
    # 1. Edad (Max ~130)
    if 18 <= age <= 30: score += 130
    elif age <= 45: score += (130 - (age - 30) * 5)
    
    # 2. Educación (Max ~90)
    if education == t['opt_phd']: score += 90
    elif education == t['opt_master']: score += 75
    elif education == t['opt_bachelor']: score += 60
    elif education == t['opt_diploma']: score += 45
    
    # 3. Área de Formación (Max ~60)
    if area_training == t['opt_area_a']: score += 60
    elif area_training == t['opt_area_b']: score += 40
    elif area_training == t['opt_area_c']: score += 20
    
    # 4. Experiencia (Max ~80)
    # Aprox 1.3 puntos por mes hasta llegar al tope
    score += min(80, int(experience_months * 1.5))
    
    # 5. Idiomas (Max Fr ~145 + En ~25 = 170 aprox)
    # Francés (Ponderación alta)
    fr_scores = {"0":0, "A1":0, "A2":20, "B1":40, "B2":80, "C1":120, "C2":145}
    score += fr_scores.get(french_level, 0)
    
    # Inglés
    en_scores = {"0":0, "A1":0, "A2":0, "B1":0, "B2":10, "C1":15, "C2":25}
    score += en_scores.get(english_level, 0)
    
    # 6. Oferta Validada (VJO) - Factor Crítico (Max ~380 - 180 dependiendo la zona)
    # Ajuste para acercarse a la escala de 1350 puntos.
    if vjo == t['opt_vjo_out']:
        score += 380 # Fuera de Montreal da muchos puntos
    elif vjo == t['opt_vjo_mtl']:
        score += 180 # Dentro de Montreal
        
    # 7. Factores Quebec / Pareja
    if quebec_degree: score += 50
    if spouse: score += 40 # Simplificado
    
    return score

# --- RESULTADOS / RÉSULTATS ---
if submitted:
    final_score = calculate_score()
    
    st.markdown("---")
    st.metric(label=t['result_title'], value=f"{final_score} / 1350")
    st.info(f"{final_score} {t['result_msg']}")
    
    # Lógica visual simple / Logique visuelle simple
    if final_score >= 600:
        st.balloons()
        st.success("¡Tienes un perfil competitivo! / Vous avez un profil compétitif !")
    else:
        st.warning("Podrías necesitar mejorar el idioma o conseguir una oferta. / Vous pourriez avoir besoin d'améliorer la langue ou d'obtenir une offre.")
