SELECT O.ANIMAL_ID,O.NAME
FROM ANIMAL_INS AS I
RIGHT OUTER JOIN ANIMAL_OUTS AS O
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE INTAKE_CONDITION IS NULL;