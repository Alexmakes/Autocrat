from pyaxidraw import axidraw 

# declare the varible and seup some options for the plotter 
ad = axidraw.AxiDraw()
#ad.plot_setup("test_files/a5pdfwithtext.svg")
ad.plot_setup("text.svg")
ad.options.pen_pos_up = 57      # set pen-up position
ad.options.pen_pos_down = 46    # set pen-down position
ad.options.pen_rate_lower = 100
ad.options.pen_rate_raise  = 100
ad.options.accel = 100
ad.options.speed_penup = 100
ad.options.speed_pendown = 100
ad.options.accel = 100



ad.plot_run() # run the plot