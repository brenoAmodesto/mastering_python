"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidare (ruim)
"""



velocidade = 61 #velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada



RADAR_1 = 60    #velocidade máxima do radar 1
LOCAL_1 = 100   # local onde o radar está
RADAR_RANGE = 1 # a distância onde o radar pega




vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and  local_carro <= (LOCAL_1 + RADAR_RANGE)




if vel_carro_passou_radar_1: print (" Velocidade carro passou do radar 1")

if carro_multado_radar_1 and vel_carro_passou_radar_1:
    
    print("Carro multado")