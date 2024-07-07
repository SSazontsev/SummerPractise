import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QLine
from PyQt5.QtGui import QImage, QIcon
import cv2
import imutils

"""Описание программы

Эта программа является простым приложением для обработки изображений с использованием PyQt5 и OpenCV.
Она позволяет пользователям загружать изображения,
применять различные операции обработки изображений,
такие как преобразование в оттенки серого, отображение отдельных цветовых каналов, добавление границ,
рисование линий на изображении и сохранение обработанных изображений.
"""

"""Используемые библиотеки

- os: Интерфейсы операционной системы для файловых операций.
- PyQt5: Библиотека для создания графического интерфейса пользователя для настольных приложений.
- cv2 (OpenCV): Библиотека для компьютерного зрения и обработки изображений.
- imutils: Библиотека для основных функций обработки изображений.
"""

"""Класс Ui_MainWindow

- setupUi: Настраивает пользовательский интерфейс для главного окна.
- snapshot_img: Захватывает изображение с веб-камеры.
- load_img: Загружает изображение из файла.
- grey_img: Отображает изображение в оттенках серого.
- red_img: Отображает изображение только с красным каналом.
- grn_img: Отображает изображение только с зеленым каналом.
- blue_img: Отображает изображение только с синим каналом.
- border_img: Добавляет границы к изображению.
- line_img: Рисует линию на изображии.
- set_img: Устанавливает изображение в метку пользовательского интерфейса.
- save_img: Сохраняет текущее изображение.
- retranslateUi: Устанавливает текст и метки в пользовательском интерфейсе.
"""


class Ui_MainWindow(object):

    """
    Класс, отвечающий за настройку пользовательского интерфейса главного окна и подключение кнопок к функциям.
    """

    def setupUi(self, MainWindow):
        """
        Настройте пользовательский интерфейс для главного окна.

        Parameters:
        - MainWindow: QMainWindow object

        Returns:
        - None
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 847)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(500, 500))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.saveBut = QtWidgets.QPushButton(self.centralwidget)
        self.saveBut.setMaximumSize(QtCore.QSize(150, 45))
        self.saveBut.setObjectName("saveBut")
        self.verticalLayout_4.addWidget(self.saveBut)
        self.loudButton = QtWidgets.QPushButton(self.centralwidget)
        self.loudButton.setMinimumSize(QtCore.QSize(0, 0))
        self.loudButton.setMaximumSize(QtCore.QSize(150, 45))
        self.loudButton.setObjectName("loudButton")
        self.verticalLayout_4.addWidget(self.loudButton)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setMaximumSize(QtCore.QSize(181, 60))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_3.addWidget(self.textBrowser_5)
        self.redButton = QtWidgets.QPushButton(self.centralwidget)
        self.redButton.setObjectName("redButton")
        self.verticalLayout_3.addWidget(self.redButton)
        self.blueButton = QtWidgets.QPushButton(self.centralwidget)
        self.blueButton.setObjectName("blueButton")
        self.verticalLayout_3.addWidget(self.blueButton)
        self.greenButton = QtWidgets.QPushButton(self.centralwidget)
        self.greenButton.setObjectName("greenButton")
        self.verticalLayout_3.addWidget(self.greenButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(181, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.borderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.borderBtn.setObjectName("borderBtn")
        self.verticalLayout_2.addWidget(self.borderBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setMaximumSize(QtCore.QSize(181, 61))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.verticalLayout_5.addWidget(self.textBrowser_7)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(181, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(51, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setMaximumSize(QtCore.QSize(81, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setMaximumSize(QtCore.QSize(81, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 1, 0, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setMaximumSize(QtCore.QSize(80, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(51, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(51, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(51, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 2, 1, 1, 2)
        self.lineBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lineBtn.setObjectName("lineBtn")
        self.gridLayout.addWidget(self.lineBtn, 3, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.snapshotButton = QtWidgets.QPushButton(self.centralwidget)
        self.snapshotButton.setMaximumSize(QtCore.QSize(150, 45))
        self.snapshotButton.setObjectName("snapshotButton")
        self.verticalLayout_4.addWidget(self.snapshotButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.snapshotButton.clicked.connect(self.snapshot_img)  # type: ignore
        self.loudButton.clicked.connect(self.load_img)  # type: ignore
        self.redButton.clicked.connect(self.red_img)  # type: ignore
        self.blueButton.clicked.connect(self.blue_img)  # type: ignore
        self.greenButton.clicked.connect(self.grn_img)  # type: ignore
        self.saveBut.clicked.connect(self.save_img)  # type: ignore
        self.lineBtn.clicked.connect(self.line_img)  # type: ignore
        self.borderBtn.clicked.connect(self.border_img)  # type: ignore
        self.pushButton.clicked.connect(self.grey_img)  # Серый
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def snapshot_img(self):
        """
        Функция для захвата изображения с веб-камеры.

        Returns:
        - None
        """

        # Функция для захвата изображения с веб-камеры
        # Инициализируем захват видео с первой камеры
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()  # Читаем один кадр
        if ret:
            cv2.imwrite('image.jpg', frame)  # Сохраняем изображение в файл
            self.image = cv2.imread("image.jpg")
            # Если кадр успешно захвачен, отображаем его в интерфейсе
            self.set_img(frame)

        cap.release()  # Освобождаем камеру

    def load_img(self):
        """
        Функция для загрузки изображения из файла.

        Returns:
        - None
        """

        try:
            os.chdir("C:/Users/chebb/PycharmProjects/Praktika")
            self.filename = QFileDialog.getOpenFileName(
                filter="Image (*.*)")[0]
            if self.filename:
                self.image = cv2.imread(self.filename)
                self.testim = self.image
                self.set_img(self.image)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "Изображение несуществующего формата или на не английском языке")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def grey_img(self):
        """
        Функция отображения изображения в оттенках серого.

        Returns:
        - None
        """

        try:
            image = imutils.resize(self.image, width=640)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Gray image', gray)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение не найдено")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def red_img(self):
        """
        Функция отображения изображения только с красным каналом.

        Returns:
        - None
        """

        try:
            image = imutils.resize(self.image, width=640)
            red = image.copy()
            red[:, :, 0] = 0
            red[:, :, 1] = 0
            cv2.imshow('R-RGB', red)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение не найдено")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def grn_img(self):
        """
        Функция отображения изображения только с зеленым каналом.

        Returns:
        - None
        """

        try:
            image = imutils.resize(self.image, width=640)
            green = image.copy()
            green[:, :, 0] = 0
            green[:, :, 2] = 0
            cv2.imshow('G-RGB', green)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение не найдено")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def blue_img(self):
        """
        Функция отображения изображения только с синим каналом.

        Returns:
        - None
        """

        try:
            image = imutils.resize(self.image, width=640)
            blue = image.copy()
            blue[:, :, 1] = 0
            blue[:, :, 2] = 0
            cv2.imshow('B-RGB', blue)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение не найдено")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def border_img(self):
        """
        Функция добавления границ к изображению.

        Returns:
        - None
        """

        try:
            image = imutils.resize(self.image, width=640)
            border = int(self.lineEdit.text())
            borderoutput = cv2.copyMakeBorder(
                image,
                border,
                border,
                border,
                border,
                cv2.BORDER_CONSTANT,
                value=[
                    255,
                    255,
                    0])
            cv2.imshow("border_image", borderoutput)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение не найдено")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def line_img(self):
        """
        Функция для рисования линии на изображении.

        Returns:
        - None
        """

        while True:
            try:
                pt1_fst_crd = int(self.lineEdit_2.text())
                pt2_fst_crd = int(self.lineEdit_3.text())
                pt1_scn_crd = int(self.lineEdit_4.text())
                pt2_scn_crd = int(self.lineEdit_5.text())
                tkss = int(self.lineEdit_6.text())
            except BaseException:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(
                    "Изображение не найдено или введены неправильные данные")
                msg.setInformativeText('Попробуйте снова')
                msg.setWindowTitle("Error")
                msg.exec_()
                break
            points_1 = (pt1_fst_crd, pt2_fst_crd)
            points_2 = (pt1_scn_crd, pt2_scn_crd)
            self.image = cv2.line(self.image, points_1,
                                  points_2, (51, 255, 51), tkss)
            self.set_img(self.image)
            break

    def set_img(self, image):
        """
        Функция для установки изображения в метке пользовательского интерфейса.

        Parameters:
        - image: numpy array представляющий изображение

        Returns:
        - None
        """

        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame,
            frame.shape[1],
            frame.shape[0],
            frame.strides[0],
            QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def save_img(self):
        """
        Функция сохранения текущего изображения.

        Returns:
        - None
        """

        try:
            filename = QFileDialog.getSaveFileName(
                filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
            cv2.imwrite(filename, self.tmp)
        except BaseException:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Отсутствует изображение")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def retranslateUi(self, MainWindow):
        """
        Функция для установки текста и надписей в пользовательском интерфейсе.

        Parameters:
        - MainWindow: QMainWindow object

        Returns:
        - None
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveBut.setText(_translate("MainWindow", "сохранить"))
        self.loudButton.setText(_translate("MainWindow", "загрузить"))
        self.textBrowser_5.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Изменить канал изображения</p></body></html>"))
        self.redButton.setText(_translate("MainWindow", "красный"))
        self.blueButton.setText(_translate("MainWindow", "синий"))
        self.greenButton.setText(_translate("MainWindow", "зеленый"))
        self.textBrowser.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добавить границы к изображению. Введите размер</p></body></html>"))
        self.borderBtn.setText(_translate("MainWindow", "добавить"))
        self.textBrowser_7.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Показать изображение в оттенках серого</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "серый"))
        self.textBrowser_2.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Добавить линию на изображении</p></body></html>"))
        self.textBrowser_3.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 кордината</p></body></html>"))
        self.textBrowser_4.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2 кордината</p></body></html>"))
        self.textBrowser_6.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Размер линии</p></body></html>"))
        self.lineBtn.setText(_translate("MainWindow", "добавить"))
        self.snapshotButton.setText(_translate("MainWindow", "Сделать снимок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
