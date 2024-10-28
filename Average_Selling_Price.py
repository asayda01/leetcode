# --1251. Average Selling Price
# --SQL Schema
# --
# --Table: Prices
# --
# --+---------------+---------+
# --| Column Name   | Type    |
# --+---------------+---------+
# --| product_id    | int     |
# --| start_date    | date    |
# --| end_date      | date    |
# --| price         | int     |
# --+---------------+---------+
# --(product_id, start_date, end_date) is the primary key (combination of columns with unique values) for this table.
# --Each row of this table indicates the price of the product_id in the period from start_date to end_date.
# --For each product_id there will be no two overlapping periods. That means there will be no two intersecting periods for the same product_id.
# --
# --
# --
# --Table: UnitsSold
# --
# --+---------------+---------+
# --| Column Name   | Type    |
# --+---------------+---------+
# --| product_id    | int     |
# --| purchase_date | date    |
# --| units         | int     |
# --+---------------+---------+
# --This table may contain duplicate rows.
# --Each row of this table indicates the date, units, and product_id of each product sold.
# --
# --
# --
# --Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places. If a product does not have any sold units, its average selling price is assumed to be 0.
# --
# --Return the result table in any order.
# --
# --The result format is in the following example.
# --
# --
# --
# --Example 1:
# --
# --Input:
# --Prices table:
# --+------------+------------+------------+--------+
# --| product_id | start_date | end_date   | price  |
# --+------------+------------+------------+--------+
# --| 1          | 2019-02-17 | 2019-02-28 | 5      |
# --| 1          | 2019-03-01 | 2019-03-22 | 20     |
# --| 2          | 2019-02-01 | 2019-02-20 | 15     |
# --| 2          | 2019-02-21 | 2019-03-31 | 30     |
# --+------------+------------+------------+--------+
# --UnitsSold table:
# --+------------+---------------+-------+
# --| product_id | purchase_date | units |
# --+------------+---------------+-------+
# --| 1          | 2019-02-25    | 100   |
# --| 1          | 2019-03-01    | 15    |
# --| 2          | 2019-02-10    | 200   |
# --| 2          | 2019-03-22    | 30    |
# --+------------+---------------+-------+
# --Output:
# --+------------+---------------+
# --| product_id | average_price |
# --+------------+---------------+
# --| 1          | 6.96          |
# --| 2          | 16.96         |
# --+------------+---------------+
# --Explanation:
# --Average selling price = Total Price of Product / Number of products sold.
# --Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
# --Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96
# --
#

import pandas as pd


def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:

    # Merge prices with units_sold based on the product_id and the purchase_date falling within the price period
    merged = (
        pd.merge(units_sold, prices, on='product_id')
        .query('start_date <= purchase_date <= end_date')
    )

    # Calculate total price and total units sold per product_id
    result = (
        merged.groupby('product_id')
        .apply(lambda x: (x['units'] * x['price']).sum() / x['units'].sum() if x['units'].sum() > 0 else 0)
        .reset_index(name='average_price')
    )

    # For products with no sales, ensure they appear in the result with average_price = 0
    all_product_ids = pd.DataFrame(prices['product_id'].unique(), columns=['product_id'])
    final_result = pd.merge(all_product_ids, result, on='product_id', how='left').fillna(0)

    # Round the 'average_price' column to 2 decimal places
    final_result['average_price'] = final_result['average_price'].round(2)

    return final_result
