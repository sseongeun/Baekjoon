SELECT O.ANIMAL_ID,O.NAME
FROM ANIMAL_OUTS AS O
WHERE O.ANIMAL_ID NOT IN (SELECT ANIMAL_ID
                         FROM ANIMAL_INS);