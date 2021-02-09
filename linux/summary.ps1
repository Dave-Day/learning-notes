
# dir *.md /b /s /o N >summary.txt
Get-ChildItem -Path $(Get-Location) -Name -Include *.md -Exclude summary.md -Recurse -Force | Sort-Object -CaseSensitive | ForEach-Object -Process { python summary.py $_ }
# | ForEach-Object -Process { "'" + $(Get-Location) + "\" + $_ + "'" } 
# | Out-File -FilePath .\summary.txt -Encoding utf8 -Force 
# Get-Content -Path .\summary.txt