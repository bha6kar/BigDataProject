# BigDataProject
>Obtain the top 10 donors over the whole dataset bitcoin in 2009 to December 2014  for the Wikileaks bitcoin address: **{1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v}**. Found the information on who these wallets belong to. Found out how much was being donated if converted into pounds.

To achieve this task I used dataframes of pyspark. First we need to filter the data from whole vout files which are based on wikileaks bitcoin address: **{1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v}**.

  


List of Top 10 Donors: For the confirmation of wallet the check has been done in https://www.blockchain.com with the transactions that this wallet is donating actually to wikileak or not and how much they have donated :

Rank | Wallet Address | Amount Donated (BitCoin) | Amount Donated GBP |
| ------| ------ | ------ | ------ |
| 1 | {17B6mtZr14VnCKaHkvzqpkuxMYKTvezDcp} | 46515.1894803 | 146441445.2813545 |
| 2 | {19TCgtx62HQmaaGy8WNhLvoLXLr7LvaDYn} | 5770.0 | 18165402.5 |
| 3 | {14dQGpcUhejZ6QhAQ9UGVh7an78xoDnfap} | 1931.482 | 6080788.2065 |
| **4** | **{1LNWw6yCxkUmkhArb2Nf2MPw6vG7u5WG7q}** | **1894.37418624** | **5963963.53183008** |
| 5 | {1L8MdMLrgkCQJ1htiGRAcP11eJs662pYSS} | 806.13402728 | 2537911.4513842603 |
|6 | {1ECHwzKtRebkymjSnRKLqhQPkHCdDn6NeK} | 648.5199788 | 2041703.0232571 |
|7 | {18pcznb96bbVE1mR7Di3hK7oWKsA1fDqhJ} | 637.04365574 | 2004986.609020174 |
| 8 | {19eXS2pE5f1yBggdwhPjauqCjS8YQCmnXa} | 576.835 | 1815490.10055 |
| 9 | {1B9q5KG69tzjhqq3WSz3H7PAxDVTAwNdbV} | 556.7 | 1752118.611 |
| 10 | {1AUGSxE5e8yPPLGd7BM2aUxfzbokT6ZYSq} | 500.0 | 1573665 |

I found 1 wallet owner that belongs to Mt. Gox
that’s address:{1LNWw6yCxkUmkhArb2Nf2MPw6vG7u5WG7q} highlighted in the table. Using https://www.blockchain.com/btc/address/1LNWw6yCxkUmkhArb2Nf2MPw6vG7u5WG7q

This wallet has donated to wikileaks till 2014 is 1894.37418624 BitCoins.
Rest wallet users are anonymous.

