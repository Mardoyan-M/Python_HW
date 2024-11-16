from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "13 Pro", "+79991232112"),
    Smartphone("Apple", "Iphone 16 Pro Max", "+79963453215"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79046235987"),
    Smartphone("OnePlus", "12R", "+79526459563"),
    Smartphone("Google", "Pixel 8a", "+79954562312")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.ph_number}")
