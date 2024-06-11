-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER)
from FIRST_HALF as  fh
inner join ICECREAM_INFO as ii
where fh.flavor = ii.flavor
group by ingredient_type
order by total_order ;