import svgwrite
import math

width = 700
height= 700

tarde = "#68302b","#783127","#893322","#9a341d","#ab3518","#bc3713","#cd380e","#dd390a","#ee3b05","#ff3c00"

# Para hacer el triangulo equilatero, apartir
# de un segmento calculas la altura y se traza los otros
# dos segmentos
raiz_3 = 1.7320508 # Raiz cuadrada de 3
h = (raiz_3 * width)/2 + 2 #Calcular la altura de t_equilatero


razon = 1/25#La razon de los segmentos 


dwg = svgwrite.Drawing('tronco.svg', size = (width*2, h*2))  # output will be in the same folder as this script


def _triangulo(x1,y1,x2,y2,x3,y3):
	points=[(x1,y1),(x2,y2),(x3,y3),(x1,y1)]
	#Trinagulo base
	dwg.add(dwg.polyline(points,fill="none",stroke="black",stroke_width=1))
		
	new_pts = []
	for i in range(75):
		x4 = (x2 + (razon*x3))/ (1+razon)
		y4 = (y2 + (razon*y3))/ (1+razon)

		x5 = (x3 + (razon*x1))/ (1+razon)
		y5 = (y3 + (razon*y1))/ (1+razon)

		x6 = (x1 + (razon*x4))/ (1+razon)
		y6 = (y1 + (razon*y4))/ (1+razon)

		new_pts = [(x4,y4),(x5,y5),(x6,y6),(x4,y4)]

		dwg.add(dwg.polyline(new_pts,fill="none",stroke="black",stroke_width=1))
		
		x1,y1 = x4,y4
		x2,y2 = x5,y5
		x3,y3 = x6,y6

'''
   # HEXAGONO --------------------------
x1,y1 = width*0.5,2
x2,y2 = 0,h
x3,y3 = width,h
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = width*0.5,2
x2,y2 = width*1.5,2
x3,y3 = width,h
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = width*1.5,2
x2,y2 = width,h
x3,y3 = width*2,h
_triangulo(x1,y1,x2,y2,x3,y3)


x1,y1 = width*2,h
x2,y2 = width*1.5,h*2
x3,y3 = width,h
_triangulo(x1,y1,x2,y2,x3,y3)


x1,y1 = width*1.5,h*2
x2,y2 = width,h
x3,y3 = width*0.5,h*2
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = width*0.5,h*2
x2,y2 = 0,h
x3,y3 = width,h
_triangulo(x1,y1,x2,y2,x3,y3)

#HEXAGONO --------------------------
'''
# TRIANGULO EQUILATERO

#Punto donde intersectan dos lineas
def pnt_int(px1,py1,px2,py2,px3,py3,px4,py4):
	
	ua_n = (px4-px3)*(py1-py3) - (py4-py3)*(px1-px3)
	ua_d = (py4-py3)*(px2-px1) - (px4-px3)*(py2-py1) 

	ub_n = (px2-px1)*(py1-py3) - (py2-py1)*(px1-px3)
	ub_d = (py4-py3)*(px2-px1) - (px4-px3)*(py2-py1) 

	ua = ua_n / ua_d
	ub = ub_n / ub_d  

	x = px1 + (ua*(px2-px1))
	y = py1 + (ua*(py2-py1))
	return x,y

px1,py1 = (width)*(0.5),(h*2)* (0.5)
px2,py2 = width*2,h*2
px3,py3 = width,0
px4,py4 = width,h*2
x,y = pnt_int(px1,py1,px2,py2,px3,py3,px4,py4)

x1,y1 = x,y
x2 = (width)*(0.5)
y2 = (h*2)* (0.5)
x3,y3 = width,0
_triangulo(x1,y1,x2,y2,x3,y3)


x1,y1 = x,y
x2 = (width)*(0.5)
y2 = (h*2)* (0.5)
x3,y3 = 0,h*2
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = x,y
x2 = ((width*2) + width)* (.5)
y2 = (h*2)* (.5)
x3,y3 = width,0
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = x,y
x2 = ((width*2) + width)* (.5)
y2 = (h*2)* (.5)
x3,y3 = width*2,h*2
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = width,h*2
x2,y2 = 0, h*2
x3,y3 = x,y
_triangulo(x1,y1,x2,y2,x3,y3)

x1,y1 = width,h*2
x2,y2 = width*2, h*2
x3,y3 = x,y
_triangulo(x1,y1,x2,y2,x3,y3)


# Save the file
dwg.save()
