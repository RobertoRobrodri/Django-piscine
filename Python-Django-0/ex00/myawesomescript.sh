#!/bin/bash

# --head or -I to show only the header && -s silent
# grep Location searches for field Location
# Cut -d get only the url after locations

curl -s --head $1 | grep Location | cut -d ' ' -f 2
