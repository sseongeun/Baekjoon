-- 코드를 작성해주세요
SELECT F.ID,N.FISH_NAME,F.LENGTH
FROM FISH_INFO AS F
INNER JOIN FISH_NAME_INFO AS N
ON F.FISH_TYPE = N.FISH_TYPE
INNER JOIN (SELECT I.FISH_TYPE,MAX(I.LENGTH) AS LENGTH
FROM FISH_INFO AS I
JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY I.FISH_TYPE) AS TEMP

ON F.FISH_TYPE = TEMP.FISH_TYPE
AND F.LENGTH = TEMP.LENGTH;