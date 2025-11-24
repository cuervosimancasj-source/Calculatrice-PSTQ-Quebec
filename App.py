import streamlit as st
import pandas as pd

# --- Configuración / Configuration ---
st.set_page_config(page_title="Calculadora PSTQ Pro / Arrima", page_icon="⚜️")

# --- 1. Diccionario de Traducciones ---
translations = {
    "Español": {
        "sidebar_title": "Configuración",
        "lang_select": "Idioma / Langue",
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
        "q_children": "¿Número de hijos menores de 18? (Informativo)",
        
        "s_job": "7. Oferta de Empleo Validada (VJO)",
        "q_vjo": "¿Tienes una oferta de empleo validada?",
        "opt_vjo": ["No", "Sí, en Montreal", "Sí, FUERA de Montreal"],
        
        "result_title": "🏆 Estimación Total",
        "chart_title": "Desglose de Puntos"
    },
    "Français": {
        "sidebar_title": "Configuration",
        "lang_select": "Langue / Language",
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
        "q_children": "Nombre d'enfants de moins de 18 ans ? (Informatif)",
        
        "s_job": "7. Offre d'emploi validée (VJO)",
        "q_vjo": "Avez-vous une offre d'emploi validée ?",
        "opt_vjo": ["Non", "Oui, à Montréal", "Oui, HORS Montréal"],
        
        "result_title": "🏆 Estimation Totale",
        "chart_title": "Répartition des Points"
    }
}

# --- 2. Configuración Inicial ---
st.sidebar.header("Configuration")
lang_choice = st.sidebar.selectbox("Language", ["Español", "Français"])
t = translations[lang_choice]

st.warning(t['disclaimer_text'])
st.title(t['main_title'])
st.write(t['intro'])

# Variables de puntaje
score_age = 0
score_edu = 0
score_lang = 0
score_exp = 0
score_stay = 0 # Estancia previa
score_vjo = 0
score_spouse = 0 # Puntos que aporta la pareja

# --- SECCIÓN 1: ESTADO CIVIL ---
st.header(t['s_status'])
status_sel = st.radio(t['q_status'], t['opt_status'])
is_couple = (t['opt_status'].index(status_sel) == 1)

# --- SECCIÓN 2: EDAD ---
st.header(t['s_age'])
col1, col2 = st.columns(2)

with col1:
    age_princ = st.number_input(t['q_age_principal'], 18, 65, 30)
    
    # Lógica Edad Principal (Varía si es Soltero o Pareja)
    # En Arrima: Soltero Max 130, Pareja Max 110 (aprox)
    max_pts_age = 110 if is_couple else 130
    
    if 18 <= age_princ <= 30: score_age = max_pts_age
    elif age_princ == 31: score_age = max_pts_age - 15
    elif age_princ == 32: score_age = max_pts_age - 25
    elif age_princ > 32 and age_princ < 45: score_age = max(0, max_pts_age - (age_princ - 30) * 10)
    else: score_age = 0

with col2:
    if is_couple:
        age_spouse = st.number_input(t['q_age_spouse'], 18, 65, 30)
        # Edad Conjoint (Max ~20 aprox en Arrima actual)
        if 18 <= age_spouse <= 30: score_spouse += 20
        elif age_spouse < 40: score_spouse += 10
        else: score_spouse += 0

# --- SECCIÓN 3: EDUCACIÓN ---
st.header(t['s_edu'])
col3, col4 = st.columns(2)

with col3:
    edu_princ = st.selectbox(t['q_edu_principal'], t['opt_edu'])
    idx_edu = t['opt_edu'].index(edu_princ)
    
    # Puntos Base Edu
    pts_base_edu = [10, 30, 50, 60, 75, 90] # Sec, Tec1, Tec2, Univ, Maes, Doc
    raw_edu = pts_base_edu[idx_edu]
    
    # Ajuste por pareja: Si tienes pareja, tus puntos valen un poco menos
    # Soltero Max 90 / Pareja Max 80 (aprox)
    if is_couple:
        score_edu = int(raw_edu * 0.9) # Reducción simple
    else:
        score_edu = raw_edu

with col4:
    if is_couple:
        edu_spouse = st.selectbox(t['q_edu_spouse'], t['opt_edu'])
        idx_edu_sp = t['opt_edu'].index(edu_spouse)
        # Puntos Conjoint Edu (Max ~10-20)
        score_spouse += [2, 5, 10, 12, 15, 20][idx_edu_sp]

# --- SECCIÓN 4: IDIOMAS ---
st.header(t['s_lang'])
fr_princ = st.select_slider(t['q_fr_principal'], ["A1", "A2", "B1", "B2", "C1", "C2"])
en_princ = st.select_slider(t['q_en_principal'], ["A1", "A2", "B1", "B2", "C1", "C2"])

# Francés Principal
if fr_princ in ["C1", "C2"]: score_lang += 140 # Aprox
elif fr_princ == "B2": score_lang += 100
elif fr_princ == "B1": score_lang += 40

# Inglés Principal
if en_princ in ["C1", "C2"]: score_lang += 60 # Aprox
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

# Estancia
stay_sel = st.radio(t['q_stay'], t['opt_stay'])
if t['opt_stay'].index(stay_sel) == 2: # Trabajo
    score_stay += 80 
elif t['opt_stay'].index(stay_sel) == 1: # Estudio
    score_stay += 60

# Familia (Informativo en Arrima, pero lo preguntamos)
fam = st.radio(t['q_fam'], ["No", "Si / Oui"])
children = st.number_input(t['q_children'], 0, 10, 0)
st.caption(f"ℹ️ {t['note_fam']}")

# --- SECCIÓN 7: VJO ---
st.header(t['s_job'])
vjo_sel = st.radio(t['q_vjo'], t['opt_vjo'])
if t['opt_vjo'].index(vjo_sel) == 2: # Fuera MTL
    score_vjo = 380
elif t['opt_vjo'].index(vjo_sel) == 1: # En MTL
    score_vjo = 180

# --- CÁLCULOS FINALES ---
total_score = score_age + score_edu + score_lang + score_exp + score_stay + score_vjo + score_spouse

st.markdown("---")
st.subheader(f"{t['result_title']}: {total_score} / 1320")

# --- GRÁFICO ---
data = {
    'Category': ['Edad/Âge', 'Edu', 'Lang', 'Exp', 'Quebec', 'VJO', 'Pareja/Conjoint'],
    'Points': [score_age, score_edu, score_lang, score_exp, score_stay, score_vjo, score_spouse]
}
st.bar_chart(pd.DataFrame(data).set_index('Category'))

if total_score > 580:
    st.success("✅ Buen perfil para aplicar. / Bon profil.")
else:
    st.info("💡 Necesitas subir puntos (Francés o VJO). / Besoin de plus de points.")
