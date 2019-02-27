Import-Module WinSCP
$session=New-SshSession -ComputerName 47.104.145.198 -Username root -Password HITwh1604102 
$SshSessions."47.104.145.198".RunCommand("rm -rf /var/www/AmyYoga")
$sessionOptions = New-Object WinSCP.SessionOptions -Property @{
        Protocol = [WinSCP.Protocol]::Scp
        HostName = "47.104.145.198"
        UserName = "root"
        Password = "HITwh1604102"
        SshHostKeyFingerprint = "ssh-rsa 2048 90:ef:1b:a4:75:bd:0c:05:6c:be:84:3d:7a:ef:ee:e1"
}
$scpsession=New-WinSCPSession -SessionOption $sessionOptions
$transferOptions = New-WinSCPTransferOption
Send-WinSCPItem -WinSCPSession $scpsession -LocalPath "./AmyYoga" -RemotePath "/var/www/" -TransferOptions $transferOptions
$scpsession.Dispose()
$SshSessions."47.104.145.198".RunCommand("/etc/init.d/apache2 restart")
pause