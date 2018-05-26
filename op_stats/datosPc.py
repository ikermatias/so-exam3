import psutil

class Datos():

 @classmethod
 def darPorcentajeCpu(cls):
  return psutil.cpu_percent()
 @classmethod
 def darMemoriaRam(cls):
  arregloMemoria = psutil.virtual_memory()
  memoriaDisponible = arregloMemoria[1]
  return memoriaDisponible
 @classmethod
 def darEspacioLibreDisco(cls):
  arregloDisco = psutil.disk_usage('/')
  espacioDisponible = arregloDisco[2]
  return espacioDisponible
