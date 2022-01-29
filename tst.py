class Person:
    ...


class AnyThing:
    ...


class Knowledge(AnyThing):
    ...


class MaterialThing(AnyThing):
    ...


person = Person("Misha")
k1 = Knowledge("Python")
k2 = Knowledge("Guitar player")
k3 = Knowledge("Cooking")
person += k1
person = person + k2
person = person.__add__(k3)

person += MaterialThing("Mobile Phone")
person += MaterialThing("wired phone")
person += MaterialThing("car")
person += MaterialThing("yacht")

print(person.knowledfe)  # хочу увидеть все его знания через запятую
print(person.material)  # хочу увидет ьвсе его вещи

s1 = person.pop()  # у него должна пропасть яхта
s1 = person.pop()  # у него должна пропасть машина
s1 = person.pop()  # у него должна пропасть проводная телефония
s1 = person.pop()  # у него должна пропасть мобилка

try:
    person.pop()
    assert False, "должен случится индекс еррор так как знания не изымаемые а вещей у него нет."
except IndexError:
    pass

assert person("Python") == "О да я умею в Python"
assert person("Cooking") == "О да я умею в Cooking"
assert person("debugging") == "Нажаль debugging не входит в список моих умений"
