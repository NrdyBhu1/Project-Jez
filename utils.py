#!/usr/bin/env python3

def brighten_color(color, intensity=10):
    return (color[0]+intensity, color[1]+intensity, color[2]+intensity)


def darken_color(color, intensity=10):
    return (color[0]-intensity, color[1]-intensity, color[2]-intensity)
