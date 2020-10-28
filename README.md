# glimpse

Suppose you are in the following directory:

gss/work/edba4025/glimpse/pbe_pcm+tddft/I2_gd3bj


And there are the following subdirectories:

gss/work/edba4025/glimpse/pbe_pcm+tddft/I2_gd3bj/I-DMSO

gss/work/edba4025/glimpse/pbe_pcm+tddft/I2_gd3bj/I-DMF

gss/work/edba4025/glimpse/pbe_pcm+tddft/I2_gd3bj/I-GBL

gss/work/edba4025/glimpse/pbe_pcm+tddft/I2_gd3bj/I-PC



where your calculations are stored. If you run from terminal:

python3 get_hlgap.py and a file structured like this will be created:


species    HL_GAP      HOMO      LUMO
  I-DMSO  2.818570 -3.952744 -1.134173
  I-NMP  2.845933 -3.884231 -1.038298
  I-DMF  2.856963 -4.015105 -1.158142
  I-GBL  2.779117 -4.252461 -1.473344

for example.

The script will search for files based on 02 and .out patterns.
( You can modify the script based on your needs)   




