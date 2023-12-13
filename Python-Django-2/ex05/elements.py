from elem import Elem

class html(Elem):
    def __init__(content=None):
        super().__init__("html", content, "simple")
    
class head(Elem):
    def __init__(content=None):
        super().__init__("head", content, "simple")

class body(Elem):
    def __init__(content=None):
        super().__init__("body", content, "simple")


if __name__ == '__main__':
    html_example = html()
    print(html_example.__str__())