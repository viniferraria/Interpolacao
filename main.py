import math

def interpolacao(x, x_valores, f_valores):
  x_valores = list(map(float, x_valores))
  f_valores = list(map(float, f_valores))
  resultado_final = 0
  for i in range(len(x_valores)):
    temp_x = 1
    temp_y = 1
    for j in range(len(x_valores)):
      if j!=i:
        temp_x *= round((x-x_valores[j]),4)
        temp_y *= round((x_valores[i]-x_valores[j]),4)
    resultado_final += (temp_x/temp_y)*f_valores[i]
  return resultado_final

#1)a)
x = 8.4
x_valores = [8.1, 8.3, 8.6, 8.7]
f = [16.94410, 17.56492, 18.50515, 18.82091]

#1)b)
x1 = -1/3
x_valores_1 = [-0.75, -0.5, -0.25, 0]
f1 = [-0.07181250, -0.02475000, 0.33493750, 1.1010000]

#1)c)
x2 = 0.25
x_valores_2 = [0.1, 0.2, 0.3, 0.4]
f2 = [0.62049958, -0.28398668, 0.0066095, 0.24842440]

#1)d)
x3 = 0.9
x_valores_3 = [0.6, 0.7, 0.8, 1]
f3 = [-0.17694460, 0.01375227, 0.22363362, 0.65809197]

#2)a)
x4 = 0.25
x_valores_4 = [0, 1, 2]
f4 = [math.exp(0), math.exp(1), math.exp(2)]

#2)b)
x5 = 0.75

print("Interpolação - Exercícios Extra-Classe\n")
print("1)a) = {}".format(interpolacao(x, x_valores, f)))
print("  b) = {}".format(interpolacao(x1, x_valores_1, f1)))
print("  c) = {}".format(interpolacao(x2, x_valores_2, f2)))
print("  d) = {}\n".format(interpolacao(x3, x_valores_3, f3)))
print("2)a) = {}".format(interpolacao(x4, x_valores_4, f4)))
print("  b) = {}\n".format(interpolacao(x5, x_valores_4, f4)))