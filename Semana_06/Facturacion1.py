# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import financieros
subtotal = 800.77
print(f"subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal):.2f}")