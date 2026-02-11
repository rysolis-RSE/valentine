import streamlit as st
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Valentine?", page_icon="💖", layout="centered")

# --- CSS / STYLE (Pour mobile et animation) ---
st.markdown("""
<style>
    /* Pour que ça rende bien sur mobile */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 600px;
    }
    
    /* Cacher les menus Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style de base des boutons */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALISATION DES VARIABLES (MÉMOIRE) ---
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'yes_clicked' not in st.session_state:
    st.session_state.yes_clicked = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# NOM DE L'IMAGE (Doit être exactement pareil que le fichier)
img_filename = "valentine_cat.png"

# --- ÉTAPE 3 : FIN (MESSAGE TIGRE) ---
if st.session_state.form_submitted:
    st.balloons()
    st.markdown("""
        <div style='text-align: center; margin-top: 50px;'>
            <h1 style='color: #ff4b4b; font-size: 50px;'>bv t un tigre 🐯</h1>
            <p>Formulaire envoyé avec succès !</p>
        </div>
        """, unsafe_allow_html=True)

# --- ÉTAPE 2 : FORMULAIRE ---
elif st.session_state.yes_clicked:
    st.markdown("<h2 style='text-align: center;'>Une dernière étape... 📝</h2>", unsafe_allow_html=True)
    
    with st.form("valentine_form"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        
        # Âge : Liste de 13 à 21
        age = st.selectbox("Âge", list(range(13, 22)))
        
        adresse = st.text_input("Adresse")
        telephone = st.text_input("Numéro portable")
        
        # Bodycount (Nombre positif uniquement)
        bodycount = st.number_input("Bodycount", min_value=0, step=1)
        
        st.write("")
        # Bouton pour valider
        submitted = st.form_submit_button("Valider 💘", use_container_width=True)
        
        if submitted:
            st.session_state.form_submitted = True
            st.rerun()

# --- ÉTAPE 1 : ACCUEIL (BOUTONS QUI GRANDISSENT) ---
else:
    # --- LOGIQUE DE GRANDISSEMENT ---
    # Facteur de base 1.0. On ajoute 0.5 à chaque clic sur NON.
    # 0 clics = taille x1
    # 1 clic = taille x1.5
    # 2 clics = taille x2.0
    scale_factor = 1.0 + (st.session_state.no_count * 0.5)
    
    # Injection du CSS dynamique pour cibler le bouton YES (colonne 1)
    st.markdown(
        f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{
            transform: scale({scale_factor});
            transform-origin: center;
            transition: all 0.2s ease-in-out; /* Animation fluide */
            background-color: #ff4b4b !important;
            color: white !important;
            border: 2px solid #ff4b4b !important;
            z-index: 9999; /* Pour passer au-dessus du reste quand il est énorme */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>WILL YOU BE MY VALENTINE??!</h2>", unsafe_allow_html=True)

    # Affichage de l'image
    if os.path.exists(img_filename):
        # use_container_width=True permet à l'image de s'adapter au mobile
        st.image(img_filename, use_container_width=True)
    else:
        st.error(f"Image '{img_filename}' introuvable. Vérifiez le nom du fichier.")

    st.write("") # Espacement vertical
    st.write("")

    # Création des deux colonnes pour les boutons
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        # BOUTON YES
        if st.button("YES 😍", key="yes_btn"):
            st.session_state.yes_clicked = True
            st.rerun()

    with col2:
        # BOUTON NO
        # Désactivé après 3 clics
        if st.session_state.no_count >= 3:
             st.button("NO 🚫", disabled=True, key="no_btn_disabled")
        else:
            # Textes changeants pour le bouton Non
            labels = ["NO", "Sûre ?", "Vraiment ?"]
            current_label = labels[st.session_state.no_count]
            
            if st.button(current_label, key="no_btn"):
                st.session_state.no_count += 1
                st.rerun()
