import cairosvg
import svgwrite
from io import BytesIO

def convert_text_to_path(input_svg_file, output_svg_file):
    try:
        # Render SVG to PNG
        png_output = BytesIO()
        cairosvg.svg2png(url=input_svg_file, write_to=png_output)

        # Convert PNG to SVG
        svg_output = BytesIO()
        cairosvg.surface.PNGSurface.convert(
            png_output.getvalue(), 
            write_to=svg_output
        )

        # Write SVG to file
        with open(output_svg_file, "wb") as f:
            f.write(svg_output.getvalue())

        print(f"Text in {input_svg_file} converted to path and saved to {output_svg_file}")
    except Exception as e:
        print(f"Error converting SVG: {e}")

# Replace these with your SVG file paths
input_svg_file = "input.svg"
output_svg_file = "output.svg"

convert_text_to_path(input_svg_file, output_svg_file)