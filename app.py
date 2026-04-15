import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sales Excellence Suite", page_icon="📈", layout="wide")

# --- 1. INITIALIZATION ---
if "all_history" not in st.session_state:
    st.session_state.all_history = []
if "selected_tier" not in st.session_state:
    st.session_state.selected_tier = None
if "menu" not in st.session_state:
    st.session_state.menu = "Main"
if "step" not in st.session_state:
    st.session_state.step = 1
if "q_count" not in st.session_state:
    st.session_state.q_count = 1
if "final_level" not in st.session_state:
    st.session_state.final_level = None

# Sidebar Reset
if st.sidebar.button("🗑️ Reset All & Back to Start"):
    st.session_state.clear()
    st.rerun()

# --- 2. STYLES ---
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        max-width: 420px;
        border-radius: 10px;
        min-height: 4.2em;
        height: auto;
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        white-space: normal !important;
        word-wrap: break-word;
        padding: 0.85rem 1rem;
        line-height: 1.3;
        font-size: 1rem;
        text-align: left;
        justify-content: flex-start;
    }

    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .gate-box {
        background-color: #000000 !important;
        padding: 25px;
        border-radius: 8px;
        border: 2px solid #555;
        text-align: center;
    }

    .gate-title {
        color: #ffffff !important;
        font-weight: bold;
        font-size: 1.4em;
        display: block;
        margin-bottom: 10px;
    }

    .gate-question {
        color: #ffffff !important;
        font-weight: 800;
        font-size: 1.6em;
    }

    .criteria-box {
        background-color: #f1f3f5 !important;
        padding: 20px;
        border-radius: 10px;
        border-left: 8px solid #2E7D32;
        margin-bottom: 20px;
    }

    .criteria-text {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.2em;
        display: block;
        margin-bottom: 10px;
    }

    .criteria-question {
        color: #000000 !important;
        font-weight: 800;
        font-size: 1.5em;
    }

    .question-number {
        color: #555;
        font-weight: bold;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. MAIN MENU / TIER SELECTOR ---
if st.session_state.menu == "Main":

    # =========================
    # TIER SELECTOR
    # =========================
    if st.session_state.selected_tier is None:
        st.markdown("<div class='main-title'>🏆 Sales Competency Assessment Suite</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Select a competency tier to begin</div>", unsafe_allow_html=True)

        left, center, right = st.columns([1, 8, 1])

        with center:
            c1, c2, c3 = st.columns(3)

            if c1.button("🥇 Tier 1\nCore Selling Competencies", use_container_width=True):
                st.session_state.selected_tier = "Tier 1"
                st.rerun()

            if c2.button("🥈 Tier 2\nAdvanced Selling Competencies", use_container_width=True):
                st.session_state.selected_tier = "Tier 2"
                st.rerun()

            if c3.button("🥉 Tier 3\nOperational & Team Competencies", use_container_width=True):
                st.session_state.selected_tier = "Tier 3"
                st.rerun()

        if st.session_state.all_history:
            st.divider()
            st.subheader("📜 Historical Records")
            st.table(pd.DataFrame(st.session_state.all_history))

    # =========================
    # TIER 1 MENU
    # =========================
    elif st.session_state.selected_tier == "Tier 1":
        st.title("🏆 Tier 1 Sales Competencies Assessment Suite")

        back_col, _ = st.columns([1, 5])
        with back_col:
            if st.button("⬅️ Back to Tier Selector"):
                st.session_state.selected_tier = None
                st.rerun()

        st.markdown("### Select a competency")

        if st.button("📦 Product Knowledge"):
            st.session_state.menu = "Product Knowledge"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🤝 Deal Progression, Negotiation & Closing"):
            st.session_state.menu = "Deal"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🔍 Prospecting & Lead Management"):
            st.session_state.menu = "Prospecting"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("💡 Insight Selling"):
            st.session_state.menu = "Insight"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🧠 Adaptability & Learning Agility"):
            st.session_state.menu = "Adaptability"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.session_state.all_history:
            st.divider()
            st.subheader("📜 Historical Records")
            st.table(pd.DataFrame(st.session_state.all_history))

    # =========================
    # TIER 2 MENU
    # =========================
    elif st.session_state.selected_tier == "Tier 2":
        st.title("🥈 Tier 2 Sales Competencies Assessment Suite")

        back_col, _ = st.columns([1, 5])
        with back_col:
            if st.button("⬅️ Back to Tier Selector"):
                st.session_state.selected_tier = None
                st.rerun()

        st.markdown("### Select a competency")

        if st.button("🌍 Market Knowledge"):
            st.session_state.menu = "Market Knowledge"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("💬 SiteMinder Platform Value Proposition"):
            st.session_state.menu = "SiteMinder Platform Value Proposition"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🎥 Product Demonstration"):
            st.session_state.menu = "Product Demonstration"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("⏱️ Self-Management & Productivity"):
            st.session_state.menu = "Self-Management & Productivity"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("📈 Pipeline & Forecast Management"):
            st.session_state.menu = "Pipeline & Forecast Management"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.session_state.all_history:
            st.divider()
            st.subheader("📜 Historical Records")
            st.table(pd.DataFrame(st.session_state.all_history))

    # =========================
    # TIER 3 MENU
    # =========================
    elif st.session_state.selected_tier == "Tier 3":
        st.title("🥉 Tier 3 Sales Competencies Assessment Suite")

        back_col, _ = st.columns([1, 5])
        with back_col:
            if st.button("⬅️ Back to Tier Selector"):
                st.session_state.selected_tier = None
                st.rerun()

        st.markdown("### Select a competency")

        if st.button("🗺️ Market Management"):
            st.session_state.menu = "Market Management"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🤝 Onboarding & Handover Process"):
            st.session_state.menu = "Onboarding & Handover Process"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🧾 Salesforce Hygiene"):
            st.session_state.menu = "Salesforce Hygiene"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("⚙️ Technical Quoting & Order Management"):
            st.session_state.menu = "Technical Quoting & Order Management"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

        if st.button("🤝 Teamwork & Collaboration"):
            st.session_state.menu = "Teamwork & Collaboration"
            st.session_state.step = 1
            st.session_state.q_count = 1
            st.session_state.final_level = None
            st.rerun()

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
                    if st.button("YES ✅", key="pk1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Explains 2-way sync and API limitations.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Submitted 3+ product feedback requests.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Is the seller a recognized SME who trains others AND predicts market trends?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Initiates feedback that led to a measurable improvement.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Acts as team´s lead trainer on competitive product strategy.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="pk6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller consistently and independently address basic product questions AND effectively utilize their knowledge to pre-empt technical objections?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Never escalates basic product queries.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Proactively addresses technical concerns before they become objections.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="pk9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller meet basic expectations by having fewer than one incorrect product fit error per month AND knowing the main function of all core products?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Error rate is negligible for standard deals.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pk11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Clearly defines the purpose of core products (e.g., Channel Manager).</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pk12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="pk12n"): st.session_state.final_level = "L1"; st.rerun()

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
                    st.markdown('<div class="criteria-box"><span class="criteria-text"> 2. Provided data-backed recommendations on improving pricing/terms strategy.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
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
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Can neutralize "too expensive" or "send me an email" without escalation.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="d12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="d12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🔍 PROSPECTING & LEAD MANAGEMENT
            # ==========================================
            elif assessment_type == "Prospecting":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Do they efficiently manage MQLs AND does their pipeline come primarily from proactive outbound prospecting  that includes discovering new, viable segments?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. MQLs processed faster than peers.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Found a new target group team was missing.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller pioneered a new lead generation channel/strategy AND can they accurately predict the conversion rate of leads from new sources?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Implemented a unique, team-scalable prospecting channel (e.g., custom LinkedIn strategy)</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Forecasts the success of new channels based on market intelligence.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="pr6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller consistently process MQLs within the target SLA AND successfully use non-traditional channels (e.g., social) to source high-quality leads?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Zero overdue MQLs month-over-month.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Secured 2+ high-quality leads from an outbound social strategy this quarter.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="pr9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller consistently meet minimum daily/weekly activity targets AND consistently close MQLs within the target follow-up SLA?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Meets all activity KPIs (calls, emails, meetings).</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pr11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Never lets inbound leads go cold due to follow-up delay.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pr12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="pr12n"): st.session_state.final_level = "L1"; st.rerun()

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
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Created a solution involving 3+ SiteMinder products/integrations based on discovery.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
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
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Accurately links a stated problem (e.g., manual updates) to a core product (e.g., Channel Manager)</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="i12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="i12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🧠 ADAPTABILITY & LEARNING AGILITY
            # ==========================================
            elif assessment_type == "Adaptability":
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
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller driven innovation by overhauling a team process based on their own learning  AND are they involved in designing the team´s future learning curriculum?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. The overhaul resulted in a permanent, positive change to team workflow.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Provides input to management on what skills the team should prioritize next.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="a6n"): st.session_state.final_level = "L4"; st.rerun()
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
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller quickly adapt to new required processes  AND successfully apply a new methodology learned in training to a live call?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Implements a new rule/process change within the first week. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="a11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2 Can be observed using a new selling technique or showcasing new products  immediately after training.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="a12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="a12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🌍 MARKET KNOWLEDGE
            # ==========================================
            elif assessment_type == "Market Knowledge":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Does the seller regularly anticipate market shifts AND provide strategic market insights that you share with the wider sales team?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Identified a market shift 6+ months in advance</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Provides non-obvious insights that inform team discussions.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L4/L5</span><span class="gate-question">Has this seller\'s market insight influenced the company\'s GTM strategy AND do they act as a recognized thought leader by presenting insights to leadership?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Advice led to a measurable GTM change (e.g., targeting a new segment). </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Presents strategic market reviews to management/leadership.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="m6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L2/L3</span><span class="gate-question">Does the seller use deep industry insights to frame the entire conversation AND effectively act as a trusted market advisor to customers?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Leads discussions using a trend/challenge, not a product. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Customer explicitly trusts their perspective over competitors.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="m9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L1/L2</span><span class="gate-question">Can the seller clearly and concisely articulate how SiteMinder differentiates from the top competitors AND use a current market trend to open a conversation?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Clearly explains the competitive advantage of our 3 core products. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="m11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Effectively uses recent industry news to start a new discussion.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="m12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="m12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 💬 SITEMINDER PLATFORM VALUE PROPOSITION
            # ==========================================
            elif assessment_type == "SiteMinder Platform Value Proposition":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Can the seller successfully anchor the pitch on key hotelier metrics (RevPAR/ADR) AND articulate the RFD value proposition without needing a visual aid?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Consistently ties pitch to quantifiable hotel metrics.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Can articulate the full value story without relying on slides/demo.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L4/L5</span><span class="gate-question">Has the seller successfully used the RFD to fundamentally shift a customer\'s business strategy AND developed a new pitch narrative that you or the team adopted?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Advice led to a structural change in the customer\'s pricing or inventory model. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Created a new, high-impact value framework (e.g., cost of inaction).</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="v6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L2/L3</span><span class="gate-question">Does the seller consistently link features to outcomes AND successfully anchor the entire pitch on a single, compelling RFD value proposition?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Always translates features into business benefits (e.g., "saves you X hours"). </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. The entire sales process revolves around one core value proposition.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="v9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L1/L2</span><span class="gate-question">Can the seller at least consistently link an RFD feature to the basic customer need for more revenue (L2 Q2) AND define a single tangible financial value (L1 Q3)?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Can state how a feature impacts revenue/occupancy. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="v11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="v11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown("<div class='criteria-box'><span class='criteria-text'>2. Defines what a \"tangible financial value\" means in a sales context.</span><span class='criteria-question'>Meet?</span></div>", unsafe_allow_html=True)
                    if st.button("YES ✅", key="v12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="v12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🎥 PRODUCT DEMONSTRATION
            # ==========================================
            elif assessment_type == "Product Demonstration":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Does the seller successfully use the demo to counter major competitive claims AND leverage customer success stories/data within the demo to paint a vision?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Successfully refutes a competitor\'s claim in the demo. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Seamlessly integrates relevant case study data points into the presentation.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L4/L5</span><span class="gate-question">Has the seller pioneered a new demonstration methodology that significantly improved the team\'s close rate AND do they integrate Business Intelligence tools and data into the demo?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Created a unique, high-impact demo structure adopted by peers</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Successfully demonstrated the data and reporting features of the platform.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="pd6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown("<div class='gate-box'><span class='gate-title'>📊 GATE: L2/L3</span><span class='gate-question'>Does the seller deliver a highly personalized demo AND use it to create \"aha\" moments that show the customer exactly how their pain will be solved?</span></div>", unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Demo is customised to the customer\'s logo/needs/property type. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Customer visibly reacts positively to the solution shown.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="pd9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L1/L2</span><span class="gate-question">Can the seller at least adapt a standard demo to a customer\'s basic needs AND handle a live interruption or question during the demo without losing focus?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Modifies the standard flow to focus on 1-2 key features identified in discovery. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pd11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Maintains professional composure during Q&A and technical hiccups.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pd12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="pd12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # ⏱️ SELF-MANAGEMENT & PRODUCTIVITY
            # ==========================================
            elif assessment_type == "Self-Management & Productivity":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller found a new way to optimize their workflow that significantly increased personal productivity AND do they mentor a peer on organization best practices?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Created a measurable efficiency gain for themselves</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Teaches specific time-management techniques to others.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L4/L5</span><span class="gate-question">Has the seller designed and implemented a new productivity system for the team AND do they work with leadership to eliminate team-wide productivity bottlenecks?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. System is formally adopted by the entire team </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Identifies and helps solve process inefficiencies that affect multiple departments.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="sp6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L2/L3</span><span class="gate-question">Does the seller use productivity techniques to maximize focused output AND do they work with a high degree of autonomy ?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Uses methods like time-blocking effectively. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Requires minimal oversight to meet goals and manage their schedule.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="sp9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L1/L2</span><span class="gate-question">Can the seller clearly articulate their process for prioritizing tasks AND is their schedule focused on revenue-generating activities?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Has a clear system for ranking daily tasks (e.g., urgent vs. important). </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sp11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Majority of time is spent on selling/prospecting activities.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sp12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="sp12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 📈 PIPELINE & FORECAST MANAGEMENT
            # ==========================================
            elif assessment_type == "Pipeline & Forecast Management":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller leveraged their pipeline data to successfully predict a market slowdown AND is the variance between their final forecast and actual results less than 10%?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Identified a macro trend (e.g., seasonality shift) using pipeline data. </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Forecast accuracy is consistently high across multiple periods.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L4/L5</span><span class="gate-question">Has the seller pioneered an innovative pipeline or forecasting strategy adopted by the team AND do they act as the final arbiter of truth for pipeline health?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Developed a new, team-wide methodology (e.g., qualification matrix). </span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Their word on pipeline health is trusted by management above all else.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="pf6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L2/L3</span><span class="gate-question">Does the seller proactively identify and address stalled deals before they become an issue AND provide detailed, data-backed forecasts during weekly review?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown("<div class='criteria-box'><span class='criteria-text'>1. Consistently addresses deals before they hit the \"stalled\" criteria. </span><span class='criteria-question'>Meet?</span></div>", unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Can articulate the health of their pipeline using conversion rates and activity data.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="pf9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L1/L2</span><span class="gate-question">Is their pipeline free of outdated opportunities  AND is their forecast reasonably accurate on a consistent basis ?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. All deals have recent activity (within 14 days) and a future next step.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="pf11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Forecast is typically within 15-20% of actual results.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="pf12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="pf12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🗺️ MARKET MANAGEMENT
            # ==========================================
            elif assessment_type == "Market Management":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller developed and executed a clear market segmentation and targeting strategy AND used data, resources, or partners effectively to drive measurable growth in priority segments?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Has defined and prioritized market segments using clear criteria, for example revenue potential, product fit, region, or customer profile.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Demonstrates measurable business impact from that strategy.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller created a market management strategy or framework adopted by other team members AND contributed to a significant, measurable increase in pipeline or revenue beyond their own territory?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Developed a structured approach to market segmentation or targeting that others adopted, for example revenue potential, product fit, region, or customer profile.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Their strategy produced measurable team or organizational impact.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="mm6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller proactively segment their market AND successfully grow pipeline or revenue within a priority segment through focused engagement?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Uses defined criteria to segment their market.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Demonstrates measurable improvement within a targeted segment.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="mm9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Can the seller clearly articulate which segments or accounts they are targeting AND are they executing prospecting activities consistently within those targets?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Can explain target segments or accounts and the rationale behind them.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="mm11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Demonstrates consistent execution against their targets.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="mm12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="mm12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🤝 ONBOARDING & HANDOVER PROCESS
            # ==========================================
            elif assessment_type == "Onboarding & Handover Process":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Can the seller successfully troubleshoot handover issues before they escalate AND act as a key liaison ensuring Onboarding has everything for complex accounts?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Pre-empts 80%+ of potential handover roadblocks.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Onboarding team views them as a collaborative partner, not a roadblock.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller pioneered a new process or tool that significantly reduced customer time-to-value AND developed a formal strategy for managing stalled deals?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Implemented a new internal checklist or tool.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Created a documented playbook for getting stuck deals back on track.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="oh6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller proactively prepare the customer for the next steps AND work collaboratively with Onboarding, providing additional, helpful context?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Customer is never surprised by the next stage of the process.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Provides extra notes/background to the Onboarding team beyond the checklist.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="oh9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller consistently complete the standard handoff checklist AND minimize the need for the Onboarding team to do significant follow-up for missing data?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. All mandatory fields are completed on time.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="oh11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Onboarding team reports minimal time spent chasing them for information.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="oh12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="oh12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # 🧾 SALESFORCE HYGIENE
            # ==========================================
            elif assessment_type == "Salesforce Hygiene":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Is the seller leveraging advanced Salesforce features, custom reports or dashboards, AND acting as a troubleshooter for peer questions?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Uses advanced reporting to gain personal insights.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Peers regularly seek them out for SFDC process or data help.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller partnered with Revenue Operations to enhance the system AND developed a new best practice for hygiene shared across the sales floor?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Initiated a project with Revenue or CRM Ops to fix a systemic data issue.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Created and trained peers on a new data entry or workflow shortcut.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="sf6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller proactively ensure data integrity without prompting AND use Salesforce as a strategic tool to manage their territory?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Data integrity is audited and found to be 95%+ accurate month-over-month.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Uses SFDC reports to identify where to prospect next.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="sf9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Do they consistently enter accurate and timely data AND do they use basic Salesforce reporting to track their own activity and progress?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Logs all calls and emails daily.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="sf11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Can pull a report to show their activity volume and conversion rates.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="sf12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="sf12n"): st.session_state.final_level = "L1"; st.rerun()

            # ==========================================
            # ⚙️ TECHNICAL QUOTING & ORDER MANAGEMENT
            # ==========================================
            elif assessment_type == "Technical Quoting & Order Management":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Has the seller served as the go-to resource for peer technical quoting questions AND proactively streamlined their own process for efficiency?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Is the authority on complex quoting rules for the team.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Reduced the time they spend on admin by more than 20% through optimisation.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Has the seller created a new method or training that significantly reduced the team&apos;s administrative burden or error rate AND partnered with Operations or Finance to enhance the technical quoting system?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Developed a tool or training adopted by the team.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Successfully initiated and completed a project with a cross-functional team to improve quoting.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="tq6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Can the seller handle complex quoting scenarios with efficiency AND do you receive positive feedback from the post-sales team on their order rigor?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Successfully quotes 3+ products, non-standard terms, or regional variances without error.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Post-sales team praises their detail and rigor.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="tq9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Can they independently generate accurate standard quotes with minimal errors AND do they consistently follow standard administrative steps for finalising a deal?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Error rate is less than 5% on standard deals.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tq11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. All deal documentation is submitted correctly within 24 hours of signature.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tq12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="tq12n"): st.session_state.final_level = "L1"; st.rerun()
            # ==========================================
            # 🤝 TEAMWORK & COLLABORATION
            # ==========================================
            elif assessment_type == "Teamwork & Collaboration":
                if step == 1:
                    st.markdown('<div class="gate-box"><span class="gate-title">📊 GATE: L3/L4</span><span class="gate-question">Does the seller frequently mentor and elevate the performance of struggling peers AND have they led a team initiative to improve a sales process?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw1y"): st.session_state.step = 2; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw1n"): st.session_state.step = 7; st.session_state.q_count += 1; st.rerun()
                elif step == 2:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Spends dedicated time coaching peers.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw2y"): st.session_state.step = 3; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw2n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 3:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Took ownership of a team project without being assigned by management.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw3y"): st.session_state.step = 4; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw3n"): st.session_state.final_level = "L3"; st.rerun()
                elif step == 4:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌟 GATE: L4/L5</span><span class="gate-question">Does the seller inspire and motivate the entire team as a key culture carrier AND are they involved in designing team development programs with leadership?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw4y"): st.session_state.step = 5; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw4n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 5:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Their presence and attitude consistently boost morale.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw5y"): st.session_state.step = 6; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw5n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 6:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Contributes to the formal design of onboarding or training content.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw6y"): st.session_state.final_level = "L5"; st.rerun()
                    if st.button("NO ❌", key="tw6n"): st.session_state.final_level = "L4"; st.rerun()
                elif step == 7:
                    st.markdown('<div class="gate-box"><span class="gate-title">📈 GATE: L2/L3</span><span class="gate-question">Does the seller proactively share an insight or tool that helped a peer AND do they offer to help colleagues with time-intensive tasks without being asked?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw7y"): st.session_state.step = 8; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw7n"): st.session_state.step = 10; st.session_state.q_count += 1; st.rerun()
                elif step == 8:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Regularly posts useful resources or tips in a team channel.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw8y"): st.session_state.step = 9; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw8n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 9:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Voluntarily jumps in to assist when a peer is swamped.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw9y"): st.session_state.final_level = "L3"; st.rerun()
                    if st.button("NO ❌", key="tw9n"): st.session_state.final_level = "L2"; st.rerun()
                elif step == 10:
                    st.markdown('<div class="gate-box"><span class="gate-title">🌱 GATE: L1/L2</span><span class="gate-question">Does the seller handle feedback in a mature and open way AND do they contribute to team-wide initiatives when asked?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw10y"): st.session_state.step = 11; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw10n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 11:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">1. Shows a clear willingness to change behavior based on coaching.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw11y"): st.session_state.step = 12; st.session_state.q_count += 1; st.rerun()
                    if st.button("NO ❌", key="tw11n"): st.session_state.final_level = "L1"; st.rerun()
                elif step == 12:
                    st.markdown('<div class="criteria-box"><span class="criteria-text">2. Participates fully in team meetings and required projects.</span><span class="criteria-question">Meet?</span></div>', unsafe_allow_html=True)
                    if st.button("YES ✅", key="tw12y"): st.session_state.final_level = "L2"; st.rerun()
                    if st.button("NO ❌", key="tw12n"): st.session_state.final_level = "L1"; st.rerun()
        
        # --- 5. FINAL RESULTS PAGE ---
        else:
            st.balloons()
            st.success("### 🏁 Assessment Complete!")

            new_record = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Tier": st.session_state.selected_tier,
                "Representative": rep_name,
                "Manager": manager_name,
                "Competency": assessment_type,
                "Level": st.session_state.final_level
            }

            col_res, col_extra = st.columns(2)
            with col_res:
                st.metric(label="Final Level Achieved", value=st.session_state.final_level)

            if not st.session_state.all_history or st.session_state.all_history[-1] != new_record:
                st.session_state.all_history.append(new_record)

            st.divider()

            if st.button("💾 Save Result & Return to Main Menu", use_container_width=True):
                st.session_state.step = 1
                st.session_state.q_count = 1
                st.session_state.final_level = None
                st.session_state.menu = "Main"
                st.rerun()
