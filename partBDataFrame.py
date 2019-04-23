import pyspark
import csv

def main():

    sc = pyspark.SparkContext()

    sqlContext = pyspark.sql.SQLContext(sc)

    vout = sqlContext.read.load("/data/bitcoin/vout.csv", format='com.databricks.spark.csv', inferSchema=True, header=False)
    
    vout_column = vout.selectExpr('C0 as hash', 'C1 as value', 'C2 as n', 'C3 as publicKey')

    # Filter out transactions send to wikiLeaks public address
    vout_filter = vout_column.filter(vout_column.publicKey == '{1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v}')

    vin = sqlContext.read.load("/data/bitcoin/vin.csv", format='com.databricks.spark.csv', inferSchema=True, header=False)

    vin_column = vin.selectExpr('C0 as txid', 'C1 as tx_hash', 'C2 as vout')

    # Join matching with vout transaction to retrieve donors publicKeys and bitcoins sent
    first_join = vout_filter.join(vin_column, vin_column.txid == vout_filter.hash, 'inner').select('txid', 'tx_hash', 'vout')
    #first_join.rdd.saveAsTextFile("firstJoin")

    #Conditions for join
    cond = [vout_column.hash == first_join.tx_hash, vout_column.n == first_join.vout]
    
    # Join matching with vout transaction to retrieve donors publicKeys and bitcoins sent
    second_join = first_join.join(vout_column, cond, 'inner').select('publicKey', 'value').orderBy('value', ascending=False)

    second_joins = second_join.select('publicKey',second_join.value.cast("float").alias('values'))
   
    top10Wallet = second_joins.groupBy('publicKey').sum('values').orderBy('sum(values)', ascending=False).limit(10)

    top10Wallet.rdd.saveAsTextFile("out")


if __name__ == "__main__":
    main()