#!/bin/bash

pyinstaller -w --icon=favicon.ico -n "LogBaseTwo" --add-data="favicon.ico;." .\logbasetwo.py