from plyer import filechooser
from kivymd.uix.stacklayout import StackLayout
from kivymd.uix.menu import MDDropdownMenu
from model.constants import options
from kivymd.app import MDApp

class ActionPanel(StackLayout):

    def openFileDialog(self):
        # Kivy file dialog sucks a ton - I want to open a native one instead :)
        path = filechooser.open_file(title="Open an xml file containing the DB", filters=[("*.xml")])
        # check if the user actually chose anything
        if path is not None:
            # because filechooser returns a list of chosen paths. We do not support multi-file import yet
            MDApp.get_running_app().controller.openFile(path[0]) 
        else: 
            pass
    
    def saveFileDialog(self):
            path = filechooser.save_file(title="Enter a filename for the dump file", filters=[("*.xml")])
            if path is not None:
                # because filechooser returns a list of chosen paths. We do not support multi-file import yet
                MDApp.get_running_app().controller.saveFile(path[0])
            else: 
                pass

    def searchDialog(self):
        caller = self.ids.search_caller
        items = [
            {"viewclass": "BaseListItem", 
             "text": value,
             "on_press": getattr(MDApp.get_running_app().controller, key) 
             }
             for key, value in options.items()
            ]
        self.parent.dropdown = MDDropdownMenu(caller=caller, items=items, width_mult=4)
        self.parent.dropdown.open()