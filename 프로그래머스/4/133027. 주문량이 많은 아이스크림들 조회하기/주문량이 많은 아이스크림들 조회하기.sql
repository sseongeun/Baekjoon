-- 코드를 입력하세요
SELECT a.FLAVOR from first_half a
join july as b


on a.flavor=b.flavor
group by b.flavor
order by sum(a.total_order)+sum(b.total_order) desc limit 3;