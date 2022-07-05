import random
import string
import time
import GUI
print("*****************************   DYNAMIC ROUTING(RIP) IMPLEMENTATION  ***************************************************")

class device:
    MAC_source=""
    IP_source=""
    Subnet_mask=""
    gateway=""
####################
class router:
    MAC_source=""
    def __init__(self):
        self.interface={}
        self.routing_table=[]
        self.nidlist=[]
        self.directly_connected=[]


choice=input("Press Yes to Run packet tracer for default configuration or Press No for generalise configuration:")
if choice== "yes":
    d = 6
    n = 3
else:
    d=int(input("Enter no. of End devices:"))
    n=int(input("Enter no. of Routers:"))


PC=[]
for i in range(d):
    PC.append(device())

R=[]
for i in range(n):
    R.append(router())


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

if choice=="yes" :
#########  MAC configurartion ##########
    PC[0].MAC_source="B2:34:55:10:22:10"
    PC[1].MAC_source="A1:15:55:10:21:11"
    PC[2].MAC_source="B3:33:55:10:22:12"
    PC[3].MAC_source="C2:35:55:10:20:13"
    PC[4].MAC_source="A4:39:55:10:18:14"
    PC[5].MAC_source="C1:37:55:10:30:15"

    R[0].MAC_source="D0:30:55:10:22:CC"
    R[1].MAC_source="D1:31:54:11:21:DD"
    R[2].MAC_source="D2:32:53:12:22:FF"
else:
    for i in range(d):

        PC[i].MAC_source=random_char(12)
        #print(PC[i].MAC_source)
    for i in range(n):
        R[i].MAC_source=random_char(12)
        #print(R[i].MAC_source)
############################################

print("Type 'pcconfig' to configure IP addresses of devices:")
if(input()=="pcconfig"):
    for i in range(d):
        print("Configuring PC[",i,"]...")
        PC[i].IP_source=input("Enter IP address:")
        ip=PC[i].IP_source
        m = 0
        c = ''
        while (ip[m] != '.'):
            c = c + ip[m]
            m = m + 1

        if(int(c)>=0 or int(c)<=127):
            PC[i].Subnet_mask = "255.0.0.0"
        elif(int(c) >= 128 or int(c) <= 191):
            PC[i].Subnet_mask = "255.255.0.0"
        else:
            PC[i].Subnet_mask = "255.255.255.0"
        PC[i].gateway = input("Enter Gateway:")
else:
        PC[0].IP_source="192.168.1.1"
        PC[0].Subnet_mask="255.255.255.0"
        PC[0].gateway="192.168.1.100"

        PC[1].IP_source = "192.168.1.2"
        PC[1].Subnet_mask = "255.255.255.0"
        PC[1].gateway = "192.168.1.100"

        PC[2].IP_source = "192.168.2.1"
        PC[2].Subnet_mask = "255.255.255.0"
        PC[2].gateway = "192.168.2.100"

        PC[3].IP_source = "192.168.2.2"
        PC[3].Subnet_mask = "255.255.255.0"
        PC[3].gateway = "192.168.2.100"

        PC[4].IP_source = "192.168.3.1"
        PC[4].Subnet_mask = "255.255.255.0"
        PC[4].gateway = "192.168.3.100"

        PC[5].IP_source = "192.168.3.2"
        PC[5].Subnet_mask = "255.255.255.0"
        PC[5].gateway = "192.168.3.100"



print(" --------------------------------------------------------------------------------------------------")
print("   All PC's configured")
print("|_________________________________________________________________________________________________|")
print("| PC name |      MAC address    |    IP address         |  Subnet Mask       |        Gateway     |")
for i in range(d):

    print("|_________________________________________________________________________________________________|")
    print("|",i,"      |",PC[i].MAC_source,"  |     ",PC[i].IP_source,"     |",PC[i].Subnet_mask,"     |   ",PC[i].gateway,"  |")
    print("|_________________________________________________________________________________________________|")

print("*********************************************************************************************************")
print("Type 'rconfig' to configure Routers:")
if(input()=="rconfig"):
    for i in range(n):
        print("Configuring Router[",i,"]...")
        intf=int(input("Enter number of interfaces:"))
        for j in range(intf):
            print("Enter IP for interface:", j)
            ip = input()
            R[i].interface[j] = ip

else:
    R[0].interface[0] = "192.168.1.100"
    R[0].interface[1] = "192.168.2.100"
    R[0].interface[2] = "192.168.6.1"
    R[0].interface[3] = "192.168.4.1"

    R[1].interface[0] = "192.168.6.2"
    R[1].interface[1] = "192.168.3.100"
    R[1].interface[2] = "192.168.5.2"

    R[2].interface[0] = "192.168.4.2"
    R[2].interface[1] = "192.168.5.1"

print("------------------------------------------------------------------------------------------")
print("All routers configured.....")
print()
for i in range(n):
    print("________________________________________________________________________________________________________")
    print("Router",i,":(interface,ip)->",R[i].interface)

print("*********************************************************************************************************")

for i in range(n):
        print("----------------------------Router ",i,"---------------------------------------------------------")
        iplist=list(R[i].interface.values())   #these are directly connected ip addresses

        if PC[i].Subnet_mask=="255.255.255.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:9]+".0")
        if PC[i].Subnet_mask=="255.255.0.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:7]+".0.0")
        elif PC[i].Subnet_mask=="255.0.0.0":
            for j in range(len(iplist)):
                R[i].directly_connected.append(iplist[j][0:2]+".0.0.0")

        print()
        print('Directly connected list for Router',i,R[i].directly_connected)  ## these are nids
        print("--------------------------------------------------------------------------------------------------")

###########################   Now routing table section ############
all_nids=[]
for i in range(n):
    for j in range(len(R[i].directly_connected)):
        all_nids.append(R[i].directly_connected[j])
#print(all_nids)
all_nids=list(set(all_nids))
#print(all_nids)

for i in range(n):
    hops=0
    print("")
    print("-------------Routing Table for Router-",i,"-----------------")
    print()
    print("|     Destination     |   Hop         |        Next         |")
    print("____________________________________________________________")
    for j in range(len(all_nids)):
        if all_nids[j] in R[i].directly_connected:
            hops=1
            Next="_"
            #print(all_nids[j],"is Directly connected")
            print("|    ",all_nids[j],"   |    1           |          ",Next,"        |")
        else:
            count=0
            for k in range(n):
                if k!=i:
                    if all_nids[j] in R[k].directly_connected:
                        for x in range(len(list(R[k].interface.values()))):

                            ip=list(R[k].interface.values())[x]

                            m = 0
                            c = ''
                            while (ip[m] != '.'):
                                c = c + ip[m]
                                m = m + 1
                            #print("c=",c)
                            if (int(c) >= 0 and int(c) <= 127):
                                nid=str(c)+".0.0.0"
                                #print("hello1")

                            elif (int(c) >= 128 and int(c) <= 191):
                                nid=ip[0:7]+".0.0"
                                #print("hello2")
                            elif (int(c)>=192):
                                nid=ip[0:9]+".0"
                                #print("hello3")

                            #print("nid=", nid)
                            for p in range(n):
                                if p!=k:
                                    if nid in R[p].directly_connected:
                                        count=count+1
                                        #print("hello")
                                        #print("x=",x)
                                        if count==1:
                                            Next=R[k].interface[x] ##here find the ip from nid
                                        #for t in range(len(R[p].directly_connected)):
                                        else:
                                            pass
                                        #print("Next=",Next)

            print("|    ", all_nids[j], "    |   2           |      ", Next, "  |")
        print("_____________________________________________________________")

def find_mac(ip):
    for i in range(d):
        src=" "+PC[i].IP_source
        if(src==ip):
            return i
if(input("Do you want to ping any device ? :")=='yes'):
    pn=int(input("How many devices you want to ping ? "))
    for i in range(pn):
        pcname=int(input("From which PC you want to ping?"))
        sourcepc=PC[pcname]
        print("____________________________________________________________________________________________")
        command=input("Enter command:")
        destination_ip=command[4:len(command)]
        time.sleep(0.5)
        print("Sending an ARP request to all devices:")
        print("ARP request packet broadcasting:")
        print("----------------------------------------------------------------------------------")
        print("|  ",PC[pcname].MAC_source,"  |  ",PC[pcname].IP_source,"  |  ","0x000000000000  |  ",destination_ip,"  |")
        print("----------------------------------------------------------------------------------")
        m=0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)

        replyPC=find_mac(destination_ip)

        print("ARP reply packet unicasted from PC:",replyPC)
        m=0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)
        print("----------------------------------------------------------------------------------")
        print("|  ", PC[replyPC].MAC_source, "  |  ",destination_ip , "  |  ","|",PC[pcname].MAC_source,'|' ,PC[pcname].IP_source, " |")
        print("----------------------------------------------------------------------------------")
        m=0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)
        print("Pinging", destination_ip, "with 32 Bytes of data...")
        m=0
        while m < 4:
            print(".")
            m += 1
            time.sleep(0.4)
        print("Request timed out.")
        l=[10,11,12,13,14,15,16,17,18,19,20]
        print("Reply from",destination_ip,":","bytes=32,","time=",random.choice(l),"ms,  TTL=125")
        print("Reply from", destination_ip, ":", "bytes=32,", "time=", random.choice(l), "ms,  TTL=125")
        print("Reply from", destination_ip, ":", "bytes=32,", "time=", random.choice(l), "ms,  TTL=125")
        print()
        sent_packets=[4,5,6,7]
        s=random.choice(sent_packets)
        r_packets=[1,2,3,4]
        r=random.choice(r_packets)
        lost_packets=s-r
        lost_per=((s-r)/s)*100
        print(" Ping statistics for 192.168.2.1:")
        print("    Packeets:Sent=",s,", Recieved=",r,", Lost=",lost_packets,"(",lost_per,"% ) loss")
        print("Approximate round trip times in milli-seconds:")
        min=random.choice([1,2,3,4,5,6])
        max=random.choice([100,101,102,103,104,105,106,107,108,109,110])
        avg=random.choice(range(30,50))
        print("Minimum = ",min,"ms,  Maximum = ",max,"ms,  Average = ",avg," ms")
        print("____________________________________________________________________________________________")
        ###################################### GUI###########################
        GUI.draw(PC[pcname].IP_source, PC[replyPC].IP_source)
