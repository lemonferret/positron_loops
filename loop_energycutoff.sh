#! /bin/bash
BIN=/home/anliski/Desktop/DFT/VASP/vasp_std
rm WAVECAR
for i in  190 200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370 380 390 400 410 420 430 440 450 460 470 480 490 500 510 520 530 540 550; do
cat >INCAR <<!
general:
 System = bcc Mo
 ISTART = 0; ICHARG=2 
 ENCUT  =  $i
 EDIFF = 1e-5
 ISMEAR = 1; SIGMA= 0.2
 LORBIT=11
 PREC=ACCURATE
!
echo "a= $i" ; $BIN
E=`tail -1 OSZICAR` 
K=`grep kinetic OUTCAR| grep -E -o '[0-9]+(\.[0-9]+)?'`; echo $i $E $K >>k15_a3.106_ecut
done
cat k15_a3.106_ecut
