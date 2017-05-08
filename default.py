#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import  math
def bib(height,weight):
    height = float(height)
    weight = float(weight)
    bmi = weight/(height*height)
    if bmi<18.5:
        print('过轻')
    elif bmi<25:
        print('正常')
    elif bmi<28:
        print('过重')
    elif bmi<32:
        print('肥胖')
    else:
        print('严重肥胖')

def bic():
    height = input('请输入你的身高:')
    weight = input('请输入你的体重:')
    height = float(height)
    weight = float(weight)
    bmi = weight/(height*height)
    if bmi<18.5:
        print('过轻')
    elif bmi<25:
        print('正常')
    elif bmi<28:
        print('过重')
    elif bmi<32:
        print('肥胖')
    else:
        print('严重肥胖')

def bid():
    pass

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y+step*math.sin(angle)
    return nx,ny

def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)