*xij: Where i is the supply region, and j is the demand region.
Integer Variable
x11, x12, x13, x14, x15,
x21, x22, x23, x24, x25,
x31, x32, x33, x34, x35,
x41, x42, x43, x44, x45,
x51, x52, x53, x54, x55;

*Decision variables for plant locations.
Binary Variable
lp1, lp2, lp3, lp4, lp5,
hp1, hp2, hp3, hp4, hp5; 

Free Variable
z;

Equations
con1,
con2,
con3,
con4,
con5,
con6,
con7,
con8,
con9,
con10,
obj;


*These are the constraints on the decision variables (excess capacity).
con1.. (10*lp1 + 20*hp1) - x11 - x12 - x13 - x14 - x15  =g= 0;
con2.. (10*lp2 + 20*hp2) - x21 - x22 - x23 - x24 - x25  =g= 0;
con3.. (10*lp3 + 20*hp3) - x31 - x32 - x33 - x34 - x35  =g= 0;
con4.. (10*lp4 + 20*hp4) - x41 - x42 - x43 - x44 - x45  =g= 0;
con5.. (10*lp5 + 20*hp5) - x51 - x52 - x53 - x54 - x55  =g= 0;

*These are the constraints on the decision variables (unmet demand).
con6..  12 - x11 - x12 - x13 - x14 - x15  =e= 0;
con7..  8 - x21 - x22 - x23 - x24 - x25  =e= 0;
con8..  14 - x31 - x32 - x33 - x34 - x35  =e= 0;
con9..  16 - x41 - x42 - x43 - x44 - x45  =e= 0;
con10.. 7 - x51 - x52 - x53 - x54 - x55  =e= 0;

obj..
81*x11 + 92*x12 + 101*x13 + 130*x14 + 115*x15 +
117*x21 + 77*x22 + 108*x23 + 98*x24 + 100*x25 +
102*x31 + 105*x32 + 95*x33 + 119*x34 + 111*x35 +
115*x41 + 125*x42 + 90*x43 + 59*x44 + 74*x45 +
142*x51 + 100*x52 + 103*x53 + 105*x54 + 71*x55 +
6000*lp1 + 4500*lp2 + 6500*lp3 + 4100*lp4 + 4000*lp5 +
9000*hp1 + 6750*hp2 + 9750*hp3 + 6150*hp4 + 6000*hp5 =e= z;
    
Model problem /
con1,
con2,
con3,
con4,
con5,
con6,
con7,
con8,
con9,
con10,
obj/ ;
 
Options MIP = cplex;
  
Solve problem using MIP minimizing z;
   
Display
x11.L, x12.L, x13.L, x14.L, x15.L,
x21.L, x22.L, x23.L, x24.L, x25.L,
x31.L, x32.L, x33.L, x34.L, x35.L,
x41.L, x42.L, x43.L, x44.L, x45.L,
x51.L, x52.L, x53.L, x54.L, x55.L,
lp1.L, lp2.L, lp3.L, lp4.L, lp5.L,
hp1.L, hp2.L, hp3.L, hp4.L, hp5.L,
z.L;
