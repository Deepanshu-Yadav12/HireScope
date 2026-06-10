import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace static stats
html = re.sub(r'<div class="stat-value">12,482</div>', r'<div class="stat-value">{TOTAL_JOBS}</div>', html)
html = re.sub(r'<div class="stat-value">1,240</div>', r'<div class="stat-value">{UNIQUE_COMPANIES}</div>', html)
html = re.sub(r'<div class="stat-value">₹12\.5L</div>', r'<div class="stat-value">{AVG_SALARY}</div>', html)

# Replace companies chart
html = re.sub(
    r'(<div class="section-title">Top Companies Hiring</div>\s*<a href="#" class="section-link">View all →</a>\s*</div>\s*<div class="bar-chart">)[\s\S]*?(</div>\s*</div>\s*<div class="chart-card">)',
    r'\1\n{COMPANIES_HTML}\n\2', html
)

# Replace locations chart
html = re.sub(
    r'(<div class="section-title">Top Locations</div>\s*<a href="#" class="section-link">Map view →</a>\s*</div>\s*<div class="bar-chart">)[\s\S]*?(</div>\s*</div>\s*</div>\s*<!-- ROW 2)',
    r'\1\n{LOCATIONS_HTML}\n\2', html
)

# Replace jobs list
html = re.sub(
    r'(<div class="job-list">)[\s\S]*?(</div>\s*</div>\s*<!-- ROW 3)',
    r'\1\n{JOBS_HTML}\n\2', html
)

# Replace skills grid
html = re.sub(
    r'(<div class="skills-grid">)[\s\S]*?(</div>\s*<div style="margin-top: 1.25rem;)',
    r'\1\n{SKILLS_HTML}\n\2', html
)

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Created template.html")
