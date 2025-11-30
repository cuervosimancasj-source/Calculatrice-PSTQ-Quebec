import streamlit as st

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Calculatrice PSTQ Québec",
    page_icon="⚜️",
    layout="centered"
)

# --- 2. ESTILOS CSS (BLINDADO PARA MÓVIL/INSTAGRAM/FACEBOOK) ---
st.markdown("""
    <style>
        /* === 1. FORZADO GLOBAL DE MODO CLARO === */
        [data-testid="stAppViewContainer"] {
            background-color: #f0f2f6 !important;
        }
        
        /* Texto general forzado a casi negro */
        .stApp, p, label, div, span, h1, h2, h3, h4, h5, h6 {
            color: #262730 !important;
        }
        
        /* Encabezado y Títulos Principales en Azul */
        header[data-testid="stHeader"] { background-color: #003399 !important; }
        h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { 
            color: #003399 !important; 
        }

        /* === 2. ARREGLO DE INPUTS (EDAD, HIJOS) PARA INSTAGRAM/FACEBOOK === */
        /* Forzamos el fondo blanco en las cajas de input */
        div[data-baseweb="input"], div[data-baseweb="base-input"] {
            background-color: #FFFFFF !important;
            border: 1px solid #ccc !important;
        }
        /* CRÍTICO: Forzar el color del texto dentro del input a NEGRO */
        input.st-ai, input.st-ah, input {
            color: #000000 !important;
            -webkit-text-fill-color: #000000 !important; /* Fix para iPhone/Safari */
            caret-color: #000000 !important; /* Cursor negro */
            background-color: #FFFFFF !important;
        }
        /* Arreglo para selectbox (menús desplegables) */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }

        /* === 3. BOTONES "INVISIBLES" CORREGIDOS === */
        div.stButton > button { width: 100%; border-radius: 8px; font-weight: bold; }
        
        /* Botones Secundarios (Idioma, Coffee, Cursos) */
        /* Ahora tienen BORDE AZUL y LETRA AZUL para contraste máximo */
        div.stButton > button[kind="secondary"], div.stLinkButton > a {
            background-color: #FFFFFF !important;
            color: #003399 !important;
            border: 2px solid #003399 !important;
            text-decoration: none !important;
        }
        div.stButton > button[kind="secondary"]:hover, div.stLinkButton > a:hover {
            background-color: #e6f0ff !important;
        }

        /* Botón Primario (Calcular) */
        div.stButton > button[kind="primary"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
            border: none !important;
        }

        /* === 4. TARJETAS Y CAJAS === */
        [data-testid="stForm"] {
            background-color: #FFFFFF !important;
            padding: 1.5rem; 
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
            border-top: 5px solid #003399;
        }
        .info-box { background-color: #e8f4fd; border-left: 5px solid #003399; padding: 15px; border-radius: 5px; color: #000 !important; }
        .help-box { background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; border-radius: 5px; color: #000 !important; }
        .step-box { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; color: #000 !important; }
        .result-box { background-color: #003399; color: white !important; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px; }
        .result-box h2 { color: white !important; margin: 0; }

        /* === 5. PESTAÑAS (TABS) === */
        button[data-baseweb="tab"] { color: #000000 !important; }
        button[data-baseweb="tab"][aria-selected="true"] {
            background-color: #003399 !important;
            color: #FFFFFF !important;
        }
        
        /* Footer */
        .footer { margin-top: 50px; padding: 20px; border-top: 1px solid #ccc; text-align: center; color: #666 !important; font-size: 0.85em; }
        .deco-sub { color: #666 !important; font-style: italic; margin-bottom: 15px; display: block; }

    </style>
""", unsafe_allow_html=True)

# --- 3. ESTADO Y GESTIÓN ---
if 'language' not in st.session_state:
    st.session_state.language = 'fr'
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

def cycle_language():
    if st.session_state.language == 'fr': st.session_state.language = 'es'
    elif st.session_state.language == 'es': st.session_state.language = 'en'
    else: st.session_state.language = 'fr'

def trigger_calculation():
    st.session_state.show_results = True

# --- 4. TRADUCCIONES ---
t = {
    'fr': {
        'btn_lang': "🌐 Changer la langue",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Outil d'analyse pour la Résidence Permanente (TEER, Volets, Score).",
        'disclaimer_title': "⚠️ AVIS IMPORTANT",
        'disclaimer_text': "Ce logiciel est un projet indépendant. Nous ne sommes PAS avocats ni consultants. Nous ne représentons PAS le MIFI.",
        'coffee': "☕ M'offrir un café (Soutenir)",
        'courses': "📚 Cours de Français",
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide"],
        'tabs': ["👤 Profil", "💼 Travail", "🗣️ Langues", "⚜️ Québec"],
        'tab1_header': "Votre Profil & Famille", 'tab1_sub': "Le point de départ de votre projet d'immigration.",
        'tab2_header': "Votre Expérience Québécoise", 'tab2_sub': "Votre métier est au cœur du programme PSTQ.",
        'tab3_header': "Vos Compétences Linguistiques", 'tab3_sub': "Le français est la clé du succès au Québec.",
        'tab4_header': "Facteurs Québec & OEV", 'tab4_sub': "Finalisez votre pointage avec les atouts locaux.",
        'job_title': "Quel est votre emploi actuel ?",
        'job_placeholder': "Ex: Ingénieur, Soudeur, Assembleur...",
        'teer_manual_help': "Si non trouvé, choisissez niveau :",
        'teer_label': "Catégorie TEER (Niveau)",
        'teer_guide': "**Aide:** TEER 0,1=Uni/Gestion | TEER 2=Tech | TEER 3=Métiers | TEER 4,5=Manuel",
        'exp_label': "Années d'expérience",
        'lang_info': "Volet 1=Niv 7 | Volet 2=Niv 5",
        'age': "Âge", 'spouse': "Conjoint(e) ?", 'kids12': "Enf -12", 'kids13': "Enf +12",
        'sp_section': "Conjoint (Âge/Études)",
        'sp_fr_title': "Français du Conjoint",
        'sp_fr_label': "Niveau Oral",
        'edu': "Niveau d'études", 'vjo': "Offre (OEV)", 'calc': "CALCULER SCORE",
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Profil compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV.",
        'details': "Détails",
        'sp_points': "Pts Conjoint",
        'guide_title': "Feuille de Route",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Vos points forts.",
        'g_step2': "2. Français", 'g_desc2': "Visez B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Profil gratuit.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificat Sélection.",
        'g_step5': "5. Fédéral", 'g_desc5': "Résidence Permanente.",
        'noc_link_text': "🔎 Chercher sur le site officiel du Canada (CNP)"
    },
    'es': {
        'btn_lang': "🌐 Cambiar el idioma",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Análisis Residencia Permanente (Arrima).",
        'disclaimer_title': "⚠️ AVISO LEGAL",
        'disclaimer_text': "Proyecto independiente. NO abogados/asesores. NO Gobierno (MIFI).",
        'coffee': "☕ Café (Apoyo)",
        'courses': "📚 Cursos Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía"],
        'tabs': ["👤 Perfil", "💼 Trabajo", "🗣️ Idiomas", "⚜️ Quebec"],
        'tab1_header': "Tu Perfil y Familia", 'tab1_sub': "El punto de partida de tu proyecto de inmigración.",
        'tab2_header': "Tu Experiencia Quebequense", 'tab2_sub': "Tu oficio es el corazón del programa PSTQ.",
        'tab3_header': "Tus Competencias Lingüísticas", 'tab3_sub': "El francés es la llave del éxito en Quebec.",
        'tab4_header': "Factores Quebec y VJO", 'tab4_sub': "Finaliza tu puntaje con los activos locales.",
        'job_title': "¿Cuál es tu trabajo?",
        'job_placeholder': "Ej: Ingeniero, Soldador...",
        'teer_manual_help': "Si no aparece, elige nivel:",
        'teer_label': "Categoría TEER (Nivel)",
        'teer_guide': "**Ayuda:** TEER 0,1=Uni/Gerencia | TEER 2=Técnico | TEER 3=Oficios | TEER 4,5=Manual",
        'exp_label': "Años de experiencia",
        'lang_info': "Volet 1=Niv 7 | Volet 2=Niv 5",
        'age': "Edad", 'spouse': "Pareja ?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_section': "Pareja (Edad/Estudios)",
        'sp_fr_title': "Francés Pareja",
        'sp_fr_label': "Nivel Oral",
        'edu': "Nivel estudios", 'vjo': "Oferta (VJO)", 'calc': "CALCULAR PUNTAJE",
        'res_title': "Resultado",
        'advice_good': "¡Excelente! Competitivo.",
        'advice_low': "Mejora el francés o busca VJO.",
        'details': "Detalles",
        'sp_points': "Pts Pareja",
        'guide_title': "Hoja de Ruta",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Tus fortalezas.",
        'g_step2': "2. Francés", 'g_desc2': "Apunta a B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Perfil gratis.",
        'g_step4': "4. CSQ", 'g_desc4': "Certificado Selección.",
        'g_step5': "5. Federal", 'g_desc5': "Residencia Permanente.",
        'noc_link_text': "🔎 Buscar en sitio oficial Canadá (NOC)"
    },
    'en': {
        'btn_lang': "🌐 Change Language",
        'brand': "Calculatrice PSTQ ⚜️",
        'subtitle': "Residency Analysis Tool (Arrima).",
        'disclaimer_title': "⚠️ DISCLAIMER",
        'disclaimer_text': "Independent. NOT lawyers. NOT Government (MIFI).",
        'coffee': "☕ Coffee (Support)",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide"],
        'tabs': ["👤 Profile", "💼 Work", "🗣️ Language", "⚜️ Quebec"],
        'tab1_header': "Your Profile & Family", 'tab1_sub': "The starting point of your immigration project.",
        'tab2_header': "Your Quebec Experience", 'tab2_sub': "Your trade is at the heart of the PSTQ program.",
        'tab3_header': "Your Language Skills", 'tab3_sub': "French is the key to success in Quebec.",
        'tab4_header': "Quebec Factors & VJO", 'tab4_sub': "Finalize your score with local assets.",
        'job_title': "Current job?",
        'job_placeholder': "Ex: Engineer, Welder...",
        'teer_manual_help': "If not found, select level:",
        'teer_label': "TEER Category",
        'teer_guide': "**Help:** TEER 0,1=Uni/Mgmt | TEER 2=Tech | TEER 3=Trades | TEER 4,5=Manual",
        'exp_label': "Years experience",
        'lang_info': "Volet 1=Lvl 7 | Volet 2=Lvl 5",
        'age': "Age", 'spouse': "Spouse ?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_section': "Spouse (Age/Edu)",
        'sp_fr_title': "Spouse French",
        'sp_fr_label': "Oral Level",
        'edu': "Education", 'vjo': "Offer (VJO)", 'calc': "CALCULATE SCORE",
        'res_title': "Result",
        'advice_good': "Excellent! Competitive.",
        'advice_low': "Improve French or find VJO.",
        'details': "Details",
        'sp_points': "Spouse Pts",
        'guide_title': "Roadmap",
        'g_step1': "1. Self-Assess", 'g_desc1': "Know strengths.",
        'g_step2': "2. French", 'g_desc2': "Aim B2 (7).",
        'g_step3': "3. Arrima", 'g_desc3': "Free profile.",
        'g_step4': "4. CSQ", 'g_desc4': "Selection Cert.",
        'g_step5': "5. Federal", 'g_desc5': "Residency.",
        'noc_link_text': "🔎 Search on official Canada site (NOC)"
    }
}
lang = t[st.session_state.language]

# --- 5. DATA JOBS ---
jobs_db = {
    "ingenie": {"code": "21300", "teer": "1", "volet": "Volet 1"},
    "engineer": {"code": "21300", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "web": {"code": "21222", "teer": "1", "volet": "Volet 1"},
    "infirmier": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "nurse": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "architect": {"code": "21200", "teer": "1", "volet": "Volet 1"},
    "administra": {"code": "13100", "teer": "3", "volet": "Volet 2"},
    "technicien": {"code": "22300", "teer": "2", "volet": "Volet 1/2"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "cuisinier": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cook": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "camion": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "mecanic": {"code": "72410", "teer": "2", "volet": "Volet 2"},
    "ensamblador": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "assembler": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manguera": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hose": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hidraulica": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manoeuvre": {"code": "95109", "teer": "5", "volet": "Volet 2"},
}

def find_job_details(keyword):
    keyword = keyword.lower().strip()
    for key, data in jobs_db.items():
        if key in keyword: return data
    return None

# ==========================================
# HEADER
# ==========================================
col_brand, col_lang = st.columns([3, 1])
with col_brand:
    st.markdown(f"## {lang['brand']}")
    st.caption(lang['subtitle'])
with col_lang:
    st.markdown("###") 
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary", key="top_lang_btn")

# ==========================================
# APP PRINCIPAL
# ==========================================
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

# --- PESTAÑA CALCULADORA ---
with main_tab_calc:
    tab1, tab2, tab3, tab4 = st.tabs(lang['tabs'])

    # 1. PERFIL
    with tab1:
        st.markdown(f"### 👤 {lang['tab1_header']} ⚜️")
        st.markdown(f"<span class='deco-sub'>{lang['tab1_sub']}</span>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1: age = st.number_input(lang['age'], 18, 65, 30)
        with c2: spouse = st.checkbox(lang['spouse'])
        c3, c4 = st.columns(2)
        with c3: k1 = st.number_input(lang['kids12'], 0, 5, 0)
        with c4: k2 = st.number_input(lang['kids13'], 0, 5, 0)
        
        sp_age, sp_edu = 30, "Secondary"
        if spouse:
            st.divider()
            st.markdown(f"**{lang['sp_section']}**")
            c_sp1, c_sp2 = st.columns(2)
            with c_sp1: sp_age = st.number_input("Age (Conj.)", 18, 65, 30)
            with c_sp2: sp_edu = st.selectbox("Edu (Conj.)", ["PhD", "Master", "Bachelor", "Technical", "Secondary"])

    # 2. TRABAJO
    with tab2:
        st.markdown(f"### 💼 {lang['tab2_header']} ⚜️")
        st.markdown(f"<span class='deco-sub'>{lang['tab2_sub']}</span>", unsafe_allow_html=True)

        st.markdown(f"**{lang['job_title']}**")
        job_query = st.text_input("Buscar/Recherche", placeholder=lang['job_placeholder'], label_visibility="collapsed")
        if job_query:
            result = find_job_details(job_query)
            if result:
                st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
            else:
                st.markdown(f"<div class='help-box'>{lang['teer_guide']}</div>", unsafe_allow_html=True)
                st.markdown(f"🔗 [{lang['noc_link_text']}](https://noc.esdc.gc.ca/)")

        st.divider()
        st.caption(lang['teer_manual_help'])
        
        teer_selection = st.selectbox(lang['teer_label'], 
                                      [
                                          "TEER 0, 1: Université / Ingénierie / Gestion (Haute Qualif.)",
                                          "TEER 2: Collégial / Technique / Superviseurs",
                                          "TEER 3: Métiers / Administration / Intermédiaire",
                                          "TEER 4, 5: Manœuvre / Secondaire / Service (Manuel)"
                                      ])
                                      
        education = st.selectbox(lang['edu'], ["PhD", "Master", "Bachelor (3+)", "College (3y)", "Diploma (1-2y)", "Secondary"])
        experience = st.slider(lang['exp_label'], 0, 10, 3)

    # 3. IDIOMAS
    with tab3:
        st.markdown(f"### 🗣️ {lang['tab3_header']} ⚜️")
        st.markdown(f"<span class='deco-sub'>{lang['tab3_sub']}</span>", unsafe_allow_html=True)

        st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
        fr_oral = st.select_slider("Français Oral", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
        fr_write = st.select_slider("Français Écrit", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
        en_lvl = st.select_slider("English", ["0", "Beginner", "Intermediate", "Advanced"], value="0")

        sp_fr = "0"
        if spouse:
            st.divider()
            st.markdown(f"**{lang['sp_fr_title']}**")
            sp_fr = st.select_slider(lang['sp_fr_label'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

    # 4. QUEBEC
    with tab4:
        st.markdown(f"### ⚜️ {lang['tab4_header']}")
        st.markdown(f"<span class='deco-sub'>{lang['tab4_sub']}</span>", unsafe_allow_html=True)

        vjo = st.radio(lang['vjo'], ["Non", "Montreal", "Hors Montreal"])
        cq1, cq2 = st.columns(2)
        with cq1: q_stud = st.checkbox("Diplôme QC ?")
        with cq2: q_fam = st.checkbox("Famille QC ?")
        
        st.markdown("###")
        if st.button(lang['calc'], type="primary", use_container_width=True):
            trigger_calculation()

    # LÓGICA & RESULTADOS
    if st.session_state.show_results:
        score = 0
        score_sp = 0 
        
        if 18 <= age <= 30: score += 130
        elif age <= 45: score += (130 - (age-30)*5)
        if "PhD" in education: score += 90
        elif "Master" in education: score += 75
        elif "Bachelor" in education: score += 60
        elif "College" in education: score += 50
        else: score += 30
        
        # Mapeo
        if "TEER 0, 1" in teer_selection: score += 60 
        elif "TEER 2" in teer_selection: score += 40
        elif "TEER 3" in teer_selection: score += 20
        
        score += min(80, int(experience * 10))
        fr_pts = {"0":0, "A1":0, "A2":10, "B1":20, "B2":50, "C1":70, "C2":80}
        score += fr_pts[fr_oral] * 1.2 + fr_pts[fr_write] * 0.8
        if en_lvl == "Advanced": score += 25
        elif en_lvl == "Intermediate": score += 15
        if vjo == "Hors Montreal": score += 380
        elif vjo == "Montreal": score += 180
        if q_stud: score += 50
        if q_fam: score += 30
        if spouse:
            if 18 <= sp_age <= 40: score_sp += 10
            if "Bachelor" in sp_edu or "Master" in sp_edu or "PhD" in sp_edu: score_sp += 10
            elif "College" in sp_edu: score_sp += 5
            if sp_fr in ["C1", "C2"]: score_sp += 30
            elif sp_fr == "B2": score_sp += 20
            elif sp_fr in ["A2", "B1"]: score_sp += 10
            score += score_sp
        score += (k1*4) + (k2*2)

        # Muestra resultados
        with tab4:
            st.markdown(f"""
            <div class="result-box">
                <h2>{lang['res_title']}: {int(score)} / 1350</h2>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(lang['details']):
                st.write(f"**Principal:** {int(score - score_sp - (k1*4 + k2*2))} pts")
                if spouse:
                    st.write(f"**{lang['sp_points']}:** {score_sp} pts")
                st.write(f"**Enfants:** {(k1*4 + k2*2)} pts")
            
            if score > 580:
                st.success(lang['advice_good'])
                st.balloons()
            else:
                st.warning(lang['advice_low'])

# PESTAÑA 2: GUÍA
with main_tab_guide:
    st.markdown(f"### 🗺️ {lang['guide_title']}")
    st.markdown("---")
    st.markdown(f"""
    <div class='step-box'><h4>📊 {lang['g_step1']}</h4><p>{lang['g_desc1']}</p></div>
    <div class='step-box'><h4>🗣️ {lang['g_step2']}</h4><p>{lang['g_desc2']}</p></div>
    <div class='step-box'><h4>📂 {lang['g_step3']}</h4><p>{lang['g_desc3']}</p></div>
    <div class='step-box'><h4>📩 {lang['g_step4']}</h4><p>{lang['g_desc4']}</p></div>
    <div class='step-box'><h4>🍁 {lang['g_step5']}</h4><p>{lang['g_desc5']}</p></div>
    """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown("<div class='footer'>", unsafe_allow_html=True)

fc1, fc2 = st.columns(2)
with fc1:
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
with fc2:
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com") 

st.markdown("###")
st.error(f"**{lang['disclaimer_title']}**")
st.markdown(lang['disclaimer_text'])

st.markdown("</div>", unsafe_allow_html=True)
