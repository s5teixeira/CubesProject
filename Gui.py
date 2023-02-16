from tkinter import *
import main
from main import main


# When the user selects one of the entries from your list, display the complete entry data in a Graphical User interface


class Window():
    def __init__(self):
        super().__init__()
        # Creating the tkinter Window
        self.root = Tk()
        self.root.title("Cubes Project List")
        self.root.geometry('400x350')

        # Button for closing
        exit_button = Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.grid(column=0, row=0)

        # LABELS
        prefix_label = Label(self.root, text="Prefix", bg='red')
        prefix_label.grid(column=0, row=1)
        prefix_label.insert(json_response[0])

        first_nameLabel = Label(self.root, text="first name", bg='red')
        first_nameLabel.grid(column=0, row=2)

        last_nameLabel = Label(self.root, text="Last name", bg='red')
        last_nameLabel.grid(column=0, row=3)

        titleLabel = Label(self.root, text="Title", bg='red')
        titleLabel.grid(column=0, row=4)

        organization_nameLabel = Label(self.root, text="Organization Name", bg='red')
        organization_nameLabel.grid(column=0, row=5)

        emailLabel = Label(self.root, text="Email", bg='red')
        emailLabel.grid(column=0, row=6)

        org_websiteLabel = Label(self.root, text="Organization Website", bg='red')
        org_websiteLabel.grid(column=0, row=7)

        self.root.mainloop()


test = Window()
