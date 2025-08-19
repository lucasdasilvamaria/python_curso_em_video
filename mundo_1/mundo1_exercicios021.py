# Exercício Python #021 - Tocando um MP3
#
# https://youtu.be/9FiEji_fzvk?list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-
#
#  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('assets/mundo1_exercicios21/mp3_test.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait