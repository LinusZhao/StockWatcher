__author__ = 'Ares'

from yahoo_finance import Share

import time

from threading import Thread

Add_Pre_Process = 0
sm_stock_list=[]
mid_stock_list=[]
lg_stock_list=[]
huge_stock_list=[]

if(Add_Pre_Process == 0):
    sm_list = open('sm_list.csv',"r")
    mid_list = open('mid_list.csv',"r")
    lg_list = open('lg_list.csv',"r")
    huge_list = open('huge_list.csv',"r")

    for sm_stock_name in sm_list:
        sm_stock_list.append(sm_stock_name)
    for mid_stock_name in mid_list:
        mid_stock_list.append(mid_stock_name)
    for lg_stock_name in lg_list:
        lg_stock_list.append(lg_stock_name)
    for huge_stock_name in huge_list:
        huge_stock_list.append(huge_stock_name)

sm_list.close()
mid_list.close()
lg_list.close()
huge_list.close()

def get_price_change(stock_list=[]):
    for stock_line in stock_list:
        stock_change = Share(stock_line)
        last_price = stock_change.get_open()
        real_time_price = stock_change.get_price()

        if(real_time_price==None):
            continue
        if(last_price==None):
            continue
        last_price = float(last_price)
        real_time_price = float(real_time_price)
        ratio = real_time_price/last_price
        if(ratio>=1.05):
            ratio = ratio - 1
            print (stock_line +"last: " + str(last_price) + " realtime: "+str(real_time_price)+ " price gain " + "%.2f"%(ratio*100) +"\n")

while(1):
    sm_thread   = Thread(target=get_price_change,args=(sm_stock_list,))
    mid_thread  = Thread(target=get_price_change,args=(mid_stock_list,))
    lg_thread   = Thread(target=get_price_change,args=(lg_stock_list,))
    huge_thread  = Thread(target=get_price_change,args=(huge_stock_list,))

    sm_thread.start()
    time.sleep(5)
    mid_thread.start()
    time.sleep(5)
    lg_thread.start()
    time.sleep(5)
    huge_thread.start()

    mid_thread.join()
    lg_thread.join()
    sm_thread.join()
    huge_thread.join()

    time.sleep(300)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

'''
else :
    sm_list = open('sm_list.csv',"w+")
    mid_list = open('mid_list.csv',"w+")
    lg_list = open('lg_list.csv',"w+")
    huge_list = open('huge_list.csv',"w+")
    stock_ori_list = open('my_list.csv',"r")
    sm_list_size =0
    mid_list_size =0
    lg_list_size =0
    huge_list_size =0


    for stock_name in stock_ori_list:
        stock_price = Share(stock_name)
        price = stock_price.get_price()
        if(price==None):
            price=0
        price = float(price)
        if(1 < price < 5):
            sm_stock_dict[stock_name] = price
            sm_list_size = sm_list_size + 1
            sm_list.write(stock_name)
        elif(5<=price<=25):
            mid_stock_dict[stock_name] = price
            mid_list_size = mid_list_size + 1
            mid_list.write(stock_name)
        elif(25 < price <= 50):
            lg_stock_dict[stock_name] = price
            lg_list_size = lg_list_size + 1
            lg_list.write(stock_name)
        elif(price > 50):
            huge_stock_dict[stock_name] = price
            huge_list_size = huge_list_size + 1
            huge_list.write(stock_name)
'''
