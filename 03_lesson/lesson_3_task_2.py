from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "One", "+7(999)123-45-67"),
    Smartphone("Iphone", "Two", "+7(999)234-56-78"),
    Smartphone("Iphone", "Three", "+7(999)234-56-78")
]
for smart in catalog:
    print(smart.brand + "-" + smart.model + ".", smart.number)
