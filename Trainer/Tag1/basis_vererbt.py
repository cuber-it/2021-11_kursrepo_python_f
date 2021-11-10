import basis

class HtmlService(basis.Basis):
    def write(self, html_template=None):
        if not html_template:
            super().write()
        else:
            print(html_template.format(self.text))


if __name__ == "__main__":
    o1 = HtmlService()
    o2 = HtmlService("Erster Wert")

    o1.read()

    o1.write()
    o2.write()

    o1.bearbeite_text()
    o2.bearbeite_text()

    o1.write()
    o2.write("<html><body><h1>{}</h1></body></html>")
