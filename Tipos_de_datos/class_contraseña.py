class Usuario:
  def __init__(self, nombre, correo, contraseña):
    self. nombre = nombre
    self. correo = correo
    self.__contraseña = contraseña #indicar que el atributo se busca sea privado
  def mostrar(self):
    print(f"Nombre:{self.nombre}\n correo:{self.correo}\n contraseña:{self.contraseña}")
  @property
  def contraseña(self):
    return self.__contraseña
  @contraseña.setter
  def contraseña(self, nueva_contraseña):
    self.__contraseña = self.validar_contraseña(nueva_contraseña)
  def validar_contraseña(self, contraseña):
    if len(contraseña) >= 8:
      return contraseña
    else:
      print("contraseña incorrecta")
      raise ValueError("La contraseña debe contener al menos 8 caracteres")
    
