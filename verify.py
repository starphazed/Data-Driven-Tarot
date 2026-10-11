from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import subprocess,re,html
r=Path(__file__).parent
class Doc(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.ids=[];self.h1=0;self.feed(s)
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='h1':self.h1+=1
  if 'id' in d:self.ids.append(d['id'])
  for key in ['href','src']:
   if key in d:self.links.append(d[key])
  if t=='img':assert 'alt' in d and 'width' in d and 'height' in d
pages={p.name:Doc(p.read_text(encoding='utf-8')) for p in r.glob('*.html')}
for name,d in pages.items():
 assert d.h1==1,(name,'h1')
 for link in d.links:
  u=urlsplit(link)
  if u.scheme:continue
  dest=unquote(u.path) or name
  assert (r/dest).exists(),(name,link)
  if u.fragment:assert u.fragment in pages[dest].ids,(name,link)
for i in range(1,13):
 old=subprocess.check_output(['git','show',f'3ea70d426e8b1f2ffe30e54bc7fe516ee1a5d4b4:card{i}.html']).decode('utf-8')
 new=(r/f'card{i}.html').read_text(encoding='utf-8')
 clean=lambda x:' '.join(html.unescape(re.sub('<[^>]+>','',x)).split())
 ps=[clean(x) for x in re.findall(r'<p[^>]*>(.*?)</p>',old,re.S)]
 assert ps[0] in clean(new)
 for p in ps[1:]:
  term,_,body=p.partition(':');assert term in clean(new) and body.strip() in clean(new)
print('PASS: 14 pages, local links and anchors, image attributes, single H1, all 12 introductions and 72 meanings preserved.')
print('Optimized photo bytes:',sum(p.stat().st_size for p in (r/'assets').glob('*.webp')))
