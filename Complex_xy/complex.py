import math


print(
    '''\n
                        V                     VH               HV                     V
                         V                   V H               H V                   V
                          V                 V  H               H  V                 V
                           V               V   H               H   V               V
                            V             V    H               H    V             V
                             V           V     H               H     V           V
                              V         V      HHHHHHHHHHHHHHHHH      V         V
                               V       V       H               H       V       V
                                V     V        H               H        V     V
                                 V   V         H               H         V   V
                                  V V          H               H          V V
                                   V           H               H           V  
                 
''')

 
class Complex:
    
    def __init__(self,r,a):
        self.__re=r*math.cos(a)
        self.__im=r*math.sin(a)
        
    def get_re(self):
        return self.__re
    def set_re(self,v):
        raise AttributeError
    def del_re(self):
        raise AttributeError
    re=property(get_re,set_re,del_re,"Действительная часть read-only")   
    
    def get_im(self):
        return self.__im
    def set_im(self,v):
        raise AttributeError
    def del_im(self):
        raise AttributeError
    im=property(get_im,set_im,del_im,"Мнимая часть read-only")       
    
    def __str__(self):
        if abs(self.__im)>1.0e-15:
            if self.__im<0:
                sim="-"
            else:
                sim="+"
            return "("+str(self.__re)+sim+"I*"+str(abs(self.__im))+")"
        else:     
            return "("+str(self.__re)+"+I*0)"
        
    def toTrig(x,y):
        if abs(y)>1.0e-15:
            return (math.sqrt(x**2+y**2),math.atan(y/x))
        elif x>0:
            return (math.sqrt(x**2+y**2),0)
        else:
            return (math.sqrt(x**2+y**2),math.pi)
            
    def __add__(self,o):
        re_sum=self.__re+o.__re
        im_sum=self.__im+o.__im
        (r_sum,a_sum)=Complex.toTrig(re_sum,im_sum)
        return Complex(r_sum,a_sum) 
        
    def __sub__(self,o):
        re_sub=self.__re-o.__re
        im_sub=self.__im-o.__im
        (r_sub,a_sub)=Complex.toTrig(re_sub,im_sub)
        return Complex(r_sub,a_sub) 
        
    def __mul__(self,o):
        re_pro=self.__re*o.__re-self.__im*o.__im
        im_pro=self.__im*o.__re+self.__re*o.__im
        (r_pro,a_pro)=Complex.toTrig(re_pro,im_pro)
        return Complex(r_pro,a_pro) 
 
    def __truediv__(self,o):
        a=self.__re
        b=self.__im
        c=o.__re
        d=o.__im
        zz=c**2+d**2
        aa=(a*c+b*d)/zz
        bb=(b*c-a*d)/zz
        (r_div,a_div)=Complex.toTrig(aa,bb)
        return Complex(r_div,a_div)
        
    def cabs(self):
        return math.sqrt(self.__re**2+self.__im**2)


if __name__ == "__main__":
    z1 = Complex(3, math.pi/4)
    z2 = Complex(2, -math.pi/6)
    
    print("z1 = ", z1)
    print("z2 = ", z2)
    print("z1 + z2 = ", z1 + z2)
    print("z1 - z2 = ", z1 - z2)
    print("z1 * z2 = ", z1 * z2)
    print("z1 / z2 = ", z1 / z2)
    print("|z1| = ", z1.cabs())
    
    
    
