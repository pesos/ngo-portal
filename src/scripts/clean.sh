#!/bin/bash

# Remove all *.pyc files recursively from project root
find ../ -name \*.pyc -delete

# Remove all *~ files recursively from project root
find ../ -name \*~ -delete