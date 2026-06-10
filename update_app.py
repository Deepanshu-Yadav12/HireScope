import re

with open('app.py', 'r', encoding='utf-8') as f:
    app_code = f.read()

# We want to replace everything after "# MAIN CONTENT"
main_content_marker = "# -----------------------------\n# MAIN CONTENT\n# -----------------------------"
idx = app_code.find(main_content_marker)
if idx != -1:
    app_code = app_code[:idx + len(main_content_marker)]

new_main_content = """
import streamlit.components.v1 as components
from collections import Counter

if df_display.empty:
    st.info("No data yet. Use the sidebar to fetch real-time jobs.")
else:
    # Read the HTML template
    with open("template.html", "r", encoding="utf-8") as f:
        html_template = f.read()
    
    # Calculate stats
    total_jobs = f"{len(df_display):,}"
    unique_companies = f"{df_display['Company'].nunique():,}"
    salary_df = df_display[df_display["salary"] > 0]
    avg_salary = f"₹{salary_df['salary'].mean() / 100000:.1f}L" if not salary_df.empty else "N/A"
    
    # Generate Companies HTML
    companies_html = ""
    top_companies = df_display["Company"].value_counts().head(7)
    max_comp_count = top_companies.max() if not top_companies.empty else 1
    for comp, count in top_companies.items():
        width = int((count / max_comp_count) * 100)
        companies_html += f'<div class="bar-row"><span class="bar-label">{comp}</span><div class="bar-track"><div class="bar-fill" style="width:{width}%"></div></div><span class="bar-count">{count}</span></div>\\n'
        
    # Generate Locations HTML
    locations_html = ""
    top_locations = df_display["Location"].value_counts().head(7)
    max_loc_count = top_locations.max() if not top_locations.empty else 1
    for loc, count in top_locations.items():
        width = int((count / max_loc_count) * 100)
        locations_html += f'<div class="bar-row"><span class="bar-label">{loc}</span><div class="bar-track"><div class="bar-fill green" style="width:{width}%"></div></div><span class="bar-count">{count}</span></div>\\n'
        
    # Generate Jobs HTML
    jobs_html = ""
    for _, row in df_display.head(5).iterrows():
        salary_text = f"₹{row['salary']/100000:.1f}L" if row["salary"] > 0 else "Not Disclosed"
        jobs_html += f'''
        <div class="job-row">
            <div class="job-row-left">
                <div class="job-title">{row['Title']}</div>
                <div class="job-company">{row['Company']} · {row['Location']}</div>
            </div>
            <div class="job-row-right">
                <span class="job-salary">{salary_text}</span>
            </div>
        </div>'''
        
    # Generate Skills HTML
    skills_html = ""
    valid_skills = [s for s in df_display["skills"] if pd.notna(s) and s != "Not Specified"]
    if valid_skills:
        all_skills = ",".join(valid_skills)
        skills_list = [s.strip() for s in all_skills.split(",") if s.strip()]
        skill_counts = Counter(skills_list).most_common(12)
        for i, (skill, count) in enumerate(skill_counts):
            if i < 3: style = "skill-hot"
            elif i < 8: style = "skill-warm"
            else: style = "skill-cool"
            skills_html += f'<span class="skill-pill {style}">{skill}</span>\\n'

    # Inject into template
    html_filled = html_template.replace("{TOTAL_JOBS}", total_jobs)
    html_filled = html_filled.replace("{UNIQUE_COMPANIES}", unique_companies)
    html_filled = html_filled.replace("{AVG_SALARY}", avg_salary)
    html_filled = html_filled.replace("{COMPANIES_HTML}", companies_html)
    html_filled = html_filled.replace("{LOCATIONS_HTML}", locations_html)
    html_filled = html_filled.replace("{JOBS_HTML}", jobs_html)
    html_filled = html_filled.replace("{SKILLS_HTML}", skills_html)
    
    # Hide default Streamlit padding
    st.markdown('''
        <style>
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
                max-width: 100%;
            }
            header {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    ''', unsafe_allow_html=True)
    
    # Render custom HTML
    components.html(html_filled, height=1800, scrolling=True)
"""

app_code += "\n" + new_main_content

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Updated app.py")
