-- 코드를 입력하세요
SELECT P.PRODUCT_CODE,P.PRICE*sum(OS.SALES_AMOUNT) as SALES
from PRODUCT as P
inner join OFFLINE_SALE as OS
where P.PRODUCT_ID=OS.PRODUCT_ID
GROUP by P.PRODUCT_CODE
order by SALES DESC, P.PRODUCT_CODE ASC;

