import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sales Excellence Suite", page_icon="📈", layout="wide")

# --- 1. INITIALIZATION ---
if 'all_history' not in st.session_state:
    st.session_state.all_history = []
if 'menu' not in st.session_state:
    st.session_state.menu = "Main"
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'q_count' not in st.session_state:
    st.session_state.q_count = 1
if 'final_level' not in st.session_state:
    st.session_state.final_level = None

# Sidebar Reset
if st.sidebar.button("🗑️ Reset All & Back to Menu"):
    st.session_state.clear()
    st.rerun()

# --- 2. STYLES ---
st.markdown("""<style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #2E7D32; color: white; font-weight: bold; }
    .gate-box { background-color: #000000 !important; padding: 25px; border-radius: 8px; border: 2px solid #555; text-align: center; }
    .gate-title { color: #ffffff !important; font-weight: bold; font-size: 1.4em; display: block; margin-bottom: 10px; }
    .gate-question { color: #ffffff !important; font-weight: 800; font-size: 1.6em; }
    .criteria-box { background-color: #f1f3f5 !important; padding: 20px; border-radius: 10px; border-left: 8px solid #2E7D32; margin-bottom: 20px; }
    .criteria-text { color: #000000 !important; font-weight: bold; font-size: 1.2em; display: block; margin-bottom: 10px; }
    .criteria-question { color: #000000 !important; font-weight: 800; font-size: 1.5em; }
    .question-number { color: #555; font-weight: bold; font-size: 1.1em; }
    </style>""", unsafe_allow_html=True)

# --- 3. MAIN MENU ---
if st.session_state.menu == "Main":
    st.title("🏆 Tier 1 Sales Competencies Assessment Suite")
    # Definimos las 5 columnas correctamente
    c1, c2, c3, c4, c5 = st.columns(5)
    if c1.button("📦 Product Knowledge"): st.session_state.menu = "Product Knowledge"; st.rerun()
    if c2.button("🤝 Deal Progression, Negotiation & Closing"): st.session_state.menu = "Deal"; st.rerun()
    if c3.button("🔍 Prospecting & Lead Management"): st.session_state.menu = "Prospecting"; st.rerun()
    if c4.button("💡 Insight Selling"): st.session_state.menu = "Insight"; st.rerun()
    if c5.button("🧠 Adaptability & Learning Agility"): st.session_state.menu = "Adaptability"; st.rerun()
    
    if st.session_state.all_history:
        st.divider()
        st.subheader("📜 Historical Records")
        st.table(pd.DataFrame(st.session_state.all_history))

# --- 4. ASSESSMENT FLOW ---
else:
    assessment_type = st.session_state.menu
    st.title(f"🎯 {assessment_type} Assessment")
    c1, c2 = st.columns(2)
    rep_name = c1.text_input("Representative Name:")
    manager_name = c2.text_input("Manager Name:")

    if rep_name and manager_name:
        if st.session_state.final_level is None:
            st.divider()
            step = st.session_state.step
            st.markdown(f"<div class='question-number'>Question #{st.session_state.q_count}</div>", unsafe_allow_html=True)

            # ==========================================
            # 📦 PRODUCT KNOWLEDGE
            # ==========================================
            if assessment_type == "Product Knowledge":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Can the seller successfully address complex, cross-product functionality questions AND actively neutralize a key competitor during a pitch without your support?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Explains 2-way sync and API limitations.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Submitted 3+ product feedback requests.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Is the seller a recognized SME who trains others AND predicts market trends?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Initiates feedback that led to a measurable improvement.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Acts as team´s lead trainer on competitive product strategy.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="p6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller consistently and independently address basic product questions AND effectively utilize their knowledge to pre-empt technical objections?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Never escalates basic product queries.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Proactively addresses technical concerns before they become objections.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="p9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller meet basic expectations by having fewer than one incorrect product fit error per month AND knowing the main function of all core products?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Error rate is negligible for standard deals.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Clearly defines the purpose of core products (e.g., Channel Manager).</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="p12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🤝 DEAL PROGRESSION & NEGOTIATION
            # ==========================================
            elif assessment_type == "Deal":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller successfully traded a discount for a valuable concession AND proactively pre-empted the top competitive objections in the middle of the sales cycle?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Never gives a discount without getting something measurable in return (e.g., reference, faster close). </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Addresses common competitor FUD (Fear, Uncertainty, Doubt) before the customer asks.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller successfully closed a high-value deal without any permanent discount AND advised leadership on pricing strategy based on market feedback?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Closed a deal $X+ above the permanent discount baseline.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text"> 2. Provided data-backed recommendations on improving pricing/terms strategy.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="d6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Has the seller successfully accelerated a stalled deal AND achieved a win-win outcome by creatively reframing terms?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Saved a deal that was stuck for 30+ days.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Found a non-price solution to a key customer objection.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="d9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller consistently establish a clear, agreed-upon next step on all active deals AND demonstrate competence in handling basic objections?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Every conversation ends with a confirmed action and date from the customer.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="d11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Can neutralize "too expensive" or "send me an email" without escalation.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="d12n"): st.session_state.final_level = "L1"; st.rerun()                 
            # ==========================================
            # 🔍 PROSPECTING & LEAD MANAGEMENT
            # ==========================================
            elif assessment_type == "Prospecting":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Do they efficiently manage MQLs AND does their pipeline come primarily from proactive outbound prospecting  that includes discovering new, viable segments?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. MQLs processed faster than peers.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Found a new target group team was missing.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller pioneered a new lead generation channel/strategy AND can they accurately predict the conversion rate of leads from new sources?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Implemented a unique, team-scalable prospecting channel (e.g., custom LinkedIn strategy)</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Forecasts the success of new channels based on market intelligence.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="p6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller consistently process MQLs within the target SLA AND successfully use non-traditional channels (e.g., social) to source high-quality leads?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Zero overdue MQLs month-over-month.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Secured 2+ high-quality leads from an outbound social strategy this quarter.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="p9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller consistently meet minimum daily/weekly activity targets AND consistently close MQLs within the target follow-up SLA?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Meets all activity KPIs (calls, emails, meetings).</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="p11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Never lets inbound leads go cold due to follow-up delay.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="p12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="p12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 💡 INSIGHT SELLING
            # ==========================================
            elif assessment_type == "Insight":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller successfully used third-party information/insight/data to highlight an unforeseen problem AND used their product knowledge to pivot the discovery to that new pain point?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Introduced external insight/information./data that challenged the customer self-diagnosis.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Successfully changed the agenda mid-call based on new insights.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller successfully used a provocative question to challenge a customer´s faulty assumption AND architected a complex, multi-product solution based purely on deep discovery?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Asked a question that forced the prospect to rethink their entire strategy.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Created a solution involving 3+ SiteMinder products/integrations based on discovery.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="i6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Has the seller successfully identified the customer´s underlying emotional motivation AND gotten them to quantify the financial cost of their current challenge?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Identified why the individual stakeholder cares about the problem </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Customer verbally confirmed dollar value of pain.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="i9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller ask open-ended questions that uncover basic needs AND can they connect an identified pain point to the relevant SiteMinder product?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Customer does most of the talking during discovery.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="i11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Accurately links a stated problem (e.g., manual updates) to a core product (e.g., Channel Manager)</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="i12n"): st.session_state.final_level = "L1"; st.rerun()


            # ==========================================
            # 🧠 ADAPTABILITY & LEARNING AGILITY
            # ==========================================
            elif assessment_type == "Adaptability":
                # --- GATE L3/L4 ---
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller acted as a catalyst for change helping peers adopt new tools, AND do they proactively develop skills to meet future needs?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Is the first to master and promote a new tool or process.</span><span class="criteria-question">Meet criterion?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Enrolls in training or dedicates time to skills relevant to next year´s strategy.</span><span class="criteria-question">Meet criterion?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a3n"): st.session_state.final_level = "L3"; st.rerun()

                # --- GATE L4/L5 ---
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller driven innovation by overhauling a team process based on their own learning  AND are they involved in designing the team´s future learning curriculum?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. The overhaul resulted in a permanent, positive change to team workflow.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Provides input to management on what skills the team should prioritize next.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="a6n"): st.session_state.final_level = "L4"; st.rerun()

                # --- GATE L2/L3 ---
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller proactively seek out new information without being prompted AND have they successfully pivoted their sales strategy in response to a market shift?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Consumes training/content that is not mandatory. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Successfully changed pitch/segment focus due to a trend (e.g., competitor move).</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="a9n"): st.session_state.final_level = "L2"; st.rerun()

                # --- GATE L1/L2 ---
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller quickly adapt to new required processes  AND successfully apply a new methodology learned in training to a live call?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Implements a new rule/process change within the first week. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2 Can be observed using a new selling technique or showcasing new products  immediately after training.</span><span class="criteria-question">Meet final?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="a12n"): st.session_state.final_level = "L1"; st.rerun()




                      # --- 5. FINAL RESULTS PAGE ---
        else:
            st.balloons()
            st.success("### 🏁 Assessment Complete!")
            
            # Create the record
            new_record = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Representative": rep_name,
                "Manager": manager_name,
                "Competency": assessment_type,
                "Level": st.session_state.final_level
            }

            # Display highlighted result
            col_res, col_extra = st.columns(2)
            with col_res:
                st.metric(label="Final Level Achieved", value=st.session_state.final_level)
            
            # Save to history only once
            if not st.session_state.all_history or st.session_state.all_history[-1] != new_record:
                st.session_state.all_history.append(new_record)

            st.divider()
            
            # UNIQUE BUTTON TO RETURN
            if st.button("💾 Save Result & Return to Main Menu", use_container_width=True):
                st.session_state.step = 1
                st.session_state.q_count = 1
                st.session_state.final_level = None
                st.session_state.menu = "Main"
                st.rerun()
