from pyaxidraw import axidraw 
import xml.etree.ElementTree as ET


"""
def regex(file):
    # Function to convert the completion file to Markdown format
    changed_file = file.replace("height="100%"", "height="1052.362179"")
    changed_file = file.replace("width="100%"", "width="744.09447"")
    #changed_file = file.write(read_file("frontmatter")+changed_file+read_file("bottommatter"))
    return f"testing\n{changed_file}\n" 

file=open("/home/alex/Documents/Autocrat/img/llmtest1.svg", "a")
"""

"""
# think this is the isse 
def replace_svg_attributes(svg_file):
    # Parse the SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Define the attributes to replace
    attributes_to_replace = {
        "height": "1052.362179",
        "width": "744.09447"
    }


    # Iterate over all elements and replace attributes
    for elem in root.iter():
        for attr in elem.attrib:
            if attr in attributes_to_replace:
                elem.attrib[attr] = attributes_to_replace[attr]

    # Save the modified SVG file
    modified_svg_file = svg_file.replace(".svg", "_modified.svg")
    tree.write(modified_svg_file)

    print(f"Modified SVG file saved as: {modified_svg_file}")
"""


"""
# remove the background 
def remove_white_background(input_svg_file, output_svg_file):
    # Parse the SVG file
    tree = ET.parse(input_svg_file)
    root = tree.getroot()

    # Find and remove white background elements
    for elem in root.iter():
        if 'fill' in elem.attrib and elem.attrib['fill'] == '#ffffff':
            del elem.attrib['fill']

    # Write modified SVG to a new file
    tree.write(output_svg_file)
"""

# removes all the attribies that are not needed for the pen plotter to work and trick it to prodicing a big black box round things just genraly clears things up
"""
def remove_fill_attribute(input_svg_file, output_svg_file):
    # Parse the SVG file
    tree = ET.parse(input_svg_file)
    root = tree.getroot()

    # sets the correct values for hight and width so pen plotter is setup for A4
    for elem in root.iter():
        if 'baseProfile' in elem.attrib:
            root.set("height", "1052.362179")
            root.set("width", "744.09447")

    # Find and remove the fill attribute from elements
    for elem in root.iter():
        if 'fill' in elem.attrib:
            del elem.attrib['fill']

    # Find and remove the viewbox attribute from elements
    for elem in root.iter():
        if 'viewBox' in elem.attrib:
            del elem.attrib['viewBox']

    # Find and remove the rect attribute from elements
    for elem in root.iter():
        if 'rect' in elem.attrib:
            del elem.attrib['rect']
    
    # Find and remove the rect attribute from elements
    for elem in root.iter():
            if 'ns0:rect' in elem.attrib:
                del elem.attrib['ns0:rect']

    # Write modified SVG to a new file
    tree.write(output_svg_file)


# Replace attributes in the SVG file
#replace_svg_attributes("/home/alex/Documents/Autocrat/img/llmtest1.svg")

input_svg = "/home/alex/Documents/Autocrat/img/llmtest1.svg"  # Provide the path to your SVG file
output_svg = "/home/alex/Documents/Autocrat/img/llmtest1_modified.svg"  # Output file path

#remove_white_background
remove_fill_attribute(input_svg, output_svg)
"""
"""

def find_replace(file_path, find_str, replace_str):
    # Read the content of the file
    with open(file_path, 'r') as file:
        file_content = file.read()

    # Perform find and replace
    modified_content = file_content.replace(find_str, replace_str)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

# file paths 
file_path = "/home/alex/Documents/Autocrat/img/llmtest1.svg"
find_str = '<svg baseProfile="full" height="100%" version="1.1" viewBox="0,0,1000,660" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink"><defs /><rect fill="white" height="660" width="1000" x="0" y="0" />'
replace_str = '<svg baseProfile="full" height="1052.362179" version="1.1" viewBox="0,0,1000,720" width="744.09447" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink">'

find_replace(file_path, find_str, replace_str)

"""

# this function replaces the first section of the svg its dirty and hacky but works i tried edditing the xml nativly and it was not having it this will work eatch time as the rrm that genrates the hand writing doesnt change this section of the svg. im sorry but it works
def find_replace_with_file_content(source_file_path, replacement_file_path):
    # Read the content of the source file
    with open(source_file_path, 'r') as source_file:
        source_content = source_file.read()

    # Read the content of the replacement file
    with open(replacement_file_path, 'r') as replacement_file:
        replacement_content = replacement_file.read()

    # Find the start and end indices of the substring to be replaced
    start_index = source_content.find('<svg baseProfile')
    end_index = source_content.find('y="0" />', start_index) + len('y="0" />')

    # Replace the substring with the content from the replacement file
    modified_content = source_content[:start_index] + replacement_content + source_content[end_index:]

    # Write the modified content back to the source file
    with open(source_file_path, 'w') as source_file:
        source_file.write(modified_content)

# Example usage
source_file_path = '/home/alex/Documents/Autocrat/img/llmtest1.svg'
replacement_file_path = 'cleansvg_header'

find_replace_with_file_content(source_file_path, replacement_file_path)

# declare the varible and seup some options for the plotter 
ad = axidraw.AxiDraw()
#ad.plot_setup("test_files/a5pdfwithtext.svg")
#ad.plot_setup("/home/alex/Documents/Autocrat/handwriting-synthesis/img/all_star.svg")
#ad.plot_setup("/home/alex/Documents/Autocrat/img/llmtest1_modified.svg")
ad.plot_setup("/home/alex/Documents/Autocrat/img/llmtest1.svg")
#ad.plot_setup("/home/alex/Documents/Autocrat/img/allstar.svg")

#setting up options for the pen plotter 
ad.options.pen_pos_up = 57      # set pen-up position
ad.options.pen_pos_down = 50    # set pen-down position
ad.options.pen_rate_lower = 100
ad.options.pen_rate_raise  = 100
ad.options.accel = 100
ad.options.speed_penup = 100
ad.options.speed_pendown = 100
ad.options.accel = 100

ad.errors.connect = True        # Raise error on failure to connect
ad.errors.button = True         # Raise error on pause button press
ad.errors.keyboard = True       # Raise error on keyboard interrupt
ad.errors.disconnect = True     # Raise error on loss of connection



ad.plot_run() # run the plot

#"""
#while True:
#    ad.plot_run() # run the plot

