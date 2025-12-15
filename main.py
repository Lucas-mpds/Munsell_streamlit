import streamlit as st
import numpy as np
from PIL import Image
import colour

#streamlit run main.py

st.title("Carta Munsell!")

foto = st.camera_input("Tire a foto")

def rgb_medio_da_imagem(img_pil: Image.Image):
    arr = np.array(img_pil.convert("RGB"))
    r, g, b = arr[:, :, 0].mean(), arr[:, :, 1].mean(), arr[:, :, 2].mean()
    return float(r), float(g), float(b)

def srgb8_to_munsell(r8, g8, b8):
    # sRGB em [0,1]
    srgb = np.array([r8, g8, b8]) / 255.0

    # sRGB (D65) -> XYZ -> xyY -> Munsell
    XYZ = colour.sRGB_to_XYZ(srgb)
    xyY = colour.XYZ_to_xyY(XYZ)
    munsell = colour.xyY_to_munsell_colour(xyY)

    return munsell, srgb, xyY

if foto:
    img = Image.open(foto)
    st.image(img, caption="Imagem capturada")

    r_mean, g_mean, b_mean = rgb_medio_da_imagem(img)
    st.write(f"Média RGB (0–255): R={r_mean:.1f}, G={g_mean:.1f}, B={b_mean:.1f}")

    munsell, srgb01, xyY = srgb8_to_munsell(r_mean, g_mean, b_mean)

    st.subheader("Resultado")
    st.write("sRGB (0–1):", srgb01)
    st.write("xyY:", xyY)

    st.write("Munsell:", munsell)
