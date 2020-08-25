#!/usr/bin/env python3
# -*- ecoding: utf-8 -*-

import csv
from tkinter import messagebox as mb

db = open('dados.csv')
out_put = open('resultado.csv', 'w')

linhas = csv.reader(db)

ES = 0
MS = 0
N = 0
MC = 0
EC = 0

out_put.write('ANO,SPI,CLASSIFICAÇÃO\n')

for linha in linhas:

    try:

        # ES: SPI < -1.50
        if float(linha[1]) < -1.5:
            out_put.write(linha[0]+','+linha[1]+',Extremamente Seco-ES\n')
            ES += 1

        # Moderadamente Seco: -1.49 a -0,5
        if -1.49 <= float(linha[1]) <= -0.5:
            out_put.write(linha[0]+','+linha[1]+',Moderadamente Seco - MS\n')
            MS += 1

        # Quase normal -0.49 a 0.49
        if -0.49 <= float(linha[1]) <= 0.49:
            out_put.write(linha[0]+','+linha[1]+',Quase normal - N\n')
            N += 1

        # Moderadamente chuvoso: 0.5 a 1.49
        if 0.5 <= float(linha[1]) <= 1.49:
            out_put.write(linha[0]+','+linha[1] +
                          ',Moderadamente Chuvoso - MC\n')
            MC += 1

        # Extremamente Chuvoso: SPI > 1.50
        if float(linha[1]) > 1.50:
            out_put.write(linha[0]+','+linha[1]+',Extremamente chuvoso - EC\n')
            EC += 1

    except ValueError:
        pass

out_put.write(
    '\nTotal\nES:{}\nMS:{}\nN:{}\nMC:{}\nEC:{}'.format(ES, MS, N, MC, EC))

mb.showinfo('Sucesso', 'Arquivo exportado. :)')
