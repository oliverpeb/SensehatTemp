from sense_hat import SenseHat

# Initialiserer Sense HAT-objektet
sense = SenseHat()


# Funktion til at indstille farve og tekst baseret på temperatur
def set_led_color_and_text(temperature):
    if temperature > 19:
        # Rød farve
        sense.clear(255, 0, 0)
        if temperature > 22:
            sense.show_message("Skru ned")
    elif temperature < 19:
        # Blå farve
        sense.clear(0, 0, 255)
    else:
        # Grøn farve
        sense.clear(0, 255, 0)


# Simulerer en temperaturværdi (ændre værdien efter behov)
temperature = 23

# Viser tekst og farve baseret på temperatur
set_led_color_and_text(temperature)
print("Temperaturen er:", temperature, "grader C")
