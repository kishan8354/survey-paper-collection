"""Regenerate Markdown, CSV, paper cards and filters from papers.json (stdlib only)."""
from pathlib import Path
import json, csv
ROOT = Path(__file__).resolve().parents[1]
papers = json.loads((ROOT/'papers.json').read_text(encoding='utf-8'))
def cell(value):
    if isinstance(value, list):
        value = '; '.join(value)
    return str(value if value is not None else 'Not identified in supplied PDF').replace('|', r'\|').replace('\n',' ')
def table(items):
    lines = ['| ID | Year | Paper | Data / benchmarks | Input dimension | Evaluated tasks | Metrics |',
             '|---|---|---|---|---|---|---|']
    for p in items:
        lines.append('| '+' | '.join([p['id'],str(p['year']),f"[{cell(p['title'])}]({p['paper_url']})",cell(p['datasets']),cell(p['input_dimension']),cell(p['tasks']),cell(p['metrics'])])+' |')
    return '\n'.join(lines)+'\n'
ordered = sorted(papers,key=lambda p:(-p['year'],p['id']))
(ROOT/'CATALOG.md').write_text('# Paper comparison\n\nPapers organized by year, datasets, input dimensions, evaluated tasks and metrics.\n\n'+table(ordered),encoding='utf-8')
fields = list(papers[0])
with (ROOT/'papers.csv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=fields,lineterminator="\n")
    writer.writeheader()
    writer.writerows({k:cell(p[k]) for k in fields} for p in ordered)
for p in papers:
    fields_to_show=[('year','Year'),('topic','Category'),('local_filename','Original local PDF filename'),('paper_url','Paper / source'),('input_dimension','Input dimension'),('datasets','Data / evaluation benchmarks'),('tasks','Evaluated tasks'),('metrics','Metrics'),('method','Method'),('models','Models'),('code_url','Code / resources'),('evidence','Evidence locations and verification'),('takeaway','Why it matters'),('limitations_to_check','Limitations / questions to verify'),('reading_priority','Suggested reading priority (1 first)'),('reading_status','Reading status'),('reproduced','Reproduced'),('extracted_on','Extraction date')]
    text=f"# {p['id']}: {p['title']}\n\n"+'\n\n'.join(f'**{label}:** {cell(p[key])}' for key,label in fields_to_show)+'\n\n## My reading notes\n\n- Problem in my own words: To fill after reading.\n- One figure or equation I can explain: To fill.\n- Main result and exact table/row: To verify.\n- Fair comparison / split concerns: To fill.\n- Possible project connection: To fill.\n'
    dest=ROOT/'notes'/f"{p['id']}.md"; dest.parent.mkdir(exist_ok=True)
    # Personal notes are editable; preserve existing cards on regeneration.
    if not dest.exists(): dest.write_text(text,encoding='utf-8')
views = {
    'BY_YEAR.md':('Papers by year','year'),
    'BY_TOPIC.md':('Papers by topic','topic'),
    'BY_DIMENSION.md':('Papers by input dimension','input_dimension'),
}
for filename,(title,key) in views.items():
    chunks=[f'# {title}\n']
    for value in sorted({p[key] for p in papers},key=str,reverse=key=='year'):
        chunks.append(f'## {value}\n\n'+table([p for p in ordered if p[key]==value]))
    (ROOT/filename).write_text('\n'.join(chunks),encoding='utf-8')
for filename,key,title in [('BY_DATASET.md','datasets','Papers by dataset / benchmark'),('BY_TASK.md','tasks','Papers by evaluated task')]:
    chunks=[f'# {title}\n\nNames follow the supplied papers; related dataset variants are kept explicit.\n']
    for value in sorted({v for p in papers for v in p[key]}):
        chunks.append(f'## {value}\n\n'+'\n'.join(f"- [{p['id']}: {p['title']}](notes/{p['id']}.md)" for p in ordered if value in p[key]))
    (ROOT/filename).write_text('\n\n'.join(chunks)+'\n',encoding='utf-8')
print(f'Rendered {len(papers)} papers, CSV, comparison and five category views. Existing reading notes preserved.')
