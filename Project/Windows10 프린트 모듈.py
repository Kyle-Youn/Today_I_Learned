'''
[파이썬으로 PNG, JPG 프린트 하기]

pip install PySide6
'''

from PySide6.QtWidgets import QApplication
from PySide6.QtPrintSupport import QPrinter, QPrinterInfo
from PySide6.QtGui import QImage, QImageReader, QPainter, QPageLayout, QPageSize, Qt
import sys

def print_file(file_path, copy_count):
    app = QApplication.instance()  # 현재 인스턴스를 확인하고, 없다면 생성
    if not app:
        app = QApplication(sys.argv)

    default_printer = QPrinterInfo.defaultPrinter()
    if default_printer.isNull():
        print('연결된 프린터가 없습니다.')
        return False
    else:
        print('연결된 프린터: ' + QPrinterInfo.defaultPrinterName())

    printer = QPrinter(default_printer, mode=QPrinter.HighResolution)
    printer.setCopyCount(copy_count)
    printer.setPageSize(QPageSize.A4)
    printer.setPageOrientation(QPageLayout.Landscape)
    printer.setResolution(96)
    
    QImageReader.setAllocationLimit(0)
    
    img = QImage(file_path)
    scaled_img = img.scaled(printer.pageRect(QPrinter.DevicePixel).width(), printer.pageRect(QPrinter.DevicePixel).height(), aspectMode=Qt.KeepAspectRatio, mode=Qt.SmoothTransformation)
    painter = QPainter()
    if painter.begin(printer):
        painter.drawImage(0, 0, scaled_img)
        painter.end()
    else:
        print('프린터에 이미지를 그리는 데 실패했습니다.')




'''
QPrinterInfo.defaultPrinter() 프린터 선택 UI가 없으므로 기본으로 설정된 프린터정보를 가져온다. Null 인 경우 연결된 프린터가 없다는 에러를 표시하고 있는 경우 프린터 명을 출력한다.
QPrinter에 인자로 프린터 정보를 받아 printer 객체를 생성한다. (이 때, mode=QPrinter.HighResolution 으로 해줘야 artifact가 덜 하고 깔끔하게 나온다.)
setCopyCount() 으로 인쇄할 매수를 설정한다.
setPageSize() 으로 페이지 크기를 설정한다.
setPageOrientation() 으로 인쇄 방향(가로/세로)을 설정한다. (Landscape-가로, Portrait-세로)
setResolution() 으로 dpi(해상도)를 설정한다.
이미지 용량이 큰 경우 QImageReader.setAllocationLimit(0)으로 설정해주면 제한이 해제된다.
이미지 해상도가 용지 크기보다 큰 경우, scaled()함수를 이용하여 용지 크기에 맞게 사이즈를 조절한다. 이 때, aspectMode=KeepAspectRatio, mode=SmoothTransformation 로 설정하면 이미지 깨짐이 덜 하다.
QPainter에 PaintDevice로 설정된 Printer를 넣어 준 후, drawImage()를 이용하여 프린트할 이미지를 그려준다. begin, end로 device를 열고 닫아주면 출력이 완료된다.
출처: https://chuun92.tistory.com/10 [develop mind  : 발전하는 일상을 기록하다.:티스토리]
'''