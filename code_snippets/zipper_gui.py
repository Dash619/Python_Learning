import PySimpleGUI as sg
from zip_creator import make_archive

selection_label = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

destination_label = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="Output", text_color="green")

window = sg.Window('Zipper',
                   layout=[[selection_label, input1, choose_button1],
                           [destination_label, input2, choose_button2],
                           [compress_button, output_label]], font=('Helvetica', 12))
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["Output"].update(value="Compression Completed!")

window.read()
window.close()
