from smartphone import Smartphone
catalog = [
    Smartphone("samsung", "a 16", "+79823564545"),
    Smartphone("Nokia", "3310", "+79196232325"),
    Smartphone("TECNO", "Camon 50", "+71231231212"),
    Smartphone("iPhone", "17", "+79996586932"),
    Smartphone("Realme", "Note 80", "+79824587898")
]

for smartphone in catalog:
    print(f"{smartphone.brand} -  {smartphone.model} - {smartphone.number}")