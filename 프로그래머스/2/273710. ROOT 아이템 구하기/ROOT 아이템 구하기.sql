-- 코드를 작성해주세요
SELECT I.ITEM_ID, ITEM_NAME
FROM ITEM_INFO AS I
INNER JOIN ITEM_TREE
WHERE I.ITEM_ID = ITEM_TREE.ITEM_ID
AND PARENT_ITEM_ID is null
ORDER BY ITEM_ID;