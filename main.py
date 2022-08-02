from random import randint, randrange


class Person:
    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name
        self.age = age
        self.SEX = "H"
        self.weight = weight
        self.height = height
        self.nss = self.generate_nss()


    def generate_nss(self) -> str:
        chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
        nss = ""
        for i in range(8):
            nss += chars[randint(0, len(chars)-1)]
        return nss
    
    def is_an_adult(self) -> bool:
        return self.age >= 18
    
    def set_name(self, name: str) -> str:
        self.name = name
        return self.name
    
    def set_age(self, age) -> int:
        self.age = age
        return self.age
    
    def set_weigth(self, weight):
        selg.weight = weight
        return self.weight
    
    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_imc(self):
        height = self.height / 100
        imc = round(self.weight / (height ** 2), 2)
        if self.SEX == "H":
            if imc < 20:
                return -1
            elif imc >= 20 and imc <= 25:
                return 0
            else:
                return 1
        else:
            if imc < 19:
                return -1
            elif imc >= 19 and imc <= 24:
                return 0
            else:
                return 1

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Sex: {self.SEX}, NSS: {self.nss}, Weight: {self.weight}, Height: {self.height}'


name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
sex = input("Ingresa tu sexo (H/M): ")
weigth = float(input("Ingresa tu peso en KG: "))
height = float(input("Ingresa tu altura en CM: "))


person = Person(name=name, age=age, weight=weigth, height=height)
weigth_status = person.get_imc()

print("Es mayor de edad" if person.is_an_adult() else "No es mayor de edad")

if weigth_status == -1:
    print("Te falta peso")
elif weigth_status == 0:
    print("Estas en tu peso normal")
else:
    print("Tienes sobrepeso!")

print(person)


