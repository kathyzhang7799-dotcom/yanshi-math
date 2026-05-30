import streamlit as st

# =========================================================================
# 1. 網頁全域配置
# =========================================================================
st.set_page_config(page_title="THE MATRIX: CORE V8 (DEMO)", page_icon="⚡", layout="wide")

# =========================================================================
# 2. 初始化核心狀態機
# =========================================================================
if "hacked" not in st.session_state:
    st.session_state.hacked = False

# =========================================================================
# 3. 黑客帝國基礎視覺風格（全網頁綠字黑底）
# =========================================================================
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
    </style>
""", unsafe_allow_html=True)

# 攔截點擊事件
def trigger_purchase_wall():
    st.session_state.hacked = True
    st.rerun()

# =========================================================================
# 4. 核心分流控制（安全熔斷機制）
# =========================================================================
if st.session_state.hacked:
    # --- 【付費狀態】：清空原本的主介面，乾淨地單獨渲染付費牆 ---
    st.markdown("<h1 style='text-align: center; color: #FF0000 !important; text-shadow: 0 0 10px #FF0000; font-size: 40px;'>🚨 ACCESS DENIED 🚨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #00FF00 !important; font-size: 18px;'>TRIAL LICENSE EXPIRED. FULL CORE FUNCTIONS LOCKED.</p>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00FF00 !important; border-bottom: 1px solid #00FF00; padding-bottom: 10px;'>⚡ CHOOSE YOUR ARCHITECT PLAN ⚡</h3>", unsafe_allow_html=True)
    
    # 使用 Streamlit 的欄位佈局，排版更安全，絕對不穿幫
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style="border:2px solid #00FF00; background:rgba(0,30,0,0.6); padding:25px; border-radius:10px; min-height: 250px;">
                <h3 style="color:#FFFF00 !important; margin:0;">💡 LITE CORE</h3>
                <h2 style="color:#00FF00 !important; font-size:36px; margin:10px 0;">$2.00 <span style="font-size:16px;">USD</span></h2>
                <p style="color:#00FF00 !important; font-size:14px; line-height:1.6;">
                    • Full Web Interface Access<br>
                    • Personal Secure Account<br>
                    • Standard Computing Speed
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style="border:2px solid #FF0000; background:rgba(30,0,0,0.6); padding:25px; border-radius:10px; min-height: 250px;">
                <h3 style="color:#FF3333 !important; margin:0;">🔥 ELITE ARCHITECT</h3>
                <h2 style="color:#FF0000 !important; font-size:36px; margin:10px 0;">$4.00 <span style="font-size:16px;">USD</span></h2>
                <p style="color:#FF0000 !important; font-size:14px; line-height:1.6;">
                    • Full Web Interface Access<br>
                    • Personal Secure Account<br>
                    • <strong style="color:#FFFF00 !important;">COMPLETE PYTHON SOURCE CODE</strong><br>
                    • Lifetime Developer Support
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><p style='text-align: center; color: #FFFF00 !important; font-weight: bold; font-size: 16px;'>>>> SYSTEM PROMPT: PLEASE CONTACT DEVELOPER (HARRY) TO INITIATE TRANSACTION <<<</p>", unsafe_allow_html=True)
    
    # 後門管理按鈕
    st.markdown("---")
    if st.button("🔄 RESET SYSTEM (ADMIN ONLY)"):
        st.session_state.hacked = False
        st.rerun()

else:
    # --- 【未付費狀態】：正常顯示選單與輸入框 ---
    
    # 側邊欄選單
    menu = st.sidebar.selectbox("請選擇模組功能 (SYSTEM MENU):", [
        "1. Addition Mode", "2. Subtraction Mode", "3. Multiplication Mode", "4. Division Mode",
        "5. Advanced Formulas Selection", "6. Multi-functional Data Charts", "7. Perimeter Formulas Module",
        "8. Hexadecimal ASCII Cipher Encryption", "9. Hexadecimal ASCII Cipher Decryption"
    ])
    st.sidebar.markdown("---")
    st.sidebar.error("🔴 LICENSE STATUS: UNLICENSED")
    
    st.title("⚡ THE MATRIX: LOGIC SOURCE CORE V8")
    st.write("Welcome to the Ultimate Math Engine Web Interface. STATUS: [TRIAL MODE]")

    # 模組外殼判斷
    if menu == "1. Addition Mode":
        st.subheader("➕ [Addition Mode]")
        st.text_input("Enter 1st addend:")
        st.text_input("Enter 2nd addend:")
        if st.button("EXECUTE ADDITION"): trigger_purchase_wall()

    elif menu == "2. Subtraction Mode":
        st.subheader("➖ [Subtraction Mode]")
        st.text_input("Enter minuend:")
        st.text_input("Enter subtrahend:")
        if st.button("EXECUTE SUBTRACTION"): trigger_purchase_wall()

    elif menu == "3. Multiplication Mode":
        st.subheader("✖️ [Multiplication Mode]")
        st.text_input("Enter 1st factor:")
        st.text_input("Enter 2nd factor:")
        if st.button("EXECUTE MULTIPLICATION"): trigger_purchase_wall()

    elif menu == "4. Division Mode":
        st.subheader("➗ [Division Mode]")
        st.text_input("Enter dividend:")
        st.text_input("Enter divisor:")
        if st.button("EXECUTE DIVISION"): trigger_purchase_wall()

    elif menu == "5. Advanced Formulas Selection":
        st.subheader("🧠 [Advanced Formulas Menu]")
        adv_choice = st.selectbox("Select an advanced formula:", [
            "1. Quadratic Equation Root Solver", "2. Perfect Square Expansion", 
            "3. Pythagorean Theorem Unknown Side", "4. Area Formulas Core", "5. Volume Formulas Core"
        ])
        st.text_input("Parameter A:")
        st.text_input("Parameter B:")
        if st.button("CALCULATE FORMULA"): trigger_purchase_wall()

    elif menu == "6. Multi-functional Data Charts":
        st.subheader("📚 [Data Reference Charts]")
        st.selectbox("Select Database Chart:", ["1. Multiplication Table", "2. Prime Numbers Chart"])
        if st.button("LOAD DATABASE CHART"): trigger_purchase_wall()

    elif menu == "7. Perimeter Formulas Module":
        st.subheader("📏 [Perimeter Calculation Mode]")
        st.text_input("Enter dimension data:")
        if st.button("CALCULATE PERIMETER"): trigger_purchase_wall()

    elif menu == "8. Hexadecimal ASCII Cipher Encryption":
        st.subheader("🔒 [Hexadecimal ASCII Cipher Encryption]")
        st.text_input("Enter plaintext:")
        if st.button("RUN ENCRYPTION MODULE"): trigger_purchase_wall()

    elif menu == "9. Hexadecimal ASCII Cipher Decryption":
        st.subheader("🔓 [Hexadecimal ASCII Cipher Decryption]")
        st.text_input("Enter ciphertext:")
        if st.button("RUN DECRYPTION MODULE"): trigger_purchase_wall()
