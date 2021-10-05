"""
Assignment:

Call the API https://jsonplaceholder.typicode.com/posts
Store the response
Print the set of keys present.
Extend the response by adding the 'extrainfo' to each. The value of extrainfo are as per the below criteria.
1. if id is divisible by 4, the value is fizz
2. If id is divisible by 6, the value is buzz
3. If id is divisible by 4 and 6, the value is fizzbuzz
4. Otherwise, if id is prime or not (isprime or notprime)

Print the results, and it's length.
Filter out and store the values, based on extrainfo all together.
Make the items deletable, based on the input userid. And display the removed item and length of the current items.

"""


import logging
import traceback
import requests

from math import ceil, sqrt


def configure_logger(logger_name=__name__, log_file="logger.log"):
    logging.basicConfig()
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(log_file)
    file_log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
    file_handler.setFormatter(file_log_formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    return logger


def isprime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        if num % 2 == 0:
            if num != 2:
                # even numbers other than two are not prime
                return False
            else:
                return True
        for i in range( 3, ceil( sqrt( num ) ) + 1, 2 ):  # skip all even numbers.
            if (num % i) == 0:
                return False
                # break
        else:
            return True
    else:
        return False


def get_extra_info(value):
    if value % 4 == 0 and value % 6 ==0:
        return "fizzbuzz"
    elif value % 4 == 0:
        return "fizz"
    elif value % 6 == 0:
        return "buzz"
    elif isprime(value):
        return "isprime"
    else:
        return "notprime"


def main():
    logger = configure_logger()
    BASE_URL = "https://jsonplaceholder.typicode.com"
    END_POINT = "/posts"
    
    try:
        api_url = BASE_URL + END_POINT
        api_response = requests.get( url=api_url )
        response = api_response.json()
        print( response )
        first_element = response[0]
        logger.error( first_element.keys() )
        new_list = []
        for val in response:
            val['extrainfo'] = get_extra_info( val["id"] )

        print( response )
        print( len( response ) )
        set_extrainfo = {"fizz", "buzz", "fizzbuzz", "isprime", "notprime"}
        for i in set_extrainfo:
            new_list.append( [x for x in response if x["extrainfo"] == i] )
        print( new_list )
        try:
            userId_inp = int( input( "Enter the id to delete : " ) )

            t = [x for x in response if x["userId"] != userId_inp]
            rem = [x for x in response if x["userId"] == userId_inp]
            print( rem )
            print( len( t ) )
            #
            # for val in response:
            #     if val['userId'] == userId_inp:
            #         print(val)
            #         response = [x for x in response if x != val]
            # print(len(response))

        except ValueError as err:
            print( "Expecting only integers with non-negatie values. " )
            print( err )
            traceback.print_exc()

    except Exception as e:
        logger.error("Exception occurred. ")
        traceback.print_exc()


if __name__ == "__main__":
    main()
