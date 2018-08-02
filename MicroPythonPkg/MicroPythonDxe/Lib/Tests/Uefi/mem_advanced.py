import sys
import uefi
from ucollections import OrderedDict
from unittest import *

TEST_PROTOCOL1 = OrderedDict(
  (
    ("Signature", "Q"),
    ("Revision", "I"),
  )
)
TEST_PROTOCOL2 = OrderedDict(
  (
    ("Signature", "Q"),
    ("Revision", "I"),
    ("Data", "I"),
  )
)



Comprises_b = OrderedDict((
    ("b0", "b:1"),
    ("b1", "b:1"),
    ("b2", "b:1"),
    ("b3", "b:1"),
    ("b4", "b:1"),
    ("b5", "b:1"),
    ("b6", "b:1"),
    ("b7", "b:1"),    
))



Comprises_B = OrderedDict((
    ("B0", "B:1"),
    ("B1", "B:1"),
    ("B2", "B:1"),
    ("B3", "B:1"),
    ("B4", "B:1"),
    ("B5", "B:1"),
    ("B6", "B:1"),
    ("B7", "B:1"),   
))


Comprises_h = OrderedDict((
    ("h0", "h:1"),
    ("h1", "h:1"),
    ("h2", "h:1"),
    ("h3", "h:1"),
    ("h4", "h:1"),
    ("h5", "h:1"),
    ("h6", "h:1"),
    ("h7", "h:1"),  
    ("h8", "h:1"),
    ("h9", "h:1"),
    ("h10", "h:1"),
    ("h11", "h:1"),
    ("h12", "h:1"),
    ("h13", "h:1"),
    ("h14", "h:1"),
    ("h15", "h:1"),  
))



Comprises_H = OrderedDict((
    ("H0", "H:1"),
    ("H1", "H:1"),
    ("H2", "H:1"),
    ("H3", "H:1"),
    ("H4", "H:1"),
    ("H5", "H:1"),
    ("H6", "H:1"),
    ("H7", "H:1"),  
    ("H8", "H:1"),
    ("H9", "H:1"),
    ("H10", "H:1"),
    ("H11", "H:1"),
    ("H12", "H:1"),
    ("H13", "H:1"),
    ("H14", "H:1"),
    ("H15", "H:1"),  
))


Comprises_l = OrderedDict((
    ("l0", "l:1"),
    ("l1", "l:1"),
    ("l2", "l:1"),
    ("l3", "l:1"),
    ("l4", "l:1"),
    ("l5", "l:1"),
    ("l6", "l:1"),
    ("l7", "l:1"),  
    ("l8", "l:1"),
    ("l9", "l:1"),
    ("l10", "l:1"),
    ("l11", "l:1"),
    ("l12", "l:1"),
    ("l13", "l:1"),
    ("l14", "l:1"),
    ("l15", "l:1"),  
    ("l16", "l:1"),
    ("l17", "l:1"),
    ("l18", "l:1"),
    ("l19", "l:1"),
    ("l20", "l:1"),
    ("l21", "l:1"),
    ("l22", "l:1"),
    ("l23", "l:1"),  
    ("l24", "l:1"),
    ("l25", "l:1"),
    ("l26", "l:1"),
    ("l27", "l:1"),
    ("l28", "l:1"),
    ("l29", "l:1"),
    ("l30", "l:1"),
    ("l31", "l:1"),   
))



Comprises_L = OrderedDict((
    ("L0", "L:1"),
    ("L1", "L:1"),
    ("L2", "L:1"),
    ("L3", "L:1"),
    ("L4", "L:1"),
    ("L5", "L:1"),
    ("L6", "L:1"),
    ("L7", "L:1"),  
    ("L8", "L:1"),
    ("L9", "L:1"),
    ("L10", "L:1"),
    ("L11", "L:1"),
    ("L12", "L:1"),
    ("L13", "L:1"),
    ("L14", "L:1"),
    ("L15", "L:1"),  
    ("L16", "L:1"),
    ("L17", "L:1"),
    ("L18", "L:1"),
    ("L19", "L:1"),
    ("L20", "L:1"),
    ("L21", "L:1"),
    ("L22", "L:1"),
    ("L23", "L:1"),  
    ("L24", "L:1"),
    ("L25", "L:1"),
    ("L26", "L:1"),
    ("L27", "L:1"),
    ("L28", "L:1"),
    ("L29", "L:1"),
    ("L30", "L:1"),
    ("L31", "L:1"),  
))





Comprises_q = OrderedDict((
    ("q0", "q:1"),
    ("q1", "q:1"),
    ("q2", "q:1"),
    ("q3", "q:1"),
    ("q4", "q:1"),
    ("q5", "q:1"),
    ("q6", "q:1"),
    ("q7", "q:1"),  
    ("q8", "q:1"),
    ("q9", "q:1"),
    ("q10", "q:1"),
    ("q11", "q:1"),
    ("q12", "q:1"),
    ("q13", "q:1"),
    ("q14", "q:1"),
    ("q15", "q:1"),  
    ("q16", "q:1"),
    ("q17", "q:1"),
    ("q18", "q:1"),
    ("q19", "q:1"),
    ("q20", "q:1"),
    ("q21", "q:1"),
    ("q22", "q:1"),
    ("q23", "q:1"),  
    ("q24", "q:1"),
    ("q25", "q:1"),
    ("q26", "q:1"),
    ("q27", "q:1"),
    ("q28", "q:1"),
    ("q29", "q:1"),
    ("q30", "q:1"),
    ("q31", "q:1"),  
    ("q32", "q:1"),
    ("q33", "q:1"),
    ("q34", "q:1"),
    ("q35", "q:1"),
    ("q36", "q:1"),
    ("q37", "q:1"),
    ("q38", "q:1"),
    ("q39", "q:1"),  
    ("q40", "q:1"),
    ("q41", "q:1"),
    ("q42", "q:1"),
    ("q43", "q:1"),
    ("q44", "q:1"),
    ("q45", "q:1"),
    ("q46", "q:1"),
    ("q47", "q:1"),  
    ("q48", "q:1"),
    ("q49", "q:1"),
    ("q50", "q:1"),
    ("q51", "q:1"),
    ("q52", "q:1"),
    ("q53", "q:1"),
    ("q54", "q:1"),
    ("q55", "q:1"),  
    ("q56", "q:1"),
    ("q57", "q:1"),
    ("q58", "q:1"),
    ("q59", "q:1"),
    ("q60", "q:1"),
    ("q61", "q:1"),
    ("q62", "q:1"),
    ("q63", "q:1"),  
))



Comprises_Q = OrderedDict((
    ("Q0", "Q:1"),
    ("Q1", "Q:1"),
    ("Q2", "Q:1"),
    ("Q3", "Q:1"),
    ("Q4", "Q:1"),
    ("Q5", "Q:1"),
    ("Q6", "Q:1"),
    ("Q7", "Q:1"),  
    ("Q8", "Q:1"),
    ("Q9", "Q:1"),
    ("Q10", "Q:1"),
    ("Q11", "Q:1"),
    ("Q12", "Q:1"),
    ("Q13", "Q:1"),
    ("Q14", "Q:1"),
    ("Q15", "Q:1"),  
    ("Q16", "Q:1"),
    ("Q17", "Q:1"),
    ("Q18", "Q:1"),
    ("Q19", "Q:1"),
    ("Q20", "Q:1"),
    ("Q21", "Q:1"),
    ("Q22", "Q:1"),
    ("Q23", "Q:1"),  
    ("Q24", "Q:1"),
    ("Q25", "Q:1"),
    ("Q26", "Q:1"),
    ("Q27", "Q:1"),
    ("Q28", "Q:1"),
    ("Q29", "Q:1"),
    ("Q30", "Q:1"),
    ("Q31", "Q:1"),  
    ("Q32", "Q:1"),
    ("Q33", "Q:1"),
    ("Q34", "Q:1"),
    ("Q35", "Q:1"),
    ("Q36", "Q:1"),
    ("Q37", "Q:1"),
    ("Q38", "Q:1"),
    ("Q39", "Q:1"),  
    ("Q40", "Q:1"),
    ("Q41", "Q:1"),
    ("Q42", "Q:1"),
    ("Q43", "Q:1"),
    ("Q44", "Q:1"),
    ("Q45", "Q:1"),
    ("Q46", "Q:1"),
    ("Q47", "Q:1"),  
    ("Q48", "Q:1"),
    ("Q49", "Q:1"),
    ("Q50", "Q:1"),
    ("Q51", "Q:1"),
    ("Q52", "Q:1"),
    ("Q53", "Q:1"),
    ("Q54", "Q:1"),
    ("Q55", "Q:1"),  
    ("Q56", "Q:1"),
    ("Q57", "Q:1"),
    ("Q58", "Q:1"),
    ("Q59", "Q:1"),
    ("Q60", "Q:1"),
    ("Q61", "Q:1"),
    ("Q62", "Q:1"),
    ("Q63", "Q:1"),   
))

#### first combined
combined_bB = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberB",    "O#Comprises_B"),
))


combined_bh = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberh",    "O#Comprises_h"),
))

combined_bl = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberl",    "O#Comprises_l"),
))


combined_bL = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberL",    "O#Comprises_L"),
))


combined_bq = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberq",    "O#Comprises_q"),
))


combined_bQ = OrderedDict((
    ("memberb",       "O#Comprises_b"),
    ("memberQ",    "O#Comprises_Q"),
))



### second conbined

secondcombined1 = OrderedDict((
    ("member2a",       "O#combined_bQ"),
    ("member2b",    "O#combined_bq"),
))


secondcombined2 = OrderedDict((
    ("member2c",       "O#combined_bq"),
    ("member2d",    "O#combined_bh"),
))

secondcombined3 = OrderedDict((
    ("member2e",       "O#combined_bL"),
    ("member2f",    "O#combined_bQ"),
))


secondcombined4 = OrderedDict((
    ("member2g",       "O#combined_bB"),
    ("member2h",    "O#combined_bL"),
))



### third order conbined

thirdcombined1 = OrderedDict((
    ("member3a",       "O#secondcombined1"),
    ("member3b",    "O#secondcombined2"),
))


thirdcombined2 = OrderedDict((
    ("member3c",       "O#secondcombined1"),
    ("member3d",    "O#secondcombined3"),
))

thirdcombined3 = OrderedDict((
    ("member3e",       "O#secondcombined1"),
    ("member3f",    "O#secondcombined4"),
))


thirdcombined4 = OrderedDict((
    ("member3g",       "O#secondcombined2"),
    ("member3h",    "O#secondcombined4"),
))


### higher order combined

highercombined1 = OrderedDict((
    ("member4a",       "O#thirdcombined1"),
    ("member4b",    "O#thirdcombined2"),
))


highercombined2 = OrderedDict((
    ("member4c",       "O#thirdcombined1"),
    ("member4d",    "O#thirdcombined3"),
))

highercombined3 = OrderedDict((
    ("member4e",       "O#thirdcombined1"),
    ("member4f",    "O#thirdcombined4"),
))


highercombined4 = OrderedDict((
    ("memberb4g",       "O#thirdcombined3"),
    ("memberb4h",    "O#thirdcombined4"),
))






class advanced_memory(TestCase):
    def setUp(self):
        log(0, "[UEFI_BOOT_SERVICES: BEGIN]")

    def tearDown(self):
        log(0, "\n[UEFI_BOOT_SERVICES: PASS]")

  

    def test_advanced_mem(self):
        log(1, "\r\n[advanced_mem Test]")   
        higherorder = mem("O#highercombined4")
		
        combined = mem("O#Comprises_B")
     
        combined.B0 = 1
   #     higherorder.memberb4g.member3e.member2a.memberb.b0 = 1


if __name__ == '__main__':
    mytest = advanced_memory()

