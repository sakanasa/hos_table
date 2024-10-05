import os
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import styles
from reportlab.pdfbase.ttfonts import TTFont
from PyPDF2 import PdfReader
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageTemplate, BaseDocTemplate



current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir) #可以找出當前執行檔案的目錄

font_msjh_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'font', 'msjh.ttc')
font_msjhbd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'font', 'msjhbd.ttc')

pdfmetrics.registerFont(TTFont('Msjh', font_msjh_path))    #微軟正黑體
pdfmetrics.registerFont(TTFont('MsjhB', font_msjhbd_path)) #粗體




outptu_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'my_table.pdf')
doc = SimpleDocTemplate(outptu_file,
                        pagesize=A4,
                        leftMargin=0,
                        rightMargin=0,
                        topMargin=0.25*inch,
                        bottomMargin=0
                        )



ans01="　脂肪肝( 輕 中度以上)\n\n　肝囊腫\n\n　疑似血管瘤\n\n　疑似脂肪分布不均\n\n　肝內鈣化\n\n　肝實質疾病\n\n　(高/同/低)回音病灶\n\n\n"
ans02="　切除術後\n\n　結石ｘｘｘmm\n\n　結石(多發性)\n　ｘｘｘmm~ｘｘｘmm\n\n　瘜肉ｘｘｘmm\n\n　瘜肉(多發性)\n　ｘｘｘmm~ｘｘｘmm\n\n　膽壁增厚\n\n　總膽管擴張ｘｘｘmm\n\n　膽泥、膽砂\n\n　進食後膽囊\n\n\n"
ans03="　結石ＸＸＸmm\n\n　囊腫ＸＸＸmm\n\n　鈣化點ＸＸＸmm\n\n　疑似血管肌脂瘤(缺陷瘤)\n\n　賢盂積水\n\n\n\n"
ans04="　切除術後\n\n　尾部腸氣遮蔽\n\n　囊腫ＸＸＸmm"
ans05="　結石ＸＸＸmm\n\n　囊腫ＸＸＸmm\n\n　鈣化點ＸＸＸmm\n\n　疑似血管肌脂瘤(缺陷瘤)\n\n　賢盂積水"
ans06="　切除術後\n\n　腫大\n\n　副脾"
ans07="　肥大\n\n　鈣化點ｘｘｘmm\n\n　囊腫ｘｘｘmm"
ans08="　膀胱結石\n\n　疑似膀胱腫瘤\n\n　其他:"
ans09="　IMTＸＸＸmm\n\n　IMT增厚ＸＸＸmm\n\n　疑似斑塊ＸＸＸmm"
ans10="　IMTＸＸＸmm\n\n　IMT增厚ＸＸＸmm\n\n　疑似斑塊ＸＸＸmm"
ans11="　疑似囊腫ＸＸＸmm\n\n　疑似結節ＸＸＸmm"









data=  [['超音波檢查紀錄單', 'x', 'x', '檢查日期:', '04', '05', '操作者:', '07'],
        ['姓名/ID:', '11', '套組:', '13', '14', '15', '16', '17'],
        ['性別:', '21', '22', '23', '24', '25', '26', '27'],
        ['　腹部超音波', '', '　無明顯異常', '33', '　已告知回診', '35', '　備註', '37'],
        ['肝臟', '41', '膽囊', '43', '右腎', '45', '左腎', '47'],
        ['50', '51', '52', '53', '54', '55', '56', '57'],
        ['60', '61', '62', '63', '胰臟', '65', '脾臟', '67'],
        ['70', '71', '72', '73', '74', '75', '76', '77'],
        ['　攝護腺、膀胱超音波', '81', '82', '83', '　甲狀腺超音波', '85', '86', '87'],
        ['　　　無明顯異常　　已告知回診　　備註', '91', '92', '93', '　　　無明顯異常　　已告知回診　　備註', '95', '96', '797'],
        ['攝護腺', '101', '膀胱', '103', '峽部', '105', '106', '107'],
        ['110', '111', '112', '113', '114', '115', '116', '117'],
        ['120', '121', '122', '123', '右側', '125', '左側', '127'],
        ['130', '131', '132', '133', '', '135', '', ''],
        ['　頸動脈中內膜厚度超音波', '141', '142', '143', '144', '145', '146', ''],
        ['　　　無明顯異常　　已告知回診　　備註', '151', '152', '153', '154', '155', '156', ''],
        ['右側', '161', '左側', '163', '164', '165', '166', ''],
        ['170', '171', '172', '173', '174', '175', '176', ''],
        ]

data[5][0]=ans01
data[5][2]=ans02
data[5][4]=ans03
data[7][4]=ans04
data[5][6]=ans05
data[7][6]=ans06
data[11][0]=ans07
data[11][2]=ans08
data[17][0]=ans09
data[17][2]=ans10
data[11][4]=ans11

check = [0] * 78





table_width = (A4[0] - 1 * inch) / 8
table_height = (A4[1] - 1 * inch) / 16
t = Table(data, colWidths=table_width)
t.setStyle(TableStyle([
    
    #('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    #('INNERGRID', (0, 0), (-1, -1), 0.25, 'gray'),
    #('BOX', (0, 0), (-1, -1), 0.25, 'black'),
    ('FONTNAME', (0, 0), (-1, -1), 'Msjh'),
    ('GRID', (0, 4), (6, 7), 1, 'gray'), #框線


    #合併Table
    ('SPAN', (0, 0), (2, 0)),  
    ('SPAN', (4, 0), (5, 0)),  
    ('SPAN', (2, 1), (2, 2)),  
    ('SPAN', (3, 1), (7, 2)),  
    ('SPAN', (0, 3), (1, 3)), 
    ('SPAN', (2, 3), (3, 3)),  
    ('SPAN', (4, 3), (5, 3)),  
    ('SPAN', (6, 3), (7, 3)),  
    ('SPAN', (0, 4), (1, 4)),  
    ('SPAN', (2, 4), (3, 4)),  
    ('SPAN', (4, 4), (5, 4)),  
    ('SPAN', (6, 4), (7, 4)),    
    ('SPAN', (0, 5), (1, 7)),  
    ('SPAN', (2, 5), (3, 7)), 
    ('SPAN', (4, 5), (5, 5)),
    ('SPAN', (4, 6), (5, 6)),  
    ('SPAN', (4, 7), (5, 7)),  
    ('SPAN', (6, 5), (7, 5)),
    ('SPAN', (6, 6), (7, 6)),  
    ('SPAN', (6, 7), (7, 7)),
    ('SPAN', (0, 8), (3, 8)),
    ('SPAN', (4, 8), (7, 8)),
    ('SPAN', (0, 9), (3, 9)),
    ('SPAN', (4, 9), (7, 9)),
    ('SPAN', (0, 10), (1, 10)),
    ('SPAN', (2, 10), (3, 10)),
    ('SPAN', (4, 10), (7, 10)),
    ('SPAN', (0, 11), (1, 13)),
    ('SPAN', (2, 11), (3, 13)),
    ('SPAN', (4, 11), (7, 11)),
    ('SPAN', (4, 12), (5, 12)),
    ('SPAN', (6, 12), (7, 12)),
    ('SPAN', (0, 14), (3, 14)),
    ('SPAN', (0, 15), (3, 15)),
    ('SPAN', (0, 16), (1, 16)),
    ('SPAN', (2, 16), (3, 16)),
    ('SPAN', (0, 17), (1, 17)),
    ('SPAN', (2, 17), (3, 17)),
    ('SPAN', (4, 13), (5, 17)),
    ('SPAN', (6, 13), (6, 17)),
    
    
    #('SPAN', (6, 13), (7, 16)),

    ('FONTSIZE', (0, 0), (0, 0), 20),
    
    

    #網底
    ('BACKGROUND', (0, 4), (7, 4),colors.Color(0.7, 0.7, 0.7)),
    ('BACKGROUND', (4, 6), (7, 6),colors.Color(0.7, 0.7, 0.7)),
    ('BACKGROUND', (0, 10), (-1, 10),colors.Color(0.7, 0.7, 0.7)),
    ('BACKGROUND', (4,12), (7, 12),colors.Color(0.7, 0.7, 0.7)),
    ('BACKGROUND', (0,16), (3, 16),colors.Color(0.7, 0.7, 0.7)),

    #外框
    ('BOX', (0, 3), (-1, -1), 1,'black' ),
    ('GRID', (0, 4), (7,4), 0.5, 'black'), #框線
    ('GRID', (0, 10), (7,10), 0.5, 'black'), #框線
    ('GRID', (4, 12), (7,12), 0.5, 'black'), #框線
    ('GRID', (4, 6), (7,6), 0.5, 'black'), #框線
    ('GRID', (0, 16), (4,16), 0.5, 'black'), #框線
    ('GRID', (0, 4), (6, 7), 1, 'gray'), #框線
    ('GRID', (0, 11), (3, 13), 1, 'gray'), #框線
    ('GRID', (0, 17), (1, 17), 1, 'gray'), #框線
    ('GRID', (4, 13), (5, 17), 1, 'gray'), #框線
    ('BOX', (0,3), (7,7), 0.5, 'black'), #框線
    ('BOX', (0,8), (3,13), 0.5, 'black'), #框線
    ('BOX', (0,14), (3,17), 0.5, 'black'), #框線
    ('BOX', (5,8), (-1,-1), 0.5, 'black'), #框線

    #對齊
    ('VALIGN', (0, 3),(7, 3), 'MIDDLE'),
    ('ALIGN', (0, 3),(7,3), 'LEFT'),
    ('VALIGN', (0, 4), (7,4), 'MIDDLE'),
    ('ALIGN', (0, 4), (7,4), 'CENTER'),
    ('VALIGN',(0, 10), (7,10), 'MIDDLE'),
    ('ALIGN', (0, 10), (7,10), 'CENTER'),
    ('VALIGN',(4, 12), (7,12), 'MIDDLE'),
    ('ALIGN', (4, 12), (7,12), 'CENTER'),
    ('VALIGN',(4, 6), (7,6), 'MIDDLE'),
    ('ALIGN', (4, 6), (7,6), 'CENTER'),
    ('VALIGN',(0, 16), (4,16), 'MIDDLE'),
    ('ALIGN', (0, 16), (4,16), 'CENTER'),
    ('VALIGN', (0, 5), (0,5), 'TOP'),
    ('VALIGN', (2, 5), (2,5), 'TOP'),
    ('VALIGN', (4, 5), (4,5), 'TOP'),
    ('VALIGN', (4, 7), (4,7), 'TOP'),
    ('VALIGN', (6, 5), (6,5), 'TOP'),
    ('VALIGN', (6, 7), (6,7), 'TOP'),

    #字體
    ('FONTSIZE', (0, 0), (0, 0), 20),
    ('FONTNAME', (0, 0),(0, 0),'MsjhB'),
    ('FONTSIZE', (0, 3),(0, 3), 15),
    ('FONTNAME', (0, 3),(0, 3),'MsjhB'),
    ('FONTSIZE', (0, 8),(-1, 8), 15),
    ('FONTNAME', (0, 8),(-1, 8),'MsjhB'),
    ('FONTSIZE', (0, 14),(0, 14), 15),
    ('FONTNAME', (0, 14),(0, 14),'MsjhB'),

    #欄高
    ('BOTTOMPADDING', (0, 0), (0, 0), 20),
    ('BOTTOMPADDING',(0, 3),(0, 3), 10),
    ('TOPPADDING',(0, 3),(0, 3), 5),
    ('BOTTOMPADDING',(0, 8),(-1, 8), 10),
    ('TOPPADDING',(0, 8),(-1, 8), 5),
    ('BOTTOMPADDING',(0, 14),(0, 14), 10),
    ('TOPPADDING',(0, 14),(0, 14), 5),

    #
    ('BOX', (0, 3), (-1, -1), 1,'black' ),
    #('LEADING', (0, 0), (7, 0),50),       

    

    
]))



def draw_square_on_canvas(canvas, doc):
    text_63_69=['切除術後',
                '疑似多發性結節',
                'xxx mm~ xxx mm',
                '疑似結節 xxx mm',
                '疑似囊腫 xxx mm',
                '疑似多發性囊腫',
                'xxx mm~ xxx mm',
                '疑似瀰漫性非均質腺體',
                '(高/同/低)回音病灶'
                ]
    
    text_70_76=['切除術後',
                '疑似多發性結節',
                'xxx mm~ xxx mm',
                '疑似結節 xxx mm',
                '疑似囊腫 xxx mm',
                '疑似多發性囊腫',
                'xxx mm~ xxx mm',
                '疑似瀰漫性非均質腺體',
                '(高/同/低)回音病灶'
                ] 

    # 保存當前畫布狀態
    canvas.saveState()
    canvas.setFont('Msjh',10)
    x1 = 313.5
    x2 = 445
    y = 295
    for i in range(0,9):
        canvas.drawString(x1, y, text_63_69[i])
        canvas.drawString(x2, y, text_70_76[i])
        y-=16

#==================================================
    check_xy = [[0,0],
                [46,729],
                [173,729.5],
                [303,729.5],
                [434,729.5],
                [42,688.5],
                [42,665],
                [42,641.5],
                [42,617.5],
                [42,593],
                [42,569],
                [42,545],
                [173.25,688.5],
                [173.25,665],
                [173.25,641.5],
                [173.25,605],
                [173.25,581],
                [173.25,545],
                [173.25,521],
                [173.25,497],
                [173.25,473],
                [303.5,688.5],
                [303.5,665],
                [303.5,641.5],
                [303.5,617.5],
                [303.5,593],
                [433.5,688.5],
                [433.5,665],
                [433.5,641.5],
                [433.5,617.5],
                [433.5,593],
                [303.5,493],
                [303.5,469],
                [303.5,445],
                [433.5,493],
                [433.5,469],
                [433.5,445],
                [46,414],
                [61,392],
                [131,392],
                [202,392],
                [42,344],
                [42,320],
                [42,296],
                [173.25,344],
                [173.25,320],
                [173.25,296],
                [46,273],
                [61,251],
                [131,251],
                [202,251],
                [42,215],
                [42,191],
                [42,167],
                [173,215],
                [173,191],
                [173,167],
                [303.5,414],
                [323,392],
                [393,392],
                [463,392],
                [303,356],
                [303,332],

                [303,295],
                [303,279],
                [303,247],
                [303,231],
                [303,215],
                [303,183],
                [303,166],

                [433.5,295],
                [433.5,279],
                [433.5,247],
                [433.5,231],
                [433.5,215],
                [433.5,183],
                [433.5,166],
                ]
    print(len(check_xy))

    
    for i in range(1,77):
        x=check_xy[i][0]
        y=check_xy[i][1]
        if check[i] == 1 : #如果沒有打勾，只畫正方形
            # 定義正方形大小
            size = 7.5
            # 繪製正方形
            canvas.rect(x, y, size, size)
        else:               #如果有打勾，畫正方形，打勾
            # 定義正方形大小
            size = 7.5
            # 繪製正方形
            canvas.rect(x, y, size, size)
            checkmark_coords = [
                        (x + 1.25, y + 3.75),  # 起点
                        (x + 2.5, y + 1.25),  # 底部
                        (x + 8, y + 8)   # 终点
                        ]

            # 使用 canvas.line 繪製每一條線
            canvas.line(checkmark_coords[0][0], checkmark_coords[0][1], checkmark_coords[1][0], checkmark_coords[1][1])  # 第一段線
            canvas.line(checkmark_coords[1][0], checkmark_coords[1][1], checkmark_coords[2][0], checkmark_coords[2][1])  # 第二段線            









    # 恢復畫布狀態
    canvas.restoreState()

# 使用 onFirstPage 來調用繪製正方形和打勾
doc.build([t], onFirstPage=lambda canvas, doc: draw_square_on_canvas(canvas, doc))

print(A4[0])
print(A4[1])









