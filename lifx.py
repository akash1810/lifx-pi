#!/usr/bin/python

import argparse
import json
import requests
import RPi.GPIO as GPIO
from time import sleep


class ButtonPoller:
    def __init__(self, button_channel, led_channel, token):
        self.button_channel = button_channel
        self.led_channel = led_channel
        self.token = token
        self.state = False

    def _setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_channel, GPIO.OUT)
        GPIO.output(self.led_channel, self.state)

    def _change_bulb_state(self):
        headers = {'Authorization': 'Bearer {}'.format(self.token), 'content-type': 'application/json'}
        data = {'power': 'on' if self.state else 'off'}
        requests.put('https://api.lifx.com/v1/lights/all/state', headers=headers, data=json.dumps(data))

    def start(self):
        print 'start'
        self._setup()

        while True:
            if GPIO.input(self.button_channel) == 1:
                self.state = not self.state
                GPIO.output(self.led_channel, self.state)
                self._change_bulb_state()
                sleep(0.2)

    @staticmethod
    def end():
        print 'end'
        GPIO.cleanup()


def parse_args():
    parser = argparse.ArgumentParser(description='Raspberry Pi Lifx switch')
    parser.add_argument('--button-channel', help='GPIO channel of switch button', required=True, type=int)
    parser.add_argument('--led-channel', help='GPIO channel of led', required=True, type=int)
    parser.add_argument('--lifx-token', help='API token for Lifx API', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    poller = ButtonPoller(args.button_channel, args.led_channel, args.lifx_token)

    try:
        poller.start()
    finally:
        poller.end()