SELECT f.FLAVOR
FROM FIRST_HALF as f
inner join JULY as j
on f.FLAVOR=j.FLAVOR
group by f.flavor
order by sum(f.total_order)+sum(j.total_order) desc
limit 3;
