from io import BytesIO
from pathlib import Path
from subprocess import run
from xml.sax.saxutils import escape

from lxml import html
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image, KeepTogether, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle,
)

from work_samples import DOCS

ROOT = Path(__file__).parent / "dist"
ASSETS = ROOT / "assets"
WIDTH = 7.1 * inch
VIOLET = colors.HexColor("#6237d0")
INK = colors.HexColor("#261b35")
LAVENDER = colors.HexColor("#f4ebff")

pdfmetrics.registerFont(TTFont("Portfolio", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("PortfolioBold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("PortfolioMono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))

TEXT = ParagraphStyle("body", fontName="Portfolio", fontSize=9.4, leading=14, textColor=INK, spaceAfter=6)
TITLE = ParagraphStyle("title", parent=TEXT, fontName="PortfolioBold", fontSize=25, leading=30, spaceAfter=9)
LABEL = ParagraphStyle("label", parent=TEXT, fontName="PortfolioBold", fontSize=9, textColor=VIOLET, spaceAfter=7)
HEADING = ParagraphStyle("heading", parent=TEXT, fontName="PortfolioBold", fontSize=14, leading=18, spaceBefore=12, keepWithNext=True)
SUBTITLE = ParagraphStyle("sub", parent=TEXT, fontName="PortfolioBold", fontSize=10, spaceBefore=7, keepWithNext=True)
CELL = ParagraphStyle("cell", parent=TEXT, fontSize=8.1, leading=11)
CELL_HEAD = ParagraphStyle("cell header", parent=CELL, fontName="PortfolioBold")
CODE = ParagraphStyle("code", parent=TEXT, fontName="PortfolioMono", fontSize=8.2, leading=11, leftIndent=8, backColor=LAVENDER)


def paragraph(text, style=TEXT):
    return Paragraph(escape(text), style)


def convert(node):
    if node.tag in ("h2", "h3", "p", "strong"):
        style = {"h2":HEADING, "h3":SUBTITLE, "p":TEXT, "strong":SUBTITLE}[node.tag]
        return [paragraph(node.text_content(), style)]
    if node.tag == "li":
        return [paragraph("• " + node.text_content())]
    if node.tag == "pre":
        return [Preformatted(node.text_content(), CODE), Spacer(1,8)]
    if node.tag == "table":
        rows = [[paragraph(cell.text_content(), CELL_HEAD if index == 0 else CELL) for cell in row.xpath("./th|./td")]
                for index, row in enumerate(node.xpath(".//tr"))]
        count = len(rows[0])
        fractions = {3:[.26,.24,.50],4:[.15,.22,.34,.29]}[count]
        table = Table(rows, colWidths=[WIDTH*x for x in fractions], repeatRows=1, hAlign="LEFT")
        table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),LAVENDER),
            ("VALIGN",(0,0),(-1,-1),"TOP"), ("LINEBELOW",(0,0),(-1,-1),.36,colors.HexColor("#e3d7eb")),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
        return [table, Spacer(1,8)]
    if node.tag == "img":
        path = ASSETS / Path(node.get("src")).name
        png = run(["inkscape", str(path), "--export-type=png", "--export-filename=-"], check=True, capture_output=True).stdout
        drawing = Image(BytesIO(png))
        ratio = min(WIDTH / drawing.imageWidth, 4.1*inch / drawing.imageHeight)
        drawing.drawWidth = drawing.imageWidth * ratio
        drawing.drawHeight = drawing.imageHeight * ratio
        return [drawing]
    items = [item for child in node for item in convert(child)]
    return [KeepTogether(items)] if node.tag == "figure" else items


def footer(canvas, document):
    canvas.setStrokeColor(colors.HexColor("#dfd3ec"))
    canvas.line(.7*inch,.56*inch,7.8*inch,.56*inch)
    canvas.setFont("Portfolio",8)
    canvas.setFillColor(VIOLET)
    canvas.drawString(.7*inch,.36*inch,"Jill Nguyen  |  Business analysis portfolio")
    canvas.drawRightString(7.8*inch,.36*inch,str(document.page))


for slug, (title, intro, content) in DOCS.items():
    document = SimpleDocTemplate(str(ASSETS/f"{slug}.pdf"),pagesize=(8.5*inch,11*inch),
                                 leftMargin=.7*inch,rightMargin=.7*inch,topMargin=.62*inch,bottomMargin=.7*inch,
                                 title=f"{title} | SMS360 portfolio sample", author="Jill Nguyen")
    body = [
        paragraph("SMS360   /   PORTFOLIO WORK SAMPLE", LABEL),
        paragraph(title, TITLE),
        paragraph(intro),
        paragraph("Adapted from SMS360 work. Records and API examples are illustrative."),
    ]
    body.extend(convert(html.fragment_fromstring(content(),create_parent=True)))
    document.build(body,onFirstPage=footer,onLaterPages=footer)
