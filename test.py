from dearpygui import dearpygui as dpg

def button_callback():
    user_input = dpg.get_value("TextInput")
    dpg.set_value("OutputLabel", f"Du hast eingegeben: {user_input}")

# Fenster erstellen
dpg.create_context()
dpg.create_viewport(title="Simple GUI", width=400, height=300)

with dpg.window(label="Hauptfenster", width=400, height=300):
    dpg.add_text("Willkommen zu Dear PyGui!")
    dpg.add_input_text(label="Gib etwas ein", tag="TextInput")
    dpg.add_button(label="Absenden", callback=button_callback)
    dpg.add_text("", tag="OutputLabel")  # Label für die Ausgabe

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
