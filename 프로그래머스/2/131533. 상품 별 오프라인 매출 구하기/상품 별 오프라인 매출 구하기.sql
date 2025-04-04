 # 상품별 매출액의 합계를 구한다.
 SELECT P.PRODUCT_CODE,SUM(O.SALES_AMOUNT) * P.PRICE AS SALES
 FROM PRODUCT AS P
 INNER JOIN OFFLINE_SALE AS O
 ON P.PRODUCT_ID = O.PRODUCT_ID
 GROUP BY P.PRODUCT_CODE
 ORDER BY SALES DESC,PRODUCT_CODE ASC;