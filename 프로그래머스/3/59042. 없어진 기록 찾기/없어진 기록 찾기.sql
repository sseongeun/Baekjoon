SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS AS I
RIGHT OUTER JOIN ANIMAL_OUTS AS O
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID ASC,NAME ASC;