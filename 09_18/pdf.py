import os
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 获取当前脚本的目录
script_dir = os.path.dirname(__file__)

# 构建图片文件的相对路径
image_path = os.path.join(script_dir, "01.png")

# 打开图片以获取尺寸
with Image.open(image_path) as img:
    image_width, image_height = img.size

# 创建一个 A4 大小的 PDF 文件
c = canvas.Canvas("output.pdf", pagesize=A4)

# 获取页面宽度和高度
pdf_width, pdf_height = A4

# 转换图片尺寸为 points (PDF 使用的单位)
image_width_in_pdf = image_width * 0.75  # 假设图片为 96 DPI
image_height_in_pdf = image_height * 0.75

# 在左上角放置第一张图片
c.drawImage(image_path, 0, pdf_height - image_height_in_pdf, width=image_width_in_pdf, height=image_height_in_pdf)

# 添加文本（在第一张图片的上方添加文字）
c.setFont("Helvetica", 12)
c.drawString(0, pdf_height - image_height_in_pdf + 15, "第一张图片上方的文字")

# 保存当前画布状态
c.saveState()

# 将画布的原点移动到第二张图片的左上角（即第一张图片的左下角）
c.translate(0, pdf_height - 2 * image_height_in_pdf)

# 旋转画布 180 度
c.rotate(180)

# 放置旋转后的第二张图片
c.drawImage(image_path, -image_width_in_pdf, -image_height_in_pdf, width=image_width_in_pdf, height=image_height_in_pdf)

# 恢复画布状态
c.restoreState()

# 在第二张图片的上方添加文字（在画布恢复原始状态后操作）
c.drawString(0, pdf_height - 2 * image_height_in_pdf - 15, "第二张图片上方的文字")

# 保存 PDF 文件
c.showPage()
c.save()