DATE=$(date +'%Y-%m-%d %H:%M:%S')
IPADDR=$(ifconfig | grep inet | awk 'BEGIN{ FS=" " }NR==1{ print $2 }')
#MAIL="bavduer@163.com"

# 检测vmstat命令是否存在
if ! which vmstat &>/dev/null; then
       yum -y install procps-ng &>/dev/null
       if [ $? -eq 0 ];then
               echo "vmstat already installed"
       fi
fi
if ! which bc &>/dev/null; then
       yum -y install bc &>/dev/null
       if [ $? -eq 0 ];then
               echo "vmstat already installed"
       fi
fi
if [ ! -d "/log" ]; then
  mkdir /log
fi
if [ ! -f "/log/access.log" ]; then
  touch /log/access.log
fi
US=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $13 }')
SY=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $14 }')
ID=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $15 }')
WA=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $16 }')
ST=$(vmstat | awk 'BEGIN{ FS=" " }NR==3{ print $17 }')
DATE=$(date +'%Y-%m-%d %H:%M:%S')
useTotal=$((${US}+${SY}))
useRate=$(df -Th | awk 'BEGIN{ FS=" " }NR==2{ print $6 }')
TOTAL=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $2 }')
USE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $3 }')
FREE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $4 }')
CACHE=$(free -mw | awk 'BEGIN{ FS=" " }NR==2{ print $7 }')
memoryused=$((${USE}+${CACHE}))
used=$(echo "((${USE}+${CACHE})/${TOTAL})*100" | bc -ql)

sed -ri "s/zero/$(hostname)/g" /systeminfo.json
sed -ri "s/second/$used/g" /systeminfo.json
sed -ri "s/first/$useTotal/g" /systeminfo.json
sed -ri "s/third/$useRate/g" /systeminfo.json
cat<<-EOF >>/log/access.log
${DATE} "hostname":$(hostname), "cpuinfo":${useTotal: 0:2 }%, "memoryinfo":${used:0:2}%,"diskinfo":${useRate}
EOF
