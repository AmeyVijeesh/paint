import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog, QWidget,
                             QSlider, QAction)

from PyQt5.QtGui import (QPen, QImage, QPainter)
from PyQt5.QtCore import (QPoint, Qt)


class Assignment_2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("File")

        brush_size_menu = main_menu.addMenu("Brush Size")
        brush_color_menu = main_menu.addMenu("Brush Colour")

        cap_option = main_menu.addMenu("Cap")
        join_option = main_menu.addMenu("Join")
        pen_option = main_menu.addMenu("Pen")

        flat_cap = QAction("Flat", self)
        cap_option.addAction(flat_cap)
        flat_cap.triggered.connect(self.flatCap)

        square_cap = QAction("Square", self)
        cap_option.addAction(square_cap)
        square_cap.triggered.connect(self.squareCap)

        round_cap = QAction("Round", self)
        cap_option.addAction(round_cap)
        round_cap.triggered.connect(self.roundCap)

        bevel_join = QAction("Bevel", self)
        join_option.addAction(bevel_join)
        bevel_join.triggered.connect(self.bevelJoin)

        miter_join = QAction("Miter", self)
        join_option.addAction(miter_join)
        miter_join.triggered.connect(self.miterJoin)

        round_join = QAction("Round", self)
        join_option.addAction(round_join)
        round_join.triggered.connect(self.roundJoin)

        solid_line = QAction("Solid Line", self)
        pen_option.addAction(solid_line)
        solid_line.triggered.connect(self.solidLine)

        dash_line = QAction("Dash Line", self)
        pen_option.addAction(dash_line)
        dash_line.triggered.connect(self.dashLine)

        dot_line = QAction("Dot Line", self)
        pen_option.addAction(dot_line)
        dot_line.triggered.connect(self.dotLine)

        dash_dot_line = QAction("Dash Dot Line", self)
        pen_option.addAction(dash_dot_line)
        dash_dot_line.triggered.connect(self.dashDotLine)

        dash_dot_dot_line = QAction("Dash Dot Dot Line", self)
        pen_option.addAction(dash_dot_dot_line)
        dash_dot_dot_line.triggered.connect(self.dashDotDotLine)

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction("Clear", self)
        clear_action.setShortcut("Ctrl+C")
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        three_action = QAction("3px", self)
        three_action.setShortcut("Ctrl+3")
        brush_size_menu.addAction(three_action)
        three_action.triggered.connect(self.three_px)

        five_px_action = QAction("5px", self)
        five_px_action.setShortcut("Ctrl+5")
        brush_size_menu.addAction(five_px_action)
        five_px_action.triggered.connect(self.five_px)

        seven_px_action = QAction("7px", self)
        seven_px_action.setShortcut("Ctrl+7")
        brush_size_menu.addAction(seven_px_action)
        seven_px_action.triggered.connect(self.seven_px)

        nine_px_action = QAction("9px", self)
        nine_px_action.setShortcut("Ctrl+9")
        brush_size_menu.addAction(nine_px_action)
        nine_px_action.triggered.connect(self.nine_px)

        twelve_px_action = QAction("12px", self)
        twelve_px_action.setShortcut("Ctrl+2")
        brush_size_menu.addAction(twelve_px_action)
        twelve_px_action.triggered.connect(self.twelve_px)

        black_action = QAction("Black", self)
        black_action.setShortcut("Ctrl+B")
        brush_color_menu.addAction(black_action)
        black_action.triggered.connect(self.black)

        red_action = QAction("Red", self)
        red_action.setShortcut("Ctrl+R")
        brush_color_menu.addAction(red_action)
        red_action.triggered.connect(self.red)

        green_action = QAction("Green", self)
        green_action.setShortcut("Ctrl+G")
        brush_color_menu.addAction(green_action)
        green_action.triggered.connect(self.green)

        white_action = QAction("White", self)
        white_action.setShortcut("Ctrl+W")
        brush_color_menu.addAction(white_action)
        white_action.triggered.connect(self.white)

        yellow_action = QAction("Yellow", self)
        yellow_action.setShortcut("Ctrl+Y")
        brush_color_menu.addAction(yellow_action)
        yellow_action.triggered.connect(self.yellow)

        blue_action = QAction("Blue", self)
        blue_action.setShortcut("Ctrl+L")
        brush_color_menu.addAction(blue_action)
        blue_action.triggered.connect(self.blue)

        top = 400
        left = 400
        width = 800
        height = 600

        self.setWindowTitle("Paint")
        self.setGeometry(top, left, width, height)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushsize = 3
        self.brushColor = Qt.black
        self.penStyle = Qt.DashDotDotLine
        self.capStyle = Qt.RoundCap
        self.joinStyle = Qt.RoundJoin

        self.lastPoint = QPoint()

        self.penWidth = QSlider(Qt.Horizontal)
        self.penWidth.setMinimum(2)
        self.penWidth.setMaximum(35)
        self.penWidth.setTickInterval(2)
        self.penWidth.setValue(3)
        self.penWidth.setTickPosition(QSlider.TicksBelow)
        self.penWidth.setFixedWidth(120)

        self.penWidth.valueChanged.connect(self.slider_change)

        central_widget = QWidget()
        # centralWidget.setLayout(layout)

        tool_bar = self.addToolBar("My Toolbar")
        tool_bar.setAllowedAreas(Qt.LeftToolBarArea)
        # toolBar.setOrientation(Qt.Vertical)
        tool_bar.allowedAreas()

        tool_bar.addWidget(self.penWidth)
        tool_bar.addSeparator()

        self.setCentralWidget(central_widget)

        self.setWindowTitle("Paint Application")
        self.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushsize, self.penStyle, self.capStyle, self.joinStyle))

            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":
            return
        self.image.save(file_path)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def three_px(self):
        self.brushsize = 3

    def five_px(self):
        self.brushsize = 5

    def seven_px(self):
        self.brushsize = 7

    def nine_px(self):
        self.brushsize = 9

    def twelve_px(self):
        self.brushsize = 12

    def black(self):
        self.brushColor = Qt.black

    def red(self):
        self.brushColor = Qt.red

    def green(self):
        self.brushColor = Qt.green

    def yellow(self):
        self.brushColor = Qt.yellow

    def white(self):
        self.brushColor = Qt.white

    def blue(self):
        self.brushColor = Qt.blue

    def slider_change(self):
        print(str(self.penWidth.value()))
        self.brushsize = int(str(self.penWidth.value()))

    def flatCap(self):
        self.capStyle = Qt.FlatCap

    def squareCap(self):
        self.capStyle = Qt.SquareCap

    def roundCap(self):
        self.capStyle = Qt.RoundCap

    def bevelJoin(self):
        self.joinStyle = Qt.BevelJoin

    def miterJoin(self):
        self.joinStyle = Qt.MiterJoin

    def roundJoin(self):
        self.joinStyle = Qt.RoundJoin

    def solidLine(self):
        self.penStyle = Qt.SolidLine

    def dashLine(self):
        self.penStyle = Qt.DashLine

    def dotLine(self):
        self.penStyle = Qt.DotLine

    def dashDotLine(self):
        self.penStyle = Qt.DashDotLine

    def dashDotDotLine(self):
        self.penStyle = Qt.DashDotDotLine


app = QApplication(sys.argv)
assignment = Assignment_2()

sys.exit(app.exec_())
