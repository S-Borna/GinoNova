"""Generate GINONOVA_OVERVIEW.pdf matching the CodeTrust one-pager design."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import ParagraphStyle

OUTPUT_PATH = "GINONOVA_OVERVIEW.pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4

MARGIN_LEFT = 38 * mm
MARGIN_RIGHT = 38 * mm
MARGIN_TOP = 32 * mm
MARGIN_BOTTOM = 28 * mm

CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

PURPLE = HexColor("#6D28D9")
BLACK = HexColor("#111111")
BODY_COLOR = HexColor("#374151")
LIGHT_GRAY = HexColor("#6B7280")
RULE_COLOR = HexColor("#D1D5DB")

SECTION_HEADING_STYLE = ParagraphStyle(
    name="SectionHeading",
    fontName="Helvetica-Bold",
    fontSize=8.5,
    leading=10,
    textColor=PURPLE,
    spaceBefore=0,
    spaceAfter=8,
    tracking=3.5,
)

BODY_STYLE = ParagraphStyle(
    name="Body",
    fontName="Helvetica",
    fontSize=9,
    leading=14.5,
    textColor=BODY_COLOR,
    alignment=TA_JUSTIFY,
    spaceBefore=0,
    spaceAfter=0,
)

BODY_BOLD_STYLE = ParagraphStyle(
    name="BodyBold",
    fontName="Helvetica-Bold",
    fontSize=9.5,
    leading=15,
    textColor=BLACK,
    alignment=TA_JUSTIFY,
    spaceBefore=0,
    spaceAfter=0,
)

FOOTER_STYLE = ParagraphStyle(
    name="Footer",
    fontName="Helvetica-Bold",
    fontSize=9,
    leading=13,
    textColor=BLACK,
    alignment=TA_CENTER,
)

FOOTER_SUB_STYLE = ParagraphStyle(
    name="FooterSub",
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    textColor=LIGHT_GRAY,
    alignment=TA_CENTER,
)


SECTIONS: list[dict[str, str | bool]] = [
    {
        "heading": "WHAT IT DOES",
        "body": (
            "GinoNova is an interactive learning platform for DevOps, Linux, and systems "
            "administration. It delivers 31 structured modules covering the full DevOps "
            "ecosystem \u2014 each with hands-on labs, flashcards, quizzes, and career-focused "
            "interview preparation. A persistent AI assistant provides context-aware guidance "
            "on every page, an AI quiz engine generates unique questions from module content "
            "in real time, and a tenta simulator serves 1,200+ exam questions across six "
            "verified question banks. Students progress through adaptive difficulty levels, "
            "earn certificates, track learning velocity through an analytics engine, and "
            "engage in a threaded community forum with reputation mechanics. A full admin "
            "surface provides real-time operational visibility."
        ),
        "bold": False,
    },
    {
        "heading": "HOW IT\u2019S BUILT",
        "body": (
            "The platform is a vertically integrated system \u2014 frontend, backend, database, "
            "AI layer, and admin tooling \u2014 built and operated as a single codebase. It "
            "supports multiple OAuth providers, real-time activity tracking, email "
            "verification, interactive code execution across five environments, and "
            "AI-powered content generation. The architecture is designed for production-grade "
            "performance and scale from day one."
        ),
        "bold": True,
    },
    {
        "heading": "THE VISION",
        "body": (
            "The DevOps education market is dominated by platforms charging $300\u2013500 per year "
            "for content designed for passive consumption \u2014 video lectures, static quizzes, "
            "no real feedback loop. None of them were built for the way developers actually "
            "learn: by doing, by failing, by iterating with intelligent assistance. GinoNova "
            "exists to close that gap. The ambition is a platform that takes a complete "
            "beginner to a job-ready DevOps engineer in 6\u201312 months \u2014 with AI-powered "
            "personalization, hands-on execution environments, structured learning paths, "
            "and career-focused content \u2014 at a quality level that competes directly with "
            "established commercial platforms. The goal is not to be software that happens "
            "to work. The goal is to be the best DevOps learning platform available, period."
        ),
        "bold": False,
    },
    {
        "heading": "CURRENT STATE",
        "body": (
            "GinoNova is in active development with a production deployment live at "
            "ginonova.com. The core platform is stable and operational: 31 modules published, "
            "AI assistant and quiz engine live, 1,200+ exam questions serving, community "
            "forum functional, admin dashboard providing full visibility. Development "
            "continues with the explicit ambition of reaching full market readiness \u2014 the "
            "distance between a working product and one that wins on first impression."
        ),
        "bold": False,
    },
]


def draw_spaced_text(
    canvas_obj: Canvas, text: str, x: float, y: float, spacing: float
) -> None:
    """Draw text with manual letter-spacing to match the uppercase heading style."""
    for char in text:
        canvas_obj.drawString(x, y, char)
        x += canvas_obj.stringWidth(char, canvas_obj._fontname, canvas_obj._fontsize) + spacing


def generate_pdf() -> None:
    """Build the single-page overview PDF."""
    c = Canvas(OUTPUT_PATH, pagesize=A4)

    cursor_y = PAGE_HEIGHT - MARGIN_TOP

    # --- Title ---
    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_LEFT, cursor_y, "GinoNova")
    cursor_y -= 22

    # --- Subtitle ---
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(BLACK)
    c.drawString(MARGIN_LEFT, cursor_y, "AI-Driven DevOps Learning Platform")
    subtitle_end_x = MARGIN_LEFT + c.stringWidth(
        "AI-Driven DevOps Learning Platform", "Helvetica-Bold", 9.5
    )
    c.setFont("Helvetica", 9.5)
    c.setFillColor(LIGHT_GRAY)
    c.drawString(subtitle_end_x + 4, cursor_y, " v2.8.0 \u2014 Created by Said Borna")
    cursor_y -= 16

    # --- Horizontal rule ---
    c.setStrokeColor(RULE_COLOR)
    c.setLineWidth(0.5)
    c.line(MARGIN_LEFT, cursor_y, PAGE_WIDTH - MARGIN_RIGHT, cursor_y)
    cursor_y -= 20

    # --- Sections ---
    for section in SECTIONS:
        # Heading (uppercase, letter-spaced, purple)
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(PURPLE)
        draw_spaced_text(c, section["heading"], MARGIN_LEFT, cursor_y, 2.2)
        cursor_y -= 18

        # Body paragraph
        style = BODY_BOLD_STYLE if section["bold"] else BODY_STYLE
        para = Paragraph(section["body"], style)
        para_width = CONTENT_WIDTH
        _, para_height = para.wrap(para_width, 400)

        para.drawOn(c, MARGIN_LEFT, cursor_y - para_height)
        cursor_y -= para_height + 24

    # --- Footer ---
    footer_y = MARGIN_BOTTOM + 10
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(BLACK)
    footer_line_1 = "ginonova.com"
    c.drawCentredString(PAGE_WIDTH / 2, footer_y + 12, footer_line_1)

    c.setFont("Helvetica", 8.5)
    c.setFillColor(LIGHT_GRAY)
    c.drawCentredString(PAGE_WIDTH / 2, footer_y, "saidborna.com")

    c.save()


if __name__ == "__main__":
    generate_pdf()
