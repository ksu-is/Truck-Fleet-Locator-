from reportlab.pdfgen import canvas
def generate_invoice(pickup_id, driver_name, customer_name, amount):
    # Create a PDF file
    pdf_file = f"invoice_{pickup_id}.pdf"
    c = canvas.Canvas(pdf_file)

    # Set title and font
    c.setTitle("Invoice")
    c.setFont("Helvetica", 12)

    # Add content to the PDF
    c.drawString(100, 800, f"Pickup ID: {pickup_id}")
    c.drawString(100, 780, f"Driver Name: {driver_name}")
    c.drawString(100, 760, f"Customer Name: {customer_name}")
    c.drawString(100, 740, f"Amount: ${amount:.2f}")

    # Save the PDF file
    c.save()

    return pdf_file
print("Invoice generated successfully!")
