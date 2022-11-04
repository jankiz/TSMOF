----------------------------- MODULE Scheduling_with_distr_${i} -----------------------------
EXTENDS Naturals, Integers, Sequences, TLC

CONSTANT MAX_NUM_OP, WINDOW_SIZE, TIMEOUT_ALG1

VARIABLES numOp, now1, now2, now3, now4, dropList, ui, pi1, pi2

vars == <<numOp, now1, now2, now3, now4, dropList, ui, pi1, pi2>>

UPLOAD_LATENCY == ${u_txt}
PROC_TIME_ALG_1 == ${a1_txt} 
PROC_TIME_ALG_2 == ${a2_txt}

TEST_SET == 0..0

Init == /\ now1 = [n \in TEST_SET |-> 0]
        /\ now2 = [n \in TEST_SET |-> 0]
        /\ now3 = [n \in TEST_SET |-> 0]
        /\ now4 = [n \in TEST_SET |-> 0]
        /\ dropList = [n \in TEST_SET |-> <<>>]
        /\ ui = [n \in TEST_SET |-> (Head(UPLOAD_LATENCY))]
        /\ pi1 = [n \in TEST_SET |-> (Head(PROC_TIME_ALG_1))]
        /\ pi2 = [n \in TEST_SET |-> (Head(PROC_TIME_ALG_2))]
        /\ numOp = [n \in TEST_SET |-> 0]

Step(t) == /\ IF numOp[t] < MAX_NUM_OP
              THEN  /\ numOp' = [numOp EXCEPT ![t] = numOp[t] + 1]     
                    /\ now1' = [now1 EXCEPT ![t] = now1[t] + WINDOW_SIZE]
                    /\ now2' = [now2 EXCEPT ![t] = now1'[t] + ui[t]]
                    /\ IF now3[t] < now2'[t] + TIMEOUT_ALG1
                       THEN /\ dropList' = [dropList EXCEPT ![t] = <<FALSE>> \o dropList[t]]
                            /\ now3' = [now3 EXCEPT ![t] = now2'[t] + pi1[t]]
                            /\ IF now3'[t] > now4[t]
                               THEN /\ now4' = [now4 EXCEPT ![t] = now3'[t] + pi2[t]]
                               ELSE /\ UNCHANGED <<now4>>
                       ELSE /\ dropList' = [dropList EXCEPT ![t] = <<TRUE>> \o dropList[t]]
                            /\ UNCHANGED <<now3, now4>>
                    
                    /\ ui' = [ui EXCEPT ![t] = (UPLOAD_LATENCY[numOp[t] + 1])]
                    /\ pi1' = [pi1 EXCEPT ![t] = (PROC_TIME_ALG_1[numOp[t] + 1])]
                    /\ pi2' = [pi2 EXCEPT ![t] = (PROC_TIME_ALG_2[numOp[t] + 1])]
            ELSE /\ UNCHANGED vars
                  
Next == \E t \in TEST_SET: Step(t)

Spec == Init /\ [][Next]_vars

=============================================================================
\* Modification History
\* Last modified Thu Jan 06 22:03:28 CET 2022 by jankiz
\* Created Mon Jan 03 18:51:30 CET 2022 by jankiz
