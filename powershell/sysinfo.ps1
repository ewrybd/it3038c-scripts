function getIP{
    (get-netipaddress).ipv4address | Select-String "192*"
}

function user{
  (Get-LocalUser) | Select-String "Admin"
}

function hostname{
   (Get-Host).Name

}

function version{
   (Get-Host).Version
}

function day{
   (Get-Date).DayOfWeek 
}

function date{
   Get-Date -Format "MM/dd/yyyy"
}

$IP = Getip

$USER = user

$HOSTNAME = hostname

$VERSION = version

$DAY = day

$DATE = date

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. Powershell version is $VERSION. Today's Date is $DAY, $DATE."

Write-Host("$BODY")

$BODY | out-file C:\info.txt
notepad C:\info.txt