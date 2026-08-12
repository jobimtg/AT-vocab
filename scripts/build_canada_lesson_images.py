#!/usr/bin/env python3
"""Build deterministic Canada Life lesson gallery images from validated JSON."""
from __future__ import annotations
import argparse, json, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

W,H=1920,1080
NAVY="#092b50"; ORANGE="#bd4318"; CREAM="#fff8e8"; GOLD="#d59b48"; PALE="#f5ead2"
FONT=Path(r"C:\Windows\Fonts\ARIALUNI.TTF")
BOLD=Path(r"C:\Windows\Fonts\msjhbd.ttc")
TC=Path(r"C:\Windows\Fonts\msjh.ttc")

def font(n,b=False,tc=False): return ImageFont.truetype(str(TC if tc else (BOLD if b else FONT)),n)
def base(title,subtitle=""):
 im=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(im)
 d.rectangle((0,0,W,142),fill=NAVY); d.text((55,22),title,fill="white",font=font(58,True,True))
 if subtitle:d.text((58,93),subtitle,fill="#ffd49b",font=font(28,False,True))
 d.text((1510,35),"YSP Learn & Shine",fill="white",font=font(35,True)); d.text((1513,84),"CANADA LIFE ENGLISH",fill="#ffb26f",font=font(22,True))
 d.rectangle((24,164,1896,1035),outline=GOLD,width=4); d.text((640,1042),"YOUR JOURNEY. YOUR VOICE. YOUR FUTURE.",fill=NAVY,font=font(23,True))
 return im,d
def wrap(d,text,f,width):
 words=text.split(); lines=[]; cur=""
 for w in words:
  test=(cur+" "+w).strip()
  if d.textbbox((0,0),test,font=f)[2]<=width:cur=test
  else:
   if cur:lines.append(cur)
   cur=w
 if cur:lines.append(cur)
 return lines
def block(d,text,x,y,width,size=30,fill=NAVY,bold=False,leading=8):
 f=font(size,bold); lines=wrap(d,text,f,width)
 for line in lines:d.text((x,y),line,fill=fill,font=f); y+=size+leading
 return y
def save(im,path): im.save(path,"PNG",optimize=True)
def phrases(data,out):
 im,d=base("USEFUL PHRASES — 實用句型",data["meta"]["title_en"])
 y=185
 for i,p in enumerate(data["phrases"],1):
  d.rounded_rectangle((50,y,1870,y+150),18,fill="#fffdf7",outline=GOLD,width=2); d.ellipse((75,y+35,155,y+115),fill=ORANGE if i<4 else NAVY); d.text((99,y+48),str(i),fill="white",font=font(31,True))
  d.text((185,y+18),p["en"],fill=NAVY,font=font(33,True)); d.text((185,y+66),p["zh"],fill="#222",font=font(28,False,True))
  nf=font(24,False,True); ny=y+25
  for line in wrap(d,p["note"],nf,760): d.text((1050,ny),line,fill=ORANGE,font=nf); ny+=29
  y+=164
 save(im,out/"ca-life-l01-phrases-1.png")
def pron(data,out):
 p=data["pronunciation"]; im,d=base("PRONUNCIATION SPOTLIGHT — 發音焦點",p["focus"]); d.text((65,160),p["fz"],fill=ORANGE,font=font(29,True,True))
 x=45
 for i,w in enumerate(p["words"],1):
  d.rounded_rectangle((x,215,x+350,735),20,fill="#fffdf7",outline=GOLD,width=3); d.text((x+25,240),f"{i}  {w['w']}",fill=NAVY,font=font(39,True)); d.text((x+25,305),w["ipa"],fill=NAVY,font=font(37)); d.text((x+25,375),f"X {w['bad']}  →  OK {w['w']}",fill=ORANGE,font=font(27,True)); block(d,w["tip"],x+25,455,300,27,NAVY,False,8); x+=375
 d.rounded_rectangle((55,770,920,1005),20,fill=PALE,outline=ORANGE,width=3); block(d,p["tip"],90,815,790,36,NAVY,True,12)
 d.rounded_rectangle((955,770,1865,1005),20,fill="#fffdf7",outline=NAVY,width=3); d.text((995,800),"PRACTICE SENTENCE",fill=ORANGE,font=font(28,True)); block(d,p["prac"],995,855,820,34,NAVY,True,10)
 save(im,out/"ca-life-l01-pronunciation-1.png")
def dialogue(data,dlg,out,practice=False):
 kind="PRACTICE" if practice else "MODEL"; im,d=base(f"DIALOGUE {dlg['id']} — {kind}",f"{dlg['title']}｜{dlg['tz']}")
 d.rounded_rectangle((45,180,430,990),20,fill=PALE,outline=GOLD,width=3); d.text((75,215),"SITUATION",fill=ORANGE,font=font(29,True)); y=block(d,dlg["sit"],75,265,325,29,NAVY,True,9); d.text((75,y+35),"CHARACTERS",fill=ORANGE,font=font(29,True)); block(d,f"A  {dlg['rA']}\nB  {dlg['rB']}",75,y+88,325,28,NAVY,True,10)
 d.rounded_rectangle((455,180,1875,990),20,fill="#fffdf7",outline=GOLD,width=3); y=205; size=25 if len(dlg["lines"])>=11 else 29
 for role,line in dlg["lines"]:
  col=NAVY if role=="A" else ORANGE; d.ellipse((485,y,530,y+45),fill=col); d.text((499,y+6),role,fill="white",font=font(23,True)); y=block(d,line,550,y,1280,size,NAVY,False,6)+5
 if practice:
  d.rounded_rectangle((475,820,1855,970),18,fill="#fff0df",outline=ORANGE,width=3); d.text((505,840),"NOW YOU TRY! 換你說",fill=ORANGE,font=font(27,True)); block(d,dlg["tp"],505,885,1300,25,ORANGE,True,5)
 save(im,out/f"ca-life-l01-d{dlg['id']:02d}-{'practice' if practice else 'model'}.png")
def speaking(data,out):
 im,d=base("SPEAKING QUESTIONS — 口說練習",data["meta"]["title_en"]); y=180
 for i,s in enumerate(data["speaking"],1):
  d.rounded_rectangle((55,y,1865,y+155),18,fill="#fffdf7",outline=GOLD,width=2); d.text((82,y+35),f"Q{i}",fill=ORANGE,font=font(36,True)); block(d,s["q"],180,y+18,1080,29,NAVY,True,6); block(d,s["h"],1280,y+25,540,24,ORANGE,False,5); y+=165
 save(im,out/"ca-life-l01-speaking-1.png")
def culture(data,c,out,index):
 im,d=base("CANADIAN CULTURE — 加拿大文化",f"{c['title']}｜{c['tz']}"); d.rounded_rectangle((55,190,1170,980),20,fill="#fffdf7",outline=GOLD,width=3); d.text((90,225),"CULTURE NOTES",fill=ORANGE,font=font(30,True)); block(d,c["notes"],90,285,1035,32,NAVY,False,11)
 d.rounded_rectangle((1200,190,1865,980),20,fill=PALE,outline=GOLD,width=3); d.text((1240,225),"DISCUSSION",fill=ORANGE,font=font(30,True)); y=290
 for i,q in enumerate(c["qs"],1): d.text((1240,y),f"{i}.",fill=ORANGE,font=font(28,True)); y=block(d,q,1290,y,520,27,NAVY,True,7)+30
 save(im,out/f"ca-life-l01-culture-{index}.png")
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--input",required=True);ap.add_argument("--output",required=True);a=ap.parse_args();data=json.loads(Path(a.input).read_text(encoding="utf-8"));out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
 phrases(data,out);pron(data,out)
 for dlg in data["dialogues"]: dialogue(data,dlg,out);dialogue(data,dlg,out,True)
 speaking(data,out)
 for i,c in enumerate(data["culture"],1):culture(data,c,out,i)
if __name__=="__main__":main()
