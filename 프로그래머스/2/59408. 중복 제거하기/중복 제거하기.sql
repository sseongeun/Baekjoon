-- 코드를 입력하세요
SELECT count(DISTINCT NAME) as count
from ANIMAL_INS
where name is not null;
