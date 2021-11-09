#iz kazala bomo pobrali url-je strani ki nas zanimajo

import re
with open('kazalo') as f:
    vsebina = f.read()
r"https://www.hofer.si/sl/posebna-ponudba/od-ponedeljka-8-11-2021/"
vzorec = (
    r'<a href="/title/tt'
    r'(?P<id>\d{7})'  # ID ima sedem števk
    r'/\?ref_=adv_li_tt"\n>'  # neka šara vmes med id-jem in naslovom
    r'(?P<naslov>.*?)'  # zajamemo naslov
    r'</a>'
    r'\s+'
    r'<span class="lister-item-year text-muted unbold">'
    r'(\([IVXLCDM]+\) )?'
    r'\((?P<leto>.*?)\)'
)

count = 0
for zadetek in re.finditer(vzorec, vsebina):
    print(zadetek.groupdict())
    count += 1
print(count)


#ugotavljam da je to vse skupaj odveč. Lahko bi samo prebral te url-je ki so relativno fiksi in potem pobral izdelke ločeno.
# danes je treba nekaj odati, tako da bom