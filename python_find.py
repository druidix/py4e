#!/usr/local/bin/python3

test_string = "X-DSPAM-Confidence:    0.8475";

print(float(test_string[test_string.rfind(' '):]))