# Lifx-Pi

A simple Python script to turn a Lifx bulb on/off via switch attached a Raspberry Pi's GPIO.
An LED attached to the Pi also provides an additional indication on the state of the Lifx bulb.

## Setup
- Attach a switch and an LED to the GPIO of a Raspberry Pi.
- Create a Lifx Token (see https://cloud.lifx.com/settings).
- Install requirements: `pip install -r requirements.txt`.

## Running
Make a note of the GPIO pins used ([this map](http://pi.gadgetoid.com/pinout) might be helpful).

Run the command, supplying the correct arguments:

```python
sudo python lifx.py --button-channel BUTTON --led-channel LED --lifx-token TOKEN
```

NB: `sudo` is needed by the [`RPi.GPIO`](https://pypi.python.org/pypi/RPi.GPIO) library.