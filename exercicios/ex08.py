medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10

print('A medida {} metros representada em quilometros é igual a {}KM \nEm Hectómetro a {}hm\nEm decâmetro a {}dam\nEm decímetro a {}dm\nEm centímetro a {}cm\nEm milímetro a {}mm'.format(medida,km,hm,dam,dm,cm,mm))