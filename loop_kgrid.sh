#! /bin/bash
BIN=/home/anliski/Desktop/DFT/VASP/vasp_std
#BIN=/home/anna/Desktop/VASP/vasp_std
rm WAVECAR
for i in 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ; do
cat >KPOINTS <<!
K-Points
 0
Gamma
 $i $i $i
 0  0  0
!
echo "a= $i" ; $BIN
E=`tail -1 OSZICAR` ; echo $i $E  >>e400_a3.106_k
done
cat e400_a3.106_k
