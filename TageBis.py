import streamlit as st
from datetime import datetime
import pytz

st.title("Countdown für Anna")

# --- Zeitzone Atlanta ---
atlanta_tz = pytz.timezone("America/New_York")
atlanta_now = datetime.now(atlanta_tz)

# --- Ziel-Datum (in Atlanta-Zeit) ---
ziel_datum = atlanta_tz.localize(datetime(2026, 5, 30))

# --- Countdown berechnen ---
tage_bis = (ziel_datum - atlanta_now).days

st.subheader(f"Heute ist der {atlanta_now.strftime('%d.%m.%Y')}.")
st.subheader(f"⏳ Es verbleiben noch {tage_bis} Tage bis zum 30.05.2026 !")




