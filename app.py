import streamlit as st
import os

# --- CONFIGURATION DE LA PAGE (Sans emoji) ---
st.set_page_config(page_title="Valentine", layout="centered")

# --- CSS / STYLE ---
st.markdown("""
<style>
    /* Optimisation mobile */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 600px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style boutons */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- VARIABLES D'ÉTAT ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Nom de l'image
img_filename = "valentine_cat.png"

# --- ETAPE 3 : FIN ---
if st.session_state.form_submitted:
    st.balloons()
    st.markdown("""
        <div style='text-align: center; margin-top: 50px;'>
            <h1 style='color: #ff4b4b; font-size: 50px;'>bv t un tigre</h1>
            <p>Formulaire envoyé.</p>
        </div>
        """, unsafe_allow_html=True)

# --- ETAPE 2 : FORMULAIRE ---
elif st.session_state.yes_clicked:
    st.markdown("<h2 style='text-align: center;'>Dernière étape</h2>", unsafe_allow_html=True)
    
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
    # CROISSANCE TRÈS RAPIDE
    # A chaque clic sur NON, on ajoute +1.5 à la taille (1 -> 2.5 -> 4 -> 5.5)
    scale_factor = 1.0 + (st.session_state.no_count * 1.5)
    
    st.markdown(
        f"""
        <style>
        /* Cible le bouton YES */
        div[data-testid="column"]:nth-of-type(1) button {{
            transform: scale({scale_factor});
            transform-origin: center;
            transition: all 0.2s ease-in-out;
            background-color: #ff4b4b !important;
            color: white !important;
            border: 2px solid #ff4b4b !important;
            z-index: 9999;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>WILL YOU BE MY VALENTINE??!</h2>", unsafe_allow_html=True)

    if os.path.exists(img_filename):
        st.image(img_filename, use_container_width=True)
    
    st.write("")
    st.write("")

    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        if st.button("YES", key="yes_btn"):
            st.session_state.yes_clicked = True
            st.rerun()

    with col2:
        if st.session_state.no_count >= 3:
             # Bouton désactivé après 3 clics
             st.button("NO", disabled=True, key="no_btn_disabled")
        else:
            # Textes sans emoji
            labels = ["NO", "Sûre ?", "Vraiment ?"]
            current_label = labels[st.session_state.no_count]
            
            if st.button(current_label, key="no_btn"):
                st.session_state.no_count += 1
                st.rerun()
