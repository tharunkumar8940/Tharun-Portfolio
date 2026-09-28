import streamlit as st
from pathlib import Path
import base64

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Tharun Kumar B | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# PROFILE PHOTO
# ============================================================

photo_path = Path("assets/profile/profile.jpg")

if not photo_path.exists():
    st.error(
        "Profile photo not found.\n\n"
        "Expected location:\n"
        "assets/profile/profile.jpg"
    )
    st.stop()

photo_base64 = base64.b64encode(
    photo_path.read_bytes()
).decode("utf-8")

# ============================================================
# PAGE BACKGROUND
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 85% 20%,
                rgba(56, 189, 248, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 10% 80%,
                rgba(37, 99, 235, 0.08),
                transparent 30%
            ),
            #060a12;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 10px;
        padding-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO / OPENING SCREEN
# ============================================================

st.html(
    """
    <style>
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 14px 4px 24px;
        margin-bottom: 10px;
    }

    .top-brand {
        color: #f8fafc;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 2px;
    }

    .top-status {
        color: #38bdf8;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    .status-dot {
        display: inline-block;
        width: 7px;
        height: 7px;
        margin-right: 7px;
        border-radius: 50%;
        background: #38bdf8;
        box-shadow: 0 0 12px rgba(56,189,248,0.8);
    }

    @media (max-width: 650px) {
        .top-bar {
            align-items: flex-start;
            gap: 12px;
            flex-direction: column;
        }
    }
    </style>

    

    <div class="top-bar">
        <div class="top-brand">THARUN KUMAR B</div>

        <div class="top-status">
            <span class="status-dot"></span>
            AVAILABLE FOR OPPORTUNITIES
        </div>
    </div>
    """
)
st.html(
    f"""
    <style>

    .portfolio-hero {{
        min-height: 680px;

        display: flex;
        align-items: center;
        justify-content: space-between;

        gap: 70px;

        padding: 40px 35px;

        box-sizing: border-box;

        color: white;

        font-family:
            Arial,
            Helvetica,
            sans-serif;
    }}

    /* ========================================================
       LEFT SIDE
       ======================================================== */

    .hero-left {{
        flex: 1.25;
    }}

    .hero-name {{
        font-size: clamp(58px, 8vw, 105px);

        font-weight: 900;

        line-height: 0.88;

        letter-spacing: -5px;

        margin: 0;
    }}

    .hero-word {{
        display: block;

        opacity: 0;

        transform: translateY(35px);

        animation:
            revealWord
            0.8s
            ease
            forwards;
    }}

    .hero-word:nth-child(1) {{
        animation-delay: 0.2s;
    }}

    .hero-word:nth-child(2) {{
        animation-delay: 0.8s;
    }}

    .hero-word:nth-child(3) {{
        animation-delay: 1.4s;

        color: #38bdf8;
    }}

    /* ========================================================
       ROLE
       ======================================================== */

    .hero-role {{
        margin-top: 34px;

        color: #cbd5e1;

        font-size: 14px;

        font-weight: 700;

        letter-spacing: 2.5px;

        opacity: 0;

        animation:
            fadeUp
            0.8s
            ease
            forwards;

        animation-delay: 2s;
    }}

    /* ========================================================
       BLUE LINE
       ======================================================== */

    .hero-line {{
        width: 85px;

        height: 3px;

        background: #38bdf8;

        margin-top: 22px;

        opacity: 0;

        animation:
            fadeUp
            0.8s
            ease
            forwards;

        animation-delay: 2.2s;
    }}

    /* ========================================================
       DESCRIPTION
       ======================================================== */

    .hero-description {{
        max-width: 620px;

        margin-top: 25px;

        color: #94a3b8;

        font-size: 17px;

        line-height: 1.8;

        opacity: 0;

        animation:
            fadeUp
            0.8s
            ease
            forwards;

        animation-delay: 2.4s;
    }}

    /* ========================================================
       RIGHT SIDE
       ======================================================== */

    .hero-right {{
        flex: 0.85;

        display: flex;

        justify-content: center;

        align-items: center;
    }}

    .profile-container {{
        text-align: center;

        opacity: 0;

        transform: scale(0.92);

        animation:
            photoReveal
            1s
            ease
            forwards;

        animation-delay: 1.1s;
    }}

    /* ========================================================
       PROFILE IMAGE
       ======================================================== */

    .profile-image {{
        width: 390px;

        height: 390px;

        object-fit: cover;

        border-radius: 50%;

        border: 3px solid #38bdf8;

        box-shadow:

            0 0 0 12px
            rgba(56, 189, 248, 0.04),

            0 0 70px
            rgba(56, 189, 248, 0.18);
    }}

    /* ========================================================
       PHOTO CAPTION
       ======================================================== */

    .photo-caption {{
        margin-top: 20px;

        color: #64748b;

        font-size: 11px;

        letter-spacing: 3px;
    }}

    /* ========================================================
       ANIMATIONS
       ======================================================== */

    @keyframes revealWord {{

        0% {{
            opacity: 0;

            transform:
                translateY(35px);
        }}

        100% {{
            opacity: 1;

            transform:
                translateY(0);
        }}

    }}

    @keyframes fadeUp {{

        0% {{
            opacity: 0;

            transform:
                translateY(20px);
        }}

        100% {{
            opacity: 1;

            transform:
                translateY(0);
        }}

    }}

    @keyframes photoReveal {{

        0% {{
            opacity: 0;

            transform:
                scale(0.92);
        }}

        100% {{
            opacity: 1;

            transform:
                scale(1);
        }}

    }}

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 800px) {{

        .portfolio-hero {{

            flex-direction: column;

            text-align: center;

            padding-top: 30px;
        }}

        .hero-left {{

            width: 100%;
        }}

        .hero-right {{

            width: 100%;
        }}

        .hero-description {{

            margin-left: auto;

            margin-right: auto;
        }}

        .hero-line {{

            margin-left: auto;

            margin-right: auto;
        }}

        .profile-image {{

            width: 280px;

            height: 280px;
        }}

    }}

    </style>

    <section class="portfolio-hero">

        <!-- ================================================
             LEFT SIDE
             ================================================ -->

        <div class="hero-left">

            <div class="hero-name">

                <span class="hero-word">
                    THARUN
                </span>

                <span class="hero-word">
                    KUMAR
                </span>

                <span class="hero-word">
                    B
                </span>

            </div>


            <div class="hero-role">

                DATA ANALYST
                &nbsp; • &nbsp;
                DATA SCIENCE DEVELOPER

            </div>


            <div class="hero-line"></div>


            <div class="hero-description">

                Turning data into useful insights,
                predictive models and intelligent
                solutions using Python and
                machine learning.

            </div>

        </div>


        <!-- ================================================
             RIGHT SIDE
             ================================================ -->

        <div class="hero-right">

            <div class="profile-container">

                <img
                    class="profile-image"

                    src="data:image/jpeg;base64,{photo_base64}"

                    alt="Tharun Kumar B"
                >

                <div class="photo-caption">

                    DATA • ML • INTELLIGENCE

                </div>

            </div>

        </div>

    </section>
    """
)
# ============================================================
# PORTFOLIO SIGNAL
# ============================================================

st.html(
    """
    <style>

    .signal-section {
        margin-top: 30px;
        padding: 70px 35px;
        border-top: 1px solid rgba(148, 163, 184, 0.12);
    }

    .signal-label {
        color: #38bdf8;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 3px;
        margin-bottom: 18px;
    }

    .signal-title {
        color: #ffffff;
        font-size: clamp(32px, 5vw, 58px);
        font-weight: 900;
        line-height: 1;
        letter-spacing: -2px;
        max-width: 700px;
    }

    .signal-description {
        color: #94a3b8;
        font-size: 16px;
        line-height: 1.8;
        max-width: 650px;
        margin-top: 22px;
    }

    .stats {
        display: grid;
        grid-template-columns:
            repeat(4, 1fr);

        gap: 16px;

        margin-top: 50px;
    }

    .stat-card {
        background:
            rgba(15, 23, 42, 0.65);

        border:
            1px solid rgba(148, 163, 184, 0.12);

        border-radius: 16px;

        padding: 28px;

        min-height: 135px;

        box-sizing: border-box;

        transition:
            transform 0.25s ease,
            border-color 0.25s ease;
    }

    .stat-card:hover {
        transform: translateY(-5px);

        border-color:
            rgba(56, 189, 248, 0.45);
    }

    .stat-number {
        color: #ffffff;

        font-size: 32px;

        font-weight: 900;
    }

    .stat-label {
        color: #64748b;

        font-size: 11px;

        font-weight: 700;

        letter-spacing: 1.5px;

        margin-top: 10px;
    }

    .focus-card {
        margin-top: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(14, 165, 233, 0.10),
                rgba(15, 23, 42, 0.72)
            );

        border:
            1px solid rgba(56, 189, 248, 0.18);

        border-radius: 18px;

        padding: 30px;

        display: flex;

        justify-content: space-between;

        align-items: center;

        gap: 30px;
    }

    .focus-small {
        color: #38bdf8;

        font-size: 10px;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .focus-title {
        color: #ffffff;

        font-size: 25px;

        font-weight: 800;

        margin-top: 10px;
    }

    .focus-text {
        color: #94a3b8;

        font-size: 14px;

        line-height: 1.7;

        max-width: 650px;

        margin-top: 8px;
    }

    .focus-status {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 2px;

        white-space: nowrap;
    }

    @media (max-width: 800px) {

        .stats {
            grid-template-columns:
                repeat(2, 1fr);
        }

        .focus-card {
            flex-direction: column;

            align-items: flex-start;
        }

    }

    @media (max-width: 500px) {

        .stats {
            grid-template-columns:
                1fr;
        }

    }

    </style>

    <section class="signal-section">

        <div class="signal-label">
            01 / PORTFOLIO SIGNAL
        </div>

        <div class="signal-title">
            BUILDING WITH DATA
            <br>
            AND MACHINE LEARNING
        </div>

        <div class="signal-description">
            A collection of practical data science projects
            focused on prediction, analytics, intelligent
            systems and real-world problem solving.
        </div>


        <div class="stats">

            <div class="stat-card">

                <div class="stat-number">
                    4
                </div>

                <div class="stat-label">
                    ML PROJECTS
                </div>

            </div>


            <div class="stat-card">

                <div class="stat-number">
                    5+
                </div>

                <div class="stat-label">
                    ML ALGORITHMS
                </div>

            </div>


            <div class="stat-card">

                <div class="stat-number">
                    PYTHON
                </div>

                <div class="stat-label">
                    PRIMARY LANGUAGE
                </div>

            </div>


            <div class="stat-card">

                <div class="stat-number">
                    LIVE
                </div>

                <div class="stat-label">
                    STREAMLIT APPS
                </div>

            </div>

        </div>


        <div class="focus-card">

            <div>

                <div class="focus-small">
                    CURRENT FOCUS
                </div>

                <div class="focus-title">
                    Machine Learning
                </div>

                <div class="focus-text">
                    Building predictive systems, analyzing
                    real-world datasets and developing
                    practical AI-powered applications.
                </div>

            </div>

            <div class="focus-status">
                ● ACTIVE
            </div>

        </div>

    </section>
    """
)

# ============================================================
# SELECTED WORK
# ============================================================

st.html(
    """
    <style>

    .work-section {
        margin-top: 20px;

        padding: 80px 35px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.12);
    }

    .work-label {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 3px;

        margin-bottom: 18px;
    }

    .work-title {
        color: #ffffff;

        font-size:
            clamp(36px, 5vw, 62px);

        font-weight: 900;

        letter-spacing: -2px;

        line-height: 1;

        margin-bottom: 18px;
    }

    .work-description {
        color: #94a3b8;

        font-size: 16px;

        line-height: 1.8;

        max-width: 720px;

        margin-bottom: 50px;
    }

    /* ========================================================
       PROJECT CARD
       ======================================================== */

    .project-card {
        background:
            linear-gradient(
                135deg,
                rgba(15, 23, 42, 0.92),
                rgba(8, 15, 28, 0.92)
            );

        border:
            1px solid
            rgba(148, 163, 184, 0.13);

        border-radius: 20px;

        padding: 32px;

        margin-bottom: 18px;

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .project-card:hover {

        transform:
            translateY(-5px);

        border-color:
            rgba(56, 189, 248, 0.35);

        box-shadow:
            0 20px 60px
            rgba(0, 0, 0, 0.25);
    }

    .project-top {

        display: flex;

        justify-content:
            space-between;

        align-items: center;

        gap: 20px;

        margin-bottom: 22px;
    }

    .project-number {

        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .project-status {

        color: #22c55e;

        font-size: 10px;

        font-weight: 800;

        letter-spacing: 1.5px;

        border:
            1px solid
            rgba(34, 197, 94, 0.25);

        padding:
            6px 10px;

        border-radius: 20px;
    }

    .project-title {

        color: #ffffff;

        font-size: 27px;

        font-weight: 800;

        line-height: 1.2;

        margin-bottom: 14px;
    }

    .project-description {

        color: #94a3b8;

        font-size: 14px;

        line-height: 1.8;

        max-width: 850px;

        margin-bottom: 20px;
    }

    .project-tech {

        color: #cbd5e1;

        font-size: 12px;

        font-weight: 600;

        line-height: 1.7;
    }

    .project-link {

        display: inline-block;

        margin-top: 22px;

        color: #38bdf8;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1px;

        text-decoration: none;
    }

    .project-link:hover {

        color: #7dd3fc;

    }

    </style>


    <section class="work-section">

        <div class="work-label">
            02 / SELECTED WORK
        </div>

        <div class="work-title">
            PROJECTS BUILT
            <br>
            TO SOLVE PROBLEMS.
        </div>

        <div class="work-description">

            A collection of practical machine-learning
            and data-science applications covering
            customer retention, healthcare risk,
            financial security and restaurant operations.

        </div>


        <!-- ==================================================
             PROJECT 01
             ================================================== -->

        <div class="project-card">

            <div class="project-top">

                <div class="project-number">
                    01 / CUSTOMER INTELLIGENCE
                </div>

                <div class="project-status">
                    ● LIVE PROJECT
                </div>

            </div>


            <div class="project-title">
                Customer Churn Prediction
            </div>


            <div class="project-description">

                Predicts customers who may leave a service
                and provides a machine-learning workflow
                for analyzing customer behaviour and
                retention patterns.

            </div>


            <div class="project-tech">

                Python · Pandas · Scikit-learn ·
                Random Forest · Streamlit

            </div>


            <a
                class="project-link"
                href="https://github.com/tharunkumar8940/Customer-churn-project.git"
                target="_blank"
            >
                VIEW SOURCE CODE →
            </a>

        </div>


        <!-- ==================================================
             PROJECT 02
             ================================================== -->

        <div class="project-card">

            <div class="project-top">

                <div class="project-number">
                    02 / HEALTHCARE ANALYTICS
                </div>

                <div class="project-status">
                    ● LIVE PROJECT
                </div>

            </div>


            <div class="project-title">
                Healthcare Disease Risk Prediction
            </div>


            <div class="project-description">

                A machine-learning risk prediction
                application that processes patient-related
                features and estimates low-risk or
                high-risk outcomes.

            </div>


            <div class="project-tech">

                Python · Pandas · XGBoost ·
                Scikit-learn · Streamlit

            </div>


            <a
                class="project-link"
                href="https://github.com/tharunkumar8940/Healthcare_Disease_Risk_prediction.git"
                target="_blank"
            >
                VIEW SOURCE CODE →
            </a>

        </div>


        <!-- ==================================================
             PROJECT 03
             ================================================== -->

        <div class="project-card">

            <div class="project-top">

                <div class="project-number">
                    03 / FINANCIAL SECURITY
                </div>

                <div class="project-status">
                    ● LIVE PROJECT
                </div>

            </div>


            <div class="project-title">
                Credit Card Fraud Detection
            </div>


            <div class="project-description">

                An anomaly-focused machine-learning
                system designed to identify potentially
                fraudulent transactions in highly
                imbalanced financial data.

            </div>


            <div class="project-tech">

                Python · Pandas · Scikit-learn ·
                Classification · Streamlit

            </div>


            <a
                class="project-link"
                href="https://github.com/tharunkumar8940/Credit_Card_Fraud_Detection.git"
                target="_blank"
            >
                VIEW SOURCE CODE →
            </a>

        </div>


        <!-- ==================================================
             PROJECT 04
             ================================================== -->

        <div class="project-card">

            <div class="project-top">

                <div class="project-number">
                    04 / RESTAURANT INTELLIGENCE
                </div>

                <div class="project-status">
                    ● LIVE PROJECT
                </div>

            </div>


            <div class="project-title">
                Food Waste & Demand Prediction
            </div>


            <div class="project-description">

                An analytics and machine-learning system
                that studies restaurant demand, sales
                and food waste to support preparation
                planning and menu optimization.

            </div>


            <div class="project-tech">

                Python · Pandas · Scikit-learn ·
                Regression · Streamlit

            </div>


            <a
                class="project-link"
                href="https://github.com/tharunkumar8940/Restaurant_Food_Waste_Prediction.git"
                target="_blank"
            >
                VIEW SOURCE CODE →
            </a>

        </div>

    </section>
    """
)

# ============================================================
# TECHNICAL STACK
# ============================================================

st.html(
    """
    <style>

    .stack-section {
        margin-top: 20px;

        padding: 80px 35px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.12);
    }

    .stack-label {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 3px;

        margin-bottom: 18px;
    }

    .stack-title {
        color: #ffffff;

        font-size:
            clamp(36px, 5vw, 62px);

        font-weight: 900;

        letter-spacing: -2px;

        line-height: 1;

        margin-bottom: 18px;
    }

    .stack-description {
        color: #94a3b8;

        font-size: 16px;

        line-height: 1.8;

        max-width: 700px;

        margin-bottom: 50px;
    }

    /* ========================================================
       SKILL GRID
       ======================================================== */

    .skill-grid {
        display: grid;

        grid-template-columns:
            repeat(3, 1fr);

        gap: 18px;
    }

    .skill-card {
        background:
            rgba(15, 23, 42, 0.72);

        border:
            1px solid
            rgba(148, 163, 184, 0.13);

        border-radius: 18px;

        padding: 30px;

        min-height: 260px;

        box-sizing: border-box;

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .skill-card:hover {

        transform:
            translateY(-5px);

        border-color:
            rgba(56, 189, 248, 0.35);

        box-shadow:
            0 18px 50px
            rgba(0, 0, 0, 0.22);
    }

    .skill-index {
        color: #475569;

        font-size: 10px;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .skill-category {
        color: #38bdf8;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1.5px;

        margin-top: 25px;

        margin-bottom: 20px;
    }

    .skill-list {
        color: #e2e8f0;

        font-size: 16px;

        line-height: 2.1;

        font-weight: 600;
    }

    .skill-item {
        border-bottom:
            1px solid
            rgba(148, 163, 184, 0.08);

        padding-bottom: 4px;
    }

    .skill-item:last-child {
        border-bottom: none;
    }

    /* ========================================================
       TOOL STRIP
       ======================================================== */

    .tool-strip {

        margin-top: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(56, 189, 248, 0.08),
                rgba(15, 23, 42, 0.72)
            );

        border:
            1px solid
            rgba(56, 189, 248, 0.15);

        border-radius: 18px;

        padding: 25px 30px;

        color: #94a3b8;

        font-size: 12px;

        line-height: 2;

        letter-spacing: 0.5px;
    }

    .tool-highlight {
        color: #ffffff;

        font-weight: 700;
    }

    @media (max-width: 850px) {

        .skill-grid {
            grid-template-columns:
                1fr;
        }

    }

    </style>


    <section class="stack-section">

        <div class="stack-label">
            03 / TECHNICAL STACK
        </div>


        <div class="stack-title">
            TOOLS I BUILD
            <br>
            WITH.
        </div>


        <div class="stack-description">

            Technologies and tools I use across
            data analysis, machine learning,
            visualization and application development.

        </div>


        <div class="skill-grid">


            <!-- ============================================
                 PROGRAMMING
                 ============================================ -->

            <div class="skill-card">

                <div class="skill-index">
                    01
                </div>

                <div class="skill-category">
                    PROGRAMMING & DATA
                </div>

                <div class="skill-list">

                    <div class="skill-item">
                        Python
                    </div>

                    <div class="skill-item">
                        SQL
                    </div>

                    <div class="skill-item">
                        Pandas
                    </div>

                    <div class="skill-item">
                        NumPy
                    </div>

                </div>

            </div>


            <!-- ============================================
                 MACHINE LEARNING
                 ============================================ -->

            <div class="skill-card">

                <div class="skill-index">
                    02
                </div>

                <div class="skill-category">
                    MACHINE LEARNING
                </div>

                <div class="skill-list">

                    <div class="skill-item">
                        Scikit-learn
                    </div>

                    <div class="skill-item">
                        XGBoost
                    </div>

                    <div class="skill-item">
                        Classification
                    </div>

                    <div class="skill-item">
                        Regression
                    </div>

                </div>

            </div>


            <!-- ============================================
                 VISUALIZATION & DEPLOYMENT
                 ============================================ -->

            <div class="skill-card">

                <div class="skill-index">
                    03
                </div>

                <div class="skill-category">
                    VISUALIZATION & DEPLOYMENT
                </div>

                <div class="skill-list">

                    <div class="skill-item">
                        Data Visualization
                    </div>

                    <div class="skill-item">
                        Plotly
                    </div>

                    <div class="skill-item">
                        Streamlit
                    </div>

                    <div class="skill-item">
                        GitHub
                    </div>

                </div>

            </div>

        </div>


        <div class="tool-strip">

            <span class="tool-highlight">
                WORKFLOW:
            </span>

            Data Collection
            →
            Data Cleaning
            →
            EDA
            →
            Feature Engineering
            →
            Model Training
            →
            Evaluation
            →
            Interactive Application

        </div>

    </section>
    """
)

# ============================================================
# ABOUT / DATA SCIENCE JOURNEY
# ============================================================

st.html(
    """
    <style>

    .about-section {
        margin-top: 20px;

        padding: 80px 35px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.12);
    }

    .about-label {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 3px;

        margin-bottom: 18px;
    }

    .about-title {
        color: #ffffff;

        font-size:
            clamp(36px, 5vw, 62px);

        font-weight: 900;

        letter-spacing: -2px;

        line-height: 1;

        max-width: 850px;
    }

    .about-grid {

        display: grid;

        grid-template-columns:
            1.15fr 0.85fr;

        gap: 25px;

        margin-top: 50px;
    }

    .about-card {

        background:
            rgba(15, 23, 42, 0.72);

        border:
            1px solid
            rgba(148, 163, 184, 0.13);

        border-radius: 20px;

        padding: 32px;

        box-sizing: border-box;
    }

    .about-card-title {

        color: #ffffff;

        font-size: 20px;

        font-weight: 800;

        margin-bottom: 20px;
    }

    .about-text {

        color: #94a3b8;

        font-size: 15px;

        line-height: 1.9;

        margin-bottom: 18px;
    }

    .about-text:last-child {
        margin-bottom: 0;
    }

    /* ========================================================
       PROCESS
       ======================================================== */

    .process {

        display: flex;

        flex-direction: column;

        gap: 13px;
    }

    .process-item {

        display: flex;

        align-items: center;

        gap: 16px;

        padding: 14px 16px;

        border:
            1px solid
            rgba(148, 163, 184, 0.08);

        border-radius: 12px;

        background:
            rgba(2, 6, 23, 0.35);
    }

    .process-number {

        color: #38bdf8;

        font-size: 11px;

        font-weight: 900;

        min-width: 28px;
    }

    .process-name {

        color: #e2e8f0;

        font-size: 13px;

        font-weight: 700;
    }

    .process-arrow {

        margin-left: auto;

        color: #475569;

        font-size: 14px;
    }

    /* ========================================================
       DIRECTION CARD
       ======================================================== */

    .direction-card {

        margin-top: 18px;

        background:
            linear-gradient(
                135deg,
                rgba(56, 189, 248, 0.08),
                rgba(15, 23, 42, 0.75)
            );

        border:
            1px solid
            rgba(56, 189, 248, 0.15);

        border-radius: 18px;

        padding: 28px 32px;
    }

    .direction-label {

        color: #38bdf8;

        font-size: 10px;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .direction-title {

        color: #ffffff;

        font-size: 22px;

        font-weight: 800;

        margin-top: 10px;
    }

    .direction-text {

        color: #94a3b8;

        font-size: 14px;

        line-height: 1.8;

        max-width: 800px;

        margin-top: 8px;
    }

    @media (max-width: 850px) {

        .about-grid {
            grid-template-columns: 1fr;
        }

    }

    </style>


    <section class="about-section">

        <div class="about-label">
            04 / ABOUT
        </div>


        <div class="about-title">
            FROM RAW DATA
            <br>
            TO USEFUL DECISIONS.
        </div>


        <div class="about-grid">


            <!-- ============================================
                 ABOUT ME
                 ============================================ -->

            <div class="about-card">

                <div class="about-card-title">
                    My Approach
                </div>

                <div class="about-text">

                    My focus is on building practical
                    data-science solutions rather than
                    only training machine-learning models.

                </div>

                <div class="about-text">

                    I work across the complete workflow:
                    understanding the problem, preparing
                    data, performing exploratory analysis,
                    engineering useful features, training
                    models, evaluating performance and
                    turning the results into interactive
                    applications.

                </div>

                <div class="about-text">

                    Each project is an opportunity to connect
                    technical machine-learning concepts with
                    a practical problem that can be understood
                    and used by people.

                </div>

            </div>


            <!-- ============================================
                 WORKFLOW
                 ============================================ -->

            <div class="about-card">

                <div class="about-card-title">
                    My Data Science Workflow
                </div>


                <div class="process">


                    <div class="process-item">

                        <div class="process-number">
                            01
                        </div>

                        <div class="process-name">
                            Understand the Problem
                        </div>

                        <div class="process-arrow">
                            →
                        </div>

                    </div>


                    <div class="process-item">

                        <div class="process-number">
                            02
                        </div>

                        <div class="process-name">
                            Prepare the Data
                        </div>

                        <div class="process-arrow">
                            →
                        </div>

                    </div>


                    <div class="process-item">

                        <div class="process-number">
                            03
                        </div>

                        <div class="process-name">
                            Explore & Analyze
                        </div>

                        <div class="process-arrow">
                            →
                        </div>

                    </div>


                    <div class="process-item">

                        <div class="process-number">
                            04
                        </div>

                        <div class="process-name">
                            Build ML Models
                        </div>

                        <div class="process-arrow">
                            →
                        </div>

                    </div>


                    <div class="process-item">

                        <div class="process-number">
                            05
                        </div>

                        <div class="process-name">
                            Evaluate Results
                        </div>

                        <div class="process-arrow">
                            →
                        </div>

                    </div>


                    <div class="process-item">

                        <div class="process-number">
                            06
                        </div>

                        <div class="process-name">
                            Build the Application
                        </div>

                    </div>

                </div>

            </div>

        </div>


        <!-- ================================================
             CURRENT DIRECTION
             ================================================= -->

        <div class="direction-card">

            <div class="direction-label">
                CURRENT DIRECTION
            </div>

            <div class="direction-title">
                Advanced Machine Learning & AI Engineering
            </div>

            <div class="direction-text">

                My current learning direction is focused on
                advanced machine learning and AI engineering,
                with an emphasis on building technically
                strong projects that demonstrate practical
                problem-solving.

            </div>

        </div>

    </section>
    """
)

# ============================================================
# CONNECT
# ============================================================

st.html(
    """
    <style>

    .connect-section {
        margin-top: 20px;

        padding: 90px 35px 50px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.12);
    }

    .connect-label {
        color: #38bdf8;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 3px;

        margin-bottom: 20px;
    }

    .connect-title {
        color: #ffffff;

        font-size:
            clamp(40px, 6vw, 72px);

        font-weight: 900;

        letter-spacing: -3px;

        line-height: 0.95;

        max-width: 800px;
    }

    .connect-text {
        color: #94a3b8;

        font-size: 16px;

        line-height: 1.8;

        max-width: 650px;

        margin-top: 25px;
    }

    .connect-actions {

        display: flex;

        flex-wrap: wrap;

        gap: 14px;

        margin-top: 35px;
    }

    .connect-button {

        display: inline-block;

        padding: 14px 22px;

        border-radius: 10px;

        text-decoration: none;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1px;

        transition:
            transform 0.2s ease,
            background 0.2s ease,
            border-color 0.2s ease;
    }

    .connect-primary {

        background: #38bdf8;

        color: #06111d;

        border:
            1px solid #38bdf8;
    }

    .connect-secondary {

        background:
            rgba(15, 23, 42, 0.7);

        color: #e2e8f0;

        border:
            1px solid
            rgba(148, 163, 184, 0.18);
    }

    .connect-button:hover {

        transform:
            translateY(-3px);

    }

    .connect-secondary:hover {

        border-color:
            rgba(56, 189, 248, 0.45);

    }

    /* ========================================================
       FOOTER
       ======================================================== */

    .portfolio-footer {

        margin-top: 80px;

        padding-top: 25px;

        border-top:
            1px solid
            rgba(148, 163, 184, 0.08);

        display: flex;

        justify-content:
            space-between;

        align-items: center;

        gap: 20px;

        color: #475569;

        font-size: 11px;

        letter-spacing: 1px;
    }

    .footer-name {

        color: #94a3b8;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .footer-role {

        text-align: right;
    }

    @media (max-width: 650px) {

        .portfolio-footer {

            flex-direction: column;

            align-items: flex-start;
        }

        .footer-role {

            text-align: left;
        }

    }

    </style>


    <section class="connect-section">

        <div class="connect-label">
            05 / CONNECT
        </div>


        <div class="connect-title">
            LET THE
            <br>
            WORK SPEAK.
        </div>


        <div class="connect-text">

            Explore the source code, machine-learning
            projects and technical work through GitHub.

        </div>


        <div class="connect-actions">

            <a
                class="connect-button connect-primary"
                href="https://github.com/tharunkumar8940"
                target="_blank"
            >
                OPEN GITHUB PROFILE →
            </a>


            <a
                class="connect-button connect-secondary"
                href="https://github.com/tharunkumar8940/Customer-churn-project"
                target="_blank"
            >
                VIEW CUSTOMER CHURN →
            </a>

        </div>


        <footer class="portfolio-footer">

            <div class="footer-name">
                THARUN KUMAR B
            </div>

            <div class="footer-role">
                DATA ANALYST • DATA SCIENCE DEVELOPER
            </div>

        </footer>

    </section>
    """
)

st.html(
    """
    <style>
    .cert-section {
        margin-top: 20px;
        padding: 90px 35px 30px;
        border-top: 1px solid rgba(148,163,184,0.12);
    }

    .cert-label {
        color: #38bdf8;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 3px;
        margin-bottom: 20px;
    }

    .cert-title {
        color: #ffffff;
        font-size: clamp(40px, 6vw, 72px);
        font-weight: 900;
        letter-spacing: -3px;
        line-height: .95;
        max-width: 800px;
    }

    .cert-card {
        margin-top: 45px;
        max-width: 850px;
        padding: 30px;
        border: 1px solid rgba(148,163,184,0.15);
        border-radius: 16px;
        background: rgba(15,23,42,0.55);
        transition: transform .2s ease, border-color .2s ease;
    }

    .cert-card:hover {
        transform: translateY(-4px);
        border-color: rgba(56,189,248,0.45);
    }

    .cert-provider {
        color: #38bdf8;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    .cert-name {
        color: #f8fafc;
        font-size: 28px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .cert-org {
        color: #cbd5e1;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .cert-date {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 25px;
    }

    .cert-button {
        display: inline-block;
        padding: 12px 18px;
        border-radius: 9px;
        background: rgba(56,189,248,0.08);
        border: 1px solid rgba(56,189,248,0.3);
        color: #38bdf8;
        text-decoration: none;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1px;
        transition: all .2s ease;
    }

    .cert-button:hover {
        background: rgba(56,189,248,0.15);
        transform: translateY(-2px);
    }
    </style>

    <section class="cert-section">
        <div class="cert-label">06 / CERTIFICATIONS</div>

        <div class="cert-title">
            CONTINUOUS<br>LEARNING.
        </div>

        <div class="cert-card">

            <div class="cert-provider">
                COURSERA
            </div>

            <div class="cert-name">
                Cryptography
            </div>

            <div class="cert-org">
                Authorized by University of Maryland, College Park
            </div>

            <div class="cert-date">
                Completed September 9, 2026
            </div>

            <a
                class="cert-button"
                href="https://coursera.org/share/3a5a6c7469788e18badbd3abde6ef427"
                target="_blank"
            >
                VERIFY CERTIFICATE →
            </a>

        </div>
    </section>
    """
)