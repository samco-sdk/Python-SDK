# StockNoteBridge - Python SDK for Stocknote API
Official Python SDK for accessing and integrating Stocknote API

This documentation covers details of the Python bridge / SDK provided by SAMCO, for accessing the [SAMCO Stocknote APIs](https://docs-tradeapi.samco.in).

The primary purpose of this Python Bridge is to help our customers quickly create python based client scripts using our SDK and integrate with StockNote APIs. Our Python Bridge provides a wrapper over the RESTful StockNote APIs where the HTTP calls have been converted to method calls with JSON responses. Websocket connections are handled automatically with the library.

Please refer the below documentation for details on installation, set up and API specific sample code/request-responses to create your own Python client code.

## Installation

This module is installed via pip:

```
pip install stocknotebridge
```
Once done, you can verify if package is appropriately installed using  below command.

```
pip list
```

### Prerequisites

Python 2.x or 3.x setup. You can verify the version installed using

```
python --version
```

You can verify the Pip version installed using
```
pip --version
```
Also, you need the following modules:

* `future`
* `requests`
* `websocket`
* `websocket_client`

These modules can also be installed using `pip`

## Getting started with API

### Overview
Stocknote python SDK is a python client library for easily accessing the stocknote API. It exposes the individual APIs as python method calls and provides an easy-to-use interface for implementing your strategies in Python language. 

For specific details on parameters passed on the request, and details about API response, please refer our [Stocknote API documentation](https://docs-tradeapi.samco.in).

## List of API
* [Login](#login)
* [SearchEquityDerivative](#searchequityderivative)
* [SpanMargin](#spanmargin)
* [Quote](#quote)
* [IndexQuote](#indexquote)
* [MultiQuote](#multiquote)
* [OptionChain](#optionchain)
* [FutureChain](#futurechain)
* [UserLimits](#userlimits)
* [PlaceOrder](#placeorder)
* [PlaceOrderBO](#placeorderbo)
* [PlaceOrderCO](#placeorderco)
* [ModifyOrder](#modifyorder)
* [OrderBook](#orderbook)
* [TriggerOrders](#triggerorders)
* [OrderStatus](#orderstatus)
* [AddGtt](#addgtt)
* [ModifyGtt](#modifygtt)
* [DeleteGtt](#deletegtt)
* [AddOco](#addoco)
* [ModifyOco](#modifyoco)
* [DeleteOco](#deleteoco)
* [ListGttOco](#listgttoco)
* [TradeBook](#tradebook)
* [Positons](#positions)
* [PositionConversion](#positionconversion)
* [PositionSquareOff](#positionsquareoff)
* [Holdings](#holdings)
* [IntraDayCandleData](#intradaycandledata)
* [IndexIntraDayCandleData](#indexintradaycandledata)
* [HistoricalCandleData](#historicalcandledata)
* [IndexHistoricalCandleData](#indexhistoricalcandledata)
* [StreamingData](#streamingdata)
* [Logout](#logout)


## Using the API

As a first step to access StockNote APIs, you need to import our SDK in your client code and then login to get valid session token.

### Import the Python SDK and get a session token
1. Import StocknoteAPIPythonBridge
```
from snapi_py_client.snapi_bridge import StocknoteAPIPythonBridge
```

2. Create a StocknoteAPIPythonBridge object
```python
samco=StocknoteAPIPythonBridge()
```
3. Login to access Stocknote API by providing below parameters.

<a name="login"/>

## Login

## Parameters:
```
userId,password,yob
```
## Login Sample Request:

    login=samco.login(body={"userId":'*****','password':'*****','yob':'****'})
    print("Login details",login)
    ##this will return a user details and generated session token
 
 ## Login Response:
 ```python
 {
  "serverTime": "16/06/20 12:36:52",
  "msgId": "580d405d-663e-49e4-9a5d-26d439bc8390",
  "status": "Success",
  "statusMessage": "Login session token generated successfully ",
  "sessionToken": "cbcc85c02d057187a4c6512ae0978946",
  "accountID": "client_id",
  "accountName": "client_name",
  "exchangeList": [
    "BSE",
    "NSE"
  ],
  "orderTypeList": [
    "L",
    "MKT",
    "SL"
  ],
  "productList": [
    "CNC",
    "CO",
    "MIS"
  ]
}
```
4. Get the session token form login response and set it to `set_session_token()` function.
```python
samco.set_session_token(sessionToken="cbcc85c02d057187a4c6512ae0978946")
## this function will help to reduce to pass session token for other apis. This will automate the session token for other apis
```

<a name="searchequityderivative"/>

## SearchEquityDerivative:

The search function `search_equity_derivative()` should be used to search equity, derivatives and commodity scrips based on user provided search symbol and exchange name. 

#### Parameters:
```python
search_symbol_name,exchange
```
#### Sample Search Request:

```python
  samco.search_equity_derivative(search_symbol_name="BANKNIFTY20JUN",exchange=samco.EXCHANGE_NFO)
```
#### Sample Search Response:
```python
{
 "msgId": "a9080992-71f3-47a9-9b53-b6103f4eb6ba",
  "status": "Success",
  "statusMessage": "Equity Search details retrieved successfully",
  "equityDertivativeValues": [
       {
            "tradingSymbol": "BANKNIFTY20JUN21000CE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN22000CE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN20500CE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN20000CE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN19000PE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN20000PE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN21500CE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        },
        {
            "tradingSymbol": "BANKNIFTY20JUN19500PE",
            "instrument": "OPTIDX",
            "exchange": "NFO"
        }
    ]
}
```


<a name="spanmargin"/>

## SpanMargin

`span_margin()`

#### Parameters:
```python
exchange ,tradingSymbol,qty
```
#### Sample Quote request:

samco.span_margin(body={
    "request":[
        {
            "exchange":"NFO",
            "tradingSymbol":"NIFTY06JUN2423200PE",
            "qty":"25"
        },
         {
            "exchange":"NFO",
            "tradingSymbol":"NIFTY24JUNFUT",
            "qty":"25"
        }
    ]
})

#### Sample Quote Response:
```python
{
  "serverTime": "03/06/24 16:39:25",
  "msgId": "26bef46f-a82e-485d-8dc7-f0d591895d19",
  "status": "Success",
  "statusMessage": "Span margin calculated",
  "spanDetails": {
    "totalRequirement": "14309.11",
    "spanRequirement": "2584.11",
    "exposureMargin": "11725.00",
    "spreadBenefit": "00.00"
  }
}

```





<a name="quote"/>

## Quote

Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.
The Quote function name in python is `get_quote()`

#### Parameters:
```python
`symbol_name`,exchange
```
#### Sample Quote request:

  samco.get_quote(symbol_name='BANKNIFTY18JUN2017900PE',exchange=samco.EXCHANGE_NFO)

#### Sample Quote Response:
```python
{
    "serverTime": "16/06/20 14:06:12",
    "msgId": "b6322a42-1e3f-4706-af6d-6e88c32a5ee5",
    "status": "Success",
    "statusMessage": "Quote details retrieved successfully",
    "tradingSymbol": "BANKNIFTY18JUN2017900PE",
    "exchange": "NFO",
    "lastTradedTime": "16/06/2020 14:08:05",
    "lastTradedPrice": "54.25",
    "changeValue": "19.45",
    "changePercentage": "55.89",
    "lastTradedQuantity": "40",
    "lowerCircuitLimit": "0.05",
    "upperCircuitLimit": "138.95",
    "averagePrice": "37.63",
    "totalBuyQuantity": "85520",
    "totalSellQuantity": "17100",
    "totalTradedValue": "1.57858 (Crs)",
    "totalTradedVolume": "419500",
    "yearlyHighPrice": "0.00",
    "yearlyLowPrice": "0.00",
    "tickSize": "0.05",
    "openInterest": "16880",
    "bestBids": [
        {
            "number": "1",
            "quantity": "20",
            "price": "54.00"
        },
        {
            "number": "2",
            "quantity": "40",
            "price": "53.95"
        },
        {
            "number": "3",
            "quantity": "40",
            "price": "53.85"
        },
        {
            "number": "4",
            "quantity": "40",
            "price": "53.75"
        },
        {
            "number": "5",
            "quantity": "120",
            "price": "53.70"
        }
    ],
    "bestAsks": [
        {
            "number": "1",
            "quantity": "20",
            "price": "54.55"
        },
        {
            "number": "2",
            "quantity": "80",
            "price": "54.60"
        },
        {
            "number": "3",
            "quantity": "40",
            "price": "54.65"
        },
        {
            "number": "4",
            "quantity": "40",
            "price": "54.70"
        },
        {
            "number": "5",
            "quantity": "480",
            "price": "54.75"
        }
    ],
    "expiryDate": "18 Jun 20",
    "spotPrice": "19959.35",
    "instrument": "OPTIDX",
    "lotQuantity": "20",
    "listingId": "41870_NFO",
    "openInterestChange": "8800",
    "oIChangePer": "58.05"
}
```

<a name="multiquote"/>

## MultiQuote

Get market depth details for multiple equity scrips including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits, etc. This helps users with a comprehensive market picture of multiple equity scrips, enabling them to make informed trading decisions. The Multi Quote function name in Python is `get_multi_quote()`. We will send the values of all parameters in an array.

#### Parameters:
```text
NFO,BFO,NSE,BSE,MCX,CDS,MFO,INDEX
```
#### Sample Multi Quote request:

```python
samco.multi_quote(body = {
    "INDEX":["NIFTY 50","NIFTY BANK"],
    "NFO": ["FINNIFTY2451416500CE"]
})
```
#### Sample Multi Quote Response:
```json
{
  "serverTime": "29/05/24 15:26:24",
  "msgId": "f70d9c1d-dda1-4742-bc62-26f15995583b",
  "status": "Success",
  "statusMessage": "Multiquotes data retrieved successfully",
  "invalidSymbol": [
    "FINNIFTY2451416500CE"
  ],
  "multiQuotes": [
    {
      "exchange": "NSE",
      "symbolName": "Nifty 50",
      "tradingSymbol": "Nifty 50",
      "companyName": "Nifty 50",
      "lotSize": "-",
      "averagePrice": "22348.05",
      "totalTradeVolume": "0",
      "symbol": "-21",
      "lastTradeTime": "03 May 2024, 03:32:16 PM",
      "lastTradeQuantity": "0",
      "lastTradePrice": "22475.85",
      "change": "-172.35",
      "changePercent": "-0.76",
      "open": "22766.35",
      "close": "22475.85",
      "previousClose": "22648.20",
      "low": "22348.05",
      "high": "22794.70",
      "tickSize": "-",
      "bidSize": "0",
      "bidPrice": "0.00",
      "totalTradedValue": "0.00",
      "askSize": "0",
      "askPrice": "0.00"
    },
    {
      "exchange": "NSE",
      "symbolName": "Nifty Bank",
      "tradingSymbol": "Nifty Bank",
      "companyName": "Nifty Bank",
      "lotSize": "-",
      "averagePrice": "48659.70",
      "totalTradeVolume": "0",
      "symbol": "-22",
      "lastTradeTime": "03 May 2024, 03:32:16 PM",
      "lastTradeQuantity": "0",
      "lastTradePrice": "48923.55",
      "change": "-307.50",
      "changePercent": "-0.62",
      "open": "49375.05",
      "close": "48923.55",
      "previousClose": "49231.05",
      "low": "48659.70",
      "high": "49607.75",
      "tickSize": "-",
      "bidSize": "0",
      "bidPrice": "0.00",
      "totalTradedValue": "0.00",
      "askSize": "0",
      "askPrice": "0.00",
      "iv": "0.00"
    }
  ]
}

```


<a name="indexquote"/>

## IndexQuote

Get detailed market information for a specific index including values such as index name, listing ID, last traded time, spot price, change percentage, average price, open value, high value, low value, close value, total buy quantity, total sell quantity, total traded value, total traded volume, and change. This comprehensive data provides users with an in-depth market picture of an index, enabling them to make informed trading decisions.
The Index Quote function name in Python is `index_quote()`.

#### Parameters:
```python
indexName
```
#### Sample Quote request:

```python
  samco.index_quote('NIFTY NEXT 50')
```

#### Sample Quote Response:
```json
{
  "serverTime": "29/05/24 15:31:59",
  "msgId": "d8c2b0fb-e18f-457c-9a60-7e70a63a3636",
  "status": "Success",
  "statusMessage": "Index Quote details retrieved successfully",
  "indexDetails": [
    {
      "indexName": "Nifty Next 50",
      "listingId": "-23",
      "lastTradedTime": "2024-05-29 15:31:55.0",
      "spotPrice": 68070.5,
      "changePercentage": -0.69,
      "averagePrice": 0,
      "openValue": 68191,
      "highValue": 68535.45,
      "lowValue": 67899.85,
      "closeValue": 68070.5,
      "totalBuyQuantity": 0,
      "totalSellQuantity": 0,
      "totalTradedValue": 0,
      "totalTradedVolume": 0,
      "change": -475.1
    }
  ]
}
```

<a name="futurechain"/>

## FutureChain:

The `get_future_chain()` function can be used to search for future contracts for equity, derivatives, and commodity scrips based on user-provided search symbols and exchange names. This function returns detailed information about the futures contract including trading symbols, exchange, expiry date, and market data such as spot price, last traded price, open interest, and bid/ask details.

#### Parameters:
```python
  search_symbol_name,exchange,expiry_date,strike_price,option_type
```
#### Sample OptionChain Request:

```python
  samco.get_option_chain(search_symbol_name='Reliance',exchange=samco.EXCHANGE_NFO,expiry_date='2020-07-30',strike_price='1961.40',option_type='PE')
```
#### Sample OptionChain Response:
```python
{
  "serverTime": "29/05/24 16:04:46",
  "msgId": "d8523da7-77c2-4ffa-9dd8-69ce69d09dc6",
  "status": "Success",
  "statusMessage": "Future chain details retrived successfully. ",
  "futureChainDetails": [
    {
      "tradingSymbol": "SENSEX24MAYFUT",
      "exchange": "BFO",
      "symbol": "859479_BFO",
      "expiryDate": "2024-05-31",
      "instrument": "IF",
      "underLyingSymbol": "SENSEX",
      "spotPrice": 74502.9,
      "lastTradedPrice": "74667.05",
      "openInterest": 3130,
      "openInterestInLot": 313,
      "openInterestChange": 3130,
      "openInterestChangeInLot": 313,
      "oichangePer": "Infinity",
      "volume": 8620,
      "bestBids": [
        {
          "number": 1,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 2,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 3,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 4,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 5,
          "quantity": "0",
          "price": "0.0000"
        }
      ],
      "bestAsks": [
        {
          "number": 1,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 2,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 3,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 4,
          "quantity": "0",
          "price": "0.0000"
        },
        {
          "number": 5,
          "quantity": "0",
          "price": "0.0000"
        }
      ]
    }
  ]
}
```

<a name="optionchain"/>

## OptionChain:

The OptionChain function `get_option_chain()` can be used to search OptionChain for equity, derivatives and commodity scrips based on user provided search symbol and exchange name.

#### Parameters:
```python
search_symbol_name,exchange,expiry_date,strike_price,option_type
```
#### Sample OptionChain Request:

    samco.get_option_chain(search_symbol_name='Reliance',exchange=samco.EXCHANGE_NFO,expiry_date='2020-07-30',strike_price='1961.40',option_type='PE')

#### Sample OptionChain Response:
```python
{
  "serverTime": "16/06/20 14:48:53",
  "msgId": "9922deb8-dcdb-402f-a282-9f8df0b2fdee",
  "status": "Success",
  "statusMessage": "OptionChain details retrived successfully. ",
  "optionChainDetails": [
    {
      "tradingSymbol": "RELIANCE20JUL1961.4PE",
      "exchange": "NFO",
      "symbol": "38914_NFO",
      "strikePrice": "1961.40",
      "expiryDate": "2020-07-30",
      "instrument": "OPTSTK",
      "optionType": "PE",
      "underLyingSymbol": "RELIANCE",
      "spotPrice": "1613.45",
      "lastTradedPrice": "0.00",
      "openInterest": "0",
      "openInterestChange": "0",
      "oichangePer": "0",
      "volume": "0"
    }
  ]
}
```



<a name="userlimits"/>

## UserLimits

The UserLimits function `get_limits()` can be used  to gets the user cash balances, available margin for trading in equity and commodity segments.

#### Sample UserLimit Request:

  samco.get_limits()

#### Sample UserLimit Response:
```python
{
  "serverTime": "18/06/20 12:27:44",
  "msgId": "095bd777-34f3-40b8-81fd-6bf25d3f3c3c",
  "status": "Success",
  "statusMessage": "User Limit details retrieved successfully",
  "equityLimit": {
    "grossAvailableMargin": "50000000000",
    "payInToday": "0",
    "notionalCash": "0",
    "marginUsed": "0",
    "netAvailableMargin": "50000000000"
  },
  "commodityLimit": {
    "grossAvailableMargin": "0",
    "payInToday": "0",
    "notionalCash": "0",
    "marginUsed": "0",
    "netAvailableMargin": "0"
  }
}
```
<a name="placeorder"/>

## PlaceOrder

The PlaceOrder function `place_order()` can be used to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. When an order is successfully placed the PlaceOrder API returns an OrderNumber in response, and the actual order status can be checked separately using the OrderStatus API call .This is for Placing CNC, MIS and NRML Orders.


#### Parameters:
```python
symbol_name,exchange,transactionType,orderType,price,quantity,disclosedQuantity,orderValidity,productType,marketProtection
```

#### Sample PlaceOrder Request:

    samco.place_order(body={
    "symbolName":"RELIANCE",
    "exchange":samco.EXCHANGE_NSE,
    "transactionType":samco.TRANSACTION_TYPE_BUY,
    "orderType":samco.ORDER_TYPE_LIMIT,
    "price":"1282",
    "quantity": "15",
    "disclosedQuantity":"",
    "orderValidity":samco.VALIDITY_DAY,
    "productType":samco.PRODUCT_MIS,
    "afterMarketOrderFlag":"NO"
    })

#### sample PlaceOrder Response:
```python
{
  "serverTime": "16/06/20 18:03:48",
  "msgId": "0b9e75c7-c624-4c77-bfbf-6d4e53536948",
  "orderNumber": "200616000000350",
  "status": "Success",
  "statusMessage": "MIS Order request placed successfully",
  "exchangeOrderStatus": "PENDING",
  "orderDetails": {
    "pendingQuantity": "15",
    "avgExecutionPrice": "0.00",
    "orderPlacedBy": "--",
    "tradingSymbol": "RELIANCE-EQ",
    "triggerPrice": "0.00",
    "exchange": "NSE",
    "totalQuantity": "15",
    "transactionType": "BUY",
    "productType": "MIS",
    "orderType": "L",
    "quantity": "15",
    "filledQuantity": "0",
    "orderPrice": "1282.0",
    "filledPrice": "0.00",
    "exchangeOrderNo": "1100000000015551",
    "orderValidity": "DAY",
    "orderTime": "16/06/2020 18:03:47"
  }
}
```
<a name="placeorderbo"/>

## PlaceOrderBO

The PlaceOrderBO function `place_order_bo()` can be used to place an equity/derivative bracket orders to the exchange i.e the place order BO request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. So when an order is successfully placed the placeOrderBO returns an orderNumber in response, and the actual order status can be checked separately using the orderStatus API call. 

#### Parameters:
```python
symbol_name,exchange,transactionType,orderType,price,quantity,disclosedQuantity,orderValidity,productType,trailingStopLoss,stopLossValue,squareOffValue,valueType,priceType,
```
#### Sample PlaceOrderBO Request:

  samco.place_order_bo(body={
    "symbolName":"TCS",
    "exchange":"BSE",
    "transactionType":samco.TRANSACTION_TYPE_BUY,
    "orderType":samco.ORDER_TYPE_LIMIT,
    "quantity": "10",
    "disclosedQuantity":"1",
    "price":"2021",
    "priceType":"LTP",
    "valueType":"Absolute",
    "orderValidity":samco.VALIDITY_DAY,
    "productType":samco.PRODUCT_BO,
    "squareOffValue":"15.00",
    "stopLossValue":"5.00",
    "trailingStopLoss":"5"
  })

#### Sample PlaceOrderBO Response:
```python
{
  "serverTime": "17/06/20 18:29:39",
  "msgId": "3dde806a-17b3-43ae-b1c1-58691f640a10",
  "orderNumber": "200617000000375",
  "status": "Success",
  "statusMessage": "Bracket Order request placed successfully",
  "exchangeOrderStatus": "EXECUTED",
  "orderDetails": {
    "pendingQuantity": "0",
    "avgExecutionPrice": "2014.95",
    "orderPlacedBy": "--",
    "tradingSymbol": "TCS",
    "triggerPrice": "0.00",
    "exchange": "BSE",
    "totalQuantity": "10",
    "transactionType": "BUY",
    "productType": "BO",
    "orderType": "L",
    "quantity": "10",
    "filledQuantity": "10",
    "orderPrice": "2021.0",
    "filledPrice": "2014.95",
    "exchangeOrderNo": "1592387449638000140",
    "orderValidity": "DAY",
    "orderTime": "17/06/2020 18:29:38"
  }
}
```
<a name="placeorderco"/>

## PlaceOrderCO

The PlaceOrderCO function `place_order_co()` can be used to place an equity/derivative CO order to the exchange i.e the place order CO request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. So when an order is successfully placed the placeOrderCO returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. 

#### Parameters:
```python
symbol_name,exchange,transactionType,orderType,price,quantity,disclosedQuantity,orderValidity,productType,marketProtection,triggerPrice
```
#### Sample PlaceOrderCO Request:

  samco.place_order_co(body={
    "symbolName":"INFY",
    "exchange":samco.EXCHANGE_NSE,
    "transactionType":samco.TRANSACTION_TYPE_BUY,
    "orderType":samco.ORDER_TYPE_LIMIT,
    "price":"679",
    "quantity": "15",
    "disclosedQuantity":"",
    "orderValidity":samco.VALIDITY_DAY,
    "productType":samco.PRODUCT_CO,
    "afterMarketOrderFlag":"NO",
    "triggerPrice":"646"
  })

#### Sample PlaceOrderCO Response:
```Python
{
  "serverTime": "17/06/20 16:37:18",
  "msgId": "9bd0ab52-f6a0-4ec6-9813-aa707795aa87",
  "orderNumber": "200617000000181",
  "status": "Success",
  "statusMessage": "CO Order request placed successfully",
  "exchangeOrderStatus": "EXECUTED",
  "orderDetails": {
    "pendingQuantity": "0",
    "avgExecutionPrice": "679.00",
    "orderPlacedBy": "--",
    "tradingSymbol": "INFY-EQ",
    "triggerPrice": "646.00",
    "exchange": "NSE",
    "totalQuantity": "15",
    "transactionType": "BUY",
    "productType": "CO",
    "orderType": "L",
    "quantity": "15",
    "filledQuantity": "15",
    "orderPrice": "679.0",
    "filledPrice": "679.00",
    "exchangeOrderNo": "1100000000026975",
    "orderValidity": "DAY",
    "orderTime": "17/06/2020 16:37:17"
  }
}
```
<a name="modifyorder"/>

## ModifyOrder

The ModifyOrder function `modify_order()` can be used to modify some attributes of an order as long as it is with open/pending status in system. For modification order identifier is mandatory. With order identifier you need to send the optional parameter(s) which needs to be modified. In case the optional parameters aren't sent, the default will be considered from the original order. Modifiable attributes include quantity, Order Type (L,MKT, SL,SL-M). This API cannot be used for modifying attributes of an executed/rejected/cancelled order. Only the attribute that needs to be modified should be sent in the request alongwith the Order Identifier.

#### Parameters:
```python
orderType,quantity,disclosedQuantity,orderValidity,price,triggerPrice,parentOrderId,marketProtection
```

#### Sample ModifyOrder Request:

  samco.modify_order(order_number='200616000000350',body={"quantity": "50"})

#### Sample ModifyOrder Response:
```python
{
  "serverTime": "16/06/20 18:12:42",
  "msgId": "c681bb4b-37c1-4e50-b3f6-60f3c43b9bef",
  "orderNumber": "200616000000350",
  "status": "Success",
  "statusMessage": "Order 200616000000350 modified successfully",
  "exchangeOrderStatus": "PENDING",
  "orderDetails": {
    "pendingQuantity": "50",
    "avgExecutionPrice": "0.00",
    "orderPlacedBy": "Dv999",
    "tradingSymbol": "RELIANCE-EQ",
    "triggerPrice": "0.00",
    "exchange": "NSE",
    "totalQuantity": "50",
    "transactionType": "BUY",
    "productType": "MIS",
    "orderType": "L",
    "quantity": "50",
    "filledQuantity": "0",
    "orderPrice": "1282.0",
    "filledPrice": "0.00",
    "exchangeOrderNo": "1100000000015551",
    "orderValidity": "DAY",
    "orderTime": "16/06/2020 18:12:41"
  }
}
```
<a name="orderbook"/>

## OrderBook

The OrderBook function `get_order_book()` retrieves and displays details of all orders placed by the user on a specific day. This API returns all states of the orders, namely, open, pending, rejected and executed ones.

#### Sample OrderBook Request:

  samco.get_order_book()

#### Sample OrderBook Response:
```Python
{
  "serverTime": "16/06/20 18:25:18",
  "msgId": "2e2d2926-1a15-4510-b98e-c86d1f87cb7e",
  "status": "Success",
  "statusMessage": "Order Book details retrieved successfully",
  "orderBookDetails": [
    {
      "orderNumber": "200616000000350",
      "exchange": "NSE",
      "tradingSymbol": "RELIANCE",
      "transactionType": "BUY",
      "productCode": "MIS",
      "orderType": "L",
      "orderPrice": "1282.00",
      "triggerPrice": "0.00",
      "orderValidity": "DAY",
      "orderStatus": "Open",
      "orderValue": "0.0",
      "orderTime": "16-Jun-2020 18:03:47",
      "userId": "DS37591",
      "filledQuantity": "0",
      "fillPrice": "0.00",
      "averagePrice": "0.00",
      "rejectionReason": "--",
      "exchangeConfirmationTime": "16-Jun-2020 18:12:41",
      "coverOrderPercentage": "0.0",
      "orderRemarks": "--",
      "exchangeOrderNumber": "1100000000015551",
      "symbol": "2885_NSE",
      "displayStrikePrice": "00.00",
      "displayNetQuantity": "50",
      "status": "Open",
      "exchangeStatus": "open",
      "expiry": "NA",
      "pendingQuantity": "50",
      "totalQuanity": "50",
      "optionType": "XX",
      "orderPlaceBy": "Dv999"
    }
  ]
}
```
<a name="triggerorders"/>

## TriggerOrders

The TriggerOrders function `get_trigger_order_numbers()` is used to get the trigger order numbers in case of BO and CO orders so that their attribute values can be modified for BO orders. It will give the order identifiers for Stop loss leg and target leg. Similarly for CO orders, it will return order identifier of stop loss leg only. Using the order identifier, the user would be able to modify the order attributes using the modifyOrder API. Refer modifyOrder API documentation for the parameters details.

#### Parameters:
```python
order_number
```

#### Sample TriggerOrders Request:

  samco.get_trigger_order_numbers(order_number="200617000000378")

#### Sample TriggerOrders Response:
```python
{
    "serverTime": "17/06/20 18:40:00",
    "msgId": "ccff75e1-9d79-4b54-b4cb-bc48e080758f",
    "status": "Success",
    "statusMessage": "SubOrder details retrieved successfully.",
    "triggerOrders": [
        {
            "targetOrderNo": "200617000000380",
            "orderStatus": "Complete",
            "orderPrice": "2010.00",
            "triggerPrice": "0.00"         
        },
        {
            "targetOrderNo": "200617000000379",
            "orderStatus": "Cancelled",
            "orderPrice": "2029.95",
            "triggerPrice": "0.00"
        }
    ]
}
```
<a name="orderstatus"/>

## OrderStatus

The OrderStatus function `get_order_status` is used to get status of an order placed previously. This API returns all states of the orders,but not limited to open, pending, and partially filled ones.

#### Parameters:
```python
order_number
```
#### Sample OrderStatus Request:

  samco.get_order_status(order_number="200617000000378")

#### Sample OrderStatus Response:
```python
{
    "serverTime": "17/06/20 20:54:53",
    "msgId": "d45688d9-31c0-4195-90ba-5474e7f50873",
    "orderNumber": "200617000000378",
    "orderStatus": "EXECUTED",
    "orderDetails": {
        "pendingQuantity": "0",
        "avgExecutionPrice": "2014.95",
        "orderPlacedBy": "--",
        "tradingSymbol": "TCS",
        "triggerPrice": "0.00",
        "exchange": "BSE",
        "totalQuantity": "10",
        "transactionType": "BUY",
        "productType": "BO",
        "orderType": "L",
        "quantity": "10",
        "filledQuantity": "10",
        "orderPrice": "2021.0",
        "filledPrice": "2014.95",
        "exchangeOrderNo": "1592387449638000143",
        "orderValidity": "DAY",
        "orderTime": "17/06/2020 18:38:37"
    }
}
```
<a name="cancelorder"/>

## CancelOrder:

The CancleOrder function `cancel_order()` is used to cancel an order which is in open or pending status in system. In other words, cancellation cannot be initiated for already Executed, Rejected orders.This is for CNC, MIS and NRML Orders.

#### Parameters:
```python
order_number
```
#### Sample CancelOrder Request:

  samco.cancel_order(order_number='200616000000350')

#### sample CancelOrder Response:
```python
{
  "serverTime" : "16/06/20 14:50:36",
  "msgId" : "25d6d99b-3224-4a77-b129-a5d0bd38349b",
  "status" : "Success",
  "orderNumber" : "200616000000350",
  "statusMessage" : "Order cancelled successfully"
}
```
<a name="cancelorderco"/>

## CancelOrderCO

The CancleOrder function `cancel_order_co()` is used for Cancellation/exit of CO orders by passing main leg Order number. 

If main leg is in Open/Pending state that order will be cancelled.
If the main leg is executed and the sublegs are created and in open/Trigger pending state, the order will be exited.
If the main leg is executed and if Stop loss is hit, API will return error message "SubOrder is in Executed status. Cannot exit/cancel such orders.

#### Parameters:
```python
order_number
```
#### Sample CancelOrderCO Request:

  samco.cancel_order_co(order_number='200617000000181')

#### sample CancelOrderCO Response:
```python
{
  "serverTime" : "16/06/20 14:50:36",
  "msgId" : "25d6d99b-3224-4a77-b129-a5d0bd38349b",
  "status" : "Success",
  "orderNumber" : "200617000000181",
  "statusMessage" : "Cover Order 200617000000181 exited successfully"
}
```
<a name="cancelorderbo"/>

## CancelOrderBO

The CancleOrder function `cancel_order_bo()` is used for Cancellation/exit of BO orders pass main leg Order number. 
If main leg is in Open/Pending state that order will be cancelled.
If the main leg is executed and the sublegs are created and in open/Trigger pending state, the order will be exited.
If the main leg is executed and if either of Stop loss or target is hit, API will return error message "SubOrder is in Executed status. Cannot exit/cancel such orders.

#### Parameters:
```python
order_number
```
#### Sample CancelOrderBO Request:

    samco.cancel_order_bo(order_number='200617000000375')

#### sample CancelOrderBO Response:
```python
{
  "serverTime" : "16/06/20 14:50:36",
  "msgId" : "25d6d99b-3224-4a77-b129-a5d0bd38349b",
  "status" : "Success",
  "orderNumber" : "200617000000375",
  "statusMessage" : "Bracket Order exited successfully"
}
```



<a name="addgtt"/>

## AddGtt

The add_gtt() function in the Samco API is utilized to add a Good Till Trigger (GTT) order to the exchange. A GTT order allows traders to set specific conditions for the execution of their orders. When this function is called successfully, it registers the GTT order with the Order Management System (OMS). However, it's important to note that successful placement of a GTT order via the API does not guarantee its immediate execution.

To know more about GTT, [ click here](https://docs-tradeapi.samco.in/#add-gtt).

#### Parameters:

```python
exchange,symbolName,transactionType,quantity,productType,orderType,triggerPrice,limitPrice,marketProtection
```

#### Sample Add GTT Request:

```python

samco.add_gtt(body={
  "exchange": "NFO",
  "symbolName": "WIPRO24JUN585PE",
  "transactionType": "BUY",
  "quantity": "1500",
  "productType": "NRML",
  "orderType": "L",
  "triggerPrice": "1180",
  "limitPrice": "1160"
})
```
#### sample Add GTT Response:
```json
{
  "serverTime": "30/05/24 11:42:25",
  "msgId": "b74e09a8-4925-42cd-bca3-2a96872684e0",
  "status": "Success",
  "statusMessage": "GTT CREATED",
  "gttSummaryId": "140954",
  "orderDetails": {
    "productType": "NRML",
    "orderType": "L",
    "triggerPrice": "1180",
    "marketProtection": "",
    "transactionType": "BUY",
    "triggerId": "177902",
    "symbol": "146465_NFO",
    "symbolName": "WIPRO24JUN585PE",
    "createdAt": "2024-05-30 11:42:25"
  }
}
```

<a name="modifygtt"/>

## ModifyGtt

Function modify_gtt() modifies an existing GTT (Good Till Triggered) order, allowing adjustments to parameters such as trigger price, quantity, product type, limit price, market protection, and order type
#### Parameters:

```python
exchange,symbolName,transactionType,quantity,productType,orderType,triggerPrice,limitPrice,marketProtection,gttSummaryId
```

#### Sample Modify GTT Request:

```python

samco.modify_gtt(body={"symbolName": "WIPRO24JUN585PE", 
  "exchange": "NFO",
  "transactionType": "BUY", 
  "orderType": "MKT",
  "quantity": "500",
  "productType": "NRML",
  "triggerPrice": "124.7",
  "limitPrice": "126.7",
  "marketProtection": "12",
  "gttSummaryId":"945505"
})
```
#### sample Modify GTT Response:
```json
{
    "serverTime": "02/06/24 12:00:52",
    "msgId": "82452735-e3b8-4fc4-8346-0ef314b5a404",
    "status": "Success",
    "statusMessage": "GTT MODIFIED",
    "gttSummaryId": "945510",
    "orderDetails": {
        "productType": "NRML",
        "orderType": "MKT",
        "triggerPrice": "124.7",
        "marketProtection": "12",
        "transactionType": "BUY",
        "limitPrice": "",
        "symbol": "146465_NFO",
        "symbolName": "WIPRO24JUN585PE",
        "quantity": "500"
    }
}
```


<a name="deletegtt"/>

## DeleteGtt

Function delete_gtt() cancels a GTT (Good Till Triggered) order before execution, removing it from the exchange's order book and preventing future execution. Once GTT is triggered, deletion is not possible.

#### Parameters:

```python
gttSummaryId
```

#### Sample Delete GTT Request:

```python

samco.delete_gtt(body={
    "gttSummaryId" : 945510
})
```
#### sample Delete GTT Response:
```json
{
    "serverTime": "02/06/24 12:06:38",
    "msgId": "20705726-9f80-4698-8bad-e327f1d087b1",
    "status": "Success",
    "statusMessage": "GTT Deleted successfully",
    "gttSummaryId": "945510",
    "orderDetails": {
        "userId": "RX372XX"
    }
}
```

<a name="addoco"/>

## AddOco
Function add_oco() adds an OCO (One-Cancels-the-Other) condition to a GTT (Good Till Triggered) order, allowing investors to set up two separate exit conditions for a single position. If one condition is triggered and its order is executed, the other order is automatically canceled.

#### Parameters:

```python
exchange,symbolName,transactionType,quantity,productType,orderType,targetTriggerPrice,targetLimitPrice,stoplossTriggerPrice,stoplossLimitPrice,marketProtection
```

#### Sample Add OCO Request:

```python

samco.add_oco(body={
    "exchange": "NFO", 
    "symbolName": "WIPRO24JUN440PE", 
    "transactionType": "SELL", 
    "quantity": "1500", 
    "productType": "NRML",
    "orderType": "L", 
    "targetTriggerPrice": "14.5",
    "targetLimitPrice": "17",
    "stoplossTriggerPrice": "14",
    "stoplossLimitPrice": "14"
})
```
#### sample Add OCO Response:
```json
{
    "serverTime": "02/06/24 12:18:19",
    "msgId": "023a6faf-b121-4066-bcac-6c7d67c6b34c",
    "status": "Success",
    "statusMessage": "GTT CREATED",
    "gttSummaryId": "945525",
    "orderDetails": {
        "transactionType": "SELL",
        "symbol": "133148_NFO",
        "symbolName": "WIPRO24JUN440PE",
        "productType": "NRML",
        "orderType": "L",
        "target": {
            "quantity": "1500",
            "triggerPrice": "14.5",
            "limitPrice": "17",
            "marketProtection": "",
            "type": "TARGET",
            "triggerId": "1345970"
        },
        "stopLoss": {
            "quantity": "1500",
            "triggerPrice": "14",
            "limitPrice": "14",
            "marketProtection": "",
            "type": "STOPLOSS",
            "triggerId": "1345975"
        }
    }
}
```






<a name="modifyoco"/>

## ModifyOco

Function modify_oco() modifies an existing GTT (Good Till Triggered) order, allowing adjustments to parameters such as trigger price, quantity, product type, limit price, market protection, and order type
#### Parameters:

```python
exchange,symbolName,transactionType,quantity,productType,orderType,targetTriggerPrice,targetLimitPrice,stoplossTriggerPrice,stoplossLimitPrice,marketProtection,gttSummaryId
```

#### Sample Modify OCO Request:

```python

samco.modify_oco(body={
    "exchange": "NFO",
    "symbolName": "WIPRO24JUN440PE",
    "transactionType": "SELL",
    "quantity": "3000",
    "productType": "NRML",
    "orderType": "L",
   "targetTriggerPrice": "15",
    "targetLimitPrice": "20",
   "stoplossTriggerPrice": "13",
   "stoplossLimitPrice": "13",
    "gttSummaryId": "945525"
})
```
#### sample Modify OCO Response:
```json
{
    "serverTime": "02/06/24 12:22:11",
    "msgId": "588cb679-18a5-4a91-9f10-1a16665c6c28",
    "status": "Success",
    "statusMessage": "GTT MODIFIED",
    "gttSummaryId": "945530",
    "orderDetails": {
        "transactionType": "SELL",
        "orderType": "L",
        "symbol": "133148_NFO",
        "symbolName": "WIPRO24JUN440PE",
        "productType": "NRML",
        "target": {
            "limitPrice": "20",
            "triggerId": "1345980",
            "triggerPrice": "15",
            "type": "TARGET",
            "quantity": "3000",
            "marketProtection": ""
        },
        "stopLoss": {
            "limitPrice": "13",
            "triggerId": "1345985",
            "triggerPrice": "13",
            "type": "STOPLOSS",
            "quantity": "3000",
            "marketProtection": ""
        }
    }
}
```


<a name="deleteoco"/>


## DeleteOco

Function delete_gtt() cancels a GTT (Good Till Triggered) order before execution, removing it from the exchange's order book and preventing future execution. Once GTT is triggered, deletion is not possible.

#### Parameters:

```python
gttSummaryId
```

#### Sample Delete OCO Request:

```python

samco.delete_oco(body={
    "gttSummaryId" : 945530
})
```
#### sample Delete GTT Response:
```json
{
    "serverTime": "02/06/24 12:23:41",
    "msgId": "bbeb4ca0-00ce-4161-948e-2fc28a9f2259",
    "status": "Success",
    "statusMessage": "GTT Deleted successfully",
    "gttSummaryId": "945530",
    "orderDetails": {
        "clientId": "RXX72XX"
    }
}
```


<a name="listgttoco"/>


## ListGttOco

Function `list_gtt_oco()` lists all GTT (Good Till Triggered) orders with OCO (One-Cancels-the-Other) conditions set by the user.

#### Parameters:

```python
listType
```

#### Sample List GTT OCO Request:

```python
samco.list_gtt_oco(listType='active')

```
#### sample List GTT OCO Response:
```json
{
    "serverTime": "02/06/24 12:26:53",
    "msgId": "d38d2888-122e-4bcf-a788-0e803336f1d2",
    "status": "Success",
    "statusMessage": "List of GTT / OCO orders received.",
    "orderDetails": [
        {
            "summary": {
                "id": 524020,
                "userId": "RXX7XXX",
                "symbol": "14366_NSE",
                "symbolName": "IDEA",
                "orderType": "L",
                "productType": "CNC",
                "gttType": "SINGLE",
                "validTill": "FOREVER",
                "createdAt": "2024-02-29 19:32:42",
                "deletedAt": "",
                "gttSummaryId": "524020",
                "isExpired": false
            },
            "triggers": {
                "gtt": {
                    "status": "",
                    "triggeredAt": "",
                    "triggerId": "717325",
                    "gttId": "717325",
                    "quantity": "20",
                    "limitPrice": "3600",
                    "marketProtection": "",
                    "ltpAtCreation": "13.65",
                    "triggerPrice": "3600",
                    "transactionType": "BUY",
                    "rejectReason": "",
                    "orderNumber": ""
                }
            }
        },
        {
            "summary": {
                "id": 524015,
                "userId": "RXX7XXX",
                "symbol": "14366_NSE",
                "symbolName": "IDEA",
                "orderType": "L",
                "productType": "CNC",
                "gttType": "SINGLE",
                "validTill": "FOREVER",
                "createdAt": "2024-02-29 19:32:30",
                "deletedAt": "",
                "gttSummaryId": "524015",
                "isExpired": false
            },
            "triggers": {
                "gtt": {
                    "status": "",
                    "triggeredAt": "",
                    "triggerId": "717320",
                    "gttId": "717320",
                    "quantity": "20",
                    "limitPrice": "3600",
                    "marketProtection": "",
                    "ltpAtCreation": "13.65",
                    "triggerPrice": "3600",
                    "transactionType": "BUY",
                    "rejectReason": "",
                    "orderNumber": ""
                }
            }
        }
    ]
}
```



<a name="tradebook"/>

## TradeBook

The TradeBook function is `get_trade_book()`which gives details of all successfully executed orders placed by the user.

#### Sample TradeBook Request:

  samco.get_trade_book()

#### Sample TradeBook Response:
```python
{
    "serverTime": "17/06/20 21:01:25",
    "msgId": "c4b7ec88-32e5-4e1f-a56b-7186f6933d79",
    "status": "Success",
    "statusMessage": "Request Successfull",
    "tradeBookDetails": [
        {
            "orderNumber": "200617000000380",
            "exchange": "BSE",
            "tradingSymbol": "TCS",
            "transactionType": "SELL",
            "productCode": "BO",
            "orderType": "L",
            "orderPrice": "2010.00",
            "quantity": "10",
            "orderValidity": "DAY",
            "orderTime": "06:39:50 PM",
            "filledQuantity": "10",
            "exchangeOrderNumber": "1592387449638000145",
            "tradeNumber": "25400",
            "tradePrice": "2010.00",
            "tradeDate": "17JUN2020",
            "tradeTime": "06:39:49 PM",
            "strikePrice": "0.00",
            "optionType": "XX",
            "expiry": "NA"
        }
    ]
}
```
<a name="positions"/>

## Positions

The Postions function `get_positions_data()` gets the position details of the user (The details of equity, derivative, commodity, currency borrowed or owned by the user).

#### Parameters:
```python
position_type
```
#### Sample Positions Request:

  samco.get_positions_data(position_type=samco.POSITION_TYPE_DAY)

#### Sample Positions Response:
```python
{
    "serverTime": "17/06/20 21:06:10",
    "msgId": "36a2cb48-2ce8-48e4-ac0a-90e68c6d26f1",
    "status": "Success",
    "statusMessage": "User Positions details retrieved successfully",
    "positionDetails": [
        {
            "averagePrice": "-4.95",
            "exchange": "BSE",
            "markToMarketPrice": "-99.00",
            "lastTradedPrice": "2,010.00",
            "previousClose": "2067.80",
            "productCode": "BO",
            "tradingSymbol": "TCS",
            "calculatedNetQuantity": "0.0",
            "averageBuyPrice": "2014.95",
            "averageSellPrice": "2010.00",
            "boardLotQuantity": "1",
            "boughtPrice": "40299.00",
            "buyQuantity": "20",
            "carryForwardQuantity": "0",
            "carryForwardValue": "0.00",
            "multiplier": "1",
            "netPositionValue": "-99.00",
            "netQuantity": "0",
            "netValue": "-99.00",
            "positionType": "DAY",
            "positionConversions": [
                "CNC",
                "NRML"
            ],
            "soldValue": "40200.00",
            "transactionType": "BUY",
            "realizedGainAndLoss": "-99.00",
            "unrealizedGainAndLoss": "0.00",
            "companyName": "TATA CONSULTANCY SERVICES LTD."
        }
    ]
}
```
<a name="positionconversion"/>

## PositionConversion

The PostionConversion function `convert_position()` is used to convert an existing position of a margin product to a different margin product type. All or a subset of an existing position quantity can be converted to a different product type.The available margin product types are MARGIN_INTRADAY_SQUAREOFF(MIS), CASHNCARRY(CNC), NORMAL(NRML).

#### Parameters:
```python
symbolName,exchange,transactionType,positionType,quantityToConvert,fromProductType,toProductType,netQuantity
```
##### Sample PositionConverstion Request:

    samco.convert_position(body={ 
      "symbolName":"TSC",
      "exchange":"BSE",
      "transactionType":"BUY",
      "positionType":"DAY",
      "quantityToConvert": "2",
       "fromProductType":"MIS",
       "toProductType":"CNC",
       "netQuantity":"2"
    })

#### Sample PostionConverstion Response:
```python
{
  "serverTime" : "17x/06/20 15:06:42",
  "msgId" : "ba32c75f-ee4b-4af6-a580-f17ad36fefd4",
  "status" : "Success",
  "statusMsg" : "Position Conversion from MIS to CNC successful"
}
```
<a name="positionsquareoff"/>

## PositionSquareOff

The PositionSquareoff function `square_off_position()` helps the user to SqareOff existing position. Mostly used in day trading, in which user buy or sell a particular quantity of a stock and later in the day reverse the transaction to earn a profit. 

#### Parameters:
```python
symbolName,exchange,transactionType,productType,netQuantity
```
##### Sample PositionSquareoff Request:

    samco.square_off_position(body={ 
        "positionSquareOffRequestList": [
        {
            "exchange": samco.EXCHANGE_NSE,
            "symbolName":"TCS",
            "productType":samco.PRODUCT_MIS,
            "netQuantity":"1",
            "transactionType":samco.TRANSACTION_TYPE_BUY
        }
       ]
    })

#### Sample PositionSquareoff Response:
```python
{
  "serverTime": "25/06/20 20:04:30",
  "msgId": "fcb519b8-dd74-422a-8a65-1dc0a0caedb7",
  "positionSquareOffResponseList": [
    {
      "status": "Success",
      "statusMessage": "Position square off successful -TCS-EQ NetQty:1"
    }
  ]
}
```
<a name="holdings"/>

## Holdings

The Holdings function `get_holding()` helps the user to get the details of the Stocks which client is holding. Here, you will be able to get the Client holdings which are bought under ‘CNC’ product type and are not sold yet.

#### Sample Holdings Request:

  samco.get_holding()

#### Sample Holdings Response:
```python
{
    "serverTime": "16/06/20 18:31:52",
    "msgId": "192d039e-6647-4e2f-8d97-5a91143d47a7",
    "status": "Success",
    "statusMessage": "User Holding details retrieved successfully",
    "holdingSummary": {
        "gainingTodayCount": "2",
        "losingTodayCount": "2",
        "totalGainAndLossAmount": "-242900000.00",
        "portfolioValue": "176205000.00"
    },
    "holdingDetails": [
        {
            "averagePrice": "51.10",
            "exchange": "BSE",
            "lastTradedPrice": "0.00",
            "previousClose": "51.10",
            "productCode": "CNC",
            "symbolDescription": "ASHOK LEYLAND LTD.",
            "tradingSymbol": "ASHOKLEY",
            "totalGainAndLoss": "-51100000.00",
            "holdingsQuantity": "1000000",
            "collateralQuantity": "0",
            "holdingsValue": "0.00",
            "sellableQuantity": "1000000"
        },
        {
            "averagePrice": "1610.60",
            "exchange": "NSE",
            "lastTradedPrice": "1760.30",
            "previousClose": "1610.60",
            "productCode": "CNC",
            "symbolDescription": "ASIAN PAINTS LIMITED",
            "tradingSymbol": "ASIANPAINT-EQ",
            "totalGainAndLoss": "14970000.00",
            "holdingsQuantity": "100000",
            "collateralQuantity": "0",
            "holdingsValue": "176030000.00",
            "sellableQuantity": "100000"
        },
        {
            "averagePrice": "1.65",
            "exchange": "NSE",
            "lastTradedPrice": "1.75",
            "previousClose": "1.65",
            "productCode": "CNC",
            "symbolDescription": "JAIPRAKASH ASSOCIATES LTD",
            "tradingSymbol": "JPASSOCIAT-EQ",
            "totalGainAndLoss": "10000.00",
            "holdingsQuantity": "100000",
            "collateralQuantity": "0",
            "holdingsValue": "175000.00",
            "sellableQuantity": "100000"
        },
        {
            "averagePrice": "2067.80",
            "exchange": "BSE",
            "lastTradedPrice": "0.00",
            "previousClose": "2067.80",
            "productCode": "CNC",
            "symbolDescription": "TATA CONSULTANCY SERVICES LTD.",
            "tradingSymbol": "TCS",
            "totalGainAndLoss": "-206780000.00",
            "holdingsQuantity": "100000",
            "collateralQuantity": "0",
            "holdingsValue": "0.00",
            "sellableQuantity": "100000"
        }
    ]
}
```
<a name="intradaycandledata"/>

## IntraDayCandleData

The IndexIntraDayCandleData function `get_intraday_candle_data()` gets the Intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific symbol.


#### Parameters:
```python
symbol_name,exchange,from_date,to_date
```
#### Sample IntraDayCandleData Request:

  samco.get_intraday_candle_data(symbol_name='INFY',exchange=samco.EXCHANGE_NSE, from_date='2020-06-17 10:22:00',to_date='2020-06-17 10:28:00')

#### Sample IntraDayCandleData Response:
```python
{
  "serverTime": "17/06/20 10:50:31",
  "msgId": "c3a1ae34-8078-4f56-8a00-83f92bfa3a4b",
  "status": "Success",
  "statusMessage": "Intraday candle data retrieved successfully",
  "intradayCandleData": [
    {
      "dateTime": "2020-06-17 10:22:00.0",
      "open": "705.25",
      "high": "705.3",
      "low": "704.6",
      "close": "704.65",
      "volume": "7627"
    },
    {
      "dateTime": "2020-06-17 10:23:00.0",
      "open": "704.6",
      "high": "704.7",
      "low": "704.0",
      "close": "704.0",
      "volume": "16154"
    },
    {
      "dateTime": "2020-06-17 10:24:00.0",
      "open": "704.25",
      "high": "704.6",
      "low": "704.05",
      "close": "704.6",
      "volume": "13767"
    },
    {
      "dateTime": "2020-06-17 10:25:00.0",
      "open": "704.75",
      "high": "704.75",
      "low": "703.8",
      "close": "703.95",
      "volume": "13091"
    },
    {
      "dateTime": "2020-06-17 10:26:00.0",
      "open": "703.95",
      "high": "704.3",
      "low": "703.8",
      "close": "704.1",
      "volume": "7039"
    },
    {
      "dateTime": "2020-06-17 10:27:00.0",
      "open": "704.15",
      "high": "704.15",
      "low": "703.55",
      "close": "703.95",
      "volume": "17886"
    },
    {
      "dateTime": "2020-06-17 10:28:00.0",
      "open": "704.0",
      "high": "704.95",
      "low": "703.75",
      "close": "704.85",
      "volume": "17760"
    }
  ]
}
```
<a name="indexintradaycandledata"/>

### IndexIntraDayCandleData

The IndexIntraDayCandleData function `get_index_intraday_candle_data()` gets the Index intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific index.

#### Parameters:
```python
index_name,from_date,to_date
```
#### Sample IndexIntraDayCandleData Request:

  samco.get_index_intraday_candle_data(index_name='sensex', from_date='2020-06-16 09:23:00',to_date='2020-06-16 9:28:00')

#### Sample IndexIntraDayCandleData Response:
```Python
{
  "serverTime": "16/06/20 19:09:13",
  "msgId": "42bc5657-2d2b-49f3-8ead-1bb07a157e2a",
  "status": "Success",
  "statusMessage": "Index IntraDay Candle data retrieved successfully ",
  "indexIntraDayCandleData": [
    {
      "dateTime": "2020-06-16 09:23:00.0",
      "open": "33896.83",
      "high": "33914.65",
      "low": "33874.05",
      "close": "33874.96",
      "volume": "0"
    },
    {
      "dateTime": "2020-06-16 09:24:00.0",
      "open": "33878.08",
      "high": "33915.78",
      "low": "33874.27",
      "close": "33909.3",
      "volume": "0"
    },
    {
      "dateTime": "2020-06-16 09:25:00.0",
      "open": "33905.3",
      "high": "33911.31",
      "low": "33884.92",
      "close": "33900.15",
      "volume": "0"
    },
    {
      "dateTime": "2020-06-16 09:26:00.0",
      "open": "33899.02",
      "high": "33936.46",
      "low": "33899.02",
      "close": "33936.46",
      "volume": "0"
    },
    {
      "dateTime": "2020-06-16 09:27:00.0",
      "open": "33936.5",
      "high": "33951.67",
      "low": "33924.21",
      "close": "33925.92",
      "volume": "0"
    },
    {
      "dateTime": "2020-06-16 09:28:00.0",
      "open": "33925.2",
      "high": "33928.91",
      "low": "33886.56",
      "close": "33890.5",
      "volume": "0"
    }
  ]
}
```
<a name="historicalcandledata"/>

## HistoricalCandleData:

The HistoricalCandleData function `get_index_intraday_candle_data()` gets the historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific symbol. From date is mandatory. End date is optional and defaults to Today.

#### Parameters:
```python
symbol_name,exchange,from_date,to_date
```

#### Sample HistoricalCandleData Request:

    samco.get_historical_candle_data(symbol_name='BANKNIFTY18JUN2018500PE',exchange=samco.EXCHANGE_NFO, from_date='2020-06-14',to_date='2020-06-17')

#### Sample HistoricalCandleData respone:
```python
{
  "serverTime": "17/06/20 11:14:06",
  "msgId": "97cdca8f-81f9-4a88-8da6-99b471e82803",
  "status": "Success",
  "statusMessage": "Historical candle data retrieved successfully",
  "historicalCandleData": [
    {
      "date": "2020-06-15",
      "open": "60.0",
      "high": "136.45",
      "low": "56.2",
      "close": "78.5",
      "ltp": "78.5",
      "volume": "9302660"
    },
    {
      "date": "2020-06-16",
      "open": "38.75",
      "high": "206.85",
      "low": "13.0",
      "close": "38.5",
      "ltp": "38.5",
      "volume": "7792900"
    }
  ]
}
```
<a name="indexhistoricalcandledata"/>

### IndexHistoricalCandleData:
The IndexHistoricalCandleData function `get_index_candle_data()` gets the Index historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific index. From date is mandatory. End date is optional and defaults to Today.

#### Parameters:
```python
index_name,from_date,to_date
```
#### Sample IndexHistoricalCandleData Request;

  samco.get_index_candle_data(index_name='NIFTY 200', from_date='2019-05-24',to_date='2019-05-29')

#### Sample IndexHistoricalCandleData Response:
```python
{
  "serverTime": "17/06/20 11:39:11",
  "msgId": "bb015c56-74e5-401b-bfe0-e2c9c415d088",
  "status": "Success",
  "statusMessage": "Index HistoricalCandle data retrieved successfully ",
  "indexCandleData": [
    {
      "date": "2019-05-24",
      "open": "6067.65",
      "high": "6134.4",
      "low": "6029.9",
      "close": "6129.8",
      "ltp": "6129.8",
      "volume": "0"
    },
    {
      "date": "2019-05-27",
      "open": "6134.35",
      "high": "6189.0",
      "low": "6114.5",
      "close": "6177.15",
      "ltp": "6177.15",
      "volume": "0"
    },
    {
      "date": "2019-05-28",
      "open": "6195.7",
      "high": "6195.7",
      "low": "6151.25",
      "close": "6181.35",
      "ltp": "6181.35",
      "volume": "0"
    },
    {
      "date": "2019-05-29",
      "open": "6172.55",
      "high": "6178.85",
      "low": "6132.0",
      "close": "6143.8",
      "ltp": "6143.8",
      "volume": "0"
    }
  ]
}
```
<a name="streamingdata"/>

## StreamingData

StockNote API platform provides the Broadcast API, as the most effective way to receive quote data for instruments across all exchanges during live market hours. The API provides continuous streaming data of quote based on user request, and primarily consists of fields such as last traded price, open, high, low, close, last traded quantity, last traded volume, last traded time etc.

The API uses WebSocket protocol to establish a dedicated TCP connection after an HTTP handshake to receive streaming quotes and thereby provides seamless streaming of quote data. You need to use a WebSocket client to connect to our broadcast API. If you have already subscribed to our StockNote API services, you will be able to access broadcast API too.

#### Sample Streaming Request:

  value=[{"symbol":"-53"},{"symbol":"1143_CDS"},{"symbol":"1270_NSE"},{"symbol":"10604_NSE"},{"symbol":"11195_NSE"}]
  samco.set_streaming_data(value)
  samco.start_streaming()

#### Sample Streaming Response:

  Message Arrived:{"response":{"data":{"aPr":"0.00","aSz":"0","avgPr":"0.00","bPr":"0.00", "bSz":"0","c":"29.65","ch":"0.38","chPer":"1.28",
  "h":"30.28","l":"27.24","lTrdT":"09 Jun 2020, 02:11:58 PM","ltp":"30.03","ltq":"0","ltt":"09 Jun 2020, 02:11:58 PM","lttUTC":"09 Jun 2020, 08:41:58 AM",
  "o":"29.65","oI":"","oIChg":"","sym":"-53","tBQ":"0","tSQ":"0","ttv":"0.00","vol":"0","yH":"0.00","yL":"0.00"},"streaming_type":"quote"}}

  Message Arrived:{"response":{"data":{"aPr":"0.00","aSz":"0","avgPr":"0.00","bPr":"0.00", "bSz":"0","c":"29.65","ch":"0.38","chPer":"1.28",
  "h":"30.28","l":"27.24","lTrdT":"09 Jun 2020, 02:11:58 PM","ltp":"30.03","ltq":"0","ltt":"09 Jun 2020, 02:11:58 PM","lttUTC":"09 Jun 2020, 08:41:58 AM",
  "o":"29.65","oI":"","oIChg":"","sym":"-53","tBQ":"0","tSQ":"0","ttv":"0.00","vol":"0","yH":"0.00","yL":"0.00"},"streaming_type":"quote"}}


<a name="logout"/>

## Logout
Logging out user from the application.
The Logout function name in python is `logout()`

#### Sample Logout Request:

  samco.logout()

#### Sample Logout Response:
```python
{
  "serverTime" : "17/06/20 12:27:52",
  "msgId" : "41627994-5c96-411c-b15c-dbda00029269",
  "status" : "Success",
  "statusMessage" : "User has successfully logged out"
}
```

## Constant List:
This section contains the list of possible constant values that can be passed for input attributes like exchanges, product types etc.

### Product types:
    PRODUCT_MIS 
    PRODUCT_CNC
    PRODUCT_NRML
    PRODUCT_CO
    PRODUCT_BO
   
    Example:- "productType":samco.PRODUCT_MIS
   
    
 ### Exchanges:
    EXCHANGE_NSE
    EXCHANGE_BSE
    EXCHANGE_NFO
    EXCHANGE_BFO
    EXCHANGE_CDS
    EXCHANGE_MCX
   
    Example:- "exchange":samco.EXCHANGE_NSE
   
    
 ### Transaction types:
    TRANSACTION_TYPE_BUY
    TRANSACTION_TYPE_SELL
   
    Example:- "transactionType":samco.TRANSACTION_TYPE_BUY
     
   
  ### Order types:
    ORDER_TYPE_MARKET
    ORDER_TYPE_LIMIT 
    ORDER_TYPE_SLM 
    ORDER_TYPE_SL 
   
    Example:- "orderType":samco.ORDER_TYPE_LIMIT
     
    
   ### Validity types:
    VALIDITY_DAY 
    VALIDITY_IOC 
 
    Example:- "orderValidity":samco.VALIDITY_DAY
   
    
   ### Position types:
    POSITION_TYPE_DAY
    POSITION_TYPE_NET
 
    Example:- position_type=samco.POSITION_TYPE_DAY
  
