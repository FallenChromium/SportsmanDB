from plyer import filechooser
from kivy.properties import ObjectProperty
from kivymd.uix.stacklayout import StackLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from view.constants import search_options, delete_options
from kivymd.app import MDApp

class IncorrectFileDialog(MDDialog):
    def __init__(self):
        super().__init__(
            title="Parsing error:",
            text="Sorry, but the file you've opened has incorrect format. Please try opening another file.",
            buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        theme_text_color="Custom",
                        on_press=self.dismiss
                    ),
                ],
        )


class ActionPanel(StackLayout):
    search_dropdown = ObjectProperty(None)
    delete_dropdown = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #search dropdown init
        search_items = [
            {"viewclass": "BaseListItem", 
            "text": value,
            "on_press": lambda x=key: self.searchDialogCallback(x) 
            }
            for key, value in search_options.items()
        ]
        self.search_dropdown = MDDropdownMenu(caller=self.ids.search_caller, items=search_items, width_mult=4) 

        #delete dropdown init
        delete_items = [
            {"viewclass": "BaseListItem", 
            "text": value,
            "on_press": lambda x=key: self.deleteDialogCallback(x) 
            }
            for key, value in delete_options.items()
        ]
        self.delete_dropdown = MDDropdownMenu(caller=self.ids.delete_caller, items=delete_items, width_mult=4)   
 
    def addRecordDialog(self):
        MDApp.get_running_app().controller.addRecord() 
 


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
    
    def deleteDialogCallback(self, key):
        self.delete_dropdown.dismiss()
        getattr(MDApp.get_running_app().controller, key)()
        
        