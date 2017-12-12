import tkinter

class ShowInfoGUI:
    def __init__(self):
        # Constructs and retrieves an instance to the Tk class. This creates
        # a widget which will be the main window of the program.
        self.main_window = tkinter.Tk()

        # Creates two frames widgets on the main window. These will be used to
        # contain other widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Creates a string variable which has the ability to be dynamically
        # updated on the window whenever self.value is changed.
        # Creates a label on the top frame which will display the contents
        # of the the string variable created.
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame,
                                           textvariable = self.value)

        # Creates a button on the bottom frame called "Show Info" which will
        # call self.show_info() when pressed.
        # Creates a button on the bottom frame called "Quit" which will close
        # the main window.
        self.address_button = tkinter.Button(self.bottom_frame,
                                             text = 'Show Info',
                                             command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)

        # Packs the label.
        self.address_label.pack()
        # Pack the buttons
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # Packs the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Runs the main loop of Tcl to start the display of the interface.
        tkinter.mainloop()

    # Updates the contents of the string variable which is displayed as a label
    # in the top frame.
    def show_info(self):
        self.value.set('Steven Marcus\n274 Baily Drive\n'
                       'Waynesville, NC 27999')

# Constructs and retrieves an instance to a ShowInfoGUI class upon the program
# running.
show_info = ShowInfoGUI()
