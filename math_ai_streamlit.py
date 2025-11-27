import streamlit as st
from sympy import symbols, Eq, solve, sympify

# إعداد الصفحة
st.set_page_config(page_title="Math AI – المساعد الرياضي الذكي", layout="centered")

# CSS لتحسين الواجهة
st.markdown("""
<style>
.stApp {
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)),
                      url("https://images.unsplash.com/photo-1603791440384-56cd371ee9a7?auto=format&fit=crop&w=1050&q=80");
    background-size: cover;
    background-attachment: fixed;
    color: white;
    font-family: Arial, sans-serif;
}
.stTextInput>div>div>input {
    background: rgba(255,255,255,0.95);
    color: black;
    font-size: 1.2em;
    padding: 0.5em;
    border-radius: 5px;
    border: 1px solid #ccc;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    height: 3em;
    width: 100%;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    font-size: 1.2em;
}
.stAlert {
    background-color: rgba(0,0,0,0.6) !important;
    color: #FFD700 !important;
    font-size: 1.4em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# عنوان البرنامج
st.title("Math AI – المساعد الرياضي الذكي 🧮")
st.markdown("اكتب أي عملية حسابية أو معادلة بسيطة، وسيقوم البرنامج بحلها وشرح الناتج.")

# سجل العمليات السابقة
if 'history' not in st.session_state:
    st.session_state.history = []

# إدخال المسألة أو العملية
user_input = st.text_input("اكتب المسألة أو المعادلة هنا:")

if user_input:
    x = symbols('x')  # رمز متغير واحد للمعادلات
    try:
        expr = sympify(user_input)

        if '=' in user_input:
            lhs, rhs = user_input.split('=')
            equation = Eq(sympify(lhs), sympify(rhs))
            solution = solve(equation, x)
            st.success(f"✅ حل المعادلة: {solution}")
            st.info("البرنامج حل المعادلة خطوة بخطوة (إذا كانت معادلة بسيطة).")
            st.session_state.history.append(f"{user_input} => {solution}")
        else:
            result = expr.evalf()
            st.success(f"✅ الناتج: {result}")
            st.info("العملية الحسابية تمت بنجاح.")
            st.session_state.history.append(f"{user_input} = {result}")
    except Exception as e:
        st.error(f"❌ خطأ في المسألة: {e}")

# عرض سجل العمليات
if st.session_state.history:
    st.subheader("📜 سجل العمليات السابقة")
    for idx, item in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{idx}. {item}")

# أزرار التحكم
col_reset, col_clear = st.columns(2)
if col_reset.button("🔄 إعادة تعيين الإدخال"):
    st.experimental_rerun()
if col_clear.button("🗑️ مسح سجل النتائج"):
    st.session_state.history = []
    st.experimental_rerun()
