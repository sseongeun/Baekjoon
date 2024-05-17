-- 코드를 입력하세요
SELECT fh.FLAVOR
from FIRST_HALF as fh
inner join ICECREAM_INFO as ii
on fh.flavor=ii.flavor
where fh.total_order >=3000 and ii.INGREDIENT_TYPE="fruit_based"
order by total_order DESC;