import glob
import os

mds = glob.glob('*.md')
mds.sort()
links = ""
for md in mds:
    html = md[:-3] + ".html"
    with open(md, 'r', encoding='utf-8') as f:
        content = f.readlines()
    if 'pandoc: true' in content[1]:
        # hacky af but idc
        os.system(f'pandoc --standalone -c style.css {md} -o build/{html}')
    else:
        os.system(f'markmap {md} -o build/{html} --no-open')
    links += f'<li><a href="{html}">{md[:-3]}</a></li>'

indexhtml = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>decuongtriethoc</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body>
    <ul>
        {links}
    </ul>
</body>
</html>'''

with open('build/index.html', 'w', encoding='utf-8') as f:
    f.write(indexhtml)
