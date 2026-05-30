import streamlit as st
from fractions import Fraction
import math
import time

# --- 1. 網頁全域配置與黑客帝國數位雨特效注入 ---
st.set_page_config(page_title="THE MATRIX: CORE V8 (DEMO)", page_icon="⚡", layout="wide")

st.markdown("""
    <canvas id="matrix-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    const katakana = "ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901";
    const fontSize = 16;
    let columns = canvas.width / fontSize;
    const rainDrops = Array(Math.floor(columns)).fill(1);
    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#00FF00';
        ctx.font = fontSize + 'px monospace';
        for (let i = 0; i < rainDrops.length; i++) {
            const text = katakana.charAt(Math.floor(Math.random() * katakana.length));
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
            if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) rainDrops[i] = 0;
            rainDrops[i]++;
        }
    }
    setInterval(draw, 30);
    </script>
    <style>
    .stApp { background: transparent; }
    .main .block-container { background-color: rgba(0, 0, 0, 0.85); border: 1px solid #00FF00; border-radius: 15px; padding: 2.5rem; }
    h1, h2, h3, label, p, span, div { color: #00FF00 !important; font-family: 'Courier New', monospace; }
    div.stButton > button { background: #000; color: #0F0; border: 1px solid #0F0; width: 100%; font-weight: bold; }
    div.stButton > button:hover { background: #FF0000; color: #000; border: 1px solid #FF0000; }
    .stTextInput>div>div>input { background-color: rgba(0,0,0,0.7) !important; color: #00FF00 !important; border: 1px solid #00FF00 !important; }
    .stSelectbox>div>div>div { background-color: rgba(0,0,0,0.7) !important; color: #00FF00 !important; border: 1px solid #00FF00 !important; }
    .stRadio>div { color: #00FF00 !important; }
    div[data-testid="stCodeBlock"] { border: 1px solid #00FF00; background-color: rgba(0,0,0,0.9); }
    </style>
""", unsafe_allow_html=True)

# --- 2. 核心整人攔截特效 ---
def trigger_purchase_wall():
    # 模擬高大上的算力連線動畫，增強欺騙感
    with st.spinner("⚡ CONNECTING TO QUANTUM SOURCE CORE..."):
        time.sleep(0.7)
    
    # 震撼錯誤提示
    st.error("🚨 [SYSTEM ERROR]: MODULE ENCRYPTION DETECTED.")
    st.error("❌ PLEASE PURCHASE APP TO UNLOCK FULL CORE FUNCTIONS.")
    
    # 指引向你付費
    st.warning("⚠️ TRIAL LICENSE EXPIRED. PLEASE CONTACT DEVELOPER (HARRY) FOR ARCHITECT KEY.")
    
    # 右下角連續噴出拒絕彈窗
    st.toast('ACCESS DENIED: Core Functions Locked.', icon='❌')

# --- 3. 主系統介面 ---
st.title("⚡ THE MATRIX: LOGIC SOURCE CORE V8")
st.write("Welcome to the Ultimate Math Engine Web Interface. STATUS: [TRIAL MODE]")

# 側邊欄系統主選單（完整保留你的 9 大功能選項）
menu = st.sidebar.selectbox("請選擇模組功能 (SYSTEM MENU):", [
    "1. Addition Mode",
    "2. Subtraction Mode",
    "3. Multiplication Mode",
    "4. Division Mode",
    "5. Advanced Formulas Selection",
    "6. Multi-functional Data Charts",
    "7. Perimeter Formulas Module",
    "8. Hexadecimal ASCII Cipher Encryption",
    "9. Hexadecimal ASCII Cipher Decryption"
])

st.sidebar.markdown("---")
st.sidebar.error("🔴 LICENSE STATUS: UNLICENSED")
st.sidebar.write("Core Engine: RESTRICTED")

# --- 4. 模組核心邏輯還原（點擊全部攔截） ---

if menu == "1. Addition Mode":
    st.subheader("➕ [Addition Mode]")
    st.text_input("Enter 1st addend:")
    st.text_input("Enter 2nd addend:")
    if st.button("EXECUTE ADDITION"):
        trigger_purchase_wall()

elif menu == "2. Subtraction Mode":
    st.subheader("➖ [Subtraction Mode]")
    st.text_input("Enter minuend:")
    st.text_input("Enter subtrahend:")
    if st.button("EXECUTE SUBTRACTION"):
        trigger_purchase_wall()

elif menu == "3. Multiplication Mode":
    st.subheader("✖️ [Multiplication Mode]")
    st.text_input("Enter 1st factor:")
    st.text_input("Enter 2nd factor:")
    if st.button("EXECUTE MULTIPLICATION"):
        trigger_purchase_wall()

elif menu == "4. Division Mode":
    st.subheader("➗ [Division Mode]")
    st.text_input("Enter dividend:")
    st.text_input("Enter divisor:")
    if st.button("EXECUTE DIVISION"):
        trigger_purchase_wall()

elif menu == "5. Advanced Formulas Selection":
    st.subheader("🧠 [Advanced Formulas Menu]")
    adv_choice = st.selectbox("Select an advanced formula:", [
        "1. Quadratic Equation Root Solver",
        "2. Perfect Square Expansion",
        "3. Pythagorean Theorem Unknown Side",
        "4. Area Formulas Core",
        "5. Volume Formulas Core"
    ])
    
    if adv_choice == "1. Quadratic Equation Root Solver":
        st.markdown("#### Quadratic Equation Solver (ax² + bx + c = 0)")
        st.text_input("Enter a:")
        st.text_input("Enter b:")
        st.text_input("Enter c:")
        if st.button("SOLVE QUADRATIC"):
            trigger_purchase_wall()

    elif adv_choice == "2. Perfect Square Expansion":
        st.markdown("#### Perfect Square Expansion (a²+2ab+b²)")
        st.text_input("Enter expression 'a':")
        st.text_input("Enter expression 'b':")
        if st.button("EXPAND EXPRESSION"):
            trigger_purchase_wall()

    elif adv_choice == "3. Pythagorean Theorem Unknown Side":
        st.markdown("#### Pythagorean Theorem Solver")
        st.radio("What do you want to solve for?", ["Hypotenuse (求斜邊)", "Leg Side (求直角邊)"])
        st.text_input("Enter 1st known side:")
        st.text_input("Enter 2nd known side:")
        if st.button("CALCULATE PYTHAGOREAN"):
            trigger_purchase_wall()

    elif adv_choice == "4. Area Formulas Core":
        st.markdown("#### [Area Calculation Mode]")
        shape = st.selectbox("Please select a shape:", ["1. Rectangle / Square Area", "2. Triangle Area", "3. Circle Area"])
        if shape == "1. Rectangle / Square Area":
            st.text_input("Enter length:")
            st.text_input("Enter width:")
        elif shape == "2. Triangle Area":
            st.text_input("Enter base length:")
            st.text_input("Enter height:")
        elif shape == "3. Circle Area":
            st.text_input("Enter radius:")
        if st.button("CALCULATE AREA"):
            trigger_purchase_wall()

    elif adv_choice == "5. Volume Formulas Core":
        st.markdown("#### [Volume Calculation Mode]")
        v_shape = st.selectbox("Please select a formula:", ["1. Cube / Rectangular Prism Volume", "2. Cylinder Volume", "3. Cone Volume"])
        st.text_input("Enter dimension parameter 1:")
        st.text_input("Enter dimension parameter 2:")
        if st.button("CALCULATE VOLUME"):
            trigger_purchase_wall()

elif menu == "6. Multi-functional Data Charts":
    st.subheader("📚 [Data Reference Charts]")
    chart_choice = st.selectbox("Select Database Chart:", [
        "1. Multiplication Table",
        "2. Prime Numbers Chart (under 1000)",
        "3. Squares Table (under 1000)",
        "4. Common Pythagorean Triples"
    ])
    st.info(">>> Demo Version: Requesting secure database synchronization...")
    if st.button("LOAD DATABASE CHART"):
        trigger_purchase_wall()

elif menu == "7. Perimeter Formulas Module":
    st.subheader("📏 [Perimeter Calculation Mode]")
    p_shape = st.selectbox("Select Perimeter Sub-module:", [
        "1. Rectangle Perimeter",
        "2. Triangle Perimeter",
        "3. Circle Circumference",
        "4. General Quadrilateral Perimeter"
    ])
    st.text_input("Enter side / radius data 1:")
    st.text_input("Enter side data 2:")
    if st.button("CALCULATE PERIMETER"):
        trigger_purchase_wall()

elif menu == "8. Hexadecimal ASCII Cipher Encryption":
    st.subheader("🔒 [Hexadecimal ASCII Cipher Encryption]")
    st.text_input("Enter plaintext to encrypt:")
    if st.button("RUN ENCRYPTION MODULE"):
        trigger_purchase_wall()

elif menu == "9. Hexadecimal ASCII Cipher Decryption":
    st.subheader("🔓 [Hexadecimal ASCII Cipher Decryption]")
    st.text_input("Enter ciphertext to decrypt:")
    if st.button("RUN DECRYPTION MODULE"):
        trigger_purchase_wall()
