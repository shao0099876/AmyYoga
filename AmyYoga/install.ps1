If (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))

{
$arguments = "& '" + $myinvocation.mycommand.definition + "'"
Start-Process powershell -Verb runAs -ArgumentList $arguments
Break
}
echo "Installing WinSCP Module..."
Install-Module -AllowClobber winSCP
echo "Installing SSHSession Module..."
Install-Module -AllowClobber sshsession

