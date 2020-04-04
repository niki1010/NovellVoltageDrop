# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define m = Character('Мику', color="#26ffff")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room 
    
    show mi_3_body

    show mi_3_pioneer

    show mi_3_serious 
    
    m "тестик"

    screen imagemap:
     imagemap:
         ground "images/plug.jpg"
         hover"images/plug.jpg"
         hotspot (385, 315, 78, 78) clicked Return("home")
         hotspot (435, 365, 78, 78) clicked Return("school")
         hotspot (485, 415, 78, 78) clicked Return("bank")
         hotspot (535, 465, 78, 78) clicked Return("hospital")
    label example_label:
         #как видим блок окна вызывается отдельно, чтобы не прописывать его каждый раз
         call screen imagemap
         #наш результат прошлого выбора в меню, благодаря действию Return()
         #был сохранен в хранилище _return
         $result = _return
         #теперь результат действий щелчка будет зависеть, от выбора который мы сделали ранее
         if result == "home":
              p "Вы выбрали дом!"
         elif result == "school":
             p "Вы выбрали школу!"
         elif result == "bank":
              p "Вы выбрали банк!"
         elif result == "hospital":
             p "Вы выбрали больницу!"