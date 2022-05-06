from plyer import filechooser
from kivy.properties import ObjectProperty
from kivymd.uix.stacklayout import StackLayout
from kivymd.uix.menu import MDDropdownMenu
from model.constants import options
from kivymd.app import MDApp

class ActionPanel(StackLayout):
    search_dropdown = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #search dropdown init
        caller = self.ids.search_caller
        items = [
            {"viewclass": "BaseListItem", 
            "text": value,
            "on_press": lambda x=key: self.searchDialogCallback(x) 
            }
            for key, value in options.items()
            ]
        self.search_dropdown = MDDropdownMenu(caller=caller, items=items, width_mult=4)   

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

    def searchDialogCallback(self, key):
        self.search_dropdown.dismiss()
        getattr(MDApp.get_running_app().controller, key)()
        
        