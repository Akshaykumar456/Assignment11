# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/171tMZV6OYkxuOIwYwpA5uQrG6wjrArqw
"""

with open("ak.txt") as f:
  with open("xx.txt","w") as f1:
    for i in f:
      f1.write(i)