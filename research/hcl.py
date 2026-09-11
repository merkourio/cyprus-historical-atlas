import math
def lab2rgb(L,a,b):
    fy=(L+16)/116; fx=fy+a/500; fz=fy-b/200
    def inv(t): return t**3 if t**3>0.008856 else (t-16/116)/7.787
    X,Y,Z=inv(fx)*0.95047, inv(fy)*1.0, inv(fz)*1.08883
    r= X*3.2406+Y*-1.5372+Z*-0.4986
    g= X*-0.9689+Y*1.8758+Z*0.0415
    bb=X*0.0557+Y*-0.2040+Z*1.0570
    out=[]
    for c in (r,g,bb):
        c=1.055*(c**(1/2.4))-0.055 if c>0.0031308 else 12.92*c
        out.append(max(0,min(255,round(c*255))))
    return tuple(out)
def hcl(L,C,H): return lab2rgb(L, C*math.cos(math.radians(H)), C*math.sin(math.radians(H)))
def rgb2hex(t): return '#%02X%02X%02X'%t
def inrange(t): return all(0<c<255 for c in t)
