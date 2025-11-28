from math import sqrt,pow
class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def formarTriangulo(self):
        c1 = self.lado1 > self.lado2+self.lado3
        c2 = self.lado2 > self.lado1+self.lado3
        c3 = self.lado3 > self.lado1+self.lado2
        return c1 and c2 and c3
    
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def area(self):
        p = self.perimetro() / 2
        return sqrt(p * (p-self.lado1) * (p-self.lado2) * (p-self.lado3))
    
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'Equilatero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'Isósceles'
        return 'Escaleno'
 
class Retangulo:
    def __init__(self, lado1,lado2,cor):
        self.lado1 = lado1
        self.lado2 = lado2
        self.cor = cor
    
    def quadrado(self):
        return self.lado1 == self.lado2
    
    def diagonal(self):
        return sqrt(pow(self.lado1,2)+pow(self.lado2,2))
    
    def perimetro(self):
        return 2 * self.lado1+ 2 * self.lado2
    
    def mesmoPerimetro(self,rect):
        return self.perimetro() == rect.perimetro()
    
    def mesmaCor(self, rect):
        if not isinstance(rect,Retangulo):
            return False
        return self.cor == rect.cor
    
class ComandoTv:
    def __init__(self, marca,anofabrico,canal,volume, ligado=False):
        self.marca = marca
        self.anofabrico = anofabrico
        self.__canal = canal
        self.__volume = volume
        self.ligado = ligado
        
    # Getter para o canal
    @property
    def canal(self):
        return self.__canal
    
    # Setter para canal
    @canal.setter
    def canal(self, novo_canal):
        if 1 > novo_canal < 99:
            self.__canal = novo_canal
        else: print("Canal Invalido (1-99)")
        
    # Getter para o volume
    @property
    def volume(self):
        return self.__volume
    
    # Setter para volume
    @canal.setter
    def volume(self, novo_volume):
        if 1 > novo_volume < 50:
            self.__canal = novo_volume
        else: print("Volume Invalido (0-50)")
    
    def aumentar_volume(self):
        if self.volume < 50:
            return self.volume == self.volume + 1
        else:
            print("Volume já está no máximo (50).")
            return self.volume
        
    def mudar_canal(self, canal):
        if canal<100 and canal >0: return canal
        else: return self.canal
        
    def alterar_volume(self, sinal):
        if sinal == '+' and self.volume < 50: 
            return self.volume+1
        elif sinal == '-' and self.volume < 0: 
            return self.volume-1
        return self.volume
    
    def mute(self):
        self.volume = 0
        return self.volume
    
    def ligar(self):
        if self.ligado:
            return False
        return True


# TESTE DO COMANDO
c1 = ComandoTv("LG",2020,25,10)
print(c1.canal)        
c1.canal = c1.mudar_canal(32)
print(c1.canal)        
c1.canal = c1.mudar_canal(135)
print(c1.canal)        
        
# TESTE DO SISTEMA - TRIANGULO
t = Triangulo(10,15,11)
if t.formarTriangulo():
    print(f"Perimetro : {t.perimetro()}")
    print(f"Area : {t.area():.2f}")
    print(t.tipo())