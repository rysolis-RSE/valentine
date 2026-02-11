import streamlit as st
import os

# Configuration : "centered" est mieux pour mobile que "wide"
st.set_page_config(page_title="Valentine?", page_icon="💖", layout="centered")

# --- CSS SPECIAL MOBILE ---
st.markdown("""
<style>
    /* Force le contenu à ne pas être trop large sur PC, mais plein écran sur mobile */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 600px;
    }
    
    /* Cache le menu hamburger et le footer Streamlit pour faire plus "app" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style des boutons */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Initialisation des variables ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

img_path = "valentine_cat.png"

# --- LOGIQUE ---

if st.session_state.form_submitted:
    st.balloons()
    st.success("C'est envoyé ! 💖")
    st.markdown("<h3 style='text-align: center;'>Je t'écris très vite ! 😘</h3>", unsafe_allow_html=True)

elif st.session_state.yes_clicked:
    st.markdown("<h2 style='text-align: center;'>Une dernière étape... 📝</h2>", unsafe_allow_html=True)
    
    with st.form("valentine_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        
        # Liste d'âges (13-21)
        age = st.selectbox("Âge", list(range(13, 22)))
        
        adresse = st.text_input("Adresse")
        telephone = st.text_input("Numéro portable")
        
        # Bodycount
        bodycount = st.number_input("Bodycount", min_value=0, step=1)
        
        st.write("")
        submitted = st.form_submit_button("Valider 💘", use_container_width=True)
        
        if submitted:
            st.session_state.form_submitted = True
            st.rerun()

else:
    # Calcul de la taille du bouton YES
    scale_factor = 1.0 + (st.session_state.no_count * 0.4) # Augmente plus vite
    
    # Injection du style dynamique pour le bouton YES
    # On utilise !important pour surcharger le style par défaut
    st.markdown(
        f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            transform: scale({scale_factor});
            transform-origin: center;
            transition: all 0.3s ease;
            background-color: #ff4b4b !important;
            color: white !important;
            border: 2px solid #ff4b4b !important;
            z-index: 1000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>WILL YOU BE MY VALENTINE??!</h2>", unsafe_allow_html=True)

    # Image responsive (s'adapte à la largeur du mobile)
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    
    st.write("")
    st.write("")

    # Colonnes pour les boutons
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        if st.button("YES 😍", key="yes_btn"):
            st.session_state.yes_clicked = True
            st.rerun()

    with col2:
        if st.session_state.no_count >= 3:
             st.button("NO 🚫", disabled=True, key="no_btn_disabled")
        else:
            labels = ["NO", "Sûre ?", "Vraiment ?"]
            if st.button(labels[st.session_state.no_count], key="no_btn"):
                st.session_state.no_count += 1
                st.rerun()
