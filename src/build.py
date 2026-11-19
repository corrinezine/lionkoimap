import base64,io,json,sys,urllib.parse
from PIL import Image
P=sys.argv[1]; tpl=sys.argv[2]
def png(name,h):
    im=Image.open(f"{P}/插画/{name}").convert("RGBA");im.thumbnail((h*2,h))
    im=im.crop(im.getbbox());b=io.BytesIO();im.save(b,"PNG",optimize=True)
    return "data:image/png;base64,"+base64.b64encode(b.getvalue()).decode()
def jpg(name):
    im=Image.open(f"{P}/图片/{name}").convert("RGB");im.thumbnail((640,640));b=io.BytesIO();im.save(b,"JPEG",quality=86)
    return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()
imgs={"logo":png("地图.png",200),"illoA":png("白色小狮猫.png",320),"illoB":png("黑色小鲤猫.png",320),
      "illoC":png("图层 5.png",320),"illoD":png("黑猫.png",320),
      "songfa":jpg("松发肉骨茶.jpg"),"katong":jpg("328加东叻沙.jpg"),"founder":jpg("发起人肉骨茶-名人墙.jpg"),"ngahsio":jpg("黄亚细.jpg"),"leongkee":jpg("梁记巴生.jpg"),"sungei":jpg("结霜桥叻沙.jpg"),"diylaksa":jpg("自选叻沙.jpg"),"qr":"data:image/png;base64,"+base64.b64encode(open(f"{P}/图片/二维码.png","rb").read()).decode()}
def svgimg(cls,w,h,body):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" preserveAspectRatio="none">{body}</svg>'
    return f'<img class="{cls}" alt="" src="data:image/svg+xml;charset=utf-8,{urllib.parse.quote(s)}">'
wt=svgimg("wave-top",900,22,'<path d="M0 0 H900 V8 C860 18 820 4 770 12 S680 20 620 10 S520 2 460 12 S350 20 290 10 S180 2 120 12 S40 18 0 8 Z" fill="#B5572A"/>')
wb=svgimg("wave-bot",900,18,'<path d="M0 18 H900 V8 C850 0 800 14 740 8 S640 0 580 9 S470 16 410 8 S300 0 240 9 S120 16 60 8 S20 4 0 8 Z" fill="#B5572A"/>')
ul=svgimg("underline",360,18,'<path d="M4 10 C60 2 120 16 175 9" stroke="#E0A13A" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M200 9 C250 3 300 15 356 7" stroke="#E0A13A" stroke-width="4" fill="none" stroke-linecap="round"/>')
pin='<svg xmlns="http://www.w3.org/2000/svg" width="14" height="18" viewBox="0 0 14 18"><path d="M7 0C3.1 0 0 3.1 0 7c0 5.2 7 11 7 11s7-5.8 7-11c0-3.9-3.1-7-7-7zm0 9.6A2.6 2.6 0 1 1 7 4.4a2.6 2.6 0 0 1 0 5.2z" fill="#7A5A3A"/></svg>'
font="data:font/woff2;base64,"+base64.b64encode(open(f"{P}/字体/NanoOldSongA-subset.woff2","rb").read()).decode()
h=open(tpl,encoding="utf8").read()
for k,v in {"{{FONT}}":font,"{{IMAGES}}":json.dumps(imgs),"{{PIN}}":"data:image/svg+xml;charset=utf-8,"+urllib.parse.quote(pin),
            "{{WAVE_TOP}}":wt,"{{WAVE_BOT}}":wb,"{{UNDERLINE}}":ul}.items():
    assert k in h,k; h=h.replace(k,v)
out=f"{P}/新加坡美食攻略.html";open(out,"w",encoding="utf8").write(h);print(len(h)//1024,"KB")
