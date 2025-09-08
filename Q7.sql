select product_name,year,price from Products join Sales on Product.products_id = Sales.sales_id; 
-- or
select product_name,year, price from Product p join Sales s on p.product_id=s.product_id ;
