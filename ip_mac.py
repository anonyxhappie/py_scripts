import os;
def getIpMac(arpStr):
	ipArr = macArr = []; ip = mac = ""; i=j=0;	
	larp = len(arpStr);
	while(i < larp):	
		ip=arpStr[1+arpStr.find('(', i, larp):arpStr.find(')', i, larp)]; 
		ipArr.append(ip);
		i=arpStr.find('\n', i, larp)+3;
		
		mac=arpStr[-2+arpStr.find(':', j, larp):arpStr.find('[', j, larp)-1]; 
		macArr.append(mac);
		j=arpStr.find(':', j+50, larp)-2;

	return ["IP n Mac Address =>"] + ipArr;
os.system("arp -a > tmp");
print getIpMac(open("tmp", "r").read());
