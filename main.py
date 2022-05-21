"""
ini adalah file percobaan pertama
"""

susu = input("Apakah susu ada?")
beli = 'tidak ada yg dibeli'
if susu == 'y':
    telur = input("Apakah ada Telur?")
    if telur == 'y':
        beli = 'telur 6 dan susu 1'
    else:
        beli = 'susu 1'

    print(beli)
else:
    print(beli)