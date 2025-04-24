param (
    [string]$custom_subfolder
)

Set-Variable -Name 'videos_subfolder' -Value $null

#Write-Host "Custom subfolder name is: $custom_subfolder "

if (-not $PSBoundParameters.ContainsKey('custom_subfolder') ) {
    #Write-Output "Custom subfolder name was not specified. "
    Set-Variable -Name 'videos_subfolder' -Value 'videos'
} else {
    Set-Variable -Name 'videos_subfolder' -Value $custom_subfolder
}

Get-Variable -Name 'videos_subfolder'

if (Test-Path -Path $videos_subfolder -PathType Container) {
    #Write-Output "Subdir exists!"
    ;
} else {
    Write-Output "Subfolder for videos does not exist. Default name is videos, or please specify a name. "
    Exit 1
}

# Check if ffmpeg is installed: 
$found = [bool] (Get-Command -ErrorAction Ignore -Type Application ffmpeg)

if (-not $found) {
    Write-Output "Essential program FFMPEG not found on this system. Please install it and try again. "
    Exit 2
}

$list_file = "list_" + $videos_subfolder + ".txt"
#Write-Output $list_file #TMP



Write-Output "END!!!" #TMP
