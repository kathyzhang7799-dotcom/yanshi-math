import streamlit as st
import time

# --- 1. 網頁全域配置 ---
st.set_page_config(page_title="THE MATRIX: CORE V8 (DEMO)", page_icon="⚡", layout="wide")

# 初始化攔截狀態
if "hacked" not in st.session_state:
    st.session_state.hacked = False

# --- 2. 核心終極攔截：一旦觸發付費，直接劫持，完全不渲染後續的側邊欄和主介面 ---
if st.session_state.hacked:
    # 注入全螢幕超高密度程式碼流 HTML + 賽博付費彈窗
    st.markdown("""
        <div style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:black; z-index:99999; overflow:hidden; font-family:'Courier New', monospace; padding:20px;">
            <canvas id="fullscreen-matrix" style="position:absolute; top:0; left:0; width:100%; height:100%; opacity:0.4;"></canvas>
            
            <div style="position:relative; max-width:700px; margin: 8% auto; background:rgba(0, 15, 0, 0.9); border:3px solid #00FF00; box-shadow: 0 0 30px #00FF00; border-radius:15px; padding:40px; text-align:center;">
                <h1 style="color:#FF0000; font-size:32px; letter-spacing:3px; margin-bottom:5px; text-shadow: 0 0 10px #FF0000;">🚨 ACCESS DENIED 🚨</h1>
                <p style="color:#00FF00; font-size:16px; margin-bottom:30px;">TRIAL LICENSE EXPIRED. FULL CORE FUNCTIONS LOCKED.</p>
                
                <h2 style="color:#00FF00; font-size:20px; border-bottom:1px solid #00FF00; padding-bottom:10px; margin-bottom:25px;">⚡ CHOOSE YOUR ARCHITECT PLAN ⚡</h2>
                
                <div style="display:flex; gap:20px; justify-content:center; margin-bottom:30px;">
                    <div style="flex:1; border:2px solid #00FF00; background:rgba(0,30,0,0.5); padding:20px; border-radius:10px; box-shadow: 0 0 10px rgba(0,255,0,0.3);">
                        <h3 style="color:#FFFF00; font-size:22px; margin:0;">💡 LITE CORE</h3>
                        <p style="color:#00FF00; font-size:28px; font-weight:bold; margin:10px 0;">$2.00 <span style="font-size:14px; font-weight:normal;">USD</span></p>
                        <ul style="color:#00FF00; text-align:left; font-size:13px; padding-left:15px; line-height:1.6;">
                            <li>Full Web Interface Access</li>
                            <li>Personal Secure Account</li>
                            <li>Standard Computing Speed</li>
                        </ul>
                    </div>
                    
                    <div style="flex:1; border:2px solid #FF0000; background:rgba(30,0,0,0.5); padding:20px; border-radius:10px; box-shadow: 0 0 15px rgba(255,0,0,0.4);">
                        <h3 style="color:#FF3333; font-size:22px; margin:0;">🔥 ELITE ARCHITECT</h3>
                        <p style="color:#FF0000; font-size:28px; font-weight:bold; margin:10px 0;">$4.00 <span style="font-size:14px; font-weight:normal; color:#FF0000;">USD</span></p>
                        <ul style="color:#FF0000; text-align:left; font-size:13px; padding-left:15px; line-height:1.6;">
                            <li>Full Web Interface Access</li>
                            <li>Personal Secure Account</li>
                            <li><strong style="color:#FFFF00;">COMPLETE PYTHON SOURCE CODE</strong></li>
                            <li>Lifetime Developer Support</li>
                        </ul>
                    </div>
                </div>
                
                <p style="color:#FFFF00; font-size:14px; margin-bottom:5px; font-weight:bold;">>>> SYSTEM PROMPT: PLEASE CONTACT DEVELOPER (HARRY) TO INITIATE TRANSACTION <<<</p>
                <p style="color:#00FF00; font-size:11px; opacity:0.6;">Securely encrypted via Hexadecimal ASCII Logic Engine.</p>
            </div>
        </div>

        <script>
        const fCanvas = document.getElementById('fullscreen-matrix');
        const fCtx = fCanvas.getContext('2d');
        fCanvas.width = window.innerWidth; fCanvas.height = window.innerHeight;
        const binStr = "0101011001010111011010010111001101101001011011110110111000111000";
        const fFontSize = 14;
        let fColumns = fCanvas.width / fFontSize;
        const fDrops = Array(Math.floor(fColumns)).fill(1);
        function drawFull() {
            fCtx.fillStyle = 'rgba(0, 0, 0, 0.08)';
            fCtx.fillRect(0, 0, fCanvas.width, fCanvas.height);
            fCtx.fillStyle = '#00FF00';
            fCtx.font = fFontSize + 'px monospace';
            for (let i = 0; i < fDrops.length; i++) {
                const text = binStr.charAt(Math.floor(Math.random() * binStr.length));
                fCtx.fillText(text, i * fFontSize, fDrops[i] * fFontSize);
                if (fDrops[i] * fFontSize > fCanvas.height && Math.random() > 0.98) fDrops[i] = 0;
                fDrops[i]++;
            }
        }
        setInterval(drawFull, 25);
        </script>
    """, unsafe_allow_html=True)
    
    # 依然保留你的後門重設按鈕（只有你知道在最底下可以點擊重設）
    if st.button("🔄 RESET SYSTEM (ADMIN ONLY)"):
        st.session_state.hacked = False
        st.rerun()
        
    # 關鍵：直接用 st.stop() 強制終止！後面的側邊欄、主選單連畫出來的機會都沒有
    st.stop()


# --- 3. 基礎黑客背景特效（未付費前正常顯示） ---
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

def trigger_purchase_wall():
    st.session_state.hacked = True
    st.rerun()

# --- 4. 正常主介面（只在 hacked == False 時才會執行到這裡） ---
st.title("⚡ THE MATRIX: LOGIC SOURCE CORE V8")
st.write("Welcome to the Ultimate Math Engine Web Interface. STATUS: [TRIAL MODE]")

menu = st.sidebar.selectbox("請選擇模組功能 (SYSTEM MENU):", [
    "1. Addition Mode", "2. Subtraction Mode", "3. Multiplication Mode", "4. Division Mode",
    "5. Advanced Formulas Selection", "6. Multi-functional Data Charts", "7. Perimeter Formulas Module",
    "8. Hexadecimal ASCII Cipher Encryption", "9. Hexadecimal ASCII Cipher Decryption"
])

# 以下為各個模組的空殼輸入框
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
