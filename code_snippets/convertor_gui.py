import PySimpleGUI as sg
import convertor

sg.theme("black")

label_1 = sg.Text("Enter Feet : ")
input_1 = sg.Input(key="feet")

label_2 = sg.Text("Enter Inches : ")
input_2 = sg.Input(key="inches")

convert_button = sg.Button("Convert", tooltip='Convert to meters')
exit_button = sg.Button("Exit")
output_label = sg.Text(key="meters", text_color="red")

window = sg.Window('Convertor',
                   layout=[[label_1, input_1],
                           [label_2, input_2],
                           [convert_button, exit_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case("Convert"):
            feet = values['feet']
            inches = values['inches']
            print(float(feet))
            print(float(inches))
            meters = convertor.convert(float(feet), float(inches))
            print(meters)
            window['meters'].update(value=meters)
        case ("Exit"):
            break
        case sg.WIN_CLOSED:
            break

window.close()

