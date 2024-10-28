
* Low-pass filter circuit with OPAMP
V1 1 0 AC 1
R1 1 2 12700.0
C2 2 0 1.1499999841291242e-09
R2 2 3 15200.0
C1 3 0 1.500000013088254e-09
X1 3 0 4 OPAMP
.subckt OPAMP 1 2 3
E1 3 0 1 2 100k
.ends OPAMP
.ac dec 10 1k 100Meg
.print ac vdb(3)
.end
