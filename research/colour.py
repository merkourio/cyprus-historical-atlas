import math
def hex2rgb(h):
    h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def over(fg,bg,a):
    return tuple(fg[i]*a+bg[i]*(1-a) for i in range(3))
def _f(t): return t**(1/3) if t>0.008856 else 7.787*t+16/116
def lab(rgb):
    r,g,b=[c/255 for c in rgb]
    r,g,b=[((c+0.055)/1.055)**2.4 if c>0.04045 else c/12.92 for c in (r,g,b)]
    x=(r*0.4124+g*0.3576+b*0.1805)/0.95047
    y=(r*0.2126+g*0.7152+b*0.0722)/1.0
    z=(r*0.0193+g*0.1192+b*0.9505)/1.08883
    fx,fy,fz=_f(x),_f(y),_f(z)
    return (116*fy-16, 500*(fx-fy), 200*(fy-fz))
def dE(c1,c2):
    """CIE76 in Lab; good enough to rank which pairs are confusable."""
    a,b=lab(c1),lab(c2)
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(3)))
