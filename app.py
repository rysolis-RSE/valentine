import streamlit as st
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="Valentine", layout="centered")

# --- CSS OPTIMISÉ (IMAGE MAÎTRISÉE) ---
st.markdown("""
<style>
    /* On limite la largeur globale pour que ça ne fasse pas "trop large" */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 500px; /* Largeur max idéale pour mobile/tablette */
    }
    
    /* Cacher les menus Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style des boutons par défaut */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 55px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Permettre au bouton de déborder des colonnes */
    .stColumn {
        overflow: visible !important;
    }
    
    /* Centrer l'image */
    div[data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# --- VARIABLES ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

img_filename = "valentine_cat.png"

# --- ETAPE 3 : FIN ---
if st.session_state.form_submitted:
    st.balloons()
    st.markdown("""
        <div style='text-align: center; margin-top: 50px;'>
            <h1 style='color: #ff4b4b; font-size: 40px;'>bv t un tigre</h1>
        </div>
        """, unsafe_allow_html=True)

# --- ETAPE 2 : FORMULAIRE ---
elif st.session_state.yes_clicked:
    st.markdown("<h3 style='text-align: center;'>Dernière étape</h3>", unsafe_allow_html=True)
    
    with st.form("valentine_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        # Âge 13-21
        age = st.selectbox("Âge", list(range(13, 22)))
        adresse = st.text_input("Adresse")
        telephone = st.text_input("Numéro portable")
        # Bodycount
        bodycount = st.number_input("Bodycount", min_value=0, step=1)
        
        st.write("")
        submitted = st.form_submit_button("Valider", use_container_width=True)
        
        if submitted:
            st.session_state.form_submitted = True
            st.rerun()

# --- ETAPE 1 : ACCUEIL ---
else:
    # --- LOGIQUE DE CROISSANCE EXTRÊME (Facteur 6) ---
    scale_factor = 1.0 + (st.session_state.no_count * 6.0)
    
    # CSS pour le bouton YES
    st.markdown(
        f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            transform: scale({scale_factor});
            transform-origin: center center;
            transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            background-color: #ff4b4b !important;
            color: white !important;
            border: none !important;
            z-index: 99999 !important;
            position: relative;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Affichage de l'image avec une taille FIXE (350px)
    # Elle sera responsive si l'écran est plus petit que 350px, mais ne dépassera pas cette taille.
    if os.path.exists(img_filename):
        st.image(img_filename, width=350) 
    
    st.write("")
    st.write("")

    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        if st.button("YES", key="yes_btn"):
            st.session_state.yes_clicked = True
            st.rerun()

    with col2:
        if st.session_state.no_count >= 3:
             st.button("NO", disabled=True, key="no_btn_disabled")
        else:
            labels = ["NO", "Sûre ?", "Vraiment ?"]
            current_label = labels[st.session_state.no_count]
            
            if st.button(current_label, key="no_btn"):
                st.session_state.no_count += 1
                st.rerun()
                st.session_state.no_count += 1
                st.rerun()
