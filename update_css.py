import re

with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

new_css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0D0D0D !important;
    color: #F0EDE8 !important;
}

/* Override Streamlit Main Container */
.stApp {
    background-color: #0D0D0D;
}

/* ── HERO BANNER ── */
.hero-banner {
    background: #141414;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 40px;
    margin-bottom: 30px;
    position: relative;
    overflow: hidden;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 900;
    color: #F0EDE8;
    margin: 0 0 10px 0;
    line-height: 1.1;
    letter-spacing: -0.03em;
}
.hero-title em {
    color: #E8C547;
    font-style: italic;
}
.hero-subtitle {
    font-size: 1.05rem;
    color: #8A8680;
    margin: 0;
    font-weight: 300;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: transparent;
    border: 1px solid rgba(61,173,127,0.3);
    color: #3DAD7F;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 20px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── KPI METRIC CARDS ── */
div[data-testid="metric-container"] {
    background: #141414;
    border: 1px solid rgba(255,255,255,0.07);
    padding: 20px 24px;
    border-radius: 12px;
    transition: background 0.2s;
}
div[data-testid="metric-container"]:hover {
    background: #1C1C1C;
}
div[data-testid="metric-container"] label {
    color: #5A5754 !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', serif;
    color: #F0EDE8 !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
}

/* ── JOB CARDS ── */
.job-card {
    background: #141414;
    padding: 20px 24px;
    border-radius: 12px;
    margin-bottom: 14px;
    border: 1px solid rgba(255,255,255,0.07);
    transition: background 0.2s;
}
.job-card:hover {
    background: #1C1C1C;
}
.job-title {
    margin: 0 0 8px 0;
    color: #F0EDE8;
    font-size: 1.15rem;
    font-weight: 500;
}
.job-detail {
    margin: 4px 0;
    color: #8A8680;
    font-size: 0.85rem;
}
.job-detail strong {
    color: #5A5754;
    font-weight: 500;
}
.skill-tag {
    display: inline-block;
    background: rgba(232,197,71,0.1);
    border: 1px solid rgba(232,197,71,0.2);
    color: #E8C547;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    margin: 4px 4px 0 0;
}
.salary-badge {
    display: inline-block;
    background: rgba(61,173,127,0.1);
    border: 1px solid rgba(61,173,127,0.2);
    color: #3DAD7F;
    font-size: 0.8rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 6px;
    margin-top: 10px;
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #F0EDE8;
    margin: 0 0 20px 0;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}

hr {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin: 30px 0;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: #141414 !important;
    border-right: 1px solid rgba(255,255,255,0.07);
}
</style>"""

# Replace the old CSS
app_code = re.sub(r'<style>.*?</style>', new_css, app_code, flags=re.DOTALL)

# Update the Hero Banner HTML to use the new stylistic tags
new_hero = """<div class="hero-banner">
    <div class="hero-badge">Live Data Analytics</div>
    <h1 class="hero-title">The <em>smartest</em> way to read the market.</h1>
    <p class="hero-subtitle">Real-Time Job Market Intelligence Platform &nbsp;·&nbsp; Powered by Adzuna API</p>
</div>"""
app_code = re.sub(r'<div class="hero-banner">.*?</div>', new_hero, app_code, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Updated CSS in app.py")
