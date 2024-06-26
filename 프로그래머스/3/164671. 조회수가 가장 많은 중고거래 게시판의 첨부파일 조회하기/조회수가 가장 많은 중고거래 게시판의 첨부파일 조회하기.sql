-- 코드를 입력하세요
SELECT concat("/home/grep/src/",B.BOARD_ID,"/",F.FILE_ID,F.FILE_NAME,F.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD as B
left join USED_GOODS_FILE as F
on B.BOARD_ID=F.BOARD_ID
where views=(select max(views) from  USED_GOODS_BOARD)
ORDER BY FILE_ID DESC;