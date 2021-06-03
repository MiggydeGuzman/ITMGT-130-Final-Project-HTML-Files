classes = {
    1: {"name":"Class 1","price":125},
    2: {"name":"Class 2","price":100},
    3: {"name":"Class 3","price":120},
    4: {"name":"Class 4","price":120},
    5: {"name":"Class 5","price":140},
    6: {"name":"Class 6","price":200},
    7: {"name":"Class 7","price":150},
    8: {"name":"Class 8","price":130},
    9: {"name":"Class 9","price":200},
    10: {"name":"Class 10","price":200}
}


def get_class(code):
    return classes[code]

def get_classes():
    class_list = []

    for i,v in classes.items():
        class_ = v
        class_.setdefault("code",i)
        class_list.append(class_)

    return class_list