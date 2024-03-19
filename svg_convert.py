import svgwrite

def mm_to_svg_units(mm):
    # Conversion factor from millimeters to SVG units (1 mm = 3.543307 SVG units)
    return mm * 3.543307

def text_to_svg(text, font_size_mm, output_file="output.svg"):
    # A4 size in millimeters
    a4_width_mm = 210
    a4_height_mm = 297
    
    # Convert font size from millimeters to SVG units
    font_size = mm_to_svg_units(font_size_mm)
    
    # Create SVG drawing with A4 dimensions
    dwg = svgwrite.Drawing(output_file, size=(mm_to_svg_units(a4_width_mm), mm_to_svg_units(a4_height_mm)))
    
    # Calculate text position to center it on A4 page
    text_width = len(text) * font_size * 0.65  # Approximate width of text
    text_x = (mm_to_svg_units(a4_width_mm) - text_width) / 2
    text_y = mm_to_svg_units(a4_height_mm) / 2
    
    # Add text to SVG drawing
    dwg.add(dwg.text(text, insert=(text_x, text_y), font_size=font_size))
    
    # Save SVG file
    dwg.save()
    print(f"SVG file '{output_file}' generated successfully.")

text = "Your text here"
font_size_mm = 1  # Font size in millimeters
text_to_svg(text, font_size_mm, output_file="text.svg")