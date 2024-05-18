-- 코드를 입력하세요
SELECT AO.ANIMAL_ID,AO.NAME
from ANIMAL_OUTS as AO
left outer join ANIMAL_INS as AI
on AI.ANIMAL_ID=AO.ANIMAL_ID
where AI.ANIMAL_ID is null
order by AO.ANIMAL_ID;