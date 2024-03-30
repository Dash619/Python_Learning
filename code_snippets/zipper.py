import PySimpleGUI as gs

selection_label = gs.Text("Select files to compress: ")
destination_label = gs.Text("Select destination folder: ")
input1 = gs.Input()
input2 = gs.Input()
choose_button1 = gs.FileBrowse("Choose")
choose_button2 = gs.FileBrowse("Choose")
compress_button = gs.Button("Compress")

window = gs.Window('Zipper',
                   layout=[[selection_label, input1, choose_button1],
                           [destination_label, input2, choose_button2],
                            [compress_button]])
window.read()
window.close()
