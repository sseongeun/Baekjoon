SELECT ID,EMAIL,FIRST_NAME,LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (select sum(code)
                   from skillcodes
                   where name in("C#","Python"))
order by id;
                   
                    