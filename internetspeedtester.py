import speedtest
#have to install speedtest-cli not speedtest 
st = speedtest.Speedtest()

option = int(input("What speed do you want to test:\n1)Download speed \n2)Upload speed\n3)Ping\nYour choice:"))
                   
if option == 1:
    print('The download speed is {0}'.format(st.download()))
elif option == 2:
    print('The upload speed is {0}'.format(st.upload()))
elif option ==3:
    servername = []
    st.get_servers(servername)
    print('The ping is {0}'.format(st.results.ping))

else:
    print("That is not a valid entry, please try again")

    