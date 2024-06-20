-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID,TITLE,PRICE,CASE when status="DONE" THEN "거래완료"
when status="SALE" THEN "판매중"
when status="RESERVED" THEN "예약중" END STATUS
from USED_GOODS_BOARD
where CREATED_DATE = "2022-10-05"

order by BOARD_ID DESC;
