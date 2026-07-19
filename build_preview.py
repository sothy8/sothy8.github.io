import re

with open('_layouts/default.html', 'r') as f:
    layout = f.read()

with open('index.md', 'r') as f:
    content = f.read()

# Remove front matter from content
content = re.sub(r'^---\n.*?^---\n', '', content, flags=re.MULTILINE | re.DOTALL)

# Replace Jekyll tags in layout
layout = layout.replace('{{ page.title | default: site.title }}', 'Sothy VANDETH - Data Scientist & AI Engineer')
layout = layout.replace('{{ site.description }}', 'Data Scientist & AI Engineer specializing in Computer Vision, Deep Learning, and Data Analysis. Building real-world AI solutions for emerging markets.')
layout = layout.replace('{{ site.author }}', 'Sothy VANDETH')
layout = layout.replace('{{ \'/assets/css/style.css\' | relative_url }}', '/assets/css/style.css')
layout = layout.replace('{{ \'now\' | date: "%Y" }}', '2026')

# Replace Jekyll tags in content
content = content.replace('{{ \'/assets/images/VST.jpg\' | relative_url }}', '/assets/images/VST.jpg')
content = content.replace('{{ \'/assets/images/P4.jpeg\' | relative_url }}', '/assets/images/P4.jpeg')
content = content.replace('{{ \'/assets/images/P2.jpeg\' | relative_url }}', '/assets/images/P2.jpeg')
content = content.replace('{{ \'/assets/images/P1.jpeg\' | relative_url }}', '/assets/images/P1.jpeg')
content = content.replace('{{ \'/assets/images/P3.jpeg\' | relative_url }}', '/assets/images/P3.jpeg')
content = content.replace('{{ site.email }}', 'sothyvandeth8034@gmail.com')
content = content.replace('{{ site.github_username }}', 'sothy8')
content = content.replace('{{ site.linkedin_username }}', 'sothy-vandeth')

# Inject content into layout
final_html = layout.replace('{{ content }}', content)

with open('preview.html', 'w') as f:
    f.write(final_html)

print("Created preview.html")
