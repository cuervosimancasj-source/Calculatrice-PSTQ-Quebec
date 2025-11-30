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
        .step-box {
            background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px;
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
        'main_tabs': ["🧮 Calculatrice", "ℹ️ Guide & Étapes"],
        'tabs': ["👤 Profil", "💼 Travail & TEER", "🗣️ Langues", "⚜️ Québec/OEV"],
        'job_title': "Quel est votre emploi actuel ?",
        'job_placeholder': "Ex: Ingénieur, Soudeur, Assembleur...",
        'teer_manual_help': "Si vous n'avez pas trouvé votre emploi, choisissez selon votre niveau :",
        'teer_label': "Sélectionnez votre niveau (Catégorie TEER)",
        'teer_guide': "**Aide:** TEER 0,1 = Université/Gestion | TEER 2 = Collégial/Technique | TEER 3 = Métiers | TEER 4,5 = Secondaire/Manuel",
        'exp_label': "Années d'expérience qualifiée",
        'lang_info': "**Exigences :** Volet 1 = Niveau 7 | Volet 2 = Niveau 5",
        'age': "Âge", 'spouse': "Conjoint(e) ?", 'kids12': "Enfants -12", 'kids13': "Enfants +12",
        'sp_section': "Calcul du niveau de Français du Conjoint",
        'sp_fr_label': "Niveau de Français (Oral) du conjoint",
        'edu': "Niveau d'études", 'vjo': "Offre d'emploi (OEV)", 'calc': "CALCULER MON SCORE",
        'res_title': "Résultat Estimé",
        'advice_good': "Excellent ! Vous êtes compétitif.",
        'advice_low': "Améliorez le français ou cherchez une OEV en région.",
        # NUEVA GUÍA
        'guide_title': "Votre Feuille de Route vers la Résidence",
        'g_step1': "1. Auto-évaluation", 'g_desc1': "Utilisez cet outil pour connaître vos points forts (Langue, VJO, Âge).",
        'g_step2': "2. Préparation (Français)", 'g_desc2': "C'est la clé. Visez un niveau B2 (7) ou C1 pour maximiser vos points.",
        'g_step3': "3. Arrima (DI)", 'g_desc3': "Créez votre profil gratuitement dans la banque Arrima du MIFI.",
        'g_step4': "4. Invitation & CSQ", 'g_desc4': "Si vous êtes sélectionné, vous demanderez le Certificat de Sélection du Québec (CSQ).",
        'g_step5': "5. Fédéral", 'g_desc5': "Avec le CSQ, demandez la Résidence Permanente au gouvernement du Canada."
    },
    'es': {
        'btn_lang': "Idioma: Español 🇪🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Herramienta de análisis para Residencia (TEER, Volets, Puntaje).",
        'disclaimer_text': "Proyecto independiente. Resultados estimados.",
        'coffee': "☕ Invítame un café",
        'courses': "📚 Cursos de Francés",
        'main_tabs': ["🧮 Calculadora", "ℹ️ Guía y Pasos"],
        'tabs': ["👤 Perfil", "💼 Trabajo y TEER", "🗣️ Idiomas", "⚜️ Quebec/VJO"],
        'job_title': "¿Cuál es tu trabajo actual?",
        'job_placeholder': "Ej: Ingeniero, Soldador, Ensamblador...",
        'teer_manual_help': "Si no encontraste tu empleo, elige según tu nivel:",
        'teer_label': "Selecciona tu nivel (Categoría TEER)",
        'teer_guide': "**Ayuda:** TEER 0,1 = Universidad/Gerencia | TEER 2 = College/Técnico | TEER 3 = Oficios | TEER 4,5 = Secundaria/Manual",
        'exp_label': "Años de experiencia calificada",
        'lang_info': "**Requisitos:** Volet 1 = Nivel 7 | Volet 2 = Nivel 5",
        'age': "Edad", 'spouse': "Pareja ?", 'kids12': "Hijos -12", 'kids13': "Hijos +12",
        'sp_section': "Calcula el nivel de francés de tu pareja",
        'sp_fr_label': "Nivel de Francés (Oral) de la pareja",
        'edu': "Nivel estudios", 'vjo': "Oferta empleo (VJO)", 'calc': "CALCULAR PUNTAJE",
        'res_title': "Resultado Estimado",
        'advice_good': "¡Excelente! Eres competitivo.",
        'advice_low': "Mejora el francés o busca una VJO en regiones.",
        # NUEVA GUÍA
        'guide_title': "Tu Hoja de Ruta hacia la Residencia",
        'g_step1': "1. Autoevaluación", 'g_desc1': "Usa esta herramienta para conocer tus fortalezas (Idioma, VJO, Edad).",
        'g_step2': "2. Preparación (Francés)", 'g_desc2': "Es la clave. Apunta a un nivel B2 (7) o C1 para maximizar puntos.",
        'g_step3': "3. Arrima (DI)", 'g_desc3': "Crea tu perfil gratis en el banco Arrima del MIFI.",
        'g_step4': "4. Invitación y CSQ", 'g_desc4': "Si eres seleccionado, solicitarás el Certificado de Selección de Quebec (CSQ).",
        'g_step5': "5. Federal", 'g_desc5': "Con el CSQ, solicita la Residencia Permanente al gobierno de Canadá."
    },
    'en': {
        'btn_lang': "Language: English 🇺🇸",
        'brand': "Calculatrice PSTQ Québec ⚜️",
        'subtitle': "Analysis tool for Residency (TEER, Volets, Score).",
        'disclaimer_text': "Independent project. Estimated results.",
        'coffee': "☕ Buy me a coffee",
        'courses': "📚 French Courses",
        'main_tabs': ["🧮 Calculator", "ℹ️ Guide & Steps"],
        'tabs': ["👤 Profile", "💼 Work & TEER", "🗣️ Languages", "⚜️ Quebec/VJO"],
        'job_title': "What is your current job?",
        'job_placeholder': "Ex: Engineer, Welder, Assembler...",
        'teer_manual_help': "If job not found, select by level:",
        'teer_label': "Select your level (TEER Category)",
        'teer_guide': "**Help:** TEER 0,1 = University/Mgmt | TEER 2 = College/Tech | TEER 3 = Trades | TEER 4,5 = High School/Manual",
        'exp_label': "Years of qualified experience",
        'lang_info': "**Requirements:** Volet 1 = Level 7 | Volet 2 = Level 5",
        'age': "Age", 'spouse': "Spouse ?", 'kids12': "Kids -12", 'kids13': "Kids +12",
        'sp_section': "Calculate Spouse's French Level",
        'sp_fr_label': "Spouse's French Level (Oral)",
        'edu': "Education Level", 'vjo': "Job Offer (VJO)", 'calc': "CALCULATE SCORE",
        'res_title': "Estimated Result",
        'advice_good': "Excellent! You are competitive.",
        'advice_low': "Improve French or find a VJO in regions.",
        # NUEVA GUÍA
        'guide_title': "Your Roadmap to Residency",
        'g_step1': "1. Self-Assessment", 'g_desc1': "Use this tool to know your strengths (Language, VJO, Age).",
        'g_step2': "2. Preparation (French)", 'g_desc2': "This is key. Aim for B2 (7) or C1 level to maximize points.",
        'g_step3': "3. Arrima (EOI)", 'g_desc3': "Create your profile for free in the MIFI Arrima bank.",
        'g_step4': "4. Invitation & CSQ", 'g_desc4': "If selected, you will apply for the Quebec Selection Certificate (CSQ).",
        'g_step5': "5. Federal", 'g_desc5': "With the CSQ, apply for Permanent Residency to the Government of Canada."
    }
}
lang = t[st.session_state.language]

# --- 5. BASE DE DATOS TRABAJOS ---
jobs_db = {
    "ingenie": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "engineer": {"code": "213xx", "teer": "1", "volet": "Volet 1"},
    "software": {"code": "21220", "teer": "1", "volet": "Volet 1"},
    "web": {"code": "21222", "teer": "1", "volet": "Volet 1"},
    "infirmier": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "nurse": {"code": "31301", "teer": "1", "volet": "Volet 1"},
    "administra": {"code": "13100", "teer": "3", "volet": "Volet 2"},
    "technicien": {"code": "22xxx", "teer": "2", "volet": "Volet 1/2"},
    "soud": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "welder": {"code": "72106", "teer": "2", "volet": "Volet 1/2"},
    "cuisinier": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "cook": {"code": "63200", "teer": "3", "volet": "Volet 2"},
    "camion": {"code": "73300", "teer": "3", "volet": "Volet 2"},
    "ensamblador": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "assembler": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manguera": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hose": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "hidraulica": {"code": "94219", "teer": "4", "volet": "Volet 2"},
    "manoeuvre": {"code": "9510", "teer": "5", "volet": "Volet 2"},
}

def find_job_details(keyword):
    keyword = keyword.lower().strip()
    for key, data in jobs_db.items():
        if key in keyword: return data
    return None

# --- 6. SIDEBAR ---
with st.sidebar:
    st.button(lang['btn_lang'], on_click=cycle_language, type="secondary")
    st.markdown("---")
    st.link_button(lang['coffee'], "https://www.buymeacoffee.com/CalculatricePSTQQuebec")
    st.link_button(lang['courses'], "https://www.TU_ENLACE_DE_AFILIADO.com") 
    st.markdown("---")
    st.warning(lang['disclaimer_text'])

# --- 7. APP PRINCIPAL ---
st.markdown(f"# {lang['brand']}")
st.write(lang['subtitle'])

# CREAMOS DOS PESTAÑAS PRINCIPALES (Para separar la Guía del Botón)
main_tab_calc, main_tab_guide = st.tabs(lang['main_tabs'])

# ==========================================
# PESTAÑA 1: CALCULADORA (CON FORMULARIO)
# ==========================================
with main_tab_calc:
    with st.form("main_form"):
        # Sub-pestañas internas
        tab1, tab2, tab3, tab4 = st.tabs(lang['tabs'])

        # SUB-TAB 1: PERFIL & PAREJA
        with tab1:
            c1, c2 = st.columns(2)
            with c1: age = st.number_input(lang['age'], 18, 65, 30)
            with c2: spouse = st.checkbox(lang['spouse'])
            
            c3, c4 = st.columns(2)
            with c3: k1 = st.number_input(lang['kids12'], 0, 5, 0)
            with c4: k2 = st.number_input(lang['kids13'], 0, 5, 0)
            
            # Variables Pareja
            sp_age, sp_edu, sp_fr = 30, "Secondary", "0"
            if spouse:
                st.divider()
                st.markdown(f"#### ❤️ {lang['sp_section']}")
                col_sp1, col_sp2 = st.columns(2)
                with col_sp1:
                    sp_age = st.number_input("Age (Spouse/Pareja)", 18, 65, 30)
                    sp_edu = st.selectbox("Education (Spouse/Pareja)", ["PhD", "Master", "Bachelor", "Technical", "Secondary"])
                with col_sp2:
                    st.info("Nivel 7 (B2) + Points.")
                    sp_fr = st.select_slider(lang['sp_fr_label'], options=["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="0")

        # SUB-TAB 2: TRABAJO
        with tab2:
            st.markdown(f"### 🔍 {lang['job_title']}")
            job_query = st.text_input("Buscador / Recherche", placeholder=lang['job_placeholder'])
            if job_query:
                result = find_job_details(job_query)
                if result:
                    st.success(f"✅ Code: {result['code']} | TEER: {result['teer']} | {result['volet']}")
                else:
                    st.markdown(f"<div class='help-box'>{lang['teer_guide']}</div>", unsafe_allow_html=True)

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

        # SUB-TAB 3: IDIOMAS
        with tab3:
            st.markdown(f"<div class='info-box'>{lang['lang_info']}</div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1: fr_oral = st.select_slider("Français Oral (Principal)", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B2")
            with c2: fr_write = st.select_slider("Français Écrit (Principal)", ["0", "A1", "A2", "B1", "B2", "C1", "C2"], value="B1")
            en_lvl = st.select_slider("English", ["0", "Beginner", "Intermediate", "Advanced"], value="0")

        # SUB-TAB 4: QUEBEC
        with tab4:
            vjo = st.radio(lang['vjo'], ["Non", "Montreal", "Hors Montreal"])
            cq1, cq2 = st.columns(2)
            with cq1: q_stud = st.checkbox("Diplôme Québec ?")
            with cq2: q_fam = st.checkbox("Famille Québec ?")

        st.markdown("###")
        # EL BOTÓN SOLO APARECE AQUÍ, DENTRO DE LA PESTAÑA CALCULADORA
        submitted = st.form_submit_button(lang['calc'], type="primary", use_container_width=True)

    # LÓGICA DE CÁLCULO (Solo se ejecuta si se presiona el botón)
    if submitted:
        score = 0
        if 18 <= age <= 30: score += 130
        elif age <= 45: score += (130 - (age-30)*5)
        
        if "PhD" in education: score += 90
        elif "Master" in education: score += 75
        elif "Bachelor" in education: score += 60
        elif "College" in education: score += 50
        else: score += 30
        
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
            if 18 <= sp_age <= 40: score += 10
            if "Bachelor" in sp_edu or "Master" in sp_edu or "PhD" in sp_edu: score += 10
            elif "College" in sp_edu: score += 5
            if sp_fr in ["C1", "C2"]: score += 30
            elif sp_fr == "B2": score += 20
            elif sp_fr in ["A2", "B1"]: score += 10
            
        score += (k1*4) + (k2*2)

        st.markdown("---")
        st.markdown(f"<h2 style='text-align: center; color: #003399;'>{lang['res_title']}: {int(score)} / 1350</h2>", unsafe_allow_html=True)
        st.progress(min(score/1350, 1.0))
        
        if score > 580:
            st.success(lang['advice_good'])
            st.balloons()
        else:
            st.warning(lang['advice_low'])


# ==========================================
# PESTAÑA 2: GUÍA (SIN BOTÓN, PURO TEXTO)
# ==========================================
with main_tab_guide:
    st.markdown(f"### 🗺️ {lang['guide_title']}")
    st.markdown("---")
    
    st.markdown(f"""
    <div class='step-box'>
        <h4>📊 {lang['g_step1']}</h4>
        <p>{lang['g_desc1']}</p>
    </div>
    
    <div class='step-box'>
        <h4>🗣️ {lang['g_step2']}</h4>
        <p>{lang['g_desc2']}</p>
    </div>
    
    <div class='step-box'>
        <h4>📂 {lang['g_step3']}</h4>
        <p>{lang['g_desc3']}</p>
    </div>
    
    <div class='step-box'>
        <h4>📩 {lang['g_step4']}</h4>
        <p>{lang['g_desc4']}</p>
    </div>
    
    <div class='step-box'>
        <h4>🍁 {lang['g_step5']}</h4>
        <p>{lang['g_desc5']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Tip:** Mantén tu CV actualizado y en formato canadiense.")
    
