-- 코드를 작성해주세요
select fi.ID,fni.FISH_NAME,fi.LENGTH
from FISH_INFO as fi
inner join FISH_NAME_INFO as fni
on fi.FISH_TYPE=fni.FISH_TYPE
where fi.FISH_TYPE in (select FISH_TYPE
                   from FISH_INFO
                   group by FISH_TYPE
                   having LENGTH=max(LENGTH))
order by fi.ID ASC;