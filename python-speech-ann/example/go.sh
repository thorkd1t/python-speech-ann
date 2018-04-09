#!/bin/bash
pulseaudio --kill
jack_control start
python soun.py
