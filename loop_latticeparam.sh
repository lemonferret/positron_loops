#! /bin/bash
BIN=/home/anliski/Desktop/DFT/VASP/vasp_std
rm WAVECAR
for i in 3.100 3.101 3.102 3.103 3.104 3.105 3.106 3.107 3.108 3.109  3.110 ; do
cat >POSCAR <<!
bcc Mo:
 $i 
 1 0 0
 0 1 0
 0 0 1
 2
cartesian
0 0 0
0.5 0.5 0.5
!
echo "a= $i" ; $BIN
E=`tail -1 OSZICAR` ; echo $i $E  >>k12_e450_a
done
cat k12_e450_a
