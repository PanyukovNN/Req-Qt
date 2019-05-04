import sys, os, docx
from PyQt5 import QtCore, QtGui, QtWidgets
from req_ui import *
from docx.shared import Pt

d = {}
personsArr = []
input = []

def makeDict():
    global d, personsArr, input
    with open("input.txt", encoding = "utf-8") as f:
        input = f.read().split("\n")

    d = {}
    personsArr = []

    d["ФИО"] = []
    d["Адрес"] = []

    for line in input:
        if line != "":
            title = line.split(": ",1)[0]
            if "Файл" in title and title != "Файл ИЦ":
                d["Файл"] = line.split(": ",1)[1]
            if title == "ФИО" or title == "Адрес":
                d[title].append(line.split(": ",1)[1])
            else:
                d[title] = line.split(": ",1)[1]

    # создаём массив лиц
    for i in range(len(d["ФИО"])):
        per = ""
        per += "ФИО: " + d["ФИО"][i] + "\n"
        per += "Адрес: " + d["Адрес"][i] + "\n"
        personsArr.append(per)

makeDict()

class MyWin(QtWidgets.QMainWindow):
    def __init__ (self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Заполняем поля сохраненными значениями
        self.fillAllFields()

        # Обработчик событий
        self.ui.mpRadioButton.clicked.connect(self.changeFabula)
        self.ui.udRadioButton.clicked.connect(self.changeFabula)
        self.ui.redCheckBox.clicked.connect(self.allowEdit)
        self.ui.readyButton.clicked.connect(self.reqFunc)
        self.ui.addPersonButton.clicked.connect(self.addPerson)
        self.ui.delPersonButton.clicked.connect(self.delPerson)
        self.ui.clearPersonButton.clicked.connect(self.clearPerson)
        self.ui.defaultButton.clicked.connect(self.defaultAll)

    def allowEdit(self):
        # Разрешаем редактирование введенных персональных данных
        if self.ui.redCheckBox.isChecked():
            self.ui.personInput.setReadOnly(False)
        else:
            self.ui.personInput.setReadOnly(True)

    def fillAllFields(self):
        # Заполняем поля сохраненными значениями
        self.ui.dataEdit.setText(d["Дата"])
        self.ui.numberEdit.setText(d["Номер материала/дела"])
        self.ui.placeEdit.setText(d["Населенный пункт"])
        if int(d["Материал/Дело[0/1]"]) == 0:
            self.ui.mpRadioButton.setChecked(True)
        if int(d["Материал/Дело[0/1]"]) == 1:
            self.ui.udRadioButton.setChecked(True)
        self.changeFabula()

        # выводим массив лиц в поле
        self.ui.personInput.setPlainText("\n".join(personsArr))

    def defaultAll(self):
        with open("input(save).txt", encoding = "utf-8") as f:
            t = f.read()
        with open("input.txt", "w", encoding = "utf-8") as f:
            f.write(t)
        makeDict(); # заново формируем словарь и массив лиц
        self.fillAllFields()

    def clearPerson(self):
        global personsArr
        personsArr = []
        self.ui.personInput.setPlainText("")

    def delPerson(self):
        # удаляем последнее лицо из массива лиц и выводим в поле
        try:
            personsArr.pop()
        except Exception:
            print("personsArr is empty")
        self.ui.personInput.setPlainText("\n".join(personsArr))

    def addPerson(self):
        per = ""
        per += "ФИО: " + self.ui.fioEdit.text()
        per += ", " + self.ui.bornEdit.text() + " г.р.\n"
        per += "Адрес: проживающий(-ая) по адресу: " + self.ui.adressTextEdit.toPlainText() + ";\n"
        personsArr.append(per)
        self.ui.personInput.setPlainText("\n".join(personsArr))

    def changeFabula(self):
        if self.ui.mpRadioButton.isChecked():
            fab = "Фабула по материалу"
        if self.ui.udRadioButton.isChecked():
            fab = "Фабула по делу"
        self.ui.fabulaInput.setPlainText(d[fab])

    def reqFunc(self):
        try:
            self.writeFunc()
            makeDict()
            doc = docx.Document("Образцы" + os.sep + d["Файл"] + ".docx")
            for p in doc.paragraphs:
                for run in p.runs:
                    if "COUNTRY" in run.text: # населенный пункт
                        run.text = run.text[:-len("COUNTRY")-1] + d["Населенный пункт"] + "»"

                    if run.text == "DATE": # номер дела или материала
                        run.text = d["Дата"] + " " * 16 + d["Номер материала/дела"]

                    if int(d["Материал/Дело[0/1]"]) == 0:
                        fab = "Фабула по материалу"
                    else:
                        fab = "Фабула по делу"

                    if "FABULA" in run.text:
                        run.text = d[fab] + run.text[len("FABULA"):]


                    if run.text == "FIO": # имя
                        while len(p.runs) < len(d["ФИО"]) * 2: # добавляем runs
                            p.add_run()

                        for i in range(len(p.runs)):
                            if i % 2 == 0: # сначала имя
                                p.runs[i].text = str(i//2 + 1) + ") " + d["ФИО"][i//2]
                                p.runs[i].bold = True
                            else: # затем адрес
                                p.runs[i].text = ", " + d["Адрес"][i//2]
                                if i < len(p.runs)-1 :
                                    p.runs[i].text += "\t\n\t"
                            p.runs[i].font.name = "Times New Roman"
                            p.runs[i].font.size = Pt(14)

            doc.save('Запросы готовые.docx')

            # требования ИЦ, ГИАЦ
            for count in range(len(d["ФИО"])):
                doc = docx.Document("Образцы" + os.sep + d["Файл ИЦ"] + ".docx") # файл ИЦ
                for p in doc.paragraphs:
                    for run in p.runs:
                        if "FAMILIA" in run.text:
                            run.text = d["ФИО"][count].split()[0]
                        if "IO" in run.text:
                            run.text = d["ФИО"][count].split()[1] + " " + d["ФИО"][count].split()[2][:-1]
                        if "YEAR" in run.text:
                            run.text = d["ФИО"][count].split(",")[1]
                        if "ADRESS" in run.text:
                            run.text =  d["Адрес"][count].split(":")[1]
                        if "NUMBER" in run.text:
                            run.text =  "№" + d["Номер материала/дела"]
                        if "CURRENT" in run.text:
                            run.text =  " " * 6 + d["Дата"]

                doc.save('Требование ИЦ, ГИАЦ ' + str(count + 1) + " " + d["ФИО"][count].split()[0] + '.docx')

            self.ui.label_6.setText("Успешно")
        except Exception as e:   
            QMessageBox.warning(None, 'Warning', "Error: " + str(e))
            self.ui.label_6.setText("Не удалось")
            self.ui.personInput.setPlainText("Error: " + str(e))

    def writeFunc(self):
        # Присваиваем значения полей в переменную input, котрую затем запишем в файл
        for line in input:
            if line != "":
                title = line.split(": ",1)[0]
                if title == "ФИО" or title == "Адрес":
                    input.remove(line)
                if title == "Дата":
                    input[input.index(line)] = title + ": " + self.ui.dataEdit.text()
                if title == "Материал/Дело[0/1]":
                    if self.ui.mpRadioButton.isChecked():
                        input[input.index(line)] = title + ": " + "0"
                    else:
                        input[input.index(line)] = title + ": " + "1"
                if title == "Номер материала/дела":
                    input[input.index(line)] = title + ": " + self.ui.numberEdit.text()

                if title == "Фабула по материалу" and self.ui.mpRadioButton.isChecked():
                    input[input.index(line)] = title + ": " + self.ui.fabulaInput.toPlainText()
                if title == "Фабула по делу" and self.ui.udRadioButton.isChecked():
                    input[input.index(line)] = title + ": " + self.ui.fabulaInput.toPlainText()

                if title == "Населенный пункт":
                    input[input.index(line)] = title + ": " + self.ui.placeEdit.text()

        # очищаем input от пустых элементов
        while "" in input:
            input.remove("")

        # вписываем в конец input содержимое поля personInput
        persons = self.ui.personInput.toPlainText().split("\n")
        for line in persons:
            if line != "":
                input.append(line)

        # добавляем в input пустые элементы через каждую строку, чтобы корректно срабатывало последующее считывание из файла
        tInput = input
        for i in range(len(tInput) * 2 - 1):
            if i % 2 != 0:
                input.insert(i, "")

        # отредактированную переменную записываем в файл
        with open("input.txt", "w", encoding = "utf-8") as f:
            f.write("\n".join(input))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    myapp.setFixedSize(myapp.geometry().width(),myapp.geometry().height());
    sys.exit(app.exec_())
