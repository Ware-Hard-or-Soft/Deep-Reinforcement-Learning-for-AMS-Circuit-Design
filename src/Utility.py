"""
Filename: utils.py
Author: David Zheng
Copyright: © 2024 David Zheng. All rights reserved.
Contact: dqzheng1996@gmail.com
Description: Utility functions for filter design project, including reward calculation, cutoff frequency estimation, and output parsing.
"""

import numpy as np

def reward_function(frequencies, magnitudes, target_cutoff, passband_tolerance=1, stopband_attenuation=-20):
    reward = 0
    penalty = 0
    for freq, mag in zip(frequencies, magnitudes):
        if freq <= target_cutoff:
            if abs(mag) <= passband_tolerance:
                reward += 5
            else:
                penalty += 5 * abs(mag)
        else:
            if mag <= stopband_attenuation:
                reward += 5
            else:
                penalty += 5 * (mag - stopband_attenuation)

    actual_cutoff = estimate_cutoff_frequency(frequencies, magnitudes, target_cutoff)
    if abs(actual_cutoff - target_cutoff) < 0.1 * target_cutoff:
        reward += 20
    else:
        penalty += 10
    return reward - penalty

def estimate_cutoff_frequency(frequencies, magnitudes, target_cutoff):
    for freq, mag in zip(frequencies, magnitudes):
        if mag <= -3:
            return freq
    return target_cutoff

def parse_output(file_path):
    frequencies = []
    magnitudes = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split()
            if len(data) >= 2:
                try:
                    freq = float(data[1].replace(',', ''))
                    vdb3 = float(data[2].replace(',', ''))
                    frequencies.append(freq)
                    magnitudes.append(vdb3)
                except ValueError:
                    continue
    return frequencies, magnitudes
'''
1. Passband Performance:
For frequencies up to the target cutoff (freq <= target_cutoff), the function checks if the magnitude is close to 0 dB (within passband_tolerance).
If it’s within this tolerance, a reward of +10 is given.
If it deviates from this ideal value, a penalty proportional to the deviation (5 * abs(mag)) is subtracted.

2. Stopband Attenuation:
For frequencies above the target cutoff (freq > target_cutoff), the function checks if the magnitude is below the target stopband attenuation level (stopband_attenuation, typically -20 dB).
If it meets this criterion, a reward of +5 is given.
If not, a penalty proportional to the deviation from the target attenuation (5 * (mag - stopband_attenuation)) is subtracted.

3. Cutoff Frequency Proximity:
The function calculates the actual cutoff frequency (where the gain drops to -3 dB) using estimate_cutoff_frequency.
If this cutoff frequency is within 10% of the target cutoff frequency, a bonus reward of +20 is given.
If it deviates by more than 10%, a penalty of -20 is applied.

'''