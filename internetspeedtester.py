import speedtest

st = speedtest.Speedtest()

option = int(input("What speed do you want to test:\n1)Download speed \n2)Upload speed\n3)Ping\nYour choice:"))
                   
if option == 1:
    print(st.download())
elif option == 2:
    print(st.upload())
elif option ==3:
    servername = []
    st.get_servers(servername)
    print(st.results.ping)

else:
    print("That is not a valid entry, please try again")