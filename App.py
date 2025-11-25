import streamlit as st
import pandas as pd

# --- Configuración / Configuration ---
st.set_page_config(page_title="Calculadora PSTQ Pro / Arrima", page_icon="⚜️")

# --- 1. Diccionario de Traducciones (ES / FR / EN) ---
translations = {
    "Español": {
        "sidebar_title": "Configuración",
        "lang_select": "Idioma",
        "bmc_text": "☕ Apóyanos",
        "main_title": "⚜️ Calculadora Arrima (Quebec) - Pro",
        "intro": "Esta herramienta estima tu puntaje de clasificación (Ranking) para recibir una invitación del gobierno de Quebec.",
        "disclaimer_text": "⚠️ NO OFICIAL: Herramienta de estimación personal. No somos abogados ni gobierno.",
        
        # Secciones
        "s_status": "1. Estado Civil",
        "q_status": "¿Cuál es tu situación?",
        "opt_status": ["Soltero(a)", "Con Pareja (Casado/Unión libre)"],
        
        "s_age": "2. Edad",
        "q_age_principal": "Edad del solicitante principal",
        "q_age_spouse": "Edad de la pareja",
        
        "s_edu": "3. Educación",
        "q_edu_principal": "Nivel de estudios (Principal)",
        "q_edu_spouse": "Nivel de estudios (Pareja)",
        "opt_edu": ["Secundaria", "Técnica (1-2 años)", "Técnica (3 años)", "Universidad (Pregrado)", "Maestría", "Doctorado"],
        
        "s_lang": "4. Idiomas (Francés e Inglés)",
        "q_fr_principal": "Tu Nivel de Francés (TEF/TCF)",
        "q_fr_spouse": "Nivel de Francés de tu Pareja",
        "q_en_principal": "Tu Nivel de Inglés (IELTS)",
        
        "s_exp": "5. Experiencia Laboral",
        "q_exp": "Experiencia en los últimos 5 años",
        
        "s_quebec": "6. Estancia y Familia en Quebec",
        "q_stay": "¿Has estudiado o trabajado previamente en Quebec?",
        "opt_stay": ["No", "Sí, estudios (diploma)", "Sí, trabajo (>6 meses)"],
        "q_fam": "¿Tienes familia directa en Quebec? (Informativo)",
        "note_fam": "Nota: En el sistema Arrima actual, la familia a veces no suma puntos al ranking numérico, pero es vital para el CSQ.",
        "opt_yes_no": ["No", "Sí"],
        "q_children": "¿Número de hijos menores de 18? (Informativo)",
        
        "s_job": "7. Oferta de Empleo Validada (VJO)",
        "q_vjo": "¿Tienes una oferta de empleo validada?",
        "opt_vjo": ["No", "Sí, en Montreal", "Sí, FUERA de Montreal"],
        
        "result_title": "🏆 Estimación Total",
        "chart_title": "Desglose de Puntos",
        "res_good": "✅ Buen perfil para aplicar.",
        "res_low": "💡 Necesitas subir puntos (Francés o VJO).",
        
        # Etiquetas cortas para el gráfico
        "chart_labels": ["Edad", "Edu", "Idiomas", "Exp", "Quebec", "VJO", "Pareja"]
    },
    "Français": {
        "sidebar_title": "Configuration",
        "lang_select": "Langue",
        "bmc_text": "☕ Soutenez-nous",
        "main_title": "⚜️ Calculateur Arrima (Québec) - Pro",
        "intro": "Cet outil estime votre score de classement pour recevoir une invitation du gouvernement du Québec.",
        "disclaimer_text": "⚠️ NON OFFICIEL : Outil d'estimation personnelle. Nous ne sommes ni avocats ni gouvernement.",
        
        "s_status": "1. État Civil",
        "q_status": "Quelle est votre situation ?",
        "opt_status": ["Célibataire", "En couple (Marié/Conjoint de fait)"],
        
        "s_age": "2. Âge",
        "q_age_principal": "Âge du demandeur principal",
        "q_age_spouse": "Âge du conjoint",
        
        "s_edu": "3. Éducation",
        "q_edu_principal": "Niveau d'études (Principal)",
        "q_edu_spouse": "Niveau d'études (Conjoint)",
        "opt_edu": ["Secondaire", "Technique (1-2 ans)", "Technique (3 ans)", "Université (1er cycle)", "Maîtrise", "Doctorat"],
        
        "s_lang": "4. Langues (Français et Anglais)",
        "q_fr_principal": "Votre niveau de Français (TEF/TCF)",
        "q_fr_spouse": "Niveau de Français du conjoint",
        "q_en_principal": "Votre niveau d'Anglais (IELTS)",
        
        "s_exp": "5. Expérience de travail",
        "q_exp": "Expérience dans les 5 dernières années",
        
        "s_quebec": "6. Séjour et Famille au Québec",
        "q_stay": "Avez-vous déjà étudié ou travaillé au Québec ?",
        "opt_stay": ["Non", "Oui, études (diplôme)", "Oui, travail (>6 mois)"],
        "q_fam": "Avez-vous de la famille directe au Québec ? (Informatif)",
        "note_fam": "Note : Dans le système Arrima, la famille ne donne pas toujours de points au classement, mais est cruciale pour le CSQ.",
        "opt_yes_no": ["Non", "Oui"],
        "q_children": "Nombre d'enfants de moins de 18 ans ? (Informatif)",
        
        "s_job": "7. Offre d'emploi validée (VJO)",
        "q_vjo": "Avez-vous une offre d'emploi validée ?",
        "opt_vjo": ["Non", "Oui, à Montréal", "Oui, HORS Montréal"],
        
        "result_title": "🏆 Estimation Totale",
        "chart_title": "Répartition des Points",
        "res_good": "✅ Bon profil pour postuler.",
        "res_low": "💡 Besoin de plus de points (Français ou VJO).",
        
        "chart_labels": ["Âge", "Édu", "Langues", "Exp", "Québec", "VJO", "Conjoint"]
    },
    "English": {
        "sidebar_title": "Configuration",
        "lang_select": "Language",
        "bmc_text": "☕ Support us",
        "main_title": "⚜️ Arrima Calculator (Quebec) - Pro",
        "intro": "This tool estimates your ranking score to receive an invitation from the Quebec government.",
        "disclaimer_text": "⚠️ UNOFFICIAL: Personal estimation tool. We are not lawyers or government officials.",
        
        "s_status": "1. Civil Status",
        "q_status": "What is your status?",
        "opt_status": ["Single", "With Spouse (Married/Common-law)"],
        
        "s_age": "2. Age",
        "q_age_principal": "Principal Applicant Age",
        "q_age_spouse": "Spouse/Partner Age",
        
        "s_edu": "3. Education",
        "q_edu_principal": "Education Level (Principal)",
        "q_edu_spouse": "Education Level (Spouse)",
        "opt_edu": ["High School", "Technical (1-2 years)", "Technical (3 years)", "University (Undergrad)", "Master's", "PhD"],
        
        "s_lang": "4. Languages (French & English)",
        "q_fr_principal": "Your French Level (TEF/TCF)",
        "q_fr_spouse": "Spouse's French Level",
        "q_en_principal": "Your English Level (IELTS)",
        
        "s_exp": "5. Work Experience",
        "q_exp": "Experience in the last 5 years",
        
        "s_quebec": "6. Stay & Family in Quebec",
        "q_stay": "Have you previously studied or worked in Quebec?",
        "opt_stay": ["No", "Yes, studies (diploma)", "Yes, work (>6 months)"],
        "q_fam": "Do you have direct family in Quebec? (Informative)",
        "note_fam": "Note: In the current Arrima system, family might not add ranking points directly, but is vital for the CSQ.",
        "opt_yes_no": ["No", "Yes"],
        "q_children": "Number of children under 18? (Informative)",
        
        "s_job": "7. Validated Job Offer (VJO)",
        "q_vjo": "Do you have a validated job offer?",
        "opt_vjo": ["No", "Yes, in Montreal", "Yes, OUTSIDE Montreal"],
        
        "result_title": "🏆 Total Estimate",
        "chart_title": "Score Breakdown",
        "res_good": "✅ Good profile to apply.",
        "res_low": "💡 You need more points (French or VJO).",
        
        "chart_labels": ["Age", "Edu", "Languages", "Exp", "Quebec", "VJO", "Spouse"]
    }
}

# --- 2. CONFIGURACIÓN Y SIDEBAR ---
st.sidebar.header("Configuration")
lang_choice = st.sidebar.selectbox("Language / Idioma", ["Español", "Français", "English"])
t = translations[lang_choice]

# Botón Buy Me a Coffee (Opcional)
st.sidebar.markdown("---")
st.sidebar.write(f"**{t['bmc_text']}**")
# CalculatricePSTQQuebec
bmc_username = CalculatricePSTQQuebec
st.sidebar.markdown(f"""
<a href="https://www.buymeacoffee.com/{bmc_username}" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 50px !important;width: 180px !important;" >
</a>
""", unsafe_allow_html=True)

# --- 3. INTERFAZ PRINCIPAL ---

st.warning(t['disclaimer_text'])
st.title(t['main_title'])
st.write(t['intro'])

# Variables de puntaje iniciales
score_age = 0
score_edu = 0
score_lang = 0
score_exp = 0
score_stay = 0 
score_vjo = 0
score_spouse = 0 

# --- SECCIÓN 1: ESTADO CIVIL ---
st.header(t['s_status'])
status_sel = st.radio(t['q_status'], t['opt_status'])
is_couple = (t['opt_status'].index(status_sel) == 1)

# --- SECCIÓN 2: EDAD ---
st.header(t['s_age'])
col1, col2 = st.columns(2)

with col1:
    age_princ = st.number_input(t['q_age_principal'], 18, 65, 30)
    max_pts_age = 110 if is_couple else 130
    
    if 18 <= age_princ <= 30: score_age = max_pts_age
    elif age_princ == 31: score_age = max_pts_age - 15
    elif age_princ == 32: score_age = max_pts_age - 25
    elif age_princ > 32 and age_princ < 45: score_age = max(0, max_pts_age - (age_princ - 30) * 10)
    else: score_age = 0

with col2:
    if is_couple:
        age_spouse = st.number_input(t['q_age_spouse'], 18, 65, 30)
        # Edad Conjoint (Max ~20 aprox)
        if 18 <= age_spouse <= 30: score_spouse += 20
        elif age_spouse < 40: score_spouse += 10
        else: score_spouse += 0

# --- SECCIÓN 3: EDUCACIÓN ---
st.header(t['s_edu'])
col3, col4 = st.columns(2)

with col3:
    edu_princ = st.selectbox(t['q_edu_principal'], t['opt_edu'])
    idx_edu = t['opt_edu'].index(edu_princ)
    
    pts_base_edu = [10, 30, 50, 60, 75, 90] 
    raw_edu = pts_base_edu[idx_edu]
    
    if is_couple:
        score_edu = int(raw_edu * 0.9)
    else:
        score_edu = raw_edu

with col4:
    if is_couple:
        edu_spouse = st.selectbox(t['q_edu_spouse'], t['opt_edu'])
        idx_edu_sp = t['opt_edu'].index(edu_spouse)
        score_spouse += [2, 5, 10, 12, 15, 20][idx_edu_sp]

# --- SECCIÓN 4: IDIOMAS ---
st.header(t['s_lang'])
fr_princ = st.select_slider(t['q_fr_principal'], ["A1", "A2", "B1", "B2", "C1", "C2"])
en_princ = st.select_slider(t['q_en_principal'], ["A1", "A2", "B1", "B2", "C1", "C2"])

# Francés Principal
if fr_princ in ["C1", "C2"]: score_lang += 140 
elif fr_princ == "B2": score_lang += 100
elif fr_princ == "B1": score_lang += 40

# Inglés Principal
if en_princ in ["C1", "C2"]: score_lang += 60
elif en_princ in ["B1", "B2"]: score_lang += 40

if is_couple:
    st.markdown("---")
    fr_spouse = st.select_slider(t['q_fr_spouse'], ["A1", "A2", "B1", "B2", "C1", "C2"])
    if fr_spouse in ["C1", "C2"]: score_spouse += 40
    elif fr_spouse == "B2": score_spouse += 20

# --- SECCIÓN 5: EXPERIENCIA ---
st.header(t['s_exp'])
years = st.slider(t['q_exp'], 0, 10, 5)
if years >= 4: score_exp = 100
elif years == 3: score_exp = 80
elif years == 2: score_exp = 60
elif years == 1: score_exp = 40

# --- SECCIÓN 6: QUEBEC & FAMILIA ---
st.header(t['s_quebec'])
stay_sel = st.radio(t['q_stay'], t['opt_stay'])
if t['opt_stay'].index(stay_sel) == 2: score_stay += 80 
elif t['opt_stay'].index(stay_sel) == 1: score_stay += 60

fam_q = st.radio(t['q_fam'], t['opt_yes_no'])
children = st.number_input(t['q_children'], 0, 10, 0)
st.caption(f"ℹ️ {t['note_fam']}")

# --- SECCIÓN 7: VJO ---
st.header(t['s_job'])
vjo_sel = st.radio(t['q_vjo'], t['opt_vjo'])
if t['opt_vjo'].index(vjo_sel) == 2: score_vjo = 380
elif t['opt_vjo'].index(vjo_sel) == 1: score_vjo = 180

# --- CÁLCULOS FINALES ---
total_score = score_age + score_edu + score_lang + score_exp + score_stay + score_vjo + score_spouse

st.markdown("---")
st.subheader(f"{t['result_title']}: {total_score} / 1320")

# --- GRÁFICO ---
# Usamos las etiquetas traducidas para el gráfico
st.write(f"### {t['chart_title']}")
data = {
    'Category': t['chart_labels'], 
    'Points': [score_age, score_edu, score_lang, score_exp, score_stay, score_vjo, score_spouse]
}
st.bar_chart(pd.DataFrame(data).set_index('Category'))

if total_score > 580:
    st.success(t['res_good'])
    st.balloons()
else:
    st.info(t['res_low'])
