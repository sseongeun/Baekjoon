-- 코드를 입력하세요
SELECT DR_NAME,DR_ID,MCDP_CD,DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
from Doctor
where MCDP_CD="CS" or MCDP_CD="GS"
Order by HIRE_YMD desc, dr_name asc;