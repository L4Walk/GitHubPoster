from Utils.GitHubHelper import g_Helper
from PIL import Image,ImageDraw,ImageFont
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer,SquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask,SquareGradiantColorMask

import os

class PosterHelper:
    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.get_repo_info()
        self.create_poster()

    def get_repo_info(self):
        # 在这里获取仓库信息
        repo = g_Helper.G.get_repo(self.repo_name)
        self.name = repo.name
        self.owner = repo.owner.name
        self.star_count = str(repo.stargazers_count)
        self.fork_count = str(repo.forks_count)
        readme_file = repo.get_readme()
        self.readme = readme_file.decoded_content.decode('utf-8')
        self.desc = repo.description

    def create_poster(self):
        # 在这里根据获取的信息创建海报
        # 你可以使用 self.star_count、self.fork_count 和 self.readme 来创建海报
        # 例如，你可以使用 Python 的图形库来绘制海报
        # 这部分的具体实现取决于你想要的海报样式和格式
         # 这里留给你来填写海报创建的代码
        template_path = os.path.join(os.getcwd(), 'Template','default')
        template = Image.open(os.path.join(template_path,'default.png'))

        # 创建
        draw = ImageDraw.Draw(template)

        # 定义字体对象
        repo_font = ImageFont.truetype(os.path.join(template_path,'fonts','SourceHanSansSC-Bold.otf'),size=60)
        owner_font = ImageFont.truetype(os.path.join(template_path,'fonts','SourceHanSansSC-Light.otf'),size=50)
        star_font = ImageFont.truetype(os.path.join(template_path,'fonts','SourceHanSansSC-Medium.otf'),size=45)
        fork_font = ImageFont.truetype(os.path.join(template_path,'fonts','SourceHanSansSC-Medium.otf'),size=45)
        desc_font = ImageFont.truetype(os.path.join(template_path,'fonts','SourceHanSansSC-Regular.otf'),size=25)

        # 在指定位置添加文字
        draw.text((73,105), self.name, font = repo_font, fill='black')
        draw.text((73,180), self.owner, font = owner_font, fill='blue')
        draw.text((139,246), self.star_count, font = star_font, fill='black')
        draw.text((139,321), self.fork_count, font = fork_font, fill='black')
        draw.text((139,425), self.desc, font = desc_font, fill='black')

        # 生成二维码
        qr_img = self.create_qrcode()
        # 调整二维码图像大小
        width, height = 90, 90 # 设置新的宽度和高度
        qr_img_resized = qr_img.resize((width, height), Image.LANCZOS)
        size = 125
        template.paste(qr_img_resized, (833,366,833 + width, 366 + height))

         # 保存
        template.save("poster.png")


    def create_qrcode(self):
        # 纠错设置为高
        qr = qrcode.QRCode(error_correction=qrcode.constants.       ERROR_CORRECT_H)
        # 如果想扫描二维码后跳转到网页，需要添加https://
        qr.add_data(f"https://github.com/{self.repo_name}")

        # 修改二维码形状
        img = qr.make_image(image_factory=StyledPilImage,         module_drawer=RoundedModuleDrawer())
        
        return  img
