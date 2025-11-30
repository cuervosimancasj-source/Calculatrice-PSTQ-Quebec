import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (BRANDING QUEBEC) ---
st.markdown("""
    <style>
        .stApp { background-color: #f0f2f6; }
        header[data-testid="stHeader"] { background-color: #003399; }
        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #003399 !important; }
        div.stButton > button[type="primary"] {
            background-color: #003399; color: white; border-radius: 8px; font-weight: bold;
        }
        div.stButton > button[type="primary"]:hover { background-color: #002266; }
        [data-testid="stForm"] {
            background-color: white; padding: 2rem; border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-top: 5px solid #003399;
        }
        .info-box {
            background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTIÓN DE IDIOMA (Default: FRANCÉS) ---
if 'language' not in st.session_state:
    st.session_state.language = 'fr'

def cycle_language():
    if st.session_state.language == 'fr':
        st.session_state.language = 'es'
    elif st.session_state.language == 'es':
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'fr'

# --- 4. TRADUCCIONES Y TEXTOS ---
t = {
    'fr': {
        'btn_lang': "Langue: Français 🇫🇷",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_text': "Projet indépendant. Nous ne sommes PAS le MIFI. Résultats estimés.",
        'coffee': "☕ M'offrir un café",
        'courses': "📚 Cours de Français",
        'tabs': ["👤 Profil", "💼 Travail & TEER", "🗣️ Langues", "⚜️ Québec/OEV", "ℹ️ Guide DI"],
        # Tab 2 (Travail)
        'job_title': "Quel est votre emploi actuel ?",
        'job_placeholder': "Ex: Ingénieur, Soudeur, Informaticien...",
        'search_btn': "Trouver mon code CNP et Volet",
        'teer_label': "Catégorie formation, expérience et responsabilités (TEER)",
        'teer_help': "Sélectionnez votre catégorie selon le code trouvé ci-dessus.",
        'exp_label': "Années d'expérience qualifiée",
        # Tab 3 (Langues)
        'lang_info': """
            **⚠️ Exigences Linguistiques (Oral) :**
            * **Volet 1 (TEER 0, 1, 2) :** Niveau 7 minimum.
            * **Volet 2 (TEER 3, 4, 5) :** Niveau 5 minimum.
            * **Conjoint(e) :** Niveau 4 recommandé.
        """,
        # Tab 5 (Guide)
        'guide_title': "Comment remplir la Déclaration d'Intérêt (DI)",
        'guide_steps': """
            1. **Créer un compte** sur le portail Arrima.
            2. **Remplir le profil** : Informations personnelles, parcours professionnel, études.
            3. **Code CNP** : Assurez-vous d'utiliser le code 2021 (5 chiffres).
            4. **Soumettre** : La DI est valide 12 mois. C'est gratuit.
        """,
        'example_title': "Exemple de Profil Gagnant",
        'example_text': """
            * **Nom :** Juan (42 ans).
            * **Emploi :** Développeur Web (TEER 1).
            * **Langue :** Français B2 (Niveau 7) + Anglais intermédiaire.
            * **Offre :** OEV à l'extérieur de Montréal.
            * **Résultat :** Invitation prioritaire.
        """,
        # General inputs
        'age': "Âge", 'spouse': "Conjoint(e) ?", 'kids12': "Enfants -12 ans", 'kids13': "Enfants +12 ans",
        'edu': "Niveau d'études", 'vjo': "Offre d'emploi (OEV)", 'calc': "CALCULER",
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Vous êtes compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV en région."
    },
    'es': {
        'btn_lang': "Idioma: Español 🇪🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Herramienta de análisis para Residencia (TEER, Volets, Puntaje).",
        'disclaimer_text': "Proyecto independiente. NO somos el MIFI. Resultados estimados.",
        'coffee': "☕ Invítame un café",
        'courses': "📚 Cursos de Francés",
        'tabs': ["👤 Perfil", "💼 Trabajo y TEER", "🗣️ Idiomas", "⚜️ Quebec/VJO", "ℹ️ Guía DI"],
        # Tab 2
        'job_title': "¿Cuál es tu trabajo actual?",
        'job_placeholder': "Ej: Ingeniero, Soldador, Cocinero...",
        'search_btn': "Buscar mi Código CNP y Volet",
        'teer_label': "Categoría formación, experiencia y responsabilidades (TEER)",
        'teer_help': "Selecciona tu categoría según el código encontrado arriba.",
        'exp_label': "Años de experiencia calificada",
        # Tab 3
        'lang_info': """
            **⚠️ Requisitos de Idioma (Oral):**
            * **Volet 1 (TEER 0, 1, 2):** Nivel 7 mínimo.
            * **Volet 2 (TEER 3, 4, 5):** Nivel 5 mínimo.
            * **Pareja:** Nivel 4 recomendado.
        """,
        # Tab 5
        'guide_title': "Cómo llenar la Declaración de Interés (DI)",
        'guide_steps': """
            1. **Crear cuenta** en el portal Arrima.
            2. **Llenar perfil**: Datos personales, historial laboral, estudios.
            3. **Código CNP**: Asegúrate de usar el código 2021 (5 dígitos).
            4. **Enviar**: La DI es válida por 12 meses. Es gratis.
        """,
        'example_title': "Ejemplo de Perfil Ganador",
        'example_text': """
            * **Nombre:** Juan (42 años).
            * **Trabajo:** Desarrollador Web (TEER 1).
            * **Idioma:** Francés B2 (Nivel 7) + Inglés intermedio.
            * **Oferta:** VJO fuera de Montreal.
            * **Resultado:** Invitación prioritaria.
        """,
        # General inputs
        'age': "Edad", 'spouse': "Pareja ?", 'kids12': "Hijos -12 años", 'kids13': "Hijos +12 años",
        'edu': "Nivel estudios", 'vjo': "Oferta empleo (VJO)", 'calc': "CALCULAR",
        'res_title': "Resultado Estimado",
        'advice_good': "¡Excelente! Eres competitivo.",
        'advice_low': "Mejora el francés o busca una VJO en regiones."
    },
    'en': {
         'btn_lang': "Language: English 🇺🇸",
         'brand': "Calculatrice PSTQ Québec ⚜️",
         'subtitle': "Analysis tool for Residency (TEER, Volets, Score).",
         'disclaimer_text': "Independent project. NOT MIFI. Estimated results.",
         'coffee': "☕ Buy me a coffee",
         'courses': "📚 French Courses",
         'tabs': ["👤 Profile", "💼 Work & TEER", "🗣️ Languages", "⚜️ Quebec/VJO", "ℹ️ DI Guide"],
         'job_title': "What is your current job?",
         'job_placeholder': "Ex: Engineer, Welder, IT...",
         'search_btn': "Find my NOC Code & Volet",
         'teer_label': "Category training, experience & responsibilities (TEER)",
         'teer_help': "Select your category based on the code found above.",
         'exp_label': "Years of qualified experience",
         'lang_info': """
            **⚠️ Language Requirements (Oral):**
            * **Volet 1 (TEER 0, 1, 2):** Level 7 minimum.
            * **Volet 2 (TEER 3, 4, 5):** Level 5 minimum.
            * **Spouse:** Level 4 recommended.
         """,
         'guide_title': "How to fill the Declaration of Interest (DI)",
         'guide_steps': """
            1. **Create account** on Arrima portal.
            2. **Fill profile**: Personal info, work history, education.
            3. **NOC Code**: Ensure you use the 2021 code (5 digits).
            4. **Submit**: Valid for 12 months. Free.
         """,
         'example_title': "Winning Profile Example",
         'example_text': """
            * **Name:** Juan (42 years old).
            * **Job:** Web Developer (TEER 1).
            * **Language:** French B2 (Level 7) + Intermediate English.
            * **Offer:** VJO outside Montreal.
            * **Result:** Priority invitation.
         """,
         'age': "Age", 'spouse': "Spouse ?", 'kids12': "Kids -12", 'kids13': "Kids +12",
         'edu': "Education Level", 'vjo': "Job Offer (VJO)", 'calc': "CALCULATE",
         'res_title': "Estimated Result",
         'advice_good': "Excellent! You are competitive.",
         'advice_low': "Improve French or find a VJO in regions."
    }
}

lang = t[st.session_state.language]

# --- 5. BASE DE DATOS SIMULADA DE TRABAJOS (DEMO) ---
# En una app real, esto sería una base de datos externa enorme.
jobs_db = {
    "ingenie": {"code": "21300", "teer": "1", "volet": "Volet 1 (Haute qualification)"},
    "engineer": {"code": "21300", "teer": "1", "volet": "Volet 1 (Haute qualification)"},
    "informati": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "web": {"code": "21222", "teer": "1", "volet": "Volet 1"},
    "administra": {"code": "13100", "teer": "3", "volet": "Volet 2 (Intermédiaire)"},
    "enfermer": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "infirmier": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "nurs": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "soldador": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "cuisinier": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cook": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cocinero": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "camion": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "driver": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "mecanic": {"code": "72410", "teer": "2", "volet": "Volet 2"},
}

def find_job_details(keyword):
    keyword = keyword.lower()
    for key, data in jobs_db.items():
        if key in keyword:
            return data
    return None

# --- 6. SIDEBAR ---
with st.sidebar:
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary")
    st.markdown("---")
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com")
    st.warning(lang['disclaimer_text'])

# --- 7. APP PRINCIPAL ---
st.markdown(f"# {lang['brand']}")
st.write(lang['subtitle'])

with st.form("main_form"):
    tab1, tab2, tab3, tab4, tab5 = st.tabs(lang['tabs'])

    # TAB 1: PERFIL
    with tab1:
        c1, c2 = st.columns(2)
        with c1: age = st.number_input(lang['age'], 18, 65, 30)
        with c2: spouse = st.checkbox(lang['spouse'])
        c3, c4 = st.columns(2)
        with c3: k1 = st.number_input(lang['kids12'], 0, 5, 0)
        with c4: k2 = st.number_input(lang['kids13'], 0, 5, 0)
        
        sp_age, sp_edu, sp_fr = 30, "Secondary", "0"
        if spouse:
            st.info("Info Pareja / Conjoint")
            sp_age = st.number_input("Edad/Âge", 18, 65, 30)
            sp_edu = st.selectbox("Edu", ["PhD", "Master", "Bachelor", "Technical", "Secondary"])
            sp_fr = st.selectbox("Français", ["C1-C2", "B2", "A1-B1", "0"])

    # TAB 2: TRABAJO & TEER (MODIFICADO)
    with tab2:
        st.markdown(f"### 🔍 {lang['job_title']}")
        job_query = st.text_input("Buscador / Recherche", placeholder=lang['job_placeholder'])
        
        # Lógica del buscador simulado
        if job_query:
            result = find_job_details(job_query)
            if result:
                st.success(f"✅ **Code CNP:** {result['code']} | **TEER:** {result['teer']}")
                st.info(f"📂 **{result['volet']}**")
            else:
                st.warning("⚠️ No encontrado en la demo. / Pas trouvé dans la démo.")
                st.markdown("[Buscar en sitio oficial Canadá](https://noc.esdc.gc.ca/)")

        st.divider()
        st.write(lang['teer_label'])
        st.caption(lang['teer_help'])
        # Reemplaza "Area of Training" visualmente, pero mantenemos lógica de puntos interna
        teer_selection = st.selectbox("Selección / Sélection", 
                                      ["TEER 0, 1 (Section A - High Demand)", 
                                       "TEER 2 (Section B)", 
                                       "TEER 3 (Section C)", 
                                       "TEER 4, 5 (General)"])
        
        education = st.selectbox(lang['edu'], ["PhD", "Master", "Bachelor (3+)", "College (3y)", "Diploma (1-2y)", "Secondary"])
        experience = st.slider(lang['exp_label'], 0, 10, 3)

    # TAB 3: IDIOMAS (CON TABLA INFO)
    with tab3:
        # Aquí insertamos la información de los Volets requerida
        st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1: fr_oral = st.select_slider("Français Oral", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        with c2: fr_write = st.select_slider("Français Écrit", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        en_lvl = st.select_slider("English", ["0", "Beginner", "Intermediate", "Advanced"], value="0")

    # TAB 4: QUEBEC
    with tab4:
        vjo = st.radio(lang['vjo'], ["Non", "Montreal", "Hors Montreal"])
        q_stud = st.checkbox("Diplôme Québec ?")
        q_fam = st.checkbox("Famille Québec ?")

    # TAB 5: GUÍA / AYUDA (NUEVO)
    with tab5:
        st.markdown(f"### ℹ️ {lang['guide_title']}")
        st.markdown(lang['guide_steps'])
        st.divider()
        st.markdown(f"#### 🏆 {lang['example_title']}")
        st.info(lang['example_text'])

    st.markdown("###")
    submitted = st.form_submit_button(lang['calc'], type="primary", use_container_width=True)

# --- 8. LÓGICA RÁPIDA DE CÁLCULO ---
if submitted:
    # Lógica simplificada para mantener el código limpio en esta iteración
    score = 0
    # Edad
    if 18 <= age <= 30: score += 130
    elif age <= 45: score += (130 - (age-30)*5)
    # Edu
    if "PhD" in education: score += 90
    elif "Master" in education: score += 75
    elif "Bachelor" in education: score += 60
    elif "College" in education: score += 50
    else: score += 30
    # TEER/Area (Mapeo)
    if "Section A" in teer_selection: score += 60
    elif "Section B" in teer_selection: score += 40
    elif "Section C" in teer_selection: score += 20
    # Experiencia
    score += min(80, int(experience * 10)) # Aprox por año
    # Idioma
    fr_pts = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
    score += fr_pts[fr_oral] * 1.2 + fr_pts[fr_write] * 0.8
    if en_lvl == "Advanced": score += 25
    elif en_lvl == "Intermediate": score += 15
    # VJO
    if vjo == "Hors Montreal": score += 380
    elif vjo == "Montreal": score += 180
    # Otros
    if q_stud: score += 50
    if q_fam: score += 30
    if spouse: score += 30 # Base pareja
    score += (k1 * 4) + (k2 * 2)

    st.markdown("---")
    st.markdown(f"<h2 style='text-align: center; color: #003399;'>{lang['res_title']}: {int(score)} / 1350</h2>", unsafe_allow_html=True)
    st.progress(min(score/1350, 1.0))
    
    if score > 580:
        st.success(lang['advice_good'])
        st.balloons()
    else:
        st.warning(lang['advice_low'])
