-- 코드를 입력하세요
SELECT AO.ANIMAL_ID,AO.NAME
from ANIMAL_INS as AI
inner join ANIMAL_OUTS as AO
on AI.ANIMAL_ID=AO.ANIMAL_ID
where AI.DATETIME>AO.DATETIME
order by AI.DATETIME;