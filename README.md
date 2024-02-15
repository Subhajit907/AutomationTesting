# AutomationTesting

Part 1:Data Verification
Platform Access:
e Login page: https://app. trvloop. ai/login/password @ Email: ga-engineer-assignment@test.com e Password: Qapasswordi23$
Action Steps:
e Access the URL: https://app. tryloop. ai/chargebacks/stores/view or navigate
using sidebar 3P Chargebacks -> History By Store
e Focus on the dropdown section dedicated to reversals. Your objective is to validate
the accuracy of the total values (grand total) displayed at the bottom of the table. These totals should represent the sum of the values for each location of each respective month.
e Implement end-to-end automated test cases using either of the testing
frameworks of your choice.
e For example:
In the above image, there are 9 locations (denoted by “Store name” column) available, with some data for 7 months. For each month, the value shown at the bottom row (labeled “Grand Total”) should be the sum of the values of the locations for each corresponding month. For the month of Feb 2024, the sum of the values of the 9 locations is $49.00, which is correct:
[$6.50+$0.00+$0.00 +$4.14+$5.45+$0.00+$0.00 +$32.91]= $49.00
Repeat this process for all 7 columns, and print the result (whether summed value is matching Grand Total or not) onto the terminal, or a file. Take a screenshot of the same and add it to the GitHub repository.


Part 2: Data Extraction and Validation
Login:
• Use the same login credentials provided in Part 1.
Action Steps:
Navigate to https://app.tryloop.ai/chargebacks/transactions or navigate using sidebar 3P Chargebacks -> Transactions
· From the topbar, apply filters: Select "Artisan Alchemy" and "Blissful Buffet" from the locations filter, and "Grubhub" from the marketplace filter.
· Extract data from the table located at the bottom of the page and generate a flat CSV file. Ensure that each transaction type (e.g., Delivery, Adjustment) is
·
represented in its own row in the CSV.
The CSV file should be organized by order_id.
Bonus Task: Use the download button located at the top of the table to download the CSV file. Cross-verify each row in the downloaded file against your generated CSV for accuracy.
Testing Framework
-
Feel free to use any of your favorite testing frameworks to automate these tasks.
A few suggestions are Cypress/Playwright/Selenium for web testing.

