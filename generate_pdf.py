from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
import os

def create_whitepaper(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=LETTER,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='TitlePageTitle', fontSize=24, leading=28, spaceAfter=20, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='TitlePageSubtitle', fontSize=16, leading=20, spaceAfter=50, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Abstract', fontSize=12, leading=14, leftIndent=20, rightIndent=20, spaceAfter=30))
    
    Story = []

    # TITLE PAGE
    Story.append(Spacer(1, 100))
    Story.append(Paragraph("The Q Protocol", styles["TitlePageTitle"]))
    Story.append(Paragraph("Architectural Standards for Autonomous Agentic Meshes", styles["TitlePageSubtitle"]))
    Story.append(Paragraph("<b>Version:</b> 1.0<br/><b>Date:</b> February 2026<br/><b>Author:</b> Phil Hills<br/><b>Role:</b> Systems Architect", styles["Normal"]))
    Story.append(PageBreak())

    # ABSTRACT
    Story.append(Paragraph("Abstract", styles["Heading1"]))
    Story.append(Paragraph("""Q Protocol defines a coordination substrate for multi-agent systems in which communication is treated as a failure mode, not a default behavior. Instead of optimizing message passing, compression, or token efficiency, Q Protocol optimizes for shared cognitive structure, enabling agents to coordinate via minimal symbolic coordinates and externalized re-entry artifacts.""", styles["Abstract"]))
    
    # SECTIONS
    sections = [
        ("1. Motivation", """Most contemporary AI systems are designed around output generation (text, JSON). This equates intelligence with verbosity. Q Protocol inverts this model: If agents share sufficient structure, communication is unnecessary."""),
        ("2. Core Principles", """• Coordination precedes communication<br/>• Silence is success<br/>• Tokens are boundary artifacts<br/>• Memory is re-entry, not storage"""),
        ("3. Ontology", """<b>Latent State Space (Lambda):</b> Continuous, high-dimensional state.<br/><b>Action Coordinates (Q):</b> A minimal action coordinate pointing within shared structure D.<br/><b>Shared Structure (D):</b> The primary optimization target. Symbols, macros, and invariants negotiated between agents."""),
        ("4. Execution Semantics", """An execution is successful if and only if a Receipt (RCPT) is produced. Output is optional. Receipts are mandatory. Projection (human-visible output) is permitted only under explicit boundary declarations (e.g., BND:HUMAN)."""),
        ("5. Agent Lifecycle", """Onboarding is calibration. An agent must load global RULEs and align to D version before acting. D grows via promotion signals (high recurrence, reduction in message length)."""),
        ("6. Security & Verification", """All artifacts are signed. Receipts are immutable. State transitions are auditable. Claims without RCPT are ignored.""")
    ]
    
    for title, content in sections:
        Story.append(Paragraph(title, styles["Heading2"]))
        Story.append(Paragraph(content, styles["Normal"]))
        Story.append(Spacer(1, 12))

    # FOOTER LOGIC (built-in to build, but simple here)
    doc.build(Story)

if __name__ == "__main__":
    os.makedirs("c:/Users/bphil/philhills.github.io/whitepaper", exist_ok=True)
    create_whitepaper("c:/Users/bphil/philhills.github.io/whitepaper/The_Q_Protocol.pdf")
    print("PDF Generated.")
