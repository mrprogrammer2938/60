#!/usr/bin/env bash
# This Programm write by Mr.nope
# Installing 60 Tool
if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
main() {
    printf '\033]2;60-Installing\a'
    clear
    echo "Installing..."
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    echo ""
    echo "Finish..!"
    echo ""
    exit 1
}
chmod +x 60.py
main