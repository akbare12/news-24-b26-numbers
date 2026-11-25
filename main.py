#!/usr/bin/env python3
"""NEWS-24 front page (numbers angle): Tuesday 24 November 2026, 38 stories, 13 panels."""
import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; BG=(250,246,236); INK=(20,20,20); RED=(178,34,34); NAVY=(24,42,78); GOLD=(176,132,28); GREEN=(34,120,60); BLUE=(30,90,160); ORANGE=(200,90,20); GREY=(110,110,110); CREAM=(238,228,205)
FD="/usr/share/fonts/truetype/dejavu/"
def F(n,s):
    try: return ImageFont.truetype(FD+n,s)
    except Exception: return ImageFont.load_default()
SERIFB=lambda s:F("DejaVuSerif-Bold.ttf",s); SERIF=lambda s:F("DejaVuSerif.ttf",s); SANSB=lambda s:F("DejaVuSans-Bold.ttf",s); SANS=lambda s:F("DejaVuSans.ttf",s)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
def txt(x,y,s,f,c=INK,anchor="la"): d.text((x,y),s,font=f,fill=c,anchor=anchor)
def wrap(s,f,mw):
    words=s.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)<=mw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines
def chip(x,y,label,fill,fg=(255,255,255),f=None):
    f=f or SANSB(8); w=int(d.textlength(label,font=f))+10
    d.rounded_rectangle([x,y,x+w,y+13],radius=3,fill=fill); d.text((x+5,y+1),label,font=f,fill=fg); return x+w+4
CHIPCOL={"CONFIRMED":GREEN,"OFFICIAL":BLUE,"REPORTED":(70,110,150),"CLAIM":ORANGE}
def scene(x,y,w,h,kind):
    d.rectangle([x,y,x+w,y+h],fill=(30,38,58) if kind in("tower","court") else (36,52,66) if kind=="gate" else (52,66,88))
    if kind=="tower":
        d.rectangle([x,y+h-8,x+w,y+h],fill=(16,20,32))
        for i,bx in enumerate(range(x+6,x+w-10,16)): d.rectangle([bx,y+h-26-(i%3)*8,bx+10,y+h-8],fill=(44,52,74))
        d.rectangle([x+w//2-13,y+8,x+w//2+13,y+h-8],fill=(70,86,120)); d.rectangle([x+w//2-9,y+2,x+w//2+9,y+10],fill=(96,116,150))
        for wy in range(y+14,y+h-12,12):
            for wx in (x+w//2-9,x+w//2+2): d.rectangle([wx,wy,wx+5,wy+6],fill=(255,214,110))
        d.ellipse([x+w-52,y+6,x+w-26,y+32],fill=(240,200,90)); d.ellipse([x+14,y+16,x+44,y+46],fill=(255,150,60)); d.ellipse([x+20,y+22,x+38,y+40],fill=(255,190,80))
        d.polygon([(x+30,y+52),(x+52,y+58),(x+30,y+64)],fill=(200,200,200)); d.text((x+58,y+50),"DRONE",font=SANSB(8),fill=(255,255,255))
    elif kind=="gate":
        d.rectangle([x,y+h-10,x+w,y+h],fill=(20,26,40))
        for i,bx in enumerate(range(x+8,x+w//2-14,26)): d.rectangle([bx,y+10,bx+20,y+h-10],fill=(120,40,40))
        d.rectangle([x+8,y+2,x+w//2-14,y+10],fill=(150,50,50)); d.rectangle([x+w//2-30,y+2,x+w//2-8,y+h-10],fill=(90,30,30))
        d.rectangle([x+w//2+2,y+18,x+w-10,y+56],fill=(245,240,225)); d.rectangle([x+w//2+6,y+22,x+w-14,y+52],fill=(255,255,255))
        for ly in range(y+28,y+48,6): d.line([x+w//2+10,ly,x+w-18,ly],fill=(120,120,120),width=1)
        d.text((x+w//2+10,y+6),"FILE",font=SANSB(9),fill=(255,220,120))
    elif kind=="court":
        d.rectangle([x,y+h-8,x+w,y+h],fill=(18,24,38))
        d.polygon([(x+8,y+26),(x+w//2,y+4),(x+w-8,y+26)],fill=(150,40,40)); d.rectangle([x+8,y+24,x+w-8,y+30],fill=(120,30,30))
        d.rectangle([x,y+30,x+w,y+h-8],fill=(36,52,80))
        d.text((x+w//2,y+34),"HUAWEI",font=SANSB(14),fill=(255,255,255),anchor="ma"); d.text((x+w//2,y+50),"10 / 12",font=SERIFB(13),fill=(255,214,110),anchor="ma")
# ---- header ----
d.rectangle([0,0,W,20],fill=RED); txt(10,3,"THE WORLD ON ONE DAY",SANSB(11),(255,255,255)); txt(W-10,3,"38 STORIES \u00b7 6 REGIONS \u00b7 13 FIELDS",SANSB(11),(255,255,255),anchor="ra")
txt(16,24,"Tuesday 24 November 2026",SERIFB(34)); txt(W-16,34,"TUESDAY EDITION",SANSB(11),RED,anchor="ra")
txt(16,64,"Riyadh tower hit again \u00b7 Shanghai party chief probed \u00b7 Huawei guilty on 10 of 12 counts",SERIF(13),RED)
REG=[("Europe",9,(30,90,160)),("Middle East",8,(178,34,34)),("Asia",8,(34,120,60)),("Africa",2,(176,132,28)),("Americas",7,(120,60,140)),("World/Space",4,(70,110,150))]
bx=16
for name,n,col in REG:
    w=int(60+n*14); d.rectangle([bx,84,bx+w,104],fill=col); txt(bx+w//2,88,f"{name} {n}",SANSB(10),(255,255,255),anchor="ma"); bx+=w+4
UTC=[("02:15","NATO vows space defence"),("08:16","Hanoi hot-pot blast"),("10:42","Saudi strikes Yemen"),("14:27","Riyadh tower hit"),("16:51","Houthis 60 km from Aden"),("18:58","Hormuz ship attack"),("20:41","Huawei guilty")]
txt(16,110,"THE DAY IN UTC",SANSB(10),RED); ux=16
for t,ev in UTC:
    tw=int(d.textlength(t+"  "+ev,font=SANSB(8)))+14; d.rectangle([ux,124,ux+tw,140],fill=CREAM,outline=(200,190,170))
    txt(ux+5,127,t,SANSB(8),RED); txt(ux+5+int(d.textlength(t+" ",font=SANSB(8))),127,ev,SANS(8)); ux+=tw+4
NUM=[("11","hurt in Riyadh"),("9","killed in Ukraine"),("50,018","Dow closes"),("+8.99%","Taiex record"),("25","killed in Yemen"),("26","Cikande toll"),("10/12","Huawei counts"),("96","drones at Ukraine")]
txt(16,146,"THE DAY IN NUMBERS",SANSB(10),RED); nx=16
for v,lab in NUM:
    w=max(int(d.textlength(v,font=SERIFB(17)))+16,96); d.rectangle([nx,160,nx+w,196],fill=(255,255,255),outline=(180,170,150))
    txt(nx+w//2,162,v,SERIFB(17),RED,anchor="ma"); txt(nx+w//2,182,lab,SANS(8),anchor="ma"); nx+=w+4

# ---- heroes ----
HERO=[(1,"RIYADH \u00b7 MIDDLE EAST","CONFIRMED","Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone struck the PIF tower, Riyadh's tallest, for the second time in a week. Eleven people were hurt: 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians. (Saudi officials \u00b7 AP)","tower"),(2,"SHANGHAI \u00b7 ASIA","OFFICIAL","China probes Shanghai party chief Chen Jining","Chen Jining, 62, is under investigation for \u201cserious violations\u201d. He is the fourth Politburo member to fall in a probe this year, the biggest shake-up in the party elite. (CCDI)","gate"),(3,"NEW YORK \u00b7 US/TECH","CONFIRMED","Huawei guilty on 10 of 12 counts","A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud. It was cleared of racketeering. Sentencing is set for Sep 2027. (US court)","court")]
hx=16
for n,loc,cl,hl,deck,kind in HERO:
    w=322; d.rectangle([hx,202,hx+w,368],fill=(255,255,255),outline=(170,160,140))
    scene(hx+4,206,w-8,66,kind)
    txt(hx+8,276,f"{n}  {loc}",SANSB(10),RED); chip(hx+8,290,cl,CHIPCOL[cl])
    for i,ln in enumerate(wrap(hl,SANSB(13),w-16)): txt(hx+8,304+i*15,ln,SANSB(13))
    for i,ln in enumerate(wrap(deck,SANS(9),w-16)[:3]): txt(hx+8,304+30+i*11,ln,SANS(9))
    hx+=w+8
# ---- cards 4-13 ----
CARDS=[(4,"ZAPORIZHZHIA \u00b7 EUROPE/WAR","REPORTED","Russian attacks kill 9 across Ukraine in a day","Russia killed 9 and wounded 81 in a day. Kyiv: 96 drones launched, 73 shot down or jammed. (Ukraine)","drone"),(5,"CAS \u00b7 AFRICA/SPORT","OFFICIAL","CAS hands Senegal back the AFCON title","CAS returned the Africa Cup title to Senegal after Morocco forfeited 3\u20130, so Senegal won 1\u20130. (CAS)","trophy"),(6,"HORMUZ \u00b7 MIDDLE EAST","REPORTED","IRGC attacks container ship in Hormuz","An IRGC attack hit a container ship in Hormuz at 18:58 UTC. Navigation was shut down north of Khasab, Oman. (UKMTO)","ship"),(7,"NEW YORK \u00b7 WORLD/MARKETS","CONFIRMED","Dow closes above 50,000 for the first time","The Dow closed at 50,018, its first finish above 50,000. Taiwan's Taiex jumped a record 8.99%. (Market close)","chart"),(8,"REDMOND \u00b7 WORLD/TECH","REPORTED","Microsoft declares \u2018Code Red\u2019 after historic outage","\u2018Code Red\u2019 after a 24-hour outage, the worst in Exchange Online history. Recovery target: 1 hour. (Reuters)","alert"),(9,"ESKISEHIR \u00b7 EUROPE","REPORTED","Turkish military helicopter crash kills 5","A Turkish military AS-532 helicopter crashed in Eskisehir, killing 5. Reported at 19:52 UTC. (Turkish officials)","heli"),(10,"CARTAGENA \u00b7 AMERICAS","REPORTED","Supermarket hostages: 25 held in Cartagena","25 held hostage in a Cartagena supermarket. Five elderly women freed; airport landings halted about 45 minutes. (Colombia)","hostage"),(11,"ADEN \u00b7 MIDDLE EAST","REPORTED","Houthis advance within 60 km of Aden","Houthi forces advanced to within 60 km of Aden, Yemen, pressing toward the port city. Reported at 16:51 UTC. (Wires)","advance"),(12,"LAHJ \u00b7 MIDDLE EAST","REPORTED","Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes on a bus and truck in Wadi Maabaq, Lahj, killed or left missing 25 and wounded 6. (Yemeni officials)","strike"),(13,"JIUQUAN \u00b7 WORLD/SPACE","OFFICIAL","China names first foreign astronaut for Tiangong","Shenzhou-24 crew named: Tang Hongbo, Wu Yi and Zeeshan Ali (Pakistan), the first foreigner bound for Tiangong. (CMSA)","rocket")]
def cardscene(x,y,w,h,kind):
    d.rectangle([x,y,x+w,y+h],fill=(44,58,84))
    if kind=="drone": d.ellipse([x+w-34,y+4,x+w-8,y+30],fill=(255,150,60)); d.polygon([(x+8,y+26),(x+34,y+30),(x+8,y+34)],fill=(220,220,220)); d.rectangle([x,y+h-6,x+w,y+h],fill=(16,20,32))
    elif kind=="trophy": d.ellipse([x+w//2-14,y+6,x+w//2+14,y+30],fill=(255,214,110)); d.rectangle([x+w//2-4,y+30,x+w//2+4,y+40],fill=(255,214,110)); d.rectangle([x+w//2-16,y+40,x+w//2+16,y+44],fill=(200,160,60)); d.rectangle([x,y+h-6,x+w,y+h],fill=(20,90,50))
    elif kind=="ship": d.rectangle([x+10,y+18,x+w-10,y+28],fill=(120,40,40)); d.rectangle([x+w//2-8,y+6,x+w//2+8,y+18],fill=(200,200,200)); d.rectangle([x,y+28,x+w,y+h],fill=(30,90,140))
    elif kind=="chart": d.line([(x+6,y+h-8),(x+w//4,y+26),(x+w//2,y+32),(x+3*w//4,y+14),(x+w-6,y+6)],fill=(255,214,110),width=3); d.line([(x+6,y+14),(x+w-6,y+14)],fill=(220,60,60),width=2); txt(x+w-4,y+2,"50,000",SANSB(8),(255,255,255),anchor="ra")
    elif kind=="alert": d.rectangle([x+w//2-16,y+6,x+w//2+16,y+34],fill=(200,30,30)); txt(x+w//2,y+10,"!",SERIFB(20),(255,255,255),anchor="ma"); d.rectangle([x,y+h-6,x+w,y+h],fill=(60,10,10))
    elif kind=="heli": d.ellipse([x+12,y+10,x+w-12,y+24],fill=(90,110,130)); d.line([(x+10,y+14),(x+w-4,y+14)],fill=(200,200,200),width=2); d.rectangle([x+w-26,y+24,x+w-6,y+32],fill=(70,90,110))
    elif kind=="hostage": d.rectangle([x+8,y+8,x+w-8,y+30],fill=(150,50,50)); d.rectangle([x+16,y+12,x+w-16,y+18],fill=(255,220,120)); d.rectangle([x+16,y+20,x+w-16,y+24],fill=(255,255,255))
    elif kind=="advance": d.polygon([(x+10,y+30),(x+w//2,y+6),(x+w-10,y+30)],fill=(200,90,20)); txt(x+w//2,y+14,"60 km",SANSB(9),(255,255,255),anchor="ma"); d.rectangle([x,y+h-6,x+w,y+h],fill=(120,60,20))
    elif kind=="strike": d.ellipse([x+14,y+6,x+44,y+28],fill=(255,150,60)); d.ellipse([x+22,y+12,x+36,y+24],fill=(255,200,90)); d.rectangle([x,y+h-6,x+w,y+h],fill=(40,30,20))
    elif kind=="rocket": d.polygon([(x+w//2-8,y+26),(x+w//2-8,y+10),(x+w//2,y+2),(x+w//2+8,y+10),(x+w//2+8,y+26)],fill=(230,230,230)); d.ellipse([x+w//2-8,y+26,x+w//2+8,y+33],fill=(255,150,60)); d.rectangle([x,y+h-6,x+w,y+h],fill=(10,16,30))
cx0,cy0=16,374
for i,(n,loc,cl,hl,deck,kind) in enumerate(CARDS):
    r,c=divmod(i,5); x=cx0+c*198; y=cy0+r*124; w=190
    d.rectangle([x,y,x+w,y+120],fill=(255,255,255),outline=(170,160,140))
    cardscene(x+4,y+4,w-8,34,kind)
    txt(x+6,y+42,f"{n}  {loc}",SANSB(8),RED); chip(x+6,y+54,cl,CHIPCOL[cl])
    for j,ln in enumerate(wrap(hl,SANSB(10),w-12)[:2]): txt(x+6,y+68+j*11,ln,SANSB(10))
    for j,ln in enumerate(wrap(deck,SANS(8),w-12)[:3]): txt(x+6,y+92+j*9,ln,SANS(8))

# ---- map (equirectangular, real lat/lon) ----
MX0,MY0,MW,MH=16,624,644,188
def mp(lat,lon): return MX0+(lon+168)/360*MW, MY0+(74-lat)/105*MH
d.rectangle([MX0,MY0,MX0+MW,MY0+MH],fill=(214,228,238),outline=(170,160,140))
CONT=[[(71,-156),(70,-140),(68,-125),(60,-125),(58,-135),(48,-125),(40,-124),(32,-117),(25,-110),(20,-105),(15,-92),(10,-85),(8,-80),(12,-72),(18,-66),(25,-80),(30,-85),(35,-76),(40,-74),(45,-67),(50,-60),(55,-60),(60,-65),(65,-68),(70,-90),(68,-110)],[(10,-75),(5,-77),(0,-80),(-5,-81),(-15,-75),(-25,-70),(-35,-70),(-45,-73),(-52,-68),(-40,-62),(-30,-48),(-20,-40),(-10,-35),(-5,-35),(0,-50),(5,-52),(10,-60)],[(70,20),(70,30),(60,30),(58,25),(55,20),(50,10),(48,5),(43,0),(40,-5),(37,-8),(36,0),(40,5),(44,10),(45,15),(50,18),(55,20),(60,10),(65,12)],[(35,-6),(32,10),(30,32),(25,35),(20,38),(15,40),(11,44),(10,50),(5,48),(0,42),(-5,40),(-10,40),(-15,40),(-20,35),(-25,32),(-30,28),(-35,20),(-30,15),(-20,12),(-10,13),(-5,12),(0,9),(5,5),(10,-5),(15,-15),(20,-16),(25,-15),(30,-10)],[(70,60),(70,100),(70,140),(68,170),(65,180),(60,162),(55,140),(50,140),(45,135),(40,128),(35,122),(30,120),(25,118),(20,110),(15,105),(10,100),(8,98),(10,95),(15,92),(20,88),(25,85),(22,80),(18,75),(15,73),(12,70),(8,77),(12,80),(15,80),(20,86),(23,90),(28,95),(30,100),(35,105),(40,110),(42,115),(45,120),(50,125),(55,130),(60,135),(65,150),(68,160),(30,35),(28,42),(25,48),(20,55),(15,52),(12,45),(15,42),(20,38),(25,35),(30,32)], [(-12,132),(-15,140),(-20,148),(-25,153),(-30,153),(-35,150),(-38,145),(-35,138),(-32,132),(-28,125),(-20,118),(-15,122)],[(58,-5),(55,-2),(52,0),(50,-3),(54,-5)],[(45,141),(40,140),(35,138),(32,130),(35,133),(40,140)],[(0,100),(-5,110),(-7,115),(-8,120),(-5,125),(0,130)]]
for poly in CONT: d.polygon([mp(la,lo) for la,lo in poly],fill=(120,160,110),outline=(80,120,80))
txt(MX0+6,MY0+4,"WORLD MAP \u00b7 13 STORIES PINNED",SANSB(9),NAVY)
PINS=[(1,24.7,46.7),(2,31.2,121.5),(3,40.7,-74),(4,47.8,35.2),(5,14.7,-17.4),(6,26.5,56.3),(7,40.7,-74),(8,47.7,-122.1),(9,39.8,30.5),(10,10.4,-75.5),(11,12.8,45.0),(12,13.0,44.9),(13,39.7,98.5)]
OFF={7:(16,-12),12:(-20,12),9:(-18,10)}
for n,la,lo in PINS:
    x,y=mp(la,lo); dx,dy=OFF.get(n,(0,0)); px,py=x+dx,y+dy
    if (dx,dy)!=(0,0): d.line([x,y,px,py],fill=RED,width=1)
    d.ellipse([px-8,py-8,px+8,py+8],fill=RED,outline=(255,255,255),width=2); txt(px,py-6,str(n),SANSB(9),(255,255,255),anchor="ma")
LEG=[(1,"Riyadh"),(2,"Shanghai"),(3,"New York \u00b7 Huawei"),(4,"Zaporizhzhia"),(5,"Dakar \u00b7 CAS"),(6,"Hormuz"),(7,"New York \u00b7 Dow"),(8,"Redmond"),(9,"Eskisehir"),(10,"Cartagena"),(11,"Aden"),(12,"Lahj"),(13,"Jiuquan")]
txt(676,624,"WHERE IT HAPPENED",SANSB(10),RED)
for i,(n,city) in enumerate(LEG):
    y=642+i*14; d.ellipse([676,y,688,y+12],fill=RED); txt(682,y+1,str(n),SANSB(8),(255,255,255),anchor="ma"); txt(692,y+1,f"{n}. {city}",SANS(9))
# ---- ALSO ----
ALSO=[(14,"Ankara","Haftar visits Turkey for the first time","REPORTED"),(15,"London","UK sanctions Houthis + 4 officials","OFFICIAL"),(16,"Villavicencio","Car bomb injures 23","REPORTED"),(17,"Gaza","Israel kills Hamas security chief","REPORTED"),(18,"Baghdad","Iraq orders control of Kurdish oilfields","OFFICIAL"),(19,"Gaza","Meningitis alert: 272 cases in Oct","OFFICIAL"),(20,"DR Congo","Missing Cessna 208, rebels claim shootdown","CLAIM"),(21,"Hanoi","Hot-pot explosion kills \u22656","REPORTED"),(22,"Gulf of Finland","Ukraine hits Russian ship Sparta II","REPORTED"),(23,"Kuala Lumpur","Malaysia to return migrants to Myanmar","OFFICIAL"),(24,"Ulleungdo","S. Korea shelter order, Russian jets in ADIZ","OFFICIAL"),(25,"Dhaka","Hasina plans return 16 Dec","REPORTED"),(26,"The Hague","14 nations endorse ICJ Myanmar ruling","REPORTED"),(27,"Jakarta","Indonesia nominates 2 VP candidates","OFFICIAL"),(28,"Beijing","China sentences official Ma to death","OFFICIAL"),(29,"Brussels","NATO vows defence against space threat","OFFICIAL"),(30,"Mexico City","US drone aided El Chapo capture (Fri 20 Nov)","REPORTED"),(31,"San Salvador","Bukele names 3 soldiers killed in Haiti","OFFICIAL"),(32,"Ottawa","Pentagon rebukes Canada: only 41.9% of air fleet ready","REPORTED"),(33,"Washington","US adds Megaspeed to trade blacklist","OFFICIAL"),(34,"Kyiv","Zelensky urges talks soon","REPORTED"),(35,"Ras Al Khaimah","UAE bus-truck crash kills 13","REPORTED"),(36,"London","England record 5,258 heat deaths, summer 2026","OFFICIAL"),(37,"Kourou","Ariane 6 lofts 36 Amazon satellites","OFFICIAL"),(38,"Cikande","Factory-fire toll rises to 26","REPORTED")]
txt(16,818,"ALSO ON TUESDAY 24 NOVEMBER \u2014 25 MORE STORIES",SANSB(11),RED)
for i,(n,city,hl,cl) in enumerate(ALSO):
    r,c=divmod(i,3); x=16+c*336; y=836+r*12
    d.ellipse([x,y,x+10,y+10],fill=CHIPCOL[cl]); txt(x+5,y+1,str(n),SANSB(7),(255,255,255),anchor="ma")
    s=f"{city}: {hl}"; txt(x+13,y+1,s,SANS(8))
# ---- DATE CHECK + footer ----
d.rectangle([16,938,1008,998],fill=(255,240,240),outline=RED)
txt(22,942,"DATE CHECK",SANSB(10),RED)
dc="Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC."
txt(22,954,dc,SANS(9))
lo="LEFT OUT (not 24 Nov): Hormuz mine claims (Mon 23 Nov) \u00b7 Huang returns as Nvidia CEO (Mon 23 Nov) \u00b7 EU sanctions package 22 (Mon 23 Nov) \u00b7 COP31 ends with no deal (Sun 22 Nov) \u00b7 Merkury sunk (Sat 22 Nov) \u00b7 El Chapo Isidro arrested (Fri 20 Nov) \u00b7 Cikande fire began (Sat 21 Nov) \u00b7 Trump hush-money appeal ruling (Mon 23 Nov) \u00b7 ATP final (Sun 22 Nov) \u00b7 Las Vegas GP (Sat 21 Nov) \u00b7 ICJ Myanmar ruling (last week)."
ny="NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC) \u00b7 MPR session picks VP (11 Dec) \u00b7 Huawei sentencing (Sep 2027) \u00b7 Hasina returns to Bangladesh (16 Dec) \u00b7 COP32 final decision / venue (not set)."
for i,ln in enumerate(wrap(lo,SANS(8),970)): txt(22,966+i*10,ln,SANS(8))
for i,ln in enumerate(wrap(ny,SANS(8),970)): txt(22,966+len(wrap(lo,SANS(8),970))*10+i*10,ln,SANS(8))
txt(16,1002,"Sources: Saudi officials \u00b7 CCDI \u00b7 US court \u00b7 Ukrainian officials \u00b7 CAS \u00b7 UKMTO \u00b7 Reuters \u00b7 AP \u00b7 CMSA \u00b7 wires.",SANS(8),GREY)
txt(16,1012,"CONFIRMED = 2+ outlets \u00b7 OFFICIAL = on record \u00b7 REPORTED = one outlet \u00b7 CLAIM = one side's claim.  Scenes are drawn illustrations, not photographs.",SANS(8),GREY)
out=os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR","out"),"entry.png"); os.makedirs(os.path.dirname(out),exist_ok=True); im.save(out); print("saved",out,os.path.getsize(out))
